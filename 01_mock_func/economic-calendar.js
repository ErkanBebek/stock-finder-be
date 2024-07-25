// pages/api/scrape.js
import axios from 'axios';
import cheerio from 'cheerio';

export default async function handler(req, res) {
  const url = 'https://fred.stlouisfed.org/releases/calendar';

  try {
    const response = await axios.get(url);
    const html = response.data;
    const $ = cheerio.load(html);

    // Tüm tarihleri ve olayları içeren bir obje oluşturun
    let data = {};

    // Tablodaki tüm satırları dolaşın
    $('table.table-condensed tbody tr').each((index, element) => {
      const date = $(element).find('span[style="font-weight: bold;"]').text().trim();
      if (date) {
        // Eğer bu tarih daha önce eklenmediyse objeye ekleyin
        if (!data[date]) {
          data[date] = [];
        }
      } else {
        // Saat ve olay adını çekin
        const time = $(element).find('td[style="width:5%; text-align:right"]').text().trim() || 'NaN';
        const event = $(element).find('td[text-align="left"] a').text().trim();

        // Sadece saat ve olay adı dolu olan satırları işle
        if (time && event && Object.keys(data).length > 0) {
          const lastDate = Object.keys(data).pop();
          data[lastDate].push({ time, event });
        }
      }
    });

    res.status(200).json({ dates: [data] });
  } catch (error) {
    res.status(500).json({ error: `Veriler çekilirken hata oluştu: ${error.message}` });
  }
}
