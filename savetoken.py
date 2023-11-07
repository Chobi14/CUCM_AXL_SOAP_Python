#import requests
import webbrowser
import msal

print("Hi")

#Setting the app id
app_id = "a4475c21-bf3b-4f31-a013-dae63440875c"
#Specify the role you want to use
SCOPES = ['User.Read']

access_token_cache = msal.SerializableTokenCache()

#Make the connectivity between 
client = msal.PublicClientApplication(client_id=app_id, token_cache=access_token_cache)

flow = client.initiate_device_flow(scopes=SCOPES)
print('user' + flow['user_code'])

webbrowser.open(flow['verification_uri'])

token_response = client.acquire_token_by_device_flow(flow)
print(token_response)

# print(access_token_cache.serialize())
# access_id = acces_token['access_token']
with open('api_token_access.json', 'w') as _f:
    _f.write(access_token_cache.serialize())

