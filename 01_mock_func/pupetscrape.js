// pages/api/scrape.js
import puppeteer from 'puppeteer';

export default async function handler(req, res) {
  const url = 'https://finance.yahoo.com/world-indices/';

  try {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    await page.goto(url, { waitUntil: 'networkidle2' });

    const stockData = await page.evaluate(() => {
      const rows = document.querySelectorAll('tr');
      const data = [];
      rows.forEach(row => {
        const symbol = row.querySelector('[aria-label="Symbol"]')?.innerText || 'N/A';
        const name = row.querySelector('[aria-label="Name"]')?.innerText || 'N/A';
        const last = row.querySelector('[aria-label="Last Price"]')?.innerText || 'N/A';
        const change = row.querySelector('[aria-label="Change"]')?.innerText || 'N/A';
        const percentage_change = row.querySelector('[aria-label="% Change"]')?.innerText || 'N/A';
        const volume = row.querySelector('[aria-label="Volume"]')?.innerText || 'N/A';

        if (symbol !== 'N/A') {
          data.push({ symbol, name, last, change, percentage_change, volume });
        }
      });
      return data;
    });

    await browser.close();
    res.status(200).json({ stockData });
  } catch (error) {
    res.status(500).json({ error: `Veriler çekilirken hata oluştu: ${error.message}` });
  }
}
