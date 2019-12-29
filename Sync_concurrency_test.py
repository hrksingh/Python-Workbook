#Synchronous I/O bound example
#Non Concurrent solution to test speed

import requests
import time



def download_site(url: str, session: str): -> None:
    with session.get(url) as response:
        print(f'Read {len(response.content)} from {url}')




def download_all_site(sites: str): -> None:
    with requests.Session() as session:
        for url in sites:
            download_site(url, session)




if __name__ == "__main__":
    sites = [
        "https://realpython.com/python-concurrency/",
        "https://www.tutorialspoint.com/python/python_multithreading.htm",
        "https://pythonprogramming.net/threading-tutorial-python/",
        "https://www.toptal.com/python/beginners-guide-to-concurrency-and-parallelism-in-python",
        ] * 20 #Repeat sites this many times
    
    start_time = time.time()
    download_all_site(sites)
    duration = time.time() - start_time

    print(f'Downloaded 4 websites "{len(sites)}" times in {duration} seconds')
    
    
        
        
