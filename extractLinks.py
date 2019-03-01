from xml.dom import minidom
import csv

wordpressExport = minidom.parse('export.xml')
linkElements = wordpressExport.getElementsByTagName('link')
linksList = list(link.firstChild.data for link in linkElements)
with open('links.csv', mode='w') as linksFile:
    link_writer = csv.writer(linksFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for link in linksList:
        link_writer.writerow([link])
