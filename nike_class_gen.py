import requests
from bs4 import BeautifulSoup 

class GenerateEarlyURL:
    def __init__(self, release_url: str, size: str) -> None:
        self.release_url = release_url
        self.size = size

        self.headers = {
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
    
    def create_url(self) -> None:
        response = requests.get(self.release_url, headers=self.headers)
        soup = BeautifulSoup(response.content, 'lxml')
        meta_element = soup.find("meta", {"name":"branch:deeplink:productId"})
        product_id = meta_element['content']

        preload_url = f"{self.release_url + '?productId=' + str(product_id) + '&size=' + str(self.size)}"
        print(preload_url)


if __name__ == "__main__":
    GenerateEarlyURL(input('Please paste the url: '), input('Please enter your size(US): ')).create_url()
