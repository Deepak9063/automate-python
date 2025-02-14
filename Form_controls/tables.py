import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
time.sleep(3)
num_of_rows = driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr")

num_of_columns = driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr[1]/th")

print("Number of rows",len(num_of_rows))
print("Number of columns",len(num_of_columns))

#To Print the single data
single_element = driver.find_element(By.XPATH,"//table[@name='BookTable']//tr[2]/td[3]")

#To print the multiple data
for r in range(1,len(num_of_rows)+1):
    for c in range(1,len(num_of_columns)+1):
        try:
            data = driver.find_element(By.XPATH,"//table[@name='BookTable']//tr[" +str(r)+ "]/td[" +str(c)+ "]").text
            print(data)

        except Exception as e:
            print("There was an error in retrieving the data")
print()
for r in range(2,len(num_of_rows)+1):
    authorName = driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]/td[2]").text
    print(authorName)
    if authorName=='Mukesh':
        bookName = driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]/td[1]").text
        price = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[" + str(r) + "]/td[4]").text
        print(authorName,"       ",bookName,"       ",price)


