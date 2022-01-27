import requests
from bs4 import BeautifulSoup 

def create_url() -> None:
    release_url = input('Please paste the url: ') 
    size = input('Please enter your size(US): ')
    
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
        "cache-control": "max-age=0",
        "sec-ch-ua": '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "none",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
    }

    response = requests.get(release_url, headers=headers)
    soup = BeautifulSoup(response.content, 'lxml')
    meta_element = soup.find("meta", {"name":"branch:deeplink:productId"})
    product_id = meta_element['content']
    preload_url = f"{release_url + '?productId=' + str(product_id) + '&size=' + str(size)}"
    print(preload_url)


if __name__ == "__main__":
    create_url()
