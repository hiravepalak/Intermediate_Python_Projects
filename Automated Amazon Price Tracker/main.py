import bs4
import requests
import re
from requests.auth import HTTPBasicAuth

request = requests.get("https://www.amazon.in/Little-Black-Classics-Box-Penguin/dp/0141398876/ref=sr_1_1?crid=3ELTJFZYE8S91&dib=eyJ2IjoiMSJ9.nc8L3qtLUL-iCxFEcxTF4WVLpPvifZKWA8GOFK7zFvTiAT2Ea2QGmO9ck77noYFk_c-hX_ossfSqaDx31DgkYL41HcMsuQM1QBM_SxqCQXThUdaEpgId4pBLjS6mThhCpesRhvV-luU8zc6aa7e7Ai7mpLKt5hRBauVaegLgM4AIz2-oT3tm5XFE3a3Q4nGpuZQkRMB8gqabdvMj07ytODPUWIGqqkITslIVJU_X90c.avFvFXUVpqFFRAigQvQoKKhB1CxPmjyg3PQQX3f84lU&dib_tag=se&keywords=Penguin+Classics+full+set&qid=1793961961&s=books&sprefix=penguin+classics+full+se%2Cstripbooks-intl-ship%2C284&sr=1-1",
    headers={
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/jxl,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/156.0.0.0 Safari/537.36"})
request.raise_for_status()

soup = bs4.BeautifulSoup(request.text, 'html.parser')

price = soup.find("span", class_="a-price-whole")
price_html = str(price)

start_idx = price_html.find('>') + 1
end_idx = price_html.find('</')
clean_number = price_html[start_idx:end_idx].replace(",", "")

if int(clean_number) < 5000:
    url = "https://od2.in/api/sms/send"
    auth = HTTPBasicAuth("AC57414e0e946d86eb1fc71dceb5b9954c", "sk_sms_b23e7f19b5c000e388101273c1b0942351dd356f130c2e41")
    payload = {
        "from": "+15551234567",
        "to": "+18005550199",
        "body": f"ALERT! Item is now at {clean_number}! Buy now! "}

    response = requests.post(url, json=payload, auth=auth)
    print(response.json())