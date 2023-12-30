import requests
import json
import time
from datetime import date
#GetDate
today = date.today()
print("Collection on" + today.strftime("%B %d, %Y"))
#Variables Definations
limit = 15
timeout = 7200
mainurl = "https://dashboard.honeygain.com/api/v1"
#Fetch Token
url = mainurl + "/users/tokens?passthrough_parameters=%7B%7D"
payload = json.dumps({
      "email": "<email>",
      "password": "<pass>"
})
headers = {
      'Content-Type': 'application/json'
}
response = requests.request("POST", url, headers=headers, data=payload)
token = response.json()
#Acquire Token for Auth Requests
tokenv = token["data"]["access_token"]
print("Fetching token Successfull !!")  
#Check for Daily Limit Reached for getting Winnings
print("Checking for "+str(limit) +"MB Limit")
def getdaily():
  today = mainurl+"/earnings/today"
  payloads = {}
  headers2 = {
      'Authorization' : "Bearer "+ tokenv
  }
  responses = requests.request("GET", today, headers=headers2, data=payloads)
  todays = responses.json()
  bytes = todays["gathering_bytes"]/ 1024 / 1024
  count = todays["total_credits"]
  return count,bytes
daily = getdaily()
count,bytes = daily
while bytes <= limit:
  daily = getdaily()
  count,bytes = daily
  print(f"Gathered sp far {bytes:.2f} of "+str(limit)+"MB")
  print("Collection so far : "+str(count))
  print("Going Sleep for "+str(timeout)+ " seconds")
  time.sleep(timeout)

print(f"Gathered sp far {bytes:.2f} of "+str(limit)+"MB")
print("Collection so far : "+str(count))

#Daily Limit Reached Req for Lucky pot opening
header2 = {
      'Authorization' : "Bearer "+ tokenv
}
url2 = mainurl + "/contest_winnings"
payload2 = {}
response2 = requests.request("POST", url2, headers=header2, data=payload2)
winning=response2.json()
try:
  credited = winning["data"]["credits"]
  honeygain="Honeygain Credited "+ str(credited)
  requests.post("https://ntfy.sh/<subscription>",
    data=honeygain,
    headers={
        "Title": "Daily Auto honeygain",
        "Priority": "default",
        "Tags": "tada,bee"
  })
except:
  error= winning["title"]
  print(winning["details"])
  requests.post("https://ntfy.sh/<subscription>",
    data=error,
    headers={
        "Title": "ERROR : Daily Auto honeygain",
        "Priority": "default",
        "Tags": "exclamation,bee"
  })


#print(winning["data"]["credits"]+ " Earned Today")