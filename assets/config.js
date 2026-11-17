// ====== এই ফাইলে দাম, নম্বর ও Sheet-এর লিংক বদলান ======
window.SHOP = {
  // Google Apps Script Web App URL (apps-script.gs ডিপ্লয় করার পর এখানে বসান)
  SCRIPT_URL: "https://script.google.com/macros/s/AKfycbzFi4e44YSNGY-O0x2vPCX_I9rO1vLwLuwnulZNEUe6mwUsMvSG0XczRgPOuGQQh9G-gA/exec",

  BKASH_NUMBER: "01674350524",

  // slug: পেজের ফাইলের নাম; price = অফার মূল্য, regular = আসল মূল্য
  PRODUCTS: {
    "prompt-engineering": { name: "প্রম্পট ইঞ্জিনিয়ারিং ই-বুক", price: 99,  regular: 499 },
    "mohalla-store":      { name: "মহল্লা স্টোর: গল্পে গল্পে পাইথন", price: 99,  regular: 499 },
    "tasbih-first-book":  { name: "আমার প্রথম শেখার বই", price: 99,  regular: 299 }
  }
};
