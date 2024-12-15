from lxml import etree
import requests
import json
import threading
import queue import Queue
import time
class Heima:
    def __init__(self):
        self.headers ={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'}
        self.url_queue = Queue()
        self.html_queue = Queue()
        self.content_queue = Queue()    
    def get_url_queue(self):
        url_temp = "http://bbs.itheima.com/forum-231-{}.html"
        url_list = [url_temp.format(i) for i in range(1,201)]
        for url in url_list:
            self.url_queue.put(url)
    def get_html_queue(self):
        while True:
            url = self.url_queue.get()
            html_source_page = requests.get(url,headers=self.headers).text
            self.html_queue.put(html_source_page)
            self.url_queue.task_done()
    def parse_html(self):
        while True:
            content_list = []
            html = self.html_queue.get()
            html_str = etree.HTML(html)
            node_list = html_str.xpath('//th[contains(@class,"new") and contains(@class,"forumtit")]')
            title_num = 0
            for node in node_list:
                title = node.xpath('./a[1]/text()')[0]
                url = node.xpath('./a[1]/@href')[0]
                author = node.xpath('./div[@class="foruminfo"]//a/span/text()')[0]
            release_time = node.xpath('./div[2]/i/span[1]text()')[0].strip().replace('@', '')
            one_page = node.xpath('./div[2]/i/span[1]/span/@title')
            if one_page:
                if title_num < len(one_page):
                    release_time = node.xpath('./div[2]/i/span[1]/span/@title')[title_num]
            else:
                release_time = node.xpath('./div[2]/i/span[1]/text()')[0].strip().replace('@', '')
            item = {
                "文本标题":title,
                "文本链接": url,
                "文本作者": author,
                "发布时间": release_time,
            }
            content_list.append(item)
            title_num += 1
        self.content_queue.put(content_list)
        self.html_queue.task_done()
    def save_data(self):
        while True:
            content_list = self.content_queue.get()
            with open('thread-heima.json', 'a+', encoding='utf-8') as f:
                f.write(json.dumps(content_list,ensure_ascii=False,indent=2))
            self.content_queue.task_done()
    def run(self):
        thread_list = []
        t_url = threading.Thread(target=self.get_url_queue)
        thread_list.append(t_url)
        for page in range(9):
            t_content = threading.Thread(target=self.get_html_queue)
            thread_list.append(t_content)
        for j in range(9):
            t_content = threading.Thread(target=self.parse_html)
            thread_list.append(t_content)
        t_save = threading.Thread(target=self.save_data)
        thread_list.append(t_save)
        for t in thread_list:
            t.setDaemon(True)
            t.start()
        for q in [self.url_queue,self.html_queue,self.content_queue]:
            q.join()
    if __name__ == '__main__':
        heima = HeiMa()
        heima.run()
