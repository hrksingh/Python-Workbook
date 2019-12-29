#asyncio version of sync_concurrency_test.py, threading,py
#asyncio tends to perform faster than threading and synchronous method
#apart form that, they all work on single CPU processor or core
#and also on single thread(that makes it thread safe) and avoid race condition

import asyncio
import time
import aiohttp


async def download_site(session, url):
    async with session.get(url) as response:
        print("Read {0} from {1}".format(response.content_length, url))


async def download_all_sites(sites):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in sites:
            task = asyncio.ensure_future(download_site(session, url))
            tasks.append(task)
        await asyncio.gather(*tasks, return_exceptions=True)


if __name__ == "__main__":
    sites = [
        "https://realpython.com/python-concurrency/",
        "https://www.tutorialspoint.com/python/python_multithreading.htm",
        "https://pythonprogramming.net/threading-tutorial-python/",
        "https://www.toptal.com/python/beginners-guide-to-concurrency-and-parallelism-in-python",
    ] * 20
    start_time = time.time()
    asyncio.get_event_loop().run_until_complete(download_all_sites(sites))
    duration = time.time() - start_time
    print(f'Downloaded 4 websites "{len(sites)}" times in {duration} seconds')
