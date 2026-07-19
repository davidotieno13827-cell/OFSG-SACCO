/* OFSG Portal — site-wide JS */
document.addEventListener('DOMContentLoaded', function () {

    /* ── Hamburger nav toggle ── */
    var toggle = document.getElementById('nav-toggle');
    var links = document.getElementById('nav-links');
    if (toggle && links) {
        toggle.addEventListener('click', function () {
            links.classList.toggle('open');
            toggle.classList.toggle('active');
        });
        /* Close menu when a link is clicked */
        links.querySelectorAll('a, button').forEach(function (el) {
            el.addEventListener('click', function () {
                links.classList.remove('open');
                toggle.classList.remove('active');
            });
        });
    }

    /* ── Password show/hide toggle ── */
    document.querySelectorAll('input[type="password"]').forEach(function (input) {
        if (input.closest('.password-wrapper')) return;

        var wrapper = document.createElement('div');
        wrapper.className = 'password-wrapper';
        input.parentNode.insertBefore(wrapper, input);
        wrapper.appendChild(input);

        var btn = document.createElement('button');
        btn.type = 'button';
        btn.className = 'password-toggle';
        btn.setAttribute('aria-label', 'Show password');
        btn.innerHTML = '&#128065;';
        btn.addEventListener('click', function () {
            var isPw = input.type === 'password';
            input.type = isPw ? 'text' : 'password';
            btn.innerHTML = isPw ? '&#128584;' : '&#128065;';
            btn.setAttribute('aria-label', isPw ? 'Hide password' : 'Show password');
        });
        wrapper.appendChild(btn);
    });

});
