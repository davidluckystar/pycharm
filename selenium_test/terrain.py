from lettuce import before, after, world
from selenium import webdriver
from mapping import site_mapping

@before.harvest
def setup(server):
    # world - ����������, ������������ lettuce ����� ����� �������� ������, �.�. �������� � ���� ���������� ����� �������
    my_proxy = "proxy:3128"
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--proxy-server=http://%s' % my_proxy)
    world.driver = webdriver.Chrome('C:\Python34\chrome_driver\chromedriver.exe',chrome_options=chrome_options)
    world.mapping = site_mapping # ��������� ��������� � world

@after.all
def teardown(total):
    world.browser.close() # ��������� �������