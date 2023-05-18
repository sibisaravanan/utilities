import requests
from multiprocess import Process
import variables as var

def make_request(url):
    try:
        response = requests.get(url)
        print(f"URL: {url}, Status Code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred while making a request to {url}: {e}")

if __name__ == "__main__":
    url = var.url
    num_requests = var.num_requests
    for i in range(1,num_requests):
        p = Process(target=make_request, args=(url,))
        p.start()
