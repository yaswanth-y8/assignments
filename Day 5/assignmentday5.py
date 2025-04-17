import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor


def page(url):
    
    response = requests.get(url)
    return response.text


def ext_links(html):
    
    soup = BeautifulSoup(html, 'html.parser')
    links = []
    for link in soup.find_all('a'):
        href = link.get('href')
        if href.startswith('http'):  
            links.append(href)
    return links


def dld_links(links):
    with ThreadPoolExecutor() as executor:
        executor.map(page, links)


def main(url):

    con = page(url)
    links = ext_links(con)
    print(f"Found {len(links)} links: {links}")
    dld_links(links)



if __name__ == '__main__':
    url = 'https://www.w3schools.com/tags/ref_colornames.asp'  
    main(url)
