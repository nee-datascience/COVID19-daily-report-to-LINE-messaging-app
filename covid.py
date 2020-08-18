# Import required packages
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as soup

# Scraping
def Scraping(Country):
 try:
 	driver = webdriver.Edge('c:\\Python37\\msedgedriver.exe')
 	url = 'https://www.worldometers.info/coronavirus/country/'+Country

 	driver.get(url)
 	page_html = driver.page_source
 	data = soup(page_html, 'html.parser')
 	
 	new_date = data.findAll('div',{'class':'news_date'})
 	new_case = data.findAll('li',{'class':'news_li'})
 	new_cases = new_case[0].text.replace('[source]','')
 	total = new_date[0].text + ': ' + new_cases
 	driver.close()
 	return total
 except:
 	return 'No Result'

# Send message to LINE messaging app 
from songline import Sendline
token = 'cxTFICPuXUU9mgbjiJBYqgzZnxxs1jdNDNuzqHVktux'	#Web Scraping
#token = 'oOCTcbTSfucGOKrdbTTdEb1wWYn8EhIwOJuveH1zCDI'	#COVID-19 Report
messenger = Sendline(token)

message = Scraping('australia')
messenger.sendtext(message)
