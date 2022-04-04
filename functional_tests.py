from selenium import webdriver
import unittest



class NewVisitTestCase(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Edge(r'C:\Program Files (x86)\Microsoft\edgedriver_win64\msedgedriver.exe')
        self.browser.implicitly_wait(3)
    def tearDown(self):
        self.browser.quit()
    
    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

unittest.main(warnings='ignore')
        