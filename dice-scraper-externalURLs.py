
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import re
import time
import csv



outfile = open('logfile.txt','w')
driver = webdriver.Firefox()

with open('C:/Python27/Your-path/Dice scraper/recURLS.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        ext_url = str(row['Ext URLs'].strip())

		driver.get(ext_url)
		time.sleep(3)
		try:
			company_url = driver.find_elements(By.XPATH, '//div[@class="company-right"]/a[1]')
			for company in company_url:
				company = company.get_attribute('href')
				print company
				outfile.write(company+'\n')
		except:
			print "No URLs found"
			pass
					
				
			
		
print "All done! Closing log file"
outfile.close()
driver.close()
