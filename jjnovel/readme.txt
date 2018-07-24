###爬虫框架scrapy练习


创建scrapy工程
scrapy startproject jianshu

工程目录：
  jjnovel/
    scrapy.cfg
    jjnovel/
        __init__.py
        items.py
        pipelines.py
        settings.py
        spiders/
            __init__.py
            jjnovelSpider.py


运行scrapy爬虫
scrapy crawl jjnovel

可直接运行工程main.py文件
cmdline.execute("scrapy crawl jjnovel".split())



