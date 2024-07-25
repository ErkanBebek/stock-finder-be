//https://tr.tradingview.com/markets/indices/quotes-major/

// pages/api/scrape.js
import axios from 'axios';
import cheerio from 'cheerio';

export default async function handler(req, res) {
  const url = 'https://markets.businessinsider.com/indices';

  try {
    const response = await axios.get(url);
    const html = response.data;
    const $ = cheerio.load(html);

    const stockData = [];
    $('tbody>tr').each((index, element) => {
      //const symbol = $(element).find('a.deep-sea-blue').attr('title');
      const symbol = $(element).find('a.deep-sea-blue').attr('title');
      const symbolcountry = $(element).find("td").html().split("<br>")[1].trim();
      const last = $(element).find("td").filter(".text-right").html().split("<br>")[0].trim();
      const prev_close = $(element).find("td").filter(".text-right").html().split("<br>")[1].trim();
      const balance = $(element).find("td").filter(".text-right").find("span").html();
      const percentage_change = $(element).find("td").filter(".text-right").eq(1).text().trim().split("\n")[1];
      const time = $(element).find("td").filter(".text-right").eq(2).find("span").eq(0).text();
      const date = $(element).find("td").filter(".text-right").eq(2).text().trim().split("\n")[1];
      const ytd = $(element).find("td").filter(".text-right").last().text().trim().split("\n")[0];
      const one_year = $(element).find("td").filter(".text-right").last().text().trim().split("\n")[1];
      // const name = $(element).find('[aria-label="Name"]').text();
      // const last = $(element).find('[aria-label="Last Price"]').text();
      // const change = $(element).find('[aria-label="Change"]').text();
      // const percentage_change = $(element).find('[aria-label="% Change"]').text();
      // const volume = $(element).find('[aria-label="Volume"]').text();


       symbol != null &&   stockData.push({ symbol,symbolcountry,last,prev_close,balance,percentage_change,time,date,ytd,one_year});
    });
    
    //console.log('Hisse Senedi Verileri:', stockData);

    res.status(200).json({ stockData });
  } catch (error) {
    res.status(500).json({ error: `Veriler çekilirken hata oluştu: ${error.message}` });
  }
}
