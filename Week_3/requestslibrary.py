#simplifies the process of sending HTTP requests and interracting with web services and APIs    
#First install the library using PIP
#(Get Requests library using pip install requests)

import requests

response = requests.get('https://api.github.com/events')
print(response.txt)

#Sending a POST request
#payload = {'key1': 'value1', 'key2': 'value2'}
#response = requests.post('https://httpbin.org/post', data=payload)
#print(response.text)

#Requests also supports HTTP methods like PUT,DELETE,HEAD,OPTIONS,TRACE
#PUT request example
#response = requests.put('https://httpbin.org/put', data={'key': 'value'})

#DELETE request example
#response = requests.delete('https://httpbin.org/delete')

#HEAD request example
#response = requests.head('https://httpbin.org/get')

#OPTIONS request example
#response = requests.options('https://httpbin.org/get')

#Handling Parameters and Headers


#Error Handling
#You can check the status code of the response to determine if the request was successful
#response.raise_for_status()  # Raises an HTTPError for bad responses (4xx or 5xx)
    

