import requests
url = "http://192.168.137.1:5000/frame"
str000='test1.jpg'
newname = str000.split('/')
print(newname[len(newname)-1])
files = {'file':(newname,open('test1.jpg','rb'),'image/jpg')}
r = requests.post(url,files = files)
result = r.text
print(result)