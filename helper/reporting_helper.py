from datetime import datetime
from selenium import webdriver
import os


def take_screenshot(driver, test_name, screenshot_dir="/Users/saharshpatel/PycharmProjects/AI_Portal/screenshot"):
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    screenshot_name = f"{test_name}_{timestamp}.png"
    screenshot_path = os.path.join(screenshot_dir, screenshot_name)
    driver.save_screenshot(screenshot_path)
    return screenshot_path


def generate_html_report(test_name, result, report_dir="/Users/saharshpatel/PycharmProjects/AI_Portal/reports"):
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    report_name = f"{test_name}_{timestamp}.html"
    report_path = os.path.join(report_dir, report_name)

    with open(report_path, 'w') as file:
        file.write(result)

    return report_path
