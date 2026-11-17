#!/usr/bin/env python3
"""index.html এবং প্রতিটি প্রোডাক্টের ল্যান্ডিং পেজ তৈরি করে। চালান: python3 build.py"""
import os, html

OUT = os.path.dirname(os.path.abspath(__file__))
E = html.escape

PRODUCTS = [
 dict(
  slug="prompt-engineering", cover="c1", accent="#1d5fd1", soft="#e8f0fd",
  title="প্রম্পট ইঞ্জিনিয়ারিং", kind="ই-বুক · PDF",
  sub="এআই-কে সঠিক নির্দেশ দেওয়ার পূর্ণাঙ্গ গাইড। শূন্য থেকে শুরু করে ধাপে ধাপে শিখুন।",
  tag="Claude, ChatGPT ও Gemini, তিনটির জন্যই প্রযোজ্য",
  short="এআই-কে সঠিকভাবে নির্দেশ দিতে শিখুন। ৩৬ অধ্যায়, ৫০টি প্রম্পট টেমপ্লেট।",
  stats=[("৩৬","অধ্যায়"),("৮","ভাগ"),("৫০","প্রম্পট টেমপ্লেট"),("১১৯","পৃষ্ঠা")],
  hook_h="একই এআই, আলাদা ফল। পার্থক্য আপনার বলার ধরনে",
  hook_p="কেউ এআই থেকে চমৎকার কাজ পান, কেউ হতাশ হন। বইয়ের প্রথম অধ্যায়ের এই উদাহরণেই বিষয়টা পরিষ্কার হয়ে যায়।",
  bad="একটি ইমেইল লিখে দাও।",
  good="আমি একটি ছোট দোকানের মালিক। আমার এক নিয়মিত ক্রেতা দুই মাস ধরে বাকি টাকা দেননি। তাঁকে একটি ভদ্র কিন্তু স্পষ্ট ইমেইল লিখুন, যেন তিনি আগামী রবিবারের মধ্যে টাকা দেন। ইমেইল পাঁচ লাইনের বেশি নয়।",
  hook_note="দ্বিতীয় প্রম্পটে বলা আছে কে লিখছে, কেন, কাকে, কী সুরে, কত বড়। এআইকে আর আন্দাজ করতে হয় না। এই বই সেই বলার কৌশলগুলোই শেখায়।",
  inside_h="বইয়ের ভেতরে যা আছে",
  inside_p="আটটি ভাগ, ৩৬টি অধ্যায়। কঠিন কোনো প্রোগ্রামিং লাগে না, দরকার শুধু পরিষ্কার চিন্তা আর একটু অনুশীলন।",
  parts=[
   ("ভাগ ১","ভিত্তি","প্রম্পট কী, এআই কীভাবে উত্তর বানায়, ভুল তথ্যের ঝুঁকি এবং ভালো প্রম্পটারের মানসিকতা।","৪ অধ্যায়"),
   ("ভাগ ২","মূল কৌশল","স্পষ্টতা, প্রসঙ্গ ও কারণ, ভূমিকা নির্ধারণ, ফরম্যাট ও দৈর্ঘ্য, উদাহরণ দিয়ে শেখানো, সীমা ও নিষেধ, ধাপে ধাপে উন্নত করা।","৭ অধ্যায়"),
   ("ভাগ ৩","উন্নত কৌশল","ধাপে ধাপে চিন্তা, প্রম্পট চেইন, নিজের উত্তর যাচাই, লম্বা নথি, টেবিল ও JSON, system prompt, ওয়েব সার্চ ও ফাইল আপলোড।","৭ অধ্যায়"),
   ("ভাগ ৪","কাজভিত্তিক প্রম্পট","লেখালেখি, অনুবাদ, সারসংক্ষেপ, পড়াশোনা, ব্যবসা ও গ্রাহকসেবা, কোডিং ও Excel, ছবি ও ফাইল।","৭ অধ্যায়"),
   ("ভাগ ৫","বাংলা ভাষায় প্রম্পটিং","বাংলা না ইংরেজিতে লিখবেন, আর বাংলা উত্তরের সুর, বানান ও সংস্কৃতি কীভাবে ঠিক রাখবেন।","২ অধ্যায়"),
   ("ভাগ ৬","নিরাপত্তা ও দায়িত্ব","গোপনীয় তথ্য, prompt injection ও প্রতারণা চেনা, পক্ষপাত, কপিরাইট ও নৈতিক ব্যবহার।","৩ অধ্যায়"),
   ("ভাগ ৭","মান যাচাই ও উন্নয়ন","প্রম্পট পরীক্ষা, নিজের প্রম্পট লাইব্রেরি ও ভার্সন রাখা, ডিবাগিং চেকলিস্ট।","৩ অধ্যায়"),
   ("ভাগ ৮","বড় প্রজেক্ট","গ্রাহকসেবা সহকারীর system prompt নিয়ে পূর্ণ কেস স্টাডি, নিজের এআই সহকারী বানানো।","৩ অধ্যায়"),
  ],
  extra_h="প্রতিটি অধ্যায়ে",
  extra=["সহজ ধারণা","দুর্বল ও ভালো প্রম্পটের পাশাপাশি তুলনা","হাতে-কলমে ধাপ ও সাধারণ ভুল","“নিজে করি” অনুশীলন ও “মনে রাখি” সারকথা"],
  extra2_h="পরিশিষ্টে",
  extra2=["এক নজরে চিট শিট","৫০টি প্রম্পট টেমপ্লেট","তিন টুলে তুলনার ছক","শব্দকোষ"],
  who=[("শিক্ষার্থী ও শিক্ষক","পড়া বোঝা, কুইজ ও পাঠ পরিকল্পনা, অথচ উত্তর মুখস্থ না করে।"),
       ("ছোট ব্যবসায়ী","পণ্যের বিবরণ, ফেসবুক পোস্ট, গ্রাহকের অভিযোগের উত্তর।"),
       ("অফিসের কাজে","ইমেইল, সারসংক্ষেপ, মিটিং নোট থেকে করণীয় তালিকা, Excel ফর্মুলা।"),
       ("এআই-তে নতুনরা","প্রোগ্রামিং না জেনেই শুরু করে নিজের এআই সহকারী গড়া পর্যন্ত।")],
  faq=[("PDF কীভাবে পাব?","আপনার দেওয়া Transaction ID মিলিয়ে দেখার পর ইমেইলে PDF পাঠানো হবে। তাই ইমেইল ঠিকানা সাবধানে লিখুন।"),
       ("বইটি কি Claude, ChatGPT ও Gemini-র অফিশিয়াল বই?","না। এটি একটি স্বাধীন গাইড। Claude, ChatGPT ও Gemini যথাক্রমে Anthropic, OpenAI ও Google-এর পণ্য।")],
  cover_lines=("ই-বুক · PDF","প্রম্পট ইঞ্জিনিয়ারিং","এআই-কে সঠিক নির্দেশ দেওয়ার পূর্ণাঙ্গ গাইড"),
  author=True, code=None, send="বই", gift=None,
 ),
 dict(
  slug="mohalla-store", cover="c3", accent="#2a4b9b", soft="#e9eefb",
  title="মহল্লা স্টোর: গল্পে গল্পে পাইথন", kind="পাইথন প্রোগ্রামিং শেখার ই-বুক · PDF",
  sub="পিয়াল আর রোবো-দাদুর সাথে দোকান চালাতে চালাতে শূন্য থেকে মাঝারি স্তর পর্যন্ত পাইথন শিখুন।",
  tag="বাংলায়, গল্পে গল্পে, হাতে-কলমে",
  short="দোকানের গল্প ধরে শূন্য থেকে পাইথন। ৮ ভাগ, ৪১ অধ্যায়, মিনি প্রজেক্ট।",
  stats=[("৮","ভাগ"),("৪১","অধ্যায়"),("৭","মিনি প্রজেক্ট"),("১৮০+","পৃষ্ঠা")],
  hook_h="কোড মুখস্থ নয়, দোকান চালাতে চালাতে শেখা",
  hook_p="বইয়ের প্রতিটি ধারণা একটি দোকানের কাজের সঙ্গে জুড়ে দেওয়া। দাম, স্টক, রসিদ, বিল, সদস্য কার্ড: সব কিছুই কোডে করে দেখবেন।",
  bad=None, good=None, code='price = 120\nqty = 3\ntotal = price * qty\nprint("মোট বিল:", total)',
  hook_note="একই ছোট ধারণা থেকে শুরু হয়ে বইয়ের শেষে আপনি নিজের হাতে একটি পূর্ণ দোকান-ব্যবস্থাপনা প্রোগ্রাম বানিয়ে ফেলবেন।",
  inside_h="বইয়ের ভেতরে যা আছে",
  inside_p="আটটি ভাগ, ৪১টি অধ্যায়। প্রতিটি ভাগের শেষে একটি মিনি প্রজেক্ট, শেষে বড় প্রজেক্ট।",
  parts=[
   ("ভাগ ১","দোকান খুলি","পাইথন কী ও ইনস্টল, print, variable, ডেটা টাইপ, অপারেটর, input, f-string, comment। মিনি প্রজেক্ট: প্রথম রসিদ।","৮ অধ্যায়"),
   ("ভাগ ২","সিদ্ধান্ত ও পুনরাবৃত্তি","if-else, elif, and/or/not, for ও while লুপ, break ও continue, নেস্টেড লুপ। মিনি প্রজেক্ট: স্মার্ট বিলিং মেশিন।","৭ অধ্যায়"),
   ("ভাগ ৩","তথ্য গুছাই","list, tuple, set, dictionary, list comprehension। মিনি প্রজেক্ট: অর্ডার নেওয়ার মেশিন।","৭ অধ্যায়"),
   ("ভাগ ৪","কাজের মেশিন","function, parameter ও return, default ও keyword argument, *args ও **kwargs, scope, lambda/map/filter, recursion।","৭ অধ্যায়"),
   ("ভাগ ৫","নিরাপদ ও গোছানো","error ও try-except, ফাইলে হিসাব সংরক্ষণ, CSV ও JSON, module, নিজের module ও pip।","৫ অধ্যায়"),
   ("ভাগ ৬","দোকানকে বস্তু বানাই","class ও object, __init__, method, inheritance, __str__ ও encapsulation।","৫ অধ্যায়"),
   ("ভাগ ৭","মিডিয়াম স্তর","generator ও decorator (সহজ পরিচয়), debugging ও assert দিয়ে টেস্ট।","২ অধ্যায়"),
   ("ভাগ ৮","বড় প্রজেক্ট","সব শেখা একসঙ্গে জুড়ে নিজের পূর্ণ দোকান-ব্যবস্থাপনা প্রোগ্রাম।","পূর্ণ প্রজেক্ট"),
  ],
  extra_h="প্রতিটি অধ্যায়ে",
  extra=["গল্প দিয়ে ধারণার পরিচয়","ছোট ছোট কোড, সঙ্গে আউটপুট","সাধারণ ভুল ও সমাধান","“নিজে করি” অনুশীলন"],
  extra2_h="পরিশিষ্টে",
  extra2=["এক নজরে পাইথন চিট শিট","নির্বাচিত অনুশীলনীর উত্তর","পরের ধাপের পথনির্দেশ","শেখা শেষের সনদ"],
  who=[("একদম নতুনরা","আগে কখনো কোড না লিখলেও চলবে। বইয়ের শুরু ইনস্টল থেকে।"),
       ("স্কুল-কলেজের শিক্ষার্থী","গল্পের মতো পড়ে পড়ে প্রোগ্রামিংয়ের ভিত তৈরি।"),
       ("ছোট ব্যবসায়ী","দোকানের হিসাব, বিল ও স্টক কোডে করার ধারণা পাবেন।"),
       ("নিজে নিজে শিখতে চান যাঁরা","অনুশীলনী, উত্তর ও প্রজেক্ট দিয়ে ধাপে ধাপে এগোন।")],
  faq=[("আগে কি প্রোগ্রামিং জানা লাগবে?","না। বই শুরু হয়েছে পাইথন কী, কীভাবে ইনস্টল করতে হয় সেখান থেকে।"),
       ("PDF কীভাবে পাব?","আপনার দেওয়া Transaction ID মিলিয়ে দেখার পর ইমেইলে PDF পাঠানো হবে। তাই ইমেইল ঠিকানা সাবধানে লিখুন।"),
       ("কম্পিউটার লাগবে?","কোড চালিয়ে দেখতে একটি কম্পিউটার বা ল্যাপটপ থাকলে সবচেয়ে ভালো।")],
  cover_lines=("পাইথন · ই-বুক","মহল্লা স্টোর","গল্পে গল্পে পাইথন"),
  author=True, send="বই", gift=None,
 ),
 dict(
  slug="tasbih-first-book", cover="c2", accent="#157a5b", soft="#e5f6ee",
  title="আমার প্রথম শেখার বই", kind="শিশুদের অ্যাকটিভিটি বই · PDF · ৩+ বছর",
  sub="হাতের দাগ, সংখ্যা, আরবি হরফ, স্বরবর্ণ ও ব্যঞ্জনবর্ণ। এক বইয়েই শেখা, খেলা আর লেখার হাতেখড়ি।",
  tag="Tasbih · Learn • Play • Grow",
  short="শিশুর প্রথম শেখার একটি বই: দাগ টানা, সংখ্যা, আরবি ও বাংলা বর্ণ। A4, প্রিন্ট করে ব্যবহার।",
  stats=[("১৭১","পৃষ্ঠা (A4)"),("১১","স্বরবর্ণ"),("২৯","আরবি হরফ"),("০–১০","সংখ্যা")],
  hook_h="ছোট্ট হাত ধরে ধরে হাতেখড়ি",
  hook_p="বই খুলেই শিশু আঙুল দিয়ে ছোঁয়, পেন্সিল দিয়ে টানে, রং করে, গোল দাগ দেয়। কোনো চাপ নেই, আছে শুধু ছোট ছোট সফলতা।",
  bad=None, good=None, code=None,
  hook_note="প্রতিটি অংশ শেষে একটি তারা আঁকার জায়গা আছে। এভাবে শিশু নিজেই বুঝতে পারে সে কতদূর এগোল।",
  inside_h="বইয়ের ভেতরে যা আছে",
  inside_p="প্রতিটি পাতায় চারটি সহজ ধাপ: ছুঁয়ে চলি, বারবার টানি, ছবি পূর্ণ করি, নিজে টানি।",
  parts=[
   ("১","হাত তৈরি","সবুজ ডট থেকে লাল ডট, দাঁড়ানো ও শোয়া দাগ, ঢেউ, গোল, কোণ, বর্গ আর ত্রিভুজ। হরফ লেখার আগে হাত তৈরি।","প্রি-রাইটিং"),
   ("২","সংখ্যা ০ থেকে ১০","প্রতিটি সংখ্যার জন্য আলাদা পাতা। গুনে বলা, ট্রেস করা, ঘর রং করা, খুঁজে গোল দাগ দেওয়া। শুধু চিনতে ও গুনতে শেখা।","১১ পাতা"),
   ("৩","আরবি হরফ","২৯টি হরফ, প্রতিটি ছবির সঙ্গে। প্রতিটি আরবি শব্দে হারাকাত (যবর, যের, পেশ), সঙ্গে বাংলা উচ্চারণ ও অর্থ।","২৯ হরফ"),
   ("৪","স্বরবর্ণ","অ থেকে ঔ পর্যন্ত ১১টি বর্ণ। ছন্দ করে বলা, ছুঁয়ে লেখা, খুঁজে গোল দাগ আর ছবির সঙ্গে মেলানো।","১১ বর্ণ"),
   ("৫","ব্যঞ্জনবর্ণ","ক-বর্গ থেকে শুরু করে সব ব্যঞ্জনবর্ণ। ছবি দেখে বর্ণ চেনা, রং করা, শব্দ বেছে টিক দেওয়া।","সব বর্ণ"),
   ("৬","লেখার অনুশীলন","প্রতিটি অংশের পরে ধরে ধরে লেখার পাতা, তারপর নিজে লেখা। সব বর্ণের চার্ট পাতাও আছে।","অনুশীলন"),
  ],
  extra_h="কেন শিশুর ভালো লাগবে",
  extra=["প্রতিটি পাতায় একই ছক, তাই বুঝতে সহজ","ছবি দেখে ছন্দ করে মুখস্থ","পেন্সিল ট্রেস করার জন্য মাঝখানে ডটেড লাইন","ঘর রং করা, গোল দাগ দেওয়া, টিক দেওয়া"],
  extra2_h="বাবা-মায়ের জন্য",
  extra2=["A4 পাতা, ঘরেই প্রিন্ট করা যায়","মানুষের ছবি নেই","ইসলামী ভাবধারা, আরবি হরফে হারাকাতসহ","শেষে সনদ"],
  who=[("৩–৫ বছরের শিশু","হাতেখড়ি থেকে শুরু। চাপ ছাড়া, খেলতে খেলতে।"),
       ("মক্তব ও ঘরোয়া পাঠদান","আরবি হরফ ও বাংলা বর্ণ একসঙ্গে শেখানোর সহজ উপকরণ।"),
       ("বাবা-মা","প্রিন্ট করে শিশুর সঙ্গে বসে কাজ করার একটি ছক।"),
       ("প্লে ও নার্সারির শিক্ষক","ক্লাসে একসঙ্গে ব্যবহারের জন্য সাজানো পাতা।")],
  faq=[("বইটি কীভাবে পাব?","আপনার দেওয়া Transaction ID মিলিয়ে দেখার পর ইমেইলে PDF পাঠানো হবে।"),
       ("প্রিন্ট করতে হবে কি?","হ্যাঁ। শিশু পেন্সিল ও রং দিয়ে কাজ করবে, তাই A4 কাগজে প্রিন্ট করে নেওয়াই ভালো।"),
       ("কোন বয়সের জন্য?","৩ বছর ও তার বেশি। ছোটদের সঙ্গে বড়রা বসলে আরও ভালো।")],
  cover_lines=("৩+ · Tasbih","আমার প্রথম শেখার বই","Learn • Play • Grow"),
  author=False, send="বই", gift=None,
 ),
]

