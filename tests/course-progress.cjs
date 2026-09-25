/* Exercise the production progress handlers with storage failures and two tabs.
   Browser rendering, quizzes and keyboard interactions are checked separately. */
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const assert = require('node:assert/strict');
const script = fs.readFileSync(path.join(__dirname,'../js/learning.js'),'utf8');
const key = 'samskrita-foundation-progress-v1';
const storage = {value:null, fail:false, getItem(){if(this.fail)throw Error('blocked');return this.value;},setItem(k,v){if(this.fail)throw Error('blocked');this.value=v;}};
function el(dataset={}) {return {dataset,textContent:'',hidden:true,attrs:{},handlers:{},setAttribute(k,v){this.attrs[k]=v;},addEventListener(k,fn){this.handlers[k]=fn;}};}
function page(id) {
  const complete=el({complete:id}), reset=el(), label=el(), note=el(), status=el(), resume=el();
  const bar=el(), node=el({node:id}), nodeStatus=el();
  node.querySelector=()=>nodeStatus;
  const window={events:{},addEventListener(k,fn){this.events[k]=fn;}};
  const selectors={'[data-progress]':[bar],'[data-progress-label]':[label],'[data-storage-note]':[note],'[data-progress-status]':[status],'[data-node]':[node],'[data-complete]':[complete],'[data-reset-progress]':[reset],'.lesson-quiz':[],'.course-interactive':[complete,reset]};
  const course={dataset:{courseIds:'sounds,script,cases'},classList:{add(){}},querySelectorAll(s){assert(s in selectors,s);return selectors[s];},querySelector(s){if(s==='[data-resume]')return resume;if(s==='.lesson-outline')return null;throw Error(s);}};
  vm.runInNewContext(script,{document:{querySelector(){return course;}},localStorage:storage,window});
  return {complete,reset,label,note,status,resume,bar,node,nodeStatus,window};
}
const first=page('sounds');
assert.equal(first.label.textContent,'0 of 3 complete');
first.complete.handlers.click();
assert.equal(first.complete.attrs['aria-pressed'],'true');
assert.equal(first.resume.href,'learn-script.html');
const reload=page('sounds');
assert.equal(reload.label.textContent,'1 of 3 complete');
const second=page('script');
second.complete.handlers.click();
assert.deepEqual(JSON.parse(storage.value).completed,['sounds','script']);
first.window.events.storage({key});
assert.equal(first.label.textContent,'2 of 3 complete');
first.complete.handlers.click();
assert.deepEqual(JSON.parse(storage.value).completed,['script']);
first.reset.handlers.click();
assert.deepEqual(JSON.parse(storage.value).completed,[]);
storage.value='{broken';
const corrupted=page('cases');
assert.match(corrupted.note.textContent,/could not be read/);
corrupted.complete.handlers.click();
assert.deepEqual(JSON.parse(storage.value).completed,['cases']);
storage.value=JSON.stringify({version:1,completed:['sounds','sounds','unknown',null]});
assert.equal(page('sounds').label.textContent,'1 of 3 complete');
storage.value=JSON.stringify({version:1,completed:['sounds','script','cases']});
assert.equal(page('sounds').resume.textContent,'Revisit the first lesson →');
storage.fail=true;
const blocked=page('sounds');
blocked.complete.handlers.click();
assert.equal(blocked.complete.attrs['aria-pressed'],'true');
assert.match(blocked.note.textContent,/only on this page/);
blocked.complete.handlers.click();
assert.equal(blocked.complete.attrs['aria-pressed'],'false');
assert.equal(blocked.label.textContent,'0 of 3 complete');
console.log('PASS: production progress handlers persist, merge tabs, refresh, unmark, reset, sanitise corrupt/unknown/duplicate data, handle full completion and keep working when storage is blocked.');
