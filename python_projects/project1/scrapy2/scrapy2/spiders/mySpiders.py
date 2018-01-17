####
import scrapy;
class MySpider(scrapy.Spider):
    name="mySpider";

    def start_requests(self):
        urls=["http://www.newsmth.net/nForum/#!board/PieLove"];
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse);

    def parse(self,response):
        page=response.url.split("/")[-2];
        fileNamne="sm_%s_.html" % page;
        with open(fileName,'wb') as f:
            f.write(response.body);
        self.log("saved file %s" % fileName);

