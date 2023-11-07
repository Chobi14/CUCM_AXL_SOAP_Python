import os
import webbrowser
import base64
import requests
# from ms_graph import generate_access_token

APP_ID = 'a4475c21-bf3b-4f31-a013-dae63440875c'
SCOPES =['Mail.Send', 'Mail.ReadWrite']

access_token = 'eyJ0eXAiOiJKV1QiLCJub25jZSI6InVYZkxHTkFZTXFOMEJqUkVkd2kyYkJOc0Z6bHBRR1ZHS1otMUdvbTJKd0UiLCJhbGciOiJSUzI1NiIsIng1dCI6Ii1LSTNROW5OUjdiUm9meG1lWm9YcWJIWkdldyIsImtpZCI6Ii1LSTNROW5OUjdiUm9meG1lWm9YcWJIWkdldyJ9.eyJhdWQiOiIwMDAwMDAwMy0wMDAwLTAwMDAtYzAwMC0wMDAwMDAwMDAwMDAiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC81YmMwNjQ1Yi03OTMxLTQ5ZDItODhiMi00YmRhMzNjNTJiNjYvIiwiaWF0IjoxNjg0NjM0NDcwLCJuYmYiOjE2ODQ2MzQ0NzAsImV4cCI6MTY4NDYzOTcwMCwiYWNjdCI6MCwiYWNyIjoiMSIsImFpbyI6IkFWUUFxLzhUQUFBQTVONVkyZ1cyY1l2cHV4TFJlQVkveUI0S0ZXOUpHczY0OXd4ckJxK0VYNFNsYlBwNGx5UlFRTnFwWHgvWGZPNXk5c2NaSTJyQTJMZjkxNFd6cWo2bVBicHlIRFV4cVhQdWRHM2UvVjhLbHZNPSIsImFtciI6WyJwd2QiLCJtZmEiXSwiYXBwX2Rpc3BsYXluYW1lIjoiQXBwdGVzdDEiLCJhcHBpZCI6ImE0NDc1YzIxLWJmM2ItNGYzMS1hMDEzLWRhZTYzNDQwODc1YyIsImFwcGlkYWNyIjoiMSIsImZhbWlseV9uYW1lIjoiR2VybWFuIiwiZ2l2ZW5fbmFtZSI6Ikx1aXMiLCJpZHR5cCI6InVzZXIiLCJpcGFkZHIiOiI4OS4yNDUuMTU1LjU0IiwibmFtZSI6Ikx1aXMgR2VybWFuIiwib2lkIjoiZDFkNDY1ODAtNGY4Ni00ZWQ0LWFmODItNzNjZGJhOTczYjRhIiwicGxhdGYiOiIzIiwicHVpZCI6IjEwMDMyMDAyOTczNTgxOTYiLCJyaCI6IjAuQVZBQVcyVEFXekY1MGttSXNrdmFNOFVyWmdNQUFBQUFBQUFBd0FBQUFBQUFBQUJfQUVBLiIsInNjcCI6Ik1haWwuUmVhZFdyaXRlIE1haWwuU2VuZCBvcGVuaWQgcHJvZmlsZSBVc2VyLlJlYWQgZW1haWwiLCJzdWIiOiJiTVdjZmdBMDRMX29CSE16QUVYTVE4TU1qVFdVRlVSX3RyNFBRS0c4ZTVVIiwidGVuYW50X3JlZ2lvbl9zY29wZSI6Ik5BIiwidGlkIjoiNWJjMDY0NWItNzkzMS00OWQyLTg4YjItNGJkYTMzYzUyYjY2IiwidW5pcXVlX25hbWUiOiJscG9uZHV0eTIwMjNAdDh2aHoub25taWNyb3NvZnQuY29tIiwidXBuIjoibHBvbmR1dHkyMDIzQHQ4dmh6Lm9ubWljcm9zb2Z0LmNvbSIsInV0aSI6InNrVG5IdFlyYkU2RVRBU2FVR1FNQUEiLCJ2ZXIiOiIxLjAiLCJ3aWRzIjpbIjYyZTkwMzk0LTY5ZjUtNDIzNy05MTkwLTAxMjE3NzE0NWUxMCIsImI3OWZiZjRkLTNlZjktNDY4OS04MTQzLTc2YjE5NGU4NTUwOSJdLCJ4bXNfc3QiOnsic3ViIjoiRWUzaTZ4STZuWG1VSFVJUHJSeUtQaXJoelJjZ3E2NlR1QUJkR21DTDUzSSJ9LCJ4bXNfdGNkdCI6MTY4MTc2ODkzN30.VkgmIp1l0oICPxPyX_ejkMMsGDkBSjv0G90rGJLVUL2ZlJWp_Qr0qGtNt6_pVlppRSlRzFIpQyhtlLo_DxDOAnQDsDGt1nhcClhf0rA4NlfAW3JmC8kKT6Kaxz3WEk2z2PuwOveQfIT2A8TKqZbU444KsufcADETPeOYZuDuQLdQKkoFzm4VrASC453K3iOVPsTqKL3cc6vXsqXjokYmBNWZMOSLKoDcvKQhyD0o9GAHvCRHtOyIYTjiszDfV6c21C1ddIDLNd7RSFhYah8Xy5sCsdibYx3qqYkkPJhG4NmwvcIZWAaa1bqDgJsGSyxDiktJCQY1HkASLDpHIhcKTQ'


headers = {
    'Authorization' : 'Bearer ' + access_token
}

request_body = {
    "message": {
        #email subject
        "subject": "Meet for lunch?",
        "body": {
            "contentType": "Text",
            "content": "The new cafeteria is open."
        },
        "toRecipients": [
        {
            "emailAddress": {
            "address": "luisonduty2023@gmail.com"
            }
        }
      ]
    }
}

GRAPH_NDPOINT = 'https://graph.microsoft.com/v1.0/'
endpoint = GRAPH_NDPOINT + 'me/sendMail'

response = requests.post(endpoint, headers=headers, json=request_body)
if response.status_code == 202:
    print('Email sent')
else:
    print(response.content)  