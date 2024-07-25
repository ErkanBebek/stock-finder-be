// pages/api/scrape.js
import axios from 'axios';
import cheerio from 'cheerio';

export default async function handler(req, res) {
  const url = 'https://bigpara.hurriyet.com.tr/borsa/canli-borsa/';

  try {
    const response = await axios.get(url);
    const html = response.data;
    const $ = cheerio.load(html);

    const stockData = [];
    $('.live-stock-item').each((index, element) => {
      const name = $(element).find('a').text();
      const last = $(element).find('.node-c').text()
      const bid = $(element).find('.node-f').text()
      const ask = $(element).find('.node-g').text()
      const high = $(element).find('.node-h').text()
      const low = $(element).find('.node-i').text()
      const weighted_average = $(element).find('.node-j').text()
      const change = $(element).find('.node-e').text()
      const status = $(element).find('.node-direction').attr('class').split(' ')[2]
    //   console.log( $(element).find('.node-direction').attr('class').split(' ')[2]);
      //console.log( $(element).find('.node-c').text());
    //   const value = $(element).find('.value').text();
      stockData.push({ name,last,bid,ask,high,low,weighted_average,change,status });
    });
    
    //console.log('Hisse Senedi Verileri:', stockData);

    res.status(200).json({ stockData });
  } catch (error) {
    res.status(500).json({ error: `Veriler çekilirken hata oluştu: ${error.message}` });
  }
}
