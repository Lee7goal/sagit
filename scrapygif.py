#author:sagit
#date:2018.3.11
import scrapy
import os,sys
import requests
import re
class scarpyone(scrapy.Spider):
                name = "stackone"
                start_urls = ["http://qq.yh31.com/ql/bd/"]
                def parse(self,response):
                    hrf = response.xpath('//*[@id="main_bblm"]/div[2]/dl/dd/li')
                    for li in hrf:
                        item = {}
                        href = li.xpath('a/@href').extract()
                        hreftext = li.xpath('a/text()').extract()
                        full_url = 'http://qq.yh31.com' + ''.join(list(href))
                        hreftext = ''.join(list(hreftext))
                        # 文件夹名称
                        if hreftext == '>更多>':
                            continue
                        path = 'C:\GIF'
                        if not os.path.exists(path):
                            os.makedirs(path)
                        item['dirname'] = hreftext
                        yield scrapy.Request(url=full_url, meta={'key': item}, callback=self.parse1)

                    def parse1(self, response):
                        ite = {}
                        full_url = []
                        url1 = response.xpath('//*[@id="pe100_page_infolist"]/a[2]/@href').extract()
                        url2 = response.xpath('//*[@id="pe100_page_infolist"]/a[2]/@href').re('\d+')
                        url1 = ''.join(url1)
                        url1 = url1.split('_')
                        url2 = ''.join(url2)
                        ite['dirn'] = response.meta['key']['dirname']
                        for i in range(1, int(url2) + 1):
                            full_url = 'http://qq.yh31.com' + url1[0] + '_' + str(i) + '.html'
                            # print(full_url)
                            yield scrapy.Request(url=full_url, meta={'key1': ite}, callback=self.parse2)

                def parse2(self, response):
                    p1 = response.meta['key1']['dirn']
                    resp = response.xpath('//*[@id="main_bblm"]/div[1]/li/dt/a')
                    path = 'C:\GIF\\' + ''.join(p1)
                    if not os.path.exists(path):
                        os.makedirs(path)
                    for lst in resp:
                        alt = lst.xpath('img/@alt').extract()
                        src = lst.xpath('img/@src').extract()
                        src = 'http://qq.yh31.com' + ''.join(list(src))
                        alt = ''.join(list(alt))
                        html = requests.get(src)
                        with open(path + '\\' + alt + '.gif', 'wb') as file:
                            file.write(html.content)

