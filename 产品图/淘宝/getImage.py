import requests
import re
import os
from pyquery import PyQuery as pq



# 获取网页源代码

with open("IMAGES.txt","r",encoding="utf-8") as m:
	a = m.read()

b = a.split('\n')

for keywords in b:
	url = "https://www.te.com.cn/chn-zh/product-" + keywords +".html"
	headers = {
		'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"
	}

	html = requests.get(url = url,headers = headers).text
	doc = pq(html)
	img_html = doc(".product-thumbnails-scroll-wrapper ul")

	# 匹配图片地址
	img_list = re.findall('<li.*?data-src-full="(.*?)"',str(img_html),re.S)
	print(img_list)
	# 访问地址，下载到本地
	count = 0
	for i in img_list:
		url1 = "https://www.te.com.cn" + i
		print(url1)
		req = requests.get(url = url1,headers = headers).content
		path = keywords
		if not os.path.exists(path):
			os.mkdir(path)
		with open(path + "/" + str(count) + ".png","wb") as f:
			f.write(req)
		count += 1
	print(keywords + " 已完成")