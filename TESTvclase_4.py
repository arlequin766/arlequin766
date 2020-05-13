from selenium import webdriver
import unittest
import time

tc = unittest.TestCase('__init__')
driver = webdriver.Chrome() # manda a llamar a chrome
driver.get('http://automationpractice.com/index.php') # Entra a esta url
driver.find_element_by_id('search_query_top').send_keys('Hola mundo') # escribe hola mundo en el buscador
driver.find_element_by_name('submit_search').click() # Da clic en el buscador
time.sleep(5) # espera 5 seg a que carge la pagina
tc.assertEqual('No results were found for your search "Hola mundo"',driver.find_element_by_xpath('//*[@id="center_column"]/p').text) # #compara "No results were found for your search "Hola"" con //*[@id="center_column"]/p
driver.find_element_by_link_text('Women').click() # Da clic en la pestaña de Women
time.sleep(5) # espera 5 seg a que carge la pagina
driver.find_element_by_partial_link_text('Dres').click() # Da clic en la pestaña de Dess (encuentra la pestaña de forma parcial al titulo)
time.sleep(5) # espera 5 seg a que carge la pagina
"""
#### Diferentes formas de encontar un elemento (En este caso no hay un ID que es lo mas importante) ###

# Link Text
driver.find_element_by_link_text('Casual Dresses').click()
# Partial Link Text
driver.find_element_by_partial_link_text('Casual ').click()
# Por Classname
driver.find_element_by_class_name('subcategory-name').click()
# Por CSSselector
driver.find_element_by_css_selector('a.subcategory-name').click()
# Por Xpath
driver.find_element_by_xpath('//*[@id="subcategories"]/ul/li[1]/h5/a').clic()
# Por Tag
driver.find_element_by_tag_name('a').clic()
"""
driver.close() # cierra el chrome
driver.quit() # cierra el chrome

