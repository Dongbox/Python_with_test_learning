from selenium import webdriver

browser = webdriver.Edge(r'C:\Program Files (x86)\Microsoft\edgedriver_win64\msedgedriver.exe')	#这里添加的是driver的绝对路径
browser.get('http://localhost:8000')


assert 'Django' in browser.title