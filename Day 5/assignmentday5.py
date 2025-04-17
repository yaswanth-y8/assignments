import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor


def download_page(url):
    
    response = requests.get(url)
    return response.text


def extract_links(html_content):
    
    soup = BeautifulSoup(html_content, 'html.parser')
    links = []
    
    for link in soup.find_all('a', href=True):
        href = link['href']
        if href.startswith('http'):  
            links.append(href)
    return links


def download_links(links):
    with ThreadPoolExecutor() as executor:
        executor.map(download_page, links)


def main(url):

    html_content = download_page(url)
    links = extract_links(html_content)
    print(f"Found {len(links)} links: {links}")
    download_links(links)



if __name__ == '__main__':
    url = 'https://www.w3schools.com/tags/ref_colornames.asp'  
    main(url)
