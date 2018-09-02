import requests

def myhttpCall():
    url="https://webhook.site/8bf3036f-cbb1-46d0-8b55-d0445aafa41e"
    r=requests.get(url)
    print(r.headers["Date"])

for i in range(0,3):
    myhttpCall()  