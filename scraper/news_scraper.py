import requests
from parsel import Selector





class NewsScraper:
    PLUS_URL = "https://www.prnewswire.com"
    URL = 'https://www.prnewswire.com/news-releases/news-releases-list/'
    HEADERS = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-GB,en;q=0.5",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:124.0) Gecko/20100101 Firefox/124.0"
    }
    IMG_XPATH = '//div[@class="img-ratio-element"]/img/@src'

    def scrape_data(self):
        response = requests.request("GET", url=self.URL, headers=self.HEADERS)
        tree = Selector(text=response.text)
        imgs = tree.xpath(self.IMG_XPATH)[0:5].getall()
        for img in imgs:
            print(img)
        return imgs

class MoviesScraper:
    PLUS_URL = "https://rezka.ag/&/"
    URL = 'https://rezka.ag/&/?filter=popular'
    HEADERS = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-GB,en;q=0.5",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:124.0) Gecko/20100101 Firefox/124.0"
    }
    FILM_XPATH = '//div[@class="b-content__inline_item"]'

    def scrape_movies(self):
        response = requests.request("GET", url=self.URL, headers=self.HEADERS)
        tree = Selector(text=response.text)
        films = tree.xpath(self.FILM_XPATH)[0:5].getall()
        for film in films:
            print(film)
        return films



if __name__ == "__main__":
    scraper = NewsScraper()
    scraper.scrape_data()
    scraper = MoviesScraper()
    scraper.scrape_movies()
