# -*- coding: utf-8 -*-
'''
This os an example of spider for forum working with scrapy lib.
'''

__author__ = "YO_N"
__license__= "MIT"


import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from aks.items import AkusherstvoItem
import datetime


class AksCrawlSpider(CrawlSpider):
    name = 'aks_crawl' #naming a spider (needed for activation)
    allowed_domains = ['forum.akusherstvo.ru'] #the name of the domain where spider could crawl
    start_urls = ['http://forum.akusherstvo.ru/viewforum.php?f=173'] #link for starting a crawl (DepthFSearch)
    custom_settings = {
        'DOWNLOAD_DELAY': 1,
        'CLOSESPIDER_ITEMCOUNT':100
    }
    
    #Rules for ccrawling between pages in forum
    rules = (
        
        Rule(LinkExtractor(restrict_xpaths='//*[contains(@class, "forumtitle")]'),
            follow=True),
        Rule(LinkExtractor(restrict_xpaths='//*[contains(@class, "topictitle")]'),
            follow=True),
        Rule(LinkExtractor(restrict_xpaths='//*[contains(@class, "right-box right")]'),
            callback='parse_item',follow=True)
    )

    def parse_item(self, response):
        sel = Selector(response) #creating a selector 
        posts = sel.xpath('//div[@class="post bg1"] | //div[@class="post bg2"]') #selecting posts
        for post in posts:
            i= AkusherstvoItem()#transferring items into container (created separately)
            i['main_topic'] = sel.xpath('//*[contains(@class,"linklist navlinks")]/li[1]/a[2]/text()').extract() #Retrieving main topic
            i['forum_topic'] = sel.xpath('//*[contains(@class,"linklist navlinks")]/li[1]/a[3]/text()').extract() #Retrieving sub-topic
            i['title_topic'] = sel.xpath('//*[@id="wrap"]/h2/a/text()').extract() # Retrieving title in post
            i['author'] = post.xpath('div/dl/dt/a/text()[normalize-space()] | div/dl/dt/strong/text()[normalize-space()]').extract() 
            i['post_text'] = post.xpath('div/div[1]/div/text()[normalize-space()]').extract()
            i['post_date'] = post.xpath('div/div[1]/p/text()[normalize-space()]').extract()
            yield i
