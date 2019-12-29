'''
Unlike using 1 CPU core for processing multi-processing approach uses
Mutliple CPU cores to perform operation. In this approach it initialize
python interpreter to each task

'''

import requests
import multiprocessing
import time

session = None


def set_global_session():
    global session
    if not session:
        session = requests.Session()


def download_site(url):
    with session.get(url) as response:
        name = multiprocessing.current_process().name
        print(f"{name}:Read {len(response.content)} from {url}")


def download_all_sites(sites):
    with multiprocessing.Pool(initializer=set_global_session) as pool:
        pool.map(download_site, sites)


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
