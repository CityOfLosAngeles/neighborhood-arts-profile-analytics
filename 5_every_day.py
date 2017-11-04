import urllib.request
from bs4 import BeautifulSoup as soup

my_url = 'http://club.5everyday.com'

req = urllib.request.Request(my_url, headers={'User-Agent': 'Mozilla/5.0'})
page_html = urllib.request.urlopen(req).read()


page_soup = soup(page_html, "html.parser")

venue_food_container = page_soup.findAll("div", {"class":"venue food"})
venue_city_container = page_soup.findAll("div", {"class":"venue city"})
venue_art_container = page_soup.findAll("div", {"class":"venue art"})
venue_music_container = page_soup.findAll("div", {"class":"venue music"})
venue_wildcard_container = page_soup.findAll("div", {"class":"venue wildcard"})

filename = "5everyday.csv"
f = open(filename, "w")

headers = "Club_Name, Store_Name, Time, Address, Phone\n"
# venue food, art, music, city, wildcard
f.write(headers)

for container in venue_food_container:
    club_name = "venue food"

    title_container = container.findAll("h3", {"class":"title"})
    store_name = title_container[0].text

    time_container = container.findAll("div", {"class":"hours"})
    time = time_container[0].text

    address_container = container.findAll("div", {"class":"address"})
    address = address_container[0].text

    neighborhood_container = container.findAll("div", {"class":"neighborhood"})
    neighborhood = neighborhood_container[0].text

    phone_container = container.findAll("div", {"class":"phone-number"})
    phone = phone_container[0].text

    f.write(club_name + "," + store_name.replace("’" , "'") + "," + time.replace("—\xa0" , "-").replace("—" , "-") + "," + address + " " + neighborhood + "," + phone.replace("—" , "-") + "\n")

for container in venue_city_container:
    club_name = "venue city"

    title_container = container.findAll("h3", {"class":"title"})
    store_name = title_container[0].text

    time_container = container.findAll("div", {"class":"hours"})
    time = time_container[0].text

    address_container = container.findAll("div", {"class":"address"})
    address = address_container[0].text

    neighborhood_container = container.findAll("div", {"class":"neighborhood"})
    neighborhood = neighborhood_container[0].text

    phone_container = container.findAll("div", {"class":"phone-number"})
    phone = phone_container[0].text

    f.write(club_name + "," + store_name.replace("’" , "'") + "," + time.replace("—\xa0" , "-").replace("—" , "-") + "," + address + " " + neighborhood + "," + phone.replace("—" , "-") + "\n")

for container in venue_art_container:
    club_name = "venue art"

    title_container = container.findAll("h3", {"class":"title"})
    store_name = title_container[0].text

    time_container = container.findAll("div", {"class":"hours"})
    time = time_container[0].text

    address_container = container.findAll("div", {"class":"address"})
    address = address_container[0].text

    neighborhood_container = container.findAll("div", {"class":"neighborhood"})
    neighborhood = neighborhood_container[0].text

    phone_container = container.findAll("div", {"class":"phone-number"})
    phone = phone_container[0].text

    f.write(club_name + "," + store_name.replace("’" , "'") + "," + time.replace("—\xa0" , "-").replace("—" , "-").replace("," , " and ") + "," + address + " " + neighborhood + "," + phone.replace("—" , "-") + "\n")

for container in venue_music_container:
    club_name = "venue music"

    title_container = container.findAll("h3", {"class":"title"})
    store_name = title_container[0].text

    time_container = container.findAll("div", {"class":"hours"})
    time = time_container[0].text

    address_container = container.findAll("div", {"class":"address"})
    address = address_container[0].text

    neighborhood_container = container.findAll("div", {"class":"neighborhood"})
    neighborhood = neighborhood_container[0].text

    phone_container = container.findAll("div", {"class":"phone-number"})
    phone = phone_container[0].text

    f.write(club_name + "," + store_name.replace("’" , "'") + "," + time.replace("—\xa0" , "-").replace("—" , "-").replace("," , " and ") + "," + address + " " + neighborhood + "," + phone.replace("—" , "-") + "\n")

for container in venue_wildcard_container:
    club_name = "venue wildcard"

    title_container = container.findAll("h3", {"class":"title"})
    store_name = title_container[0].text

    time_container = container.findAll("div", {"class":"hours"})
    time = time_container[0].text

    address_container = container.findAll("div", {"class":"address"})
    address = address_container[0].text

    neighborhood_container = container.findAll("div", {"class":"neighborhood"})
    neighborhood = neighborhood_container[0].text

    phone_container = container.findAll("div", {"class":"phone-number"})
    phone = phone_container[0].text

    #full_address = address + " " + neighborhood
    f.write(club_name + "," + store_name.replace("’" , "'") + "," + time.replace("—\xa0" , "-").replace("—" , "-") + "," + address + " " + neighborhood + "," + phone.replace("—" , "-") + "\n")

f.close()
