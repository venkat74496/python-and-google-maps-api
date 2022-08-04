import requests, json
import time
# enter your api key here
api_key = 'AIzaSyD3m3dl8VztKczjl2C0iyK61Qv6KSxeBL8'
  
# url variable store url
url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"
  
# The text string on which to search
query = input('Search query: ')


# get method of requests module
# return response object
r = requests.get(url + 'query=' + query +
                        '&key=' + api_key)



# json method of response object convert
#  json format data into python format data
x = r.json()
  
# now x contains list of nested dictionaries
# we know dictionary contain key value pair
# store the value of result key in variable y
z=x['next_page_token']
print(z)
y = x['results']
  
# keep looping upto length of y
for i in range(len(y)):
      
    # Print value corresponding to the
    # 'name' key at the ith index of y
    print(y[i]['name'])

d= requests.get(url + 'query=' + query +
                        '&key=' + api_key+ '&pageToken='+ z)
time.sleep(10)
e=d.json()
f=e['results']
for j in range(len(f)):
    print(f[j]['name'])




