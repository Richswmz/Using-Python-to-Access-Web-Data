import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location:')
print('Retrieving',url)
data = urllib.request.urlopen(url,context=ctx).read()
tree = ET.fromstring(data)
num = len(data)
print('Retrieving',num,'characters')

sum = 0
count = 0
counts = tree.findall('.//comment')
for value in counts:
    sum = sum + int(value.find('count').text)
    count = count + 1
print('Count:',count)
print('Sum:',sum)


