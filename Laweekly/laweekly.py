import urllib.request
from bs4 import BeautifulSoup as soup
import sys

"""
my_url = 'http://www.laweekly.com/calendar?dateRange[]=2017-11-07'
"""

date_year = input("Enter a year:")
date_month = input("Enter a month:")
date_day = input("Enter a day:")

def calendar(year, month, day):
    return year + "-" + month + "-" + day

my_url = 'http://www.laweekly.com/calendar?dateRange[]=' + calendar(date_year, date_month, date_day)



req = urllib.request.Request(my_url, headers={'User-Agent': 'Mozilla/5.0'})
page_html = urllib.request.urlopen(req).read()


page_soup = soup(page_html, "html.parser")

event_container = page_soup.findAll("li", {"class":"recommended"})

filename = "laweekly " + calendar(date_year, date_month, date_day) + ".csv"
f = open(filename, "w")

headers = "Recommended_Event_Name, Location, Price\n"

"""f.write("Recommended Events\n")"""
f.write(headers)

for container in event_container:

    title_container = container.find("div", {"class":"deets list"}).find("div", {"class":"title"})
    event_name = title_container.text.strip()

    location_container = container.find("div", {"class":"deets list"}).find("div", {"class":"location"})
    location = location_container.text.strip()

    if container.find("div", {"class":"tix"}).find("span", {"class":"price"}):
        price_container = container.find("div", {"class":"tix"}).find("span", {"class":"price"})
        price = price_container.text.strip()
    else:
        price_container = container.find("div", {"class":"tix"})
        price = price_container.text.strip()

    f.write(event_name.replace("," , " ").replace("\"" , "") + "," + location.replace("," , " ").replace("&commat;", "@") + "," + price.replace("," , " ") + "\n")


daily = page_soup.findAll("div", {"class":"result-day"})

"""f.write("\n\nOther Events\n")"""
f.write("Other_Event_Name, Location, Price\n")

for other in daily[1].ul.findAll("li"):

	if other.find("div", {"class": "deets list"}) != None:
		title = other.find("div", {"class": "deets list"}).find("div", {"class" : "title"})
		#print (title.text.strip())

		location = other.find("div", {"class": "deets list"}).find("div", {"class" : "location"})
		#print (location.text.strip())

		if other.find("div", {"class": "tix"}).find("span", {"class" : "price"}):
			price = other.find("div", {"class": "tix"}).find("span", {"class" : "price"}).text.strip()
			#print (price)
		else:
			price = other.find("div", {"class": "tix"}).text.strip()
			#print (price)

		f.write(title.text.strip().replace(",", " ").replace("\xe1", "?").replace("\xae", "?").replace("\xe9", "?").replace("’" , "'").replace("\"" , "") + "," + location.text.strip().replace(",", " ").replace("&commat;", "@") + "," + price.replace(",", " ") + "\n")

print("File: \"laweekly " + calendar(date_year, date_month, date_day) + ".csv\" " + "has been created")
f.close()
