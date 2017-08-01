import time
import json
import Review
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys



searchURL = "https://www.glassdoor.com/Reviews/index.htm"


def get_company_list(driver, URL, startPage, endPage, state_list, refresh):
	dict = {}
	finished_number = 0
	topURL = None
	for state in state_list:
		time.sleep(2)
		driver.get(URL)
		try:
			location_field = driver.wait.until(EC.presence_of_element_located((By.ID,"LocationSearch")))
			search_button = driver.find_element_by_id("HeroSearchButton")
			location_field.send_keys(state)
			time.sleep(1)
			search_button.click()
			time.sleep(10)
		except TimeoutException:
			print("TimeoutException! Location field or search button not found on glassdoor.com")

		time.sleep(1)

		if finished_number == 0:
			handles = driver.window_handles
			for handle in handles:
				if handle != driver.current_window_handle:
					print 'switch to ', handle
					driver.switch_to_window(handle)
					topURL = driver.current_url
		else:
			topURL = driver.current_url
		print topURL

		state_company_list(driver,topURL,startPage,endPage,state)

		finished_number += 1
	return dict

def state_company_list(driver,topURL,startPage,endPage,state):
	while startPage <= endPage:
		time.sleep(2)
		print "\n" + state + ":Page " + str(startPage) + " of " + str(endPage)
		currentURL = topURL[:-4] + "_IP" + str(startPage) + ".htm"
		driver.get(currentURL)
		print "Getting " + currentURL
		time.sleep(3)
		startPage += 1

f __name__ == "__main__":
	driver = init_driver()
	time.sleep(3)
	print "Logging into Glassdoor account ..."
	login(driver, username, password)
	time.sleep(5)
	print "\nStarting to get all company list..."
	state_list = ["CA","IN","SC"]
	get_company_list(driver, searchURL, 1, 1, state_list, True)
	driver.quit()
#endif
