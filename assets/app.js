(function () {
  var S = window.SHOP, form = document.getElementById("orderForm");
  var bn = function (n) { return String(n).replace(/\d/g, function (d) { return "০১২৩৪৫৬৭৮৯"[d]; }); };

  // দাম বসানো
  var slug = document.body.getAttribute("data-slug");
  var P = slug && S.PRODUCTS[slug];
  if (P) {
    document.querySelectorAll("[data-price]").forEach(function (e) { e.textContent = "৳" + bn(P.price); });
    document.querySelectorAll("[data-regular]").forEach(function (e) { e.textContent = "৳" + bn(P.regular); });
    document.querySelectorAll("[data-off]").forEach(function (e) { e.textContent = bn(Math.round((1 - P.price / P.regular) * 100)); });
  }
  // হোম পেজের কার্ডে দাম
  document.querySelectorAll("[data-p]").forEach(function (e) {
    var p = S.PRODUCTS[e.getAttribute("data-p")]; if (!p) return;
    e.querySelector(".now").textContent = "৳" + bn(p.price);
    e.querySelector("del").textContent = "৳" + bn(p.regular);
  });
  document.querySelectorAll("[data-bkash]").forEach(function (e) { e.textContent = S.BKASH_NUMBER; });

  var copy = document.getElementById("copyNum");
  if (copy) copy.onclick = function () {
    (navigator.clipboard ? navigator.clipboard.writeText(S.BKASH_NUMBER) : Promise.reject()).then(function () {
      copy.textContent = "কপি হয়েছে ✓";
    }, function () { copy.textContent = S.BKASH_NUMBER; });
    setTimeout(function () { copy.textContent = "নম্বর কপি"; }, 2000);
  };

  if (!form) return;
  var msg = document.getElementById("msg"), btn = document.getElementById("submitBtn");
  function show(t, c) { msg.className = "msg " + c; msg.textContent = t; }

  form.addEventListener("submit", function (ev) {
    ev.preventDefault();
    var d = {
      name: form.name.value.trim(),
      phone: form.phone.value.trim().replace(/[\s-]/g, ""),
      email: form.email.value.trim(),
      trx: form.trx.value.trim().toUpperCase(),
      website: form.website.value // honeypot
    };
    if (d.name.length < 2) return show("আপনার নাম লিখুন।", "err");
    if (!/^(\+?88)?01[3-9]\d{8}$/.test(d.phone)) return show("সঠিক মোবাইল নম্বর দিন (যেমন 017XXXXXXXX)।", "err");
    if (!/^\S+@\S+\.\S+$/.test(d.email)) return show("সঠিক ইমেইল দিন। এই ইমেইলেই বই পাঠানো হবে।", "err");
    if (d.trx.length < 6) return show("বিকাশের Transaction ID (TrxID) লিখুন।", "err");
    if (!S.SCRIPT_URL || S.SCRIPT_URL.indexOf("PASTE_") === 0) return show("সাইটের সেটআপ সম্পূর্ণ হয়নি। কিছুক্ষণ পর চেষ্টা করুন।", "err");

    d.product = P.name; d.slug = slug; d.amount = P.price; d.page = location.href;
    btn.disabled = true; btn.textContent = "জমা হচ্ছে…"; msg.className = "msg";

    // text/plain পাঠালে Apps Script-এ CORS preflight লাগে না
    fetch(S.SCRIPT_URL, { method: "POST", headers: { "Content-Type": "text/plain;charset=utf-8" }, body: JSON.stringify(d) })
      .then(function (r) { return r.json(); })
      .then(function (j) {
        if (!j.ok) throw new Error(j.error || "fail");
        form.style.display = "none";
        document.getElementById("done").classList.add("show");
        document.getElementById("done").scrollIntoView({ behavior: "smooth", block: "center" });
      })
      .catch(function () {
        btn.disabled = false; btn.textContent = "অর্ডারের তথ্য জমা দিন";
        show("জমা হয়নি। ইন্টারনেট দেখে আবার চেষ্টা করুন।", "err");
      });
  });
})();
