
import os
import requests
import json

# Auth: Generate JWT

client_id = os.environ['CLIENT_ID']
client_secret = os.environ['CLIENT_SECRET']

headers =  {"Content-Type":"application/json"}
auth_url = "https://runops.us.auth0.com/oauth/token"
creds = {
  "client_id": client_id,
  "client_secret": client_secret,
  "audience": "https://runops.us.auth0.com/api/v2/",
  "grant_type": "client_credentials"
}
response = requests.post(auth_url, json=creds, headers=headers)
token = response.json()["access_token"]

# Get squad group from current user

groups = os.environ['RUNOPS_USER_GROUPS']
groups = groups.split(',')
squad = ""
for group in groups:
    if "squad:" in group:
        squad = group

# List users

token = "Bearer " + token
api_url = "https://api.runops.io/v1/users"
headers =  {"Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": token}

print("Listing users")
response = requests.get(api_url, headers=headers)

if response.status_code == 200:
    users = response.json()
    filtered = []
    for user in users:
        if squad in user["groups"] and user["status"] == 'active':
            filtered.append(user)
    print("Users in ", squad, "=", len(filtered))
    print("Users list: ")
    for user in filtered:
      print(user)
else:
    print("Failed to create user, contact admin. Error: ", response.status_code, response.text)