def cover(p, small=False):
    a, t, s = p["cover_lines"]
    return f'''<div class="cover {p["cover"]}{" small" if small else ""}"><div class="ct">{E(a)}</div><div><div class="ti">{E(t)}</div><div class="su">{E(s)}</div></div><div class="au">{"জহির আহাম্মদ চৌধুরী · তাছবীহ প্রকাশনী" if p["author"] else "তাছবীহ প্রকাশনী"}</div></div>'''

HEAD = '''<!doctype html>
<html lang="bn"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Hind+Siliguri:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="icon" type="image/png" href="{root}assets/favicon.png">
<link rel="stylesheet" href="{root}assets/style.css">
<style>:root{{--accent:{accent};--accent-soft:{soft}}}</style>
</head><body{bodyattr}>'''

def header(root, order_href):
    return f'''<header class="top"><div class="wrap"><a class="logo" href="{root}index.html"><img src="{root}assets/logo.png" alt="StudiBay" height="34" style="height:34px;width:auto;display:block"></a>
<nav class="nav"><a class="link" href="{root}index.html">সব বই</a><a class="btn sm" href="{order_href}">অর্ডার করুন</a></nav></div></header>'''

FOOT = '''<footer><div class="wrap"><p><img src="assets/logo-white.png" alt="StudiBay" height="30" style="height:30px;width:auto;margin-bottom:8px"><br>প্রকাশক: তাছবীহ প্রকাশনী</p><p style="margin-top:6px;opacity:.8">&copy; ২০২৬ সর্বস্বত্ব সংরক্ষিত</p></div></footer>'''

