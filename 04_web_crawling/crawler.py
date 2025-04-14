# pip3 install requests
import requests



# pip3 install requests beautifulsoup4
import requests
from bs4 import BeautifulSoup

target_url = "https://www.scrapingcourse.com/ecommerce/"

# initialize the list of discovered URLs
urls_to_visit = [target_url]

# set a maximum crawl limit
max_crawl = 20

def crawler():
    # set a crawl counter to track the crawl depth
    crawl_count = 0

    while urls_to_visit and crawl_count < max_crawl:

        # get the page to visit from the list
        current_url = urls_to_visit.pop()

        # request the target URL
        response = requests.get(current_url)
        response.raise_for_status()
        # parse the HTML
        soup = BeautifulSoup(response.text, "html.parser")

        # collect all the links
        link_elements = soup.select("a[href]")
        for link_element in link_elements:
            url = link_element["href"]

            # convert links to absolute URLs
            if not url.startswith("http"):
                absolute_url = requests.compat.urljoin(target_url, url)
            else:
                absolute_url = url

            # ensure the crawled link belongs to the target domain and hasn't been visited
            if (
                absolute_url.startswith(target_url)
                and absolute_url not in urls_to_visit
            ):
                urls_to_visit.append(absolute_url)

            # update the crawl count
            crawl_count += 1

    # print the crawled URLs
    print(urls_to_visit)

# execute the crawl
crawler()
