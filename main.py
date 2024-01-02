import argparse
import time
import urllib.parse

from selenium import webdriver


def is_positive_integer(n):
    """Checks if a number is a positive integer."""
    try:
        n = int(n)
        return n > 0
    except ValueError:
        return False


def is_valid_url(url):
    """Checks if a string is a valid URL."""
    try:
        result = urllib.parse.urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False


options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)

command_line_arguments_parser = argparse.ArgumentParser(
    prog="Periodic-Mouse-Click-Chrome",
    description="Periodic Mouse Click on A Chrome Window",
    allow_abbrev=False,
)
command_line_arguments_parser.add_argument(
    "--desiredWebPageUrl",
    help="The Web Page Url to load on Chrome Window",
    metavar="desiredWebPageUrl",
    dest="desired_web_page_url",
)
command_line_arguments_parser.add_argument(
    "--desiredNoOfTimes",
    help="The No. Of Times the operation takes place",
    metavar="desiredNoOfTimes",
    dest="desired_no_of_times",
)
command_line_arguments = command_line_arguments_parser.parse_args()

# TODO : Extract the validations to common function
if command_line_arguments.desired_web_page_url and is_valid_url(
    command_line_arguments.desired_web_page_url
):
    desired_web_page_url = command_line_arguments.desired_web_page_url
else:
    if command_line_arguments.desired_web_page_url:
        print(
            "Invalid URL. Please enter a valid URL, including the protocol (e.g., https://)."
        )
    while True:
        desired_web_page_url = input(
            "Enter the desired web page url to load on Chrome Window : "
        )
        if is_valid_url(desired_web_page_url):
            break
        else:
            print(
                "Invalid URL. Please enter a valid URL, including the protocol (e.g., https://)."
            )

if command_line_arguments.desired_no_of_times and is_positive_integer(
    command_line_arguments.desired_no_of_times
):
    desired_no_of_times = command_line_arguments.desired_web_page_url
else:
    if command_line_arguments.desired_no_of_times:
        print("desired no. of times must be a positive integer")
    while True:
        desired_no_of_times = input(
            "Enter the desired no of times the operation takes place : "
        )
        if is_positive_integer(desired_no_of_times):
            break
        else:
            print("desired no. of times must be a positive integer")

driver.get(desired_web_page_url)
input("After Verification, Press Enter to continue...")

i = 1
while True:
    if i == desired_no_of_times:
        break
    time.sleep(15 * 60)
    driver.get(desired_web_page_url)
    i += 1