def product_page(p):
    stats = "".join(f'<div class="stat"><b>{n}</b><span>{l}</span></div>' for n, l in p["stats"])
    parts = "".join(f'<div class="card"><span class="no">{E(a)}</span><h3>{E(b)}</h3><p>{E(c)}</p><div class="meta">{E(d)}</div></div>' for a, b, c, d in p["parts"])
    who = "".join(f'<div class="card"><h3>{E(a)}</h3><p>{E(b)}</p></div>' for a, b in p["who"])
    faq = "".join(f'<details><summary>{E(q)}</summary><p>{E(a)}</p></details>' for q, a in p["faq"])
    faq += '<details><summary>বিকাশ ছাড়া অন্য মাধ্যমে দেওয়া যাবে?</summary><p>এখন শুধু বিকাশ Send Money নেওয়া হচ্ছে।</p></details>'
    faq += '<details><summary>TrxID কোথায় পাব?</summary><p>Send Money শেষ হলে বিকাশের নিশ্চিতকরণ এসএমএসে TrxID থাকে। বিকাশ অ্যাপের লেনদেনের ইতিহাসেও দেখা যায়।</p></details>'
    if p.get("bad"):
        hook = f'<div class="two"><div class="cmp bad"><h4>দুর্বল প্রম্পট</h4>{E(p["bad"])}</div><div class="cmp good"><h4>ভালো প্রম্পট</h4>{E(p["good"])}</div></div>'
    elif p.get("code"):
        hook = f'<pre>{E(p["code"])}</pre>'
    else:
        hook = ""
    li = lambda arr: "".join(f"<li>{E(x)}</li>" for x in arr)
    by = '<p class="by">লেখক জহির আহাম্মদ চৌধুরী · প্রকাশক তাছবীহ প্রকাশনী</p>' if p["author"] else '<p class="by">প্রকাশক তাছবীহ প্রকাশনী</p>'
    body = f'''{HEAD.format(title=E(p["title"])+" | StudiBay", desc=E(p["short"]), root="", accent=p["accent"], soft=p["soft"], bodyattr=f' data-slug="{p["slug"]}"')}
{header("", "#order")}
<section class="hero light"><div class="wrap grid">
 <div><span class="badge">{E(p["kind"])}</span><h1>{E(p["title"])}</h1><p class="sub">{E(p["sub"])}</p><p class="tag">{E(p["tag"])}</p>
 <div class="price"><span class="now" data-price></span><del data-regular></del><span class="off"><span data-off></span>% ছাড়</span></div>
 <a class="btn" href="#order">এখনই অর্ডার করুন</a>{by}</div>
 <div class="cv">{cover(p)}</div></div></section>
<div class="wrap"><div class="stats">{stats}</div></div>
<section class="sec"><div class="wrap"><h2>{E(p["hook_h"])}</h2><p class="lead">{E(p["hook_p"])}</p>{hook}<p class="lead" style="margin-top:16px">{E(p["hook_note"])}</p></div></section>
<section class="sec" style="padding-top:0"><div class="wrap"><h2>{E(p["inside_h"])}</h2><p class="lead">{E(p["inside_p"])}</p><div class="cards">{parts}</div>
<div class="two" style="margin-top:26px"><div><h3 style="color:var(--navy);margin-bottom:10px">{E(p["extra_h"])}</h3><ul class="list">{li(p["extra"])}</ul></div><div><h3 style="color:var(--navy);margin-bottom:10px">{E(p["extra2_h"])}</h3><ul class="list">{li(p["extra2"])}</ul></div></div></div></section>
<section class="sec" style="padding-top:0"><div class="wrap"><h2>বইটি কাদের কাজে লাগবে</h2><div class="cards" style="margin-top:18px">{who}</div></div></section>
<section class="sec order" id="order"><div class="wrap" style="max-width:720px"><h2>বইটি অর্ডার করুন</h2>
<p class="lead">বিকাশে টাকা পাঠিয়ে তথ্য জমা দিন। পেমেন্ট মিলিয়ে দেখার পর আপনার ইমেইলে PDF পাঠানো হবে।</p>
<div class="ostep"><h3><i>১</i>বিকাশে Send Money</h3>
 <div class="num"><span class="lab">বিকাশ পার্সোনাল নম্বর</span><strong data-bkash></strong><button type="button" class="btn sm ghost" id="copyNum">নম্বর কপি</button></div>
 <ol><li>বিকাশ অ্যাপ বা *২৪৭# ডায়াল করে <b>Send Money</b> বেছে নিন।</li><li>উপরের নম্বরটি দিন। এটি পার্সোনাল নম্বর, তাই Payment নয়, Send Money করতে হবে।</li><li>টাকার পরিমাণ: <b data-price></b> <del data-regular></del> (অফার মূল্য)</li><li>PIN দিয়ে নিশ্চিত করুন।</li><li>বিকাশের এসএমএস বা অ্যাপের ইতিহাস থেকে <b>Transaction ID (TrxID)</b> দেখে রাখুন।</li></ol>
 <div class="warn">নম্বর ভুল হলে টাকা অন্য কারও কাছে চলে যাবে। পাঠানোর আগে নম্বরটি আরেকবার মিলিয়ে নিন।</div></div>
<div class="ostep"><h3><i>২</i>আপনার তথ্য দিন</h3>
 <div class="done" id="done"><div class="tick">✓</div><h3 style="color:var(--navy)">অর্ডার জমা হয়েছে, ধন্যবাদ!</h3><p style="color:var(--muted);margin-top:6px">আপনার Transaction ID মিলিয়ে দেখার পর ইমেইলে PDF পাঠানো হবে।</p></div>
 <form id="orderForm" novalidate>
  <div class="sumline"><span>{E(p["title"])}</span><b data-price></b></div>
  <div class="field"><label for="name">আপনার নাম</label><input id="name" name="name" autocomplete="name" required></div>
  <div class="field"><label for="phone">মোবাইল নম্বর</label><input id="phone" name="phone" inputmode="tel" autocomplete="tel" placeholder="01XXXXXXXXX" required><small>যে বিকাশ নম্বর থেকে টাকা পাঠিয়েছেন, সেটি দিন।</small></div>
  <div class="field"><label for="email">ইমেইল</label><input id="email" name="email" type="email" autocomplete="email" required><small>এই ইমেইলেই PDF পাঠানো হবে। ভুল দিলে বই আপনার কাছে পৌঁছাবে না।</small></div>
  <div class="field"><label for="trx">বিকাশ Transaction ID</label><input id="trx" name="trx" autocapitalize="characters" required><small>এসএমএসে TrxID লেখা অংশের পরের কোডটি।</small></div>
  <input class="hp" type="text" name="website" tabindex="-1" autocomplete="off" aria-hidden="true">
  <button class="btn" type="submit" id="submitBtn" style="width:100%">অর্ডারের তথ্য জমা দিন</button>
  <div class="msg" id="msg" role="alert"></div>
 </form></div></div></section>
<section class="sec"><div class="wrap" style="max-width:720px"><h2>সাধারণ প্রশ্ন</h2>{faq}</div></section>
{FOOT}
<script src="assets/config.js"></script><script src="assets/app.js"></script></body></html>'''
    with open(os.path.join(OUT, p["slug"] + ".html"), "w", encoding="utf-8") as f:
        f.write(body)

