
# coding: utf-8

# In[2]:


# WEB SCRAPING


# In[6]:


import requests
from bs4 import BeautifulSoup
import pandas
import argparse
import connect


# In[8]:


parser = argparse.ArgumentParser()
parser.add_argument("--page_num_max",help="Enter the no: of pages to parse", type=int)
parser.add_argument("--dbname", help="Enter the name of db", type=int)
args=parser.parse_args()

oyo_url = "https://www.oyorooms.com/hotels-in-bangalore/?page="
page_num_MAX=3
scraped_info_list=[]
connect.connect(dbname)

for page_num in range(1, page_num_MAX):
    url=oyo_url + str(page_num)
    print("Get Request for: " +url)
    req=requests.get(url)
    content= req.content


    soup=BeautifulSoup(content, "html.parser")

    all_hotels = soup.find_all("div", {"class": "hotelCardListing"})
    

    for hotel in all_hotels:
        hotel_dict={}
        hotel_dict["name"] = hotel.find("h3", {"class":"ListingHotelDescription__hotelName"}).text
        hotel_dict["address"] = hotel.find("span", {"itemprop": "streetAddress"}).text
        hotel_dict["price"] = hotel.find("span", {"class": "ListingPrice__finalPrice"}).text
    
        try:
            hotel_dict["rating"] = hotel.find("span", {"class": "hotelRating__ratingSummary"}).text
        except AttributeError:
            hotel_dict["rating"] = None
    
        parent_amenities_element = hotel.find("div", {"class": "amenityWrapper"})
    
        amenities_list=[]
        for amenity in parent_amenities_element.find_all("div", {"class": "amenityWrapper__amenity"}):
            amenities_list.append(amenity.find("span", {"class": "d-body-sm"}).text.strip())
        
        hotel_dict["amenities"]= ', '.join(amenities_list[:-1])  
    
        scraped_info_list.append(hotel_dict)
        connect.insert_into_table(args.dbname, tuple(hotel_dict.values()))
    
dataFrame=pandas.DataFrame(scraped_info_list)
dataFrame.to_csv("Oyo.csv")
connect.get_hotel_info(args.dbname)

