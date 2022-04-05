from django.test import LiveServerTestCase
from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import sys


class NewVisitorTest(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Edge(
            r'C:\Program Files (x86)\Microsoft\edgedriver_win64\msedgedriver.exe')
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    @classmethod
    def setUpClass(cls):
        for arg in sys.argv:
            if 'liveserver' in arg:
                cls.server_url = 'http://' + arg.split('=')[1]
                return
        super().setUpClass()
        cls.server_url = cls.live_server_url

    @classmethod
    def tearDownClass(cls):
        if cls.server_url == cls.live_server_url:
            super().tearDownClass()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get(self.server_url)
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute(
            'placeholder'), 'Enter a to-do item')

        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists/.+')

        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table(
            '2: Use peacock feathers to make a fly')

        # 我们使用一个新浏览器会话
        # 确保伊迪丝的信息不会从cookie中泄露出来
        self.browser.quit()
        self.browser = webdriver.Edge(
            r'C:\Program Files (x86)\Microsoft\edgedriver_win64\msedgedriver.exe')

        # 弗朗西斯访问首页
        # 页面中看不到伊迪丝的清单
        self.browser.get(self.server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)
        # 弗朗西斯输入一个新待办事项，新建一个清单
        # 他不像伊迪丝那样兴趣盎然
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        # 弗朗西斯获得了他的唯一URL
        francis_list_url = self.browser.current_url

        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)
        # 这个页面还是没有伊迪丝的清单
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)

        self.fail('Finish the test!')

    def test_layout_and_styling(self):
        # 伊迪丝访问首页
        self.browser.get(self.server_url)
        self.browser.set_window_size(1024, 768)
        # 她看到输入框完美地居中显示
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=5
        )
