# *_* coding: UTF-8 *_*
# TEAM: Okroie
# TIME: 2022/10/17 17:54
# DEVELOPER: Zhao
# FILENAME: StockCra.PY
# IDL: PyCharm
# 微信公众号/哔哩哔哩：偶颗
# 官网：http://okroie.cn


'''
什么是编程？编程就是人将事物按照一定规范抽象为代码，一段段代码组成程序，完整的程序就构成了一个软件应用。
学习编程就像学习一门外语(但又要有理科思维)，首先学习语法框架，其次在实际应用

1. 联想应用商店官网：https://lestore.lenovo.com
2. 更换pip下载源(国内清华源)的命令：pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
'''


# import re
# def func1():
#     print('姓' + '赖')
# def func2():
#     print(len('姓赖'))
#     a = '  c         '
#     print(a.strip())
#     b = '1,2,3,4,5'
#     print(b.split(',')) # .split()方法默认以空格分割
#     c = '姓耐'
#     print(c.replace(c, '赖'))
#     d1 = '成功需要努力'
#     d2 = re.sub('努力', '坚持', d1)
#     print(d2)
#     e1, e2 = 100, str(100)
#     print(type(e1), type(e2))
# def fun3():
#     for i in range(1, 10):
#         print(str(i) + '---左边是阿拉伯数字')
# def fun4(x, y): # 括号里面的代表形参
#     z = x + y
#     if z >= 0:
#         return z
#     else:
#         print('你向函数fun4传入的两个实参之和小于0')
# def main():
#     print('函数func1()运行结果如下：')
#     func1()
#     print()
#     print('函数func2()运行结果如下：')
#     func2()
#     print()
#     print('函数func3()运行结果如下：')
#     fun3()
#     print()
#     print('函数func4()运行结果如下：')
#     print('z =', fun4(1, 5))
# if __name__ == '__main__':
#     main()

# def a(w):
#     print('你好啊！')
#     s = w * 2 - 10
#     return s
# print(a(10))


# a = 'd d ds'
# s = a.split()
# print(s)
# print(''.join(s))

# for a in range(100):
#     print(a)

# a = 0
# while 1:
#     print(a)
#     a = a + 1
#     # print(a)

# a = 100
# if a > 0:
#     print(123)
# elif a < 22:
#     print(22)
# else:
#     print(222)




'''
1. 什么是网络爬虫?
网络爬虫（又称为网页蜘蛛，网络机器人，在FOAF社区中间，更经常的称为网页追逐者），是一种按照一定的规则，自动地抓取万维网信息的程序或者脚本。
另外一些不常使用的名字还有蚂蚁、自动索引、模拟程序或者蠕虫
中文名: 网络爬虫
外文名: web crawler
别名: 网络蜘蛛、蠕虫
目的: 按要求获取万维网信息
作用: 抓取网站上的信息
算法: 网络拓扑、基于网页内容和基于用户访问行为三种算法
简而言之，就是通过代码程序批量获取目标数据

2. 什么是算法？
算法（Algorithm）是指解题方案的准确而完整的描述，是一系列解决问题的清晰指令，算法代表着用系统的方法描述解决问题的策略机制。
也就是说，能够对一定规范的输入，在有限时间内获得所要求的输出。
如果一个算法有缺陷，或不适合于某个问题，执行这个算法将不会解决这个问题。不同的算法可能用不同的时间，空间或效率来完成同样的任务。
一个算法的优劣可以用空间复杂度与时间复杂度来衡量。

3. 如何实现网络爬虫？
获取数据 + 解析数据 + 反反爬 = 网络爬虫

4. Edge浏览器的webdriver驱动下载地址：https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
'''


# # 获取数据
# from selenium import webdriver
# url = 'http://www.neea.edu.cn/'
# browser = webdriver.Edge()
# browser.get(url)
# data = browser.page_source
# print(data)
# browser.quit()

# import urllib.request, random
# from fake_useragent import UserAgent
# urb = urllib.request.build_opener()
# urb.addheaders = [('User-Agent', UserAgent().random)]
# urllib.request.install_opener(urb)
# url = 'https://diannao.jd.com'
# res = urllib.request.urlopen(url)
# print(res.read().decode('utf-8'))

# import requests
# url = 'http://www.neea.edu.cn/'
# res = requests.get(url)
# res.encoding = 'utf-8'
# print(res.text)


# # 解析数据
# from selenium import webdriver
# import re
# url = 'https://guba.eastmoney.com/'
# browser = webdriver.Edge()
# browser.get(url)
# data = browser.page_source
# browser.close()
# title = '<a href=".*?" title="(.*?)"'
# ti = re.findall(title, data)
# for i in range(len(ti)):
#     print(str(i + 1), ti[i])
# a = [1, 2, 4]
# print(a[2])


# import re
# # a = 'sd111111111111'
# # # print(a)
# # print(re.findall('sd.*?', a))
#
# a = '123as1'
# print(re.findall('123.*?', a))



# from selenium import webdriver
# from bs4 import BeautifulSoup
# option = webdriver.EdgeOptions()
# option.add_argument('--headless')
# browser = webdriver.Edge(options=option)
# def batch(tas):
#     url = 'https://so.eastmoney.com/web/s?keyword=' + tas
#     browser.get(url)
#     data = browser.page_source
#     soup = BeautifulSoup(data, 'html.parser')
#     a = soup.select('.news_item_t a')
#     for j in range(len(a)):
#         print(a[j].text)
#         print(a[j]['href'])
# tas = ['腾讯', '阿里', '字节跳动']
# for i in tas:
#     try:
#         batch(i)
#         print(i, 'Ok' + '\n\n')
#     except Exception as e:
#         print(i, 'gosh and reason:', e)


# from selenium import webdriver
# import requests, re, time
# import pandas as pd
# browser = webdriver.Edge()
# url = 'http://www.sse.com.cn/disclosure/credibility/supervision/inquiries/'
# browser.get(url)
# time.sleep(3)
# data = browser.page_source
# table = pd.read_html(data)[0]
# print(table)


# # DIY
# # import this
# import re
# from selenium import webdriver
# url = 'https://www.baidu.com/s?rtt=1&bsst=1&cl=2&tn=news&ie=utf-8&word=%E4%B8%AD%E5%9B%BD'
# browser = webdriver.Edge()
# browser.get(url)
# data = browser.page_source
# # print(data)
#
# title = '<a href=.*?aria-label="标题：(.*?)"'
# ti = re.findall(title, data)
# # print(ti)
# href = '<a href=(.*?)aria-label="标题：.*?"'
# time = '<span.*?aria-label="发布于：(.*?)">'
# resource = 'aria-label="新闻来源：(.*?)">'
# hf = re.findall(href, data)
# te = re.findall(time, data)
# rs = re.findall(resource, data)
#
# for i in range(len(ti)):
#     hf[i] = re.sub('" target="_blank" class="news-title-font_1xS-F" ', '', hf[i])
#     hf[i] = hf[i].replace('"', '')
#     print(str(i + 1) + ':', ti[i], te[i], rs[i])
#     print(hf[i])


# Python里的股票第三方库
# import tushare
# info = tushare.pro_api('token值')
# h = info.daily(ts_code='', start_date='', end_date='')
# print(h)