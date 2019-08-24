# data_scrapping
###### Learning to scrap data from the Web using different techniques like BeautifulSoup+responses and Scrapy

## Structure of repo: 

1.   datascrapping : request + BeautifulSoup. Written in ***jupyter notebooks***. For more info please refer to this [tutorial](https://towardsdatascience.com/how-to-web-scrape-with-python-in-4-minutes-bc49186a8460). 
 I also provide a two *.txt* documents for a brief example

2.  quotes: using scrapy 

## Next code example is for scrappy only.
**Type in Terminal:**

`scrapy shell "http://quotes.toscrape.com/"`
###### Using css selectors
```
In [1]: response.css("title")
Out[1]: [<Selector xpath='descendant-or-self::title' data='<title>Quotes to Scrape</title>'>]



In [2]: response.css("title::text").extract()
Out[2]: ['Quotes to Scrape']


In [3]: response.css("title::text")[0].extract()
Out[3]: 'Quotes to Scrape'


In [6]: response.css("title::text").extract_first()
Out[6]: 'Quotes to Scrape'

In [7]: response.css("span.text::text").extract()
Out[7]: 
['“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”',
 '“It is our choices, Harry, that show what we truly are, far more than our abilities.”',
 '“There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.”',
 '“The person, be it gentleman or lady, who has not pleasure in a good novel, must be intolerably stupid.”',
 "“Imperfection is beauty, madness is genius and it's better to be absolutely ridiculous than absolutely boring.”",
 '“Try not to become a man of success. Rather become a man of value.”',
 '“It is better to be hated for what you are than to be loved for what you are not.”',
 "“I have not failed. I've just found 10,000 ways that won't work.”",
 "“A woman is like a tea bag; you never know how strong it is until it's in hot water.”",
 '“A day without sunshine is like, you know, night.”']

In [8]: response.css("span.text::text")[1].extract()
Out[8]: '“It is our choices, Harry, that show what we truly are, far more than our abilities.”'

In [9]: response.css(".author::text")[1].extract()
Out[9]: 'J.K. Rowling'
```
###### Using xpath selectors
````
In [1]: response.xpath("//title").extract()
Out[1]: ['<title>Quotes to Scrape</title>']


In [3]: response.xpath("//title/text()").extract()
Out[3]: ['Quotes to Scrape']


In [4]: response.xpath("//span[@class='text']/text()").extract()
Out[4]: 
['“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”',
 '“It is our choices, Harry, that show what we truly are, far more than our abilities.”',
 '“There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.”',
 '“The person, be it gentleman or lady, who has not pleasure in a good novel, must be intolerably stupid.”',
 "“Imperfection is beauty, madness is genius and it's better to be absolutely ridiculous than absolutely boring.”",
 '“Try not to become a man of success. Rather become a man of value.”',
 '“It is better to be hated for what you are than to be loved for what you are not.”',
 "“I have not failed. I've just found 10,000 ways that won't work.”",
 "“A woman is like a tea bag; you never know how strong it is until it's in hot water.”",
 '“A day without sunshine is like, you know, night.”']

In [5]: response.xpath("//span[@class='text']/text()")[1].extract()
Out[5]: '“It is our choices, Harry, that show what we truly are, far more than our abilities.”'

In [6]: response.css("li.next a").xpath("@href").extract()
Out[6]: ['/page/2/']
````

###### Storing data in ***json / csv / xml***
`scrapy crawl quotes -o items.json/csv/xml`
#
> Scraped data -> Item Containers -> json/csv files
    
> Scraped data -> Item Containers -> Pipeline -> SQL/Mongo DB
