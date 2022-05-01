#Or Run `pip install request` if needed.
import requests

## single ip request
# response = requests.get("http://ip-api.com/json/24.48.0.1").json()
#
# print(response['lat'])
# print(response['lon'])

# batch ip request

ip = input("Insert the ip you would like to get information on! (Ex: 208.80.152.201)\n\n")

print()

response = requests.post("http://ip-api.com/batch", json=[
  {"query": ip},
  #Add another line or replace the ip in the line above to get info on the ip you desire.
]).json()

for ip_info in response:
    for k,v in ip_info.items():
        print(k,v)
    print("\n")