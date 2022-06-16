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

# Create user 
      
email = '{{user_email}}'
name = '{{user_name}}'
role = '{{user_role}}'
role = "meta_role:" + role

token = "Bearer " + token
api_url = "https://api.runops.io/v1/users"
headers =  {"Content-Type": "application/json",
            "Authorization": token}

data = {}
data['name'] = name
data["email"] = email
data["status"] = "active"
data["groups"] = [squad,role]

print("Creating user: ", data)
response = requests.post(api_url, json=data, headers=headers)

if response.status_code == 201:
    print("User created: ", response.text)
else:
    print("Failed to create user, contact admin. Error: ", response.status_code, response.text)
