import requests
import threading

def myhttpCall():
    url="https://webhook.site/8bf3036f-cbb1-46d0-8b55-d0445aafa41e"
    r=requests.get(url)
    print(r.headers["Date"])

threads=[]

for i in range(0,3):
    t=threading.Thread(target=myhttpCall)
    threads.append(t)
for thread in threads:
    thread.start()
 