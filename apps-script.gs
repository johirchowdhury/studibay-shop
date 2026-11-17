/**
 * StudiBay – অর্ডার Google Sheet-এ জমা করার Apps Script
 *
 * সেটআপ:
 * 1) আপনার Google Sheet খুলুন > Extensions > Apps Script
 * 2) এই পুরো কোড পেস্ট করে Save করুন
 * 3) Deploy > New deployment > Type: Web app
 *      Execute as: Me
 *      Who has access: Anyone
 * 4) Deploy করে যে "Web app URL" পাবেন, সেটি assets/config.js-এর SCRIPT_URL-এ বসান
 * (কোড বদলালে Deploy > Manage deployments > Edit > New version দিতে হবে)
 */
var SHEET_ID = "18-UZ7kaYzhTAB-04cRy5TQ8kbqzGd5BWeDBzgZBdnkc";
var SHEET_GID = 548329729; // আপনার দেওয়া লিংকের gid; ট্যাব না মিললে প্রথম ট্যাব ব্যবহার হবে
var HEAD = ["সময়", "পণ্য", "নাম", "মোবাইল", "ইমেইল", "TrxID", "টাকা", "পেজ", "অবস্থা"];

function doPost(e) {
  var lock = LockService.getScriptLock();
  try {
    lock.waitLock(20000);
    var d = JSON.parse(e.postData.contents);
    if (d.website) return out({ ok: true }); // বট ধরার ফাঁদ
    if (!d.name || !d.phone || !d.email || !d.trx) return out({ ok: false, error: "missing" });

    var ss = SpreadsheetApp.openById(SHEET_ID);
    var sh = ss.getSheets().filter(function (s) { return s.getSheetId() === SHEET_GID; })[0] || ss.getSheets()[0];
    if (sh.getLastRow() === 0) {
      sh.appendRow(HEAD);
      sh.getRange(1, 1, 1, HEAD.length).setFontWeight("bold");
      sh.setFrozenRows(1);
    }
    // একই TrxID দুইবার এলে সতর্কতা
    var trx = String(d.trx).toUpperCase(), status = "নতুন";
    if (sh.getLastRow() > 1) {
      var col = sh.getRange(2, 6, sh.getLastRow() - 1, 1).getValues();
      for (var i = 0; i < col.length; i++) if (String(col[i][0]).toUpperCase() === trx) { status = "ডুপ্লিকেট TrxID"; break; }
    }
    // ফোন নম্বর যেন 0 না হারায়, তাই টেক্সট হিসেবে রাখা
    var row = sh.getLastRow() + 1;
    sh.getRange(row, 4).setNumberFormat("@");
    sh.getRange(row, 1, 1, HEAD.length).setValues([[
      Utilities.formatDate(new Date(), "Asia/Dhaka", "yyyy-MM-dd HH:mm:ss"),
      d.product, d.name, d.phone, d.email, trx, d.amount, d.page, status
    ]]);
    return out({ ok: true });
  } catch (err) {
    return out({ ok: false, error: String(err) });
  } finally {
    try { lock.releaseLock(); } catch (x) {}
  }
}

function doGet() { return out({ ok: true, hello: "StudiBay order endpoint" }); }

function out(o) {
  return ContentService.createTextOutput(JSON.stringify(o)).setMimeType(ContentService.MimeType.JSON);
}
