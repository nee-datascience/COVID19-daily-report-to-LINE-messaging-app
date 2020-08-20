# Import required packages
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as soup

# Define scraping function with country as input 
def Scraping(Country):
 try:
  # Specify browser driver path e.g. using MS Edge in this case. 
 	#driver = webdriver.Edge('c:\\Python37\\msedgedriver.exe')
  #driver = webdriver.Chrome('D:\\python\\chromedriver_win32\\chromedriver.exe')
  
  # Specify URL to scrape
    url = 'https://www.worldometers.info/coronavirus/country/'+Country
     
  # Get data in html format
    #Replace driver with html parser
    #driver.get(url)
    #page_html = driver.page_source
    page_html = requests.get(url).text
    
  # Beautify data from html source
    data = soup(page_html, 'html.parser')
 	
  # Get number of new cases 
    new_date = data.findAll('div',{'class':'news_date'})
    new_case = data.findAll('li',{'class':'news_li'})
    new_cases = new_case[0].text.replace('[source]','')
    total = new_date[0].text + ': ' + new_cases

  # Close website
    #driver.close()
    return total
 except:
 	return 'No Result'

# Send message to LINE messaging app 
from songline import Sendline
token = '{Enter your LINE token here}' #COVID BOT Group in LINE App
messenger = Sendline(token)

message = Scraping('australia')
messenger.sendtext(message)
message = Scraping('new-zealand')
messenger.sendtext(message)
