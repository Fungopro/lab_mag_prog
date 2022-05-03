import asyncio
import time
import aiohttp


async def download_site(session, url):
    async with session.get(url) as response:
        async with print(f"Read {0} from {1}".format(response.text(), url)) as p:
            return f"Read {0} from {1}".format(response, url)


async def download_all_sites(sites):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in sites:
            task = asyncio.ensure_future(download_site(session, url))
            tasks.append(task)
        res = await asyncio.gather(*tasks, return_exceptions=True)
        return res


if __name__ == "__main__":
    sites = [
        "https://yandex.ru",
    ] * 2
    start_time = time.time()
    asyncio.get_event_loop().run_until_complete(download_all_sites(sites))
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} sites in {duration} seconds")
