const puppeteer = require("puppeteer");
const fs = require("fs");
const dir = "./ci/screenshots";
const url = "http://127.0.0.1:8000/admin";

if (!fs.existsSync(dir)) {
  fs.mkdirSync(dir);
}

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.setViewport({
    width: 1920,
    height: 1080,
  });
  try {
  
    await page.goto(url);
    await page.screenshot({ path: dir + "/login.png" });
    await page.type("#jsusername", "admin");
    await page.type("#jspassword", "cuc123");
    await page.click('button[type="submit"]', { delay: 3000 });
    await page.waitFor(3000);
    await page.screenshot({ path: dir + "/login_in.png" });
  } catch (e) {
    console.log(e.toString());
    process.exit(1);
  } finally {
    await browser.close();
  }
})();