def home():
    cards = "".join(f'''<a class="pcard" href="{p["slug"]}.html" data-p="{p["slug"]}">{cover(p, True)}<h3>{E(p["title"])}</h3><p>{E(p["short"])}</p>
<div class="pp"><b class="now"></b><del></del></div><span class="btn">বিস্তারিত ও অর্ডার</span></a>''' for p in PRODUCTS)
    body = f'''{HEAD.format(title="StudiBay | বই ও ই-বুক", desc="তাছবীহ প্রকাশনীর বাংলা ই-বুক: প্রম্পট ইঞ্জিনিয়ারিং, মহল্লা স্টোর (পাইথন) ও শিশুদের প্রথম শেখার বই।", root="", accent="#1d5fd1", soft="#e8f0fd", bodyattr="")}
{header("", "#books")}
<section class="hero"><div class="wrap" style="text-align:center;max-width:760px"><span class="badge">তাছবীহ প্রকাশনী</span><h1>শেখার তিনটি বাংলা ই-বুক</h1><p class="sub">এআই, প্রোগ্রামিং আর শিশুর হাতেখড়ি। পছন্দের বইটি বেছে নিয়ে বিকাশে অর্ডার করুন।</p><a class="btn" href="#books" style="margin-top:12px">বইগুলো দেখুন</a></div></section>
<section class="sec" id="books"><div class="wrap"><h2>আমাদের বই</h2><p class="lead">সবগুলো PDF ই-বুক। অর্ডারের পর ইমেইলে পাঠানো হয়।</p><div class="pgrid">{cards}</div></div></section>
<section class="sec" style="padding-top:0"><div class="wrap"><h2>অর্ডার করবেন যেভাবে</h2><div class="steps3" style="margin-top:26px">
<div class="card"><h3>বই বেছে নিন</h3><p>পছন্দের বইয়ের পেজে গিয়ে বিস্তারিত দেখুন।</p></div>
<div class="card"><h3>বিকাশে Send Money</h3><p>পেজে দেওয়া নম্বরে টাকা পাঠিয়ে TrxID রাখুন।</p></div>
<div class="card"><h3>তথ্য জমা দিন</h3><p>নাম, মোবাইল, ইমেইল ও TrxID দিন। মিলিয়ে দেখে ইমেইলে PDF পাঠানো হবে।</p></div></div></div></section>
{FOOT}
<script src="assets/config.js"></script><script src="assets/app.js"></script></body></html>'''
    with open(os.path.join(OUT, "index.html"), "w", encoding="utf-8") as f:
        f.write(body)

for p in PRODUCTS: product_page(p)
home()
print("done")
