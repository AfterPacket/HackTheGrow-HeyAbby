import requests

# Define the URL
url = "https://api-fd.dutils.com/v5/gcl"

# Define the headers as a dictionary
headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Identity": "APP/com.cl.Abby;2 SYS/iOS;17.1 SDI/78f31ab2bf09e1ac3e97160acfd73687a4eaf366 FM/APPLE;iPhone14%2C3 NE/5g;313100 Lang/en-US CLV/30248 SDK/SHARESDK;40413;0 P/ TZ_America/New_York",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.9",
    "Content-Length": "481",
    "Accept-Encoding": "gzip, deflate",
    "User-Agent": "UniversalApp/2 CFNetwork/1485 Darwin/23.1.0",
}

# Define the data as a string
data = "m=AAAAhQAAAIEAAgCEJ1GXNPZ9shgWzEzaF04LQDyopHHUXQonf%2BxroaQknRO8I9uki64gC82mHkwZ6luGZinhDRQLQ1aabditiCCgympIU3JA15jJrctlvwaqBlUG7swHV3s%2B5Mq%2FfqqBWMHZYXydF%2BM%2BCbBjGZJRJ%2BlDPObsFfV9120tCN%2BJcWIAAACwf1yFxP8PD%2BiPLVFT3OIhFuyyddFllLoPEkJJvipmOzkU%2FXp0zpqRVHswdgBZqIxH3tw8jOunsb7Qgi%2FSQAk6MCYfOWuENVwG9zz8hokQbbZ3JAFE3PosEcV6fZbDOAMihWGbud%2Bl0oiXvU40WqgoCGM87NU5QFahNAHSqH1gAshmKBaCh0sSw%2Bp1Ogf9QTf%2BqOlwGBMf4c%2F%2FiGPKGhMBnmbyGjaxtDmZK%2FYswwe8yXo%3D&appkey=3800691096b93"

# Send the POST request
response = requests.post(url, headers=headers, data=data)

# Check the response status code
if response.status_code == 200:
    print("Request was successful")
    # Print the response content
    print("Response Content:", response.text)
else:
    print("Request failed with status code:", response.status_code)
