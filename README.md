# Amazon Scraper using Scrapy

This Scrapy project is designed to scrape product information from Amazon's website. **Note**: Scraping Amazon may violate their terms of service, and certain precautions such as respecting robots.txt, rate limiting, and using proxies are essential to avoid being blocked.

## Project Setup

1. **Install Scrapy**:
   Ensure you have Python installed, then install Scrapy using pip:

   ```bash
   pip install scrapy
   ```

2. **Create a Scrapy Project**:
   If you haven’t created a Scrapy project yet, run:

   ```bash
   scrapy startproject scrapyproject
   ```

3. **Navigate to the project directory**:
   ```bash
   cd scrapyproject
   ```

4. **Generate Spider**:
   Create a new spider to scrape Amazon products by running the following command:

   ```bash
   scrapy genspider amazon_spider amazon.com
   ```

## Project Structure

The main structure of the project should look something like this:

```
scrapyproject/
│
├── scrapyproject/
│   ├── __init__.py
│   ├── items.py
│   ├── middlewares.py
│   ├── pipelines.py
│   ├── settings.py
│   └── spiders/
│       └── amazon_spider.py
├── scrapy.cfg
```

## Spider Example (`amazon_spider.py`)

Here is an example of the spider you can use to scrape Amazon product details like name, price, and rating.

```python
import scrapy
from ..items import AmazonScraperItem

class AmazonSpider(scrapy.Spider):
    name = 'amazon_spider'
    
    # Sample product search page URL
    start_urls = ['https://www.amazon.com/s?k=laptops']

    def parse(self, response):
        items = AmazonScraperItem()
        
        # Loop through each product
        for product in response.css('div.s-main-slot div.s-result-item'):
            title = product.css('h2 a span::text').get()
            price = product.css('span.a-price span.a-offscreen::text').get()
            rating = product.css('span.a-icon-alt::text').get()
            
            items['title'] = title
            items['price'] = price
            items['rating'] = rating
            
            yield items

        # Pagination - follow next page links
        next_page = response.css('li.a-last a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
```

## Items Definition (`items.py`)

Define the fields to store the scraped data in `items.py`:

```python
import scrapy

class AmazonScraperItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    rating = scrapy.Field()
```

## Essential Changes in `settings.py`

Here are some important configurations you should make in the `settings.py` file to prevent getting blocked and to ensure successful scraping.

```python
# settings.py

# Set the user agent to mimic a real browser
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'

# Obey robots.txt rules (set to False, but be cautious)
ROBOTSTXT_OBEY = False

# Enable logging to get more details during scraping
LOG_LEVEL = 'INFO'

# Configure the download delay (Amazon is strict with scraping)
DOWNLOAD_DELAY = 2

# Maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 1

# Enable retry middleware in case of failures
RETRY_ENABLED = True
RETRY_TIMES = 3

# Enable automatic throttling to avoid getting blocked
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 2
AUTOTHROTTLE_MAX_DELAY = 6
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
AUTOTHROTTLE_DEBUG = False

# Enable pipelines to save data (configure as per your needs)
ITEM_PIPELINES = {
   'scrapyproject.pipelines.AmazonScraperPipeline': 300,
}

# Rotating user agents and using proxies (Optional)
# Consider using the Scrapy-UserAgents or Scrapy-Proxies libraries to rotate user agents and proxies
# to minimize the chance of being blocked by Amazon.
```

## Scrapy Commands

### 1. **Running the Spider**

To start scraping, use the following command:

```bash
scrapy crawl amazon_spider
```

### 2. **Storing the Results in JSON/CSV**

To save the scraped data into a JSON or CSV file:

```bash
# Save output to a JSON file
scrapy crawl amazon_spider -o output.json

# Save output to a CSV file
scrapy crawl amazon_spider -o output.csv
```

### 3. **Scrapy Shell (For Testing Selectors)**

To test your selectors, you can use the Scrapy shell to interactively scrape and debug elements on the Amazon page:

```bash
scrapy shell 'https://www.amazon.com/s?k=laptops'
```

### 4. **View Logs**

Check the log files to review the status of your scraping jobs:

```bash
tail -f scrapy.log
```

## Disclaimer

Please note that scraping Amazon's website may violate their terms of service. It is important to review and follow their policies. Use this tool responsibly and ensure you comply with legal requirements and Amazon's rules when performing web scraping.

