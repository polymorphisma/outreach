import requests

df = pd.read_csv("/home/polymorphisma/adex/apollo-scraper-api/35832125-0da3-462c-a1c1-8c6f1dfa4f89.csv")

headers = {
    # 'Accept': '*/*',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    # 'Cookie': 'MyCDASDevCookie=CfDJ8D6S9Wft76tJqhcDrnh6Wb0m7pdCT8xW_lH8qFnHKlVqp4ITdWJ7Y8-i4Wr23P6eXDC1SgO8E5Lgzi1xjL2CMKAmEMCl0g0pkHo0p-p3vMrUttMvn7KucBaGylAz5Dxo-48vlOT4o17R4hwUYqPqwAwtM9uL3dpSCRmiFfbct_D03EIXX99PiiTVWRThS_0oM9voByLg-IszLJ8-BY1BZQ-V7GRmei_LM63bkjs9SLwWWSHv14ywEZ6s34i8K5QhnC-gGXG5oNu9lkd_YcJLaaaFfaC_eB5C8WxCkhu4f-NKQhHW1I0UPY8YJnoAZbQaK6D5xOtF0eIOS9fCk8JmS0SDQAFBcQu265I6AhH2Qa09iEgq2a7wJd4CX8aC21Dj43lN9vEy5hK04aGNtOGUKEBVnw1jy-x9HX7ZQTvCBISN',
    'Origin': 'https://webbackend.cdsc.com.np',
    'Referer': 'https://webbackend.cdsc.com.np/BOISIN/Home/BOISINDetails',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"'
}

reored_column = ['Website', 'Name', 'Email', "Title", "Linkedin"]
df = df[reored_column]
print(df)
df.to_csv("/home/polymorphisma/adex/apollo-scraper-api/outreach/outreach.csv", index=False)
