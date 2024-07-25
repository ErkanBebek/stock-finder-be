//https://tr.tradingview.com/markets/indices/quotes-major/

// pages/api/scrape.js
import axios from 'axios';
import cheerio from 'cheerio';

export default async function handler(req, res) {
  const url = 'https://finance.yahoo.com/world-indices/';

  try {
    const response = await axios.get(url);
    const html = response.data;
    const $ = cheerio.load(html);

    const stockData = [];
    // Bekleme süresi ekleyin
   // await new Promise(resolve => setTimeout(resolve, 5000)); // 5 saniye bekleme süresi
    $('tr').each((index, element) => {
      const symbol = $(element).find('[aria-label="Symbol"]').text();
      const name = $(element).find('[aria-label="Name"]').text();
      const last = $(element).find('[aria-label="Last Price"]').text();
      const change = $(element).find('[aria-label="Change"]').text();
      const percentage_change = $(element).find('[aria-label="% Change"]').text();
      const volume = $(element).find('[aria-label="Volume"]').text();


      symbol != "" && stockData.push({ symbol,name,last,change,percentage_change,volume});
    });
    
    //console.log('Hisse Senedi Verileri:', stockData);

    res.status(200).json({ stockData });
  } catch (error) {
    res.status(500).json({ error: `Veriler çekilirken hata oluştu: ${error.message}` });
  }
}
