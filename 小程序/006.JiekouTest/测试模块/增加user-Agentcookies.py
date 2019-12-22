url = 'https://tianqi.moji.com/weather/china/henan/' + city
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36'}
cook = {"Cookie": 'BAIDUID=FE0F97F1FC37C47792091A2523CD945F:FG=1; HMACCOUNT=CC6D0E280C842123'}
response = requests.get(url, cookies=cook, headers=headers).content
