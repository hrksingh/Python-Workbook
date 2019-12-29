#Threading Vesion of Sync_concurrency_test.py

import concurrent.futures
import requests
import threading
import time


thread_local = threading.local()


def get_session():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session


def download_site(url):
    session = get_session()
    with session.get(url) as response:
        print(f'Read {len(response.content)} from {url}')



def download_all_sites(sites):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_site, sites)


if __name__ == "__main__":
    sites = [
        "https://realpython.com/python-concurrency/",
        "https://www.tutorialspoint.com/python/python_multithreading.htm",
        "https://pythonprogramming.net/threading-tutorial-python/",
        "https://www.toptal.com/python/beginners-guide-to-concurrency-and-parallelism-in-python",
        ] * 20 #Repeat sites this many times
    
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time

    print(f'Downloaded 4 websites "{len(sites)}" times in {duration} seconds')
    
    
