from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re
js = 'C:\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe'
driver = webdriver.PhantomJS(js)
driver.set_window_size(1400,1000)
driver.get('https://calverthall.myschoolapp.com/app#login')

time.sleep(0.5)
username = driver.find_element_by_id('Username')
username.send_keys('XXXXXX')

password = driver.find_element_by_id('Password')
password.send_keys('XXXXXX')

driver.find_element_by_id("loginBtn").click()

time.sleep(1)

driver.get('https://calverthall.myschoolapp.com/api/datadirect/ParentStudentUserAcademicGroupsGet?userId=3591871&schoolYearLabel=2017+-+2018&memberLevel=1&persona=2&durationList=74251&markingPeriodId=')
page_source = (driver.page_source)
matches = re.findall('(?<="cumgrade":")(.*?)(?=",)', page_source, re.DOTALL)
classes = ['Econ: ', 'APES: ', 'Stats: ', 'English: ', 'Calc: ', 'Religion: ']
x = 0
for className in classes:
	print(className + matches[x])
	x = x + 1
results = map(float, matches)
print ("\nAverage: " + str((sum(results) / len(results))))
pause = raw_input("")
