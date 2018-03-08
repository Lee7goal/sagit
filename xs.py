import requests
import re
import urllib

def novel_url():
    resp = requests.get('https://www.ybdu.com/book1/0/1/')
    resp.enoding='gbk'
    novle_add = r'<li class="three"><a href = "(.*?)">'
    novel_url = re.findall(novle_add,resp.text)
    return novel_url
def click_url():
    resp = requests.get(url)
    resp.encoding = 'gbk'
    nol_add = r'class = "btopt"><a href="(.*?)" title='
    nol_url = re.findall(nol.add,resp.text)
    return nol_url
def part(nl_url):
    resp = requests.get(nl_url)
    resp .encoding = 'gbk'
    part_add = r'<li><a href="(.*?)">'
    part_url = re.findall(part_add,resp.text)
    return part_url
def content(content_url):
    resp = requests.get(content_url)
    resp.encoding = 'gbk'
    content_add = r'<div id = "htmlContent" class = "contentbox">(.*?)<'
    title_add = r'</a> &gt;<a href = ".*?">(.*?)</a> &gt; <a href ="'
    content = re.findall(content_add,resp.text.replace('\n',''))
    title = re.findall(title_add,resp.text)
    return content,title
def write(content,title):
    ft=open('\\D:\\小说\\%s.txt'%title,'a',encoding = 'utf-8')
    for rc in cont:
        rc = rc.replace('%nbsp;','').replace(('\n',''))
        ft.write(rc+'\n')
    ft.close()
novel_url = novel_url()
for url in novel_url:
    nol_url = click_url(url)
    for nl_url in nol_url:
        part_url = part(nl_url)
        for pt_url in part_url:
            content_url = nl_url + pt_url
            cont,title= content(content_url)
            write(content,title[0])
            #break
