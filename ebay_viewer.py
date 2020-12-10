import requests
import randomheaders
import time
import random
import threading


"""Threading is working so now I need to somehow allow dicord users to send me links for views they want"""

def viewer(url, views: int):
    if views > 200:
        return
    else:
        proxy = proxies={
            "http": "http://20982c0c036b4a639067f3dc6634056b:@proxy.crawlera.com:8010/",
        }

        for i in range(views):
            time.sleep(random.randint(4, 10))
            requests.get(url, proxies=proxy, headers=randomheaders.LoadHeader())
            print("{} view has been completed".format(i))


urls = []
counter = int(input("How many url's do you want to add: "))

for i in range(counter):
    urls.append(input("Enter your {} url: ".format(i + 1)))


threads = [threading.Thread(target=viewer, args=(url, 10,)) for url in urls]
for t in threads:
    t.start()

