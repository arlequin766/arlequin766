from selenium import webdriver
import unittest
import time

tc = unittest.TestCase('__init__')
driver = webdriver.Chrome() # manda a llamar a chrome
driver.get('http://automationpractice.com/index.php') # Entra a esta url
#search_box = driver.find_element_by_id('search_query_top')
#search_box.send_keys('Hola mundo')
driver.find_element_by_id('search_query_top').send_keys('Hola mundo') # escribe hola mundo en el buscador

#search_box_button = driver.find_element_by_name('submit_search')
#search_box_button.click()
driver.find_element_by_name('submit_search').click() # Da clic en el buscador
time.sleep(5) # espera 5 seg a que carge la pagina

#results_label = driver.find_element_by_xpath('//*[@id="center_column"]/p')
#tc.assertEqual('No results were found for your search "Hola mundo"',results_label.text)
tc.assertEqual('No results were found for your search "Hola mundo"',driver.find_element_by_xpath('//*[@id="center_column"]/p').text) # #compara "No results were found for your search "Hola"" con //*[@id="center_column"]/p

#women_link = driver.find_element_by_link_text('Women')
#women_link.click()
driver.find_element_by_link_text('Women').click() # Da clic en la pestana de Women
time.sleep(5) # espera 5 seg a que carge la pagina

#dress_link = driver.find_element_by_partial_link_text('Dres')
#dress_link.click()
driver.find_element_by_partial_link_text('res').click() # 
time.sleep(5) # espera 5 seg a que carge la pagina


#tc.assertEqual('No results were found for your search "Hola"',driver.find_element_by_xpath('//*[@id="center_column"]/p').text) #compara "No results were found for your search "Hola"" con //*[@id="center_column"]/p
#print('es igual jajaja') # Si es igual manda mensaje

driver.close() # cierra el chrome
driver.quit() # cierra el chrome




"""
##### 
#  http://jonathansoma.com/lede/foundations-2017/classes/more-scraping/selenium/
#	Paragina para instalar y hacer test a selenium
#####
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.nytimes.com")
headlines = driver.find_elements_by_class_name("story-heading")
for headline in headlines:
    print(headline.text.strip())
"""
