import scrapy


class ProductsSpider(scrapy.Spider):
    name = "products"

    def start_requests(self):
        yield scrapy.Request(
            "https://www.amazon.com/s?k=python+for+beginners",
            headers={
                "User-Agent": (
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/120.0.0.0 Safari/537.36"
                ),
                "Accept-Language": "en-US,en;q=0.9",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            },
            meta={"page": 1},
            callback=self.parse
        )

    def parse(self, response):
        page = response.meta.get("page", 1)
        books = response.css('div[data-component-type="s-search-result"]')

        self.logger.info(f"Page {page}: found {len(books)} items")

        for book in books:
            title = book.css("h2 span::text").get()

            whole = book.css("span.a-price-whole::text").get()
            fraction = book.css("span.a-price-fraction::text").get()

            if whole:
                whole = whole.replace(",", "").replace(".", "").strip()
                price = f"{whole}.{fraction.strip()}" if fraction else whole
            else:
                price = None

            yield {
                "page": page,
                "title": title,
                "price": price,
            }

        # --- Pagination ---
        # Amazon renders a dedicated "next" arrow link with
        # class="s-pagination-next" when more pages exist. It disappears
        # (or gets an "s-pagination-disabled" class with no href) on the
        # last page, which is what naturally stops the recursion below.
        next_page = response.css("a.s-pagination-next::attr(href)").get()

        if next_page is not None:
            yield response.follow(
                next_page,
                headers={
                    "User-Agent": (
                        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                        "AppleWebKit/537.36 (KHTML, like Gecko) "
                        "Chrome/120.0.0.0 Safari/537.36"
                    ),
                    "Accept-Language": "en-US,en;q=0.9",
                },
                meta={"page": page + 1},
                callback=self.parse
            )
        else:
            self.logger.info(f"No more pages. Total pages scraped: {page}")

    def closed(self, reason):
        # Called once when the spider finishes, regardless of how many
        # pages it ended up crawling.
        self.logger.info(f"Spider closed. Reason: {reason}")