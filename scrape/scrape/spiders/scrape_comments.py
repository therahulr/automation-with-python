import scrapy
import re

class GirlsComments(scrapy.Spider):
    name = 'girls_comments'
    allowed_domains = ['https://www.stylecraze.com/']
    start_urls = ['https://www.stylecraze.com/articles/compliments-for-girls/']

    def parse(self, response):
        file_name = '../scraped_data/comments.txt'

        for comment in response.xpath('//ol/li'):
            comment_text = comment.get()
            comment_text = comment_text.replace('<li>', '')
            comment_text = comment_text.replace('</li>', '')
            other_tags = re.findall(r'<.*?>', comment_text)
            for tag in other_tags:
                comment_text = comment_text.replace(tag, '')

            with open(file_name, 'a') as f:
                f.write(comment_text+'\n')
