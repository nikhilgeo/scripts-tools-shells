#!/usr/bin/bash

# Takes screenshot of a web page using selenium

# Usage 1:
# File containing line separated URLs:
# python web_capture.py url_file.txt

# Usage 2:
# List of URLs hardcoded in "urls = []"
# Example: urls = ["http://127.0.0.1","https://127.0.0.1"]

# one line code
# python -c "from selenium import webdriver; driver = webdriver.Firefox(); driver.get('http://127.0.0.1'); driver.save_screenshot('capture.png'); driver.quit()"

try:
    import sys
    from selenium import webdriver
except:
    print "[!] You should have selenium installed. Run: pip install selenium"

urls = []
if sys.len>=2:
    f = open(sys.argv[1], "r")
    data = f.readlines()
    for test_url in data:
        test_url = (test_url.replace("\r")).replace("\n")
        urls.append(test_url)

driver = webdriver.Firefox()
count = 0;
for myurl in urls:
    driver.get(myurl)
    driver.save_screenshot(str(count)+'.png')
    count = count + 1
driver.quit()"
