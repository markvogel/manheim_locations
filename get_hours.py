from bs4 import BeautifulSoup, SoupStrainer
import requests
import httplib2


def hours():
    page = requests.get("https://publish.manheim.com/en/locations/us-locations.html")
    soup = BeautifulSoup(page.content, "html.parser")
    test = soup.find_all(href=True)
    print(test)


def locations():
    http = httplib2.Http()
    status, response = http.request("https://publish.manheim.com/en/locations/us-locations.html")

    locations = []
    for link in BeautifulSoup(response, parse_only=SoupStrainer('a'), features="html.parser"):
        if link.has_attr('href'):
            if link['href'].startswith("https://publish.manheim.com/en/locations/us-locations/"):
                locations.append(link['href'])
    return locations


if __name__ == '__main__':
    manheim_locations = locations()
    print(len(manheim_locations))
