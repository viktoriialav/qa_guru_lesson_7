import os
import time

import requests
from selene import browser, query
from selenium import webdriver
import pytest

from script_os import TMP_DIR


def test_download_file_fisrt_way():
    options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": TMP_DIR,
        "download.prompt_for_download": False
    }
    options.add_experimental_option("prefs", prefs)
    browser.config.driver_options = options

    browser.open("https://github.com/pytest-dev/pytest/blob/main/README.rst")

    browser.element('[data-testid="download-raw-button"]').click()
    time.sleep(5)


def test_download_file_second_way():
    browser.open("https://github.com/pytest-dev/pytest/blob/main/README.rst")
    download_url = browser.element('[data-testid="raw-button"]').get(query.attribute("href"))
    content = requests.get(url=download_url).content

    with open(os.path.join(TMP_DIR, "readme2.rst"), 'wb') as file:
        file.write(content)

    with open(os.path.join(TMP_DIR, "readme2.rst")) as file:
        file_content_str = file.read()
        assert "test_answer" in file_content_str






