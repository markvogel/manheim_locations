from bs4 import BeautifulSoup, SoupStrainer
import requests
import httplib2
import csv


def hours(location):
    page = requests.get(location)
    soup = BeautifulSoup(page.content, "html.parser")
    # test = soup.contents()
    # div = soup.find(id="hours")
    h = soup.find_all(id="hours")
    print(h)
    # print(div)
    # print(soup.get_text())
    # print(h.get_text())


def parse_hours(location):
    page = requests.get(location)
    soup = BeautifulSoup(page.content, "html.parser")
    h = soup.find(id="hours")
    p = h.find_next_sibling('p')
    return p.get_text()


def locations():
    http = httplib2.Http()
    status, response = http.request("https://publish.manheim.com/en/locations/us-locations.html")

    location_list = []
    for link in BeautifulSoup(response, parse_only=SoupStrainer('a'), features="html.parser"):
        if link.has_attr('href'):
            if link['href'].startswith("https://publish.manheim.com/en/locations/us-locations/"):
                location_list.append(link['href'])
    return location_list


if __name__ == '__main__':
    manheim_locations = locations()
    print(manheim_locations)
    # print(manheim_locations[-1])
    # test_location = str(manheim_locations[-1])
    locations_hours = []

    for i in manheim_locations:
        try:
            locations_hours.append([i, parse_hours(i)])
        except AttributeError:
            continue
    print(locations_hours)
    print(len(locations_hours))
    rows = zip(locations_hours)
    with open("manheim_hours.csv", 'w') as myfile:
        writer = csv.writer(myfile)
        for row in rows:
            writer.writerow(row)






























