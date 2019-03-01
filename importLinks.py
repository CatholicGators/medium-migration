import os, sys, time, csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

LINKS_FILE = 'REAL_unimportedLinks.csv'

try:
    browser = webdriver.Chrome()
except ConnectionResetError:
    print("Unable to connect")
    sys.exit(0)

browser.get("https://medium.com/p/import")
browser.find_element_by_class_name("js-googleButton").click()
browser.find_element_by_id("identifierId").send_keys("rhc@catholicgators.org", Keys.ENTER)
time.sleep(2)
browser.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(os.environ['RHC_PASSWORD'], Keys.ENTER)
time.sleep(5)
with open(LINKS_FILE) as LinksFile:
    with open('not_imported.csv', mode='w') as notImportedFile:
        reader = csv.reader(LinksFile)
        not_imported_writer = csv.writer(notImportedFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        counter = 0
        for row in reader:
            try:
                browser.get("https://medium.com/p/import")
                browser.find_element_by_id('editor_6').send_keys(row[0])
                browser.find_element_by_class_name('button--primary').click()
                time.sleep(10)
                browser.find_element_by_tag_name('body').send_keys(Keys.ESCAPE)
                browser.find_element_by_css_selector('button.button.button--primary.button--publish.js-publishButton.js-buttonRequiresPostId').click()
                time.sleep(1)
                browser.find_element_by_class_name('js-publishButtonText').click()
                time.sleep(2)
                counter += 1
                if counter == 20:
                    # Medium only allows 20 imports a day
                    break;
            except:
                not_imported_writer.writerow(row)

