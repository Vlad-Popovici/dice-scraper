
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import re
import time



outfile = open('logfile.txt','w')



# Function 1 - Go to Login Page and log in

driver = webdriver.Firefox()
driver.get("https://www.dice.com/jobs/l-New_York%2C_NY-dcs-Recruiter-radius-100-jobs.html?searchid=9621927858174")
time.sleep(3)
try:
	for a in range (1,1500):
		try:
			driver.find_element(By.XPATH, '//li/a[@title="Go to next page"]').click()
			a = a+1
		
			
			try:
				all_email = driver.find_elements(By.XPATH, '//span[@class="hidden-xs"]/a')
				for email in all_email:
					email = email.get_attribute('href')
					print email
					outfile.write(email+'\n')
					
				
			except:
				print "There's an error"
				pass
			time.sleep(3)
		except:
			print "Reached the end of the list"
except:
	pass
print "All done! Closing log file"
outfile.close()
driver.close()
