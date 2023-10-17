import requests

# Define the URL
url = "https://www.beheyabby.com:9330/abby/plant/plantInfo"

# Define the headers as a dictionary
headers = {
    "Host": "www.beheyabby.com:9330",
    "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
    "Content-Length": "0",
    "Connection": "keep-alive",
    "Accept": "*/*",
    "Accept-Language": "en-US;q=1",
    "token": "",#changeme
    "Accept-Encoding": "gzip, deflate, br"
}

# Send the POST request
response = requests.post(url, headers=headers)

# Check the response status code
if response.status_code == 200:
    print("Request was successful")
    # Print the response content
    print("Response Content:", response.text)
else:
    print("Request failed with status code:", response.status_code)
