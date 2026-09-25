/* No account, network requests, or quiz locks. Completion is stored only locally. */
(() => {
  'use strict';
  const course = document.querySelector('[data-course-ids]');
  if (!course) return;
  const ids = course.dataset.courseIds.split(',');
  const key = 'samskrita-foundation-progress-v1';
  const outline = course.querySelector('.lesson-outline');
  if (outline) {
    const desktop = matchMedia('(min-width: 60.01rem)');
    outline.open = desktop.matches;
    desktop.addEventListener('change', event => { outline.open = event.matches; });
  }
  let done = new Set();
  let storageOK = true;
  let storageMessage = '';
  function read() {
    try {
      const raw = localStorage.getItem(key);
      if (raw === null) return new Set();
      const data = JSON.parse(raw);
      if (!data || data.version !== 1 || !Array.isArray(data.completed)) throw new Error('Invalid progress');
      return new Set(data.completed.filter(id => typeof id === 'string' && ids.includes(id)));
    } catch {
      storageMessage = 'Saved progress could not be read. You can still study and mark lessons here.';
      return new Set();
    }
  }
  done = read();
  function render(message = '') {
    const count = done.size;
    course.querySelectorAll('[data-progress]').forEach(bar => { bar.max = ids.length; bar.value = count; });
    course.querySelectorAll('[data-progress-label]').forEach(el => { el.textContent = `${count} of ${ids.length} complete`; });
    course.querySelectorAll('[data-progress-status]').forEach(el => { el.textContent = message; });
    course.querySelectorAll('[data-storage-note]').forEach(el => {
      el.textContent = storageMessage || 'Saved in this browser. No account needed.';
    });
    course.querySelectorAll('[data-node]').forEach(node => {
      const complete = done.has(node.dataset.node);
      node.dataset.completed = String(complete);
      node.querySelector('[data-node-status]').textContent = complete ? '✓ Complete' : 'Open lesson';
    });
    course.querySelectorAll('[data-complete]').forEach(button => {
      const complete = done.has(button.dataset.complete);
      button.setAttribute('aria-pressed', String(complete));
      button.textContent = complete ? '✓ Complete · Mark incomplete' : 'Mark lesson complete';
    });
    const resume = course.querySelector('[data-resume]');
    if (resume) {
      const next = ids.find(id => !done.has(id));
      resume.href = `learn-${next || ids[0]}.html`;
      resume.textContent = count === 0 ? 'Start with sounds →' : next ? 'Continue learning →' : 'Revisit the first lesson →';
    }
  }
  function save() {
    try {
      localStorage.setItem(key, JSON.stringify({version:1, completed:ids.filter(id => done.has(id))}));
      storageOK = true;
      storageMessage = '';
    } catch {
      storageOK = false;
      storageMessage = 'Browser storage is unavailable. Completion marks last only on this page.';
    }
  }
  course.querySelectorAll('[data-complete]').forEach(button => button.addEventListener('click', () => {
    // Merge the latest saved state, so two open lesson tabs do not overwrite each other.
    if (storageOK) done = read();
    const id = button.dataset.complete;
    const completing = !done.has(id);
    if (completing) done.add(id); else done.delete(id);
    save();
    render(completing ? 'Lesson marked complete.' : 'Lesson marked incomplete.');
  }));
  course.querySelectorAll('[data-reset-progress]').forEach(button => button.addEventListener('click', () => {
    done = new Set();
    save();
    render('Completion marks cleared. You can start again.');
  }));
  window.addEventListener('storage', event => {
    if (event.key === key || event.key === null) {
      done = read();
      render('Progress updated from another tab.');
    }
  });
  // Refresh state after browser Back/Forward restores a page from the page cache.
  window.addEventListener('pageshow', event => {
    if (event.persisted && storageOK) { done = read(); render(); }
  });

  course.querySelectorAll('.lesson-quiz').forEach(form => {
    const questions = [...form.querySelectorAll('fieldset')];
    const summary = form.querySelector('.quiz-summary');
    function clearResults() {
      summary.textContent = '';
      questions.forEach(field => {
        delete field.dataset.result;
        const feedback = field.querySelector('.quiz-feedback');
        feedback.hidden = true;
        feedback.textContent = '';
      });
    }
    form.addEventListener('change', clearResults);
    form.addEventListener('reset', clearResults);
    form.addEventListener('submit', event => {
      event.preventDefault();
      clearResults();
      const missing = questions.filter(field => !field.querySelector('input:checked'));
      if (missing.length) {
        summary.textContent = `Choose an answer for all ${questions.length} questions. ${missing.length} unanswered.`;
        missing[0].querySelector('input').focus();
        return;
      }
      let score = 0;
      questions.forEach(field => {
        const correct = field.querySelector('input:checked').value === field.dataset.answer;
        if (correct) score++;
        field.dataset.result = correct ? 'correct' : 'incorrect';
        const feedback = field.querySelector('.quiz-feedback');
        feedback.textContent = (correct ? 'Correct. ' : `Not quite. The answer is ${feedback.dataset.correctText}. `) + feedback.dataset.explanation;
        feedback.hidden = false;
      });
      summary.textContent = `${score} of ${questions.length} correct. ` + (score === questions.length ? 'Well done. Try the practice below.' : 'Read the explanations, then try again.');
      summary.focus();
    });
  });
  render();
  course.querySelectorAll('.course-interactive').forEach(el => { el.hidden = false; });
  course.classList.add('course-ready');
})();
