// S&S Legal website: menu, theme switch, copy buttons and the consultation form.
(function () {
  'use strict';

  // Mobile menu
  var menuBtn = document.getElementById('menu-btn');
  var mobileNav = document.getElementById('mobile-nav');
  if (menuBtn && mobileNav) {
    menuBtn.addEventListener('click', function () {
      var open = mobileNav.hidden;
      mobileNav.hidden = !open;
      menuBtn.setAttribute('aria-expanded', String(open));
      menuBtn.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    });
    mobileNav.addEventListener('click', function (e) {
      if (e.target.tagName === 'A') {
        mobileNav.hidden = true;
        menuBtn.setAttribute('aria-expanded', 'false');
        menuBtn.setAttribute('aria-label', 'Open menu');
      }
    });
  }

  // Light / dark theme. The visitor's system setting applies until they choose.
  var themeBtn = document.getElementById('theme-btn');
  if (themeBtn) {
    themeBtn.addEventListener('click', function () {
      var root = document.documentElement;
      var current = root.getAttribute('data-theme');
      if (!current) {
        current = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
      }
      var next = current === 'dark' ? 'light' : 'dark';
      root.setAttribute('data-theme', next);
      try { localStorage.setItem('ss-theme', next); } catch (err) { /* storage unavailable */ }
    });
  }

  // Copy phone numbers and email
  document.querySelectorAll('.copy[data-copy]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var text = btn.getAttribute('data-copy');
      var label = btn.textContent;
      var done = function () {
        btn.textContent = 'Copied';
        setTimeout(function () { btn.textContent = label; }, 1500);
      };
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(done, function () { selectNext(btn); });
      } else {
        selectNext(btn);
      }
    });
  });
  function selectNext(btn) {
    var target = btn.previousElementSibling;
    if (!target) return;
    var range = document.createRange();
    range.selectNodeContents(target);
    var sel = window.getSelection();
    sel.removeAllRanges();
    sel.addRange(range);
  }

  // Consultation form.
  // Without a form service configured, it opens the visitor's email app with the
  // request filled in, addressed to the firm. To use a form service instead
  // (for example Formspree), set the form's data-endpoint attribute; see README.
  document.querySelectorAll('form.consult').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var status = form.querySelector('.status');
      var get = function (name) { var el = form.elements[name]; return el ? el.value.trim() : ''; };
      var name = get('name');
      var contact = get('phone') || get('email');
      if (!name || !contact) {
        status.textContent = 'Please give your name and a phone number or email address so we can reply.';
        status.hidden = false;
        return;
      }
      var endpoint = form.getAttribute('data-endpoint');
      if (endpoint) {
        status.textContent = 'Sending…';
        status.hidden = false;
        fetch(endpoint, { method: 'POST', body: new FormData(form), headers: { Accept: 'application/json' } })
          .then(function (res) {
            if (!res.ok) throw new Error('send failed');
            form.reset();
            status.textContent = 'Thank you. Your request has been sent, and we will reply within one working day.';
          })
          .catch(function () {
            status.textContent = 'Your request could not be sent. Please call +233 24 447 6615 or email info@sslegal.org.';
          });
        return;
      }
      var body = 'Name: ' + name + '\nPhone / WhatsApp: ' + get('phone') + '\nEmail: ' + get('email') +
        '\nArea: ' + get('area') + '\n\n' + get('message');
      var href = 'mailto:info@sslegal.org?subject=' + encodeURIComponent('Consultation request from ' + name) +
        '&body=' + encodeURIComponent(body);
      window.location.href = href;
      status.textContent = 'Your email app should open with your request ready to send. If it does not, email info@sslegal.org or call +233 24 447 6615.';
      status.hidden = false;
    });
  });
})();
