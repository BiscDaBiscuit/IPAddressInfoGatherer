#Or Run `pip install request` if needed.
import requests

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