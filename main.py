import argparse
import time

from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome("chromedriver", options=options)

command_line_arguments_parser = argparse.ArgumentParser(prog='Periodic-Mouse-Click-Chrome',
                                                                description='Periodic Mouse Click on A Chrome Window',
                                                                allow_abbrev=False)
command_line_arguments_parser.add_argument('--desiredWebPageUrl',
                                                   help='The Web Page Url to load on Chrome WIndow',
                                                   metavar='desiredWebPageUrl', dest='desired_web_page_url')
command_line_arguments = command_line_arguments_parser.parse_args()
if command_line_arguments.desired_web_page_url:
    desired_web_page_url = command_line_arguments.desired_web_page_url
else:
    desired_web_page_url = input("Enter the desired web page url to load on Chrome Window : ")

driver.get(desired_web_page_url)
input('After Verification, Press Enter to continue...')

while True:
    time.sleep(15*60)
    driver.get(desired_web_page_url)

