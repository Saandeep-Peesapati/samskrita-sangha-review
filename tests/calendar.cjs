// Exercise the actual download/copy handlers without launching a browser.
const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const path = require('node:path');
const listeners = [];
const inert = {addEventListener(){},setAttribute(){},classList:{add(){},remove(){},toggle(){}}};
let downloaded, opened, createdBlob, clicked = false;
class TestURL extends URL {
  static createObjectURL(blob) { createdBlob=blob; return 'blob:test'; }
  static revokeObjectURL() {}
}
const document = {
  documentElement:inert,
  querySelector:selector=>['.toast','.menu-toggle','.nav-links'].includes(selector)?inert:null,
  querySelectorAll:()=>[],
  addEventListener:(name,handler)=>{if(name==='click')listeners.push(handler);},
  createElement:()=>({click(){clicked=true;downloaded=this.download;},remove(){}}),
  body:{append(){}}
};
const context = {document,URL:TestURL,URLSearchParams,TextEncoder,Blob,Date,setTimeout(){},clearTimeout(){},matchMedia:()=>inert,location:{href:'https://example.org/talks.html?q=old'},window:{open:url=>{opened=url;}}};
vm.runInNewContext(fs.readFileSync(path.resolve(__dirname,'../js/site.js'),'utf8'),context);
function trigger(data,kind='ics') {
  const record = {id:'test-event',dataset:data};
  const button = {dataset:{calendar:kind},closest:()=>record};
  const event = {target:{closest:selector=>selector==='[data-calendar]'?button:null}};
  listeners.forEach(handler=>handler(event));
}
(async()=>{
  const data={date:'2025-08-19',title:'The essentials of Ramayana',speaker:'Shri Arjun Bharadwaj',tentative:'true',location:'',url:'https://youtu.be/7UqmKLzYiPc'};
  trigger(data);
  assert(clicked);
  assert.equal(downloaded,'test-event.ics');
  assert.equal(createdBlob.type,'text/calendar;charset=utf-8');
  let text=await createdBlob.text();
  assert(text.includes('DTSTART;VALUE=DATE:20250819\r\n'));
  assert(text.includes('DTEND;VALUE=DATE:20250820\r\n'));
  assert(text.includes('STATUS:TENTATIVE'));
  assert(text.includes('[Tentative date] The essentials of Ramayana'));
  assert(!text.includes('?q='));
  trigger({...data,date:'2024-02-29',title:'संस्कृतम्; ज्ञानम्, अध्ययनम्\\\n'.repeat(8),tentative:'false'});
  text=await createdBlob.text();
  assert(text.includes('DTEND;VALUE=DATE:20240301\r\n'));
  assert(text.includes('STATUS:CONFIRMED'));
  assert(text.split('\r\n').every(line=>Buffer.byteLength(line)<=75));
  const unfolded=text.replace(/\r\n /g,'');
  assert(unfolded.includes('संस्कृतम्\\; ज्ञानम्\\, अध्ययनम्\\\\\\n'));
  trigger({...data,date:'2026-12-31'});
  assert((await createdBlob.text()).includes('DTEND;VALUE=DATE:20270101'));
  trigger(data,'google');
  const google=new URL(opened);
  assert.equal(google.hostname,'calendar.google.com');
  assert.equal(google.searchParams.get('dates'),'20250819/20250820');
  assert(google.searchParams.get('details').includes('Date to be confirmed'));
  console.log('PASS: actual calendar handlers; ICS dates, exclusive end dates, leap/year rollover, tentative status, UTF-8 folding, escaping, share URL and Google Calendar parameters.');
})().catch(error=>{console.error(error);process.exitCode=1;});
