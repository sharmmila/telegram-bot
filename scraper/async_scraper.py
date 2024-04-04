# import httpx
# import asyncio
# from parsel import Selector
#
#
# class AsyncNewsScraper:
#     PLUS_URL = "https://www.prnewswire.com"
#     URL = 'https://www.prnewswire.com/news-releases/news-releases-list/?page={page}&pagesize=25'
#     HEADERS = {
#         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
#         "Accept-Language": "en-GB,en;q=0.5",
#         "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:124.0) Gecko/20100101 Firefox/124.0"
#     }
#     LINK_XPATH = '//div[@class="row newsCards"]//a[@class="newsreleaseconsolidatelink display-outline w-100"]/@href'
#
#     async def fetch_page(self, client, page):
#         url = self.URL.format(page=page)
#         response = await client.get(url, timeout=20.0)
#         print("страница: ", page)
#         if response.status_code == 200:
#             return Selector(text=response.text)
#         else:
#             print(f"Error in page: {page}")
#             response.raise_for_status()
#
#     async def scrape_page(self, selector):
#         links = selector.xpath(self.LINK_XPATH).getall()
#         print(links)
#
#     async def get_pages(self, limit=5):
#         async with httpx.AsyncClient(headers=self.HEADERS) as client:
#             tasks = [self.fetch_page(client, page) for page in range(1, limit + 1)]
#             pages = await asyncio.gather(*tasks)
#             scraping_tasks = [self.scrape_page(selector=selector) for selector in pages if pages is not None]
#             await asyncio.gather(*scraping_tasks)
#
#
#
# class AsyncMoviesScraper:
#     PLUS_URL = "https://doramy.club/"
#     URL = 'https://doramy.club/filmy/page/{page}'
#     HEADERS = {
#         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
#         "Accept-Language": "en-GB,en;q=0.5",
#         "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:124.0) Gecko/20100101 Firefox/124.0"
#     }
#     LINK_XPATH = '//section [@class="post-list"]/@data-url'
#
#     async def fetch_page(self, client, page):
#         url = self.URL.format(page=page)
#         response = await client.get(url, timeout=20.0)
#         print("страница: ", page)
#         if response.status_code == 200:
#             return Selector(text=response.text)
#         else:
#             print(f"Error in page: {page}")
#             response.raise_for_status()
#
#     async def scrape_page(self, selector):
#         links = selector.xpath(self.LINK_XPATH).getall()
#         print(links)
#
#     async def get_pages(self, limit=5):
#         async with httpx.AsyncClient(headers=self.HEADERS) as client:
#             tasks = [self.fetch_page(client, page) for page in range(1, limit + 1)]
#             pages = await asyncio.gather(*tasks)
#             scraping_tasks = [self.scrape_page(selector=selector) for selector in pages if pages is not None]
#             await asyncio.gather(*scraping_tasks)
#
# if __name__ == "__main__":
#     scraper = AsyncNewsScraper()
#     asyncio.run(scraper.get_pages())
#     movie_scraper = AsyncMoviesScraper()
#     asyncio.run(movie_scraper.get_pages())
