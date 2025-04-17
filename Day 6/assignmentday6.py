import asyncio
import aiohttp
from bs4 import BeautifulSoup


async def page(session, url):
    async with session.get(url) as response:
        return await response.text()


def ext_links(html):
    soup = BeautifulSoup(html, 'html.parser')
    links = []
    
    for link in soup.find_all('a'):
        href = link.get('href')
        if href.startswith('http'):  
            links.append(href)
    return links


async def dld_links(url):
    async with aiohttp.ClientSession() as session:
        
        html = await page(session, url)
        links = ext_links(html)
        print(f"Found {len(links)} links: {links}")


if __name__ == '__main__':
    url = 'https://www.w3schools.com/tags/ref_colornames.asp' 
    asyncio.run(dld_links(url))
