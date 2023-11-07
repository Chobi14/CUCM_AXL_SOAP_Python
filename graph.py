# Temporary placeholder
# Library - interact with web calls !! marking a warning beacuse of the selected interpreter
import requests
# Library - Pretty print
from pprint import pprint
# Library - Regex --- Not needed at this time
import re
# Library - working with JSON structure
import json

## Reading an excel file using Python with pandas
# import pandas lib as pd !! marking a warning beacuse of the selected interpreter
import pandas as pd

# Library - configparser to read the config file 
from configparser import SectionProxy
# Library - azure connectivity
from azure.identity.aio import ClientSecretCredential
# Library - azure - MS  authentication library MSAL  
# https://learn.microsoft.com/en-us/entra/identity-platform/msal-overview
from kiota_authentication_azure.azure_identity_authentication_provider import (
    AzureIdentityAuthenticationProvider
)
# Library - Working with sdk by using ms graph as preloaded API
from msgraph import GraphRequestAdapter, GraphServiceClient
# Library - Importing the user module to retrieve user information that is included in the SDK
from msgraph.generated.users.users_request_builder import UsersRequestBuilder
# Library - Importing the Teamwork module --- Not needed at this time
from msgraph.generated.teamwork.teamwork_request_builder import TeamworkRequestBuilder

#Creating a Graph class, then use the methods that are inherited by this Class in our main script
class Graph:
    #Settings
    settings: SectionProxy
    #Specify the client secret
    client_credential: ClientSecretCredential
    #Specify the Graph Adapter
    adapter: GraphRequestAdapter
    #Specify the Client
    app_client: GraphServiceClient

    #Specify the Client
    def __init__(self, config: SectionProxy):
        self.settings = config
        '''client_id = self.settings['clientId']
        tenant_id = self.settings['tenantId']
        client_secret = self.settings['clientSecret']'''
        
        #Sharing our app id
        client_id = self.settings[0]
        #Sharing our tenant id
        tenant_id = self.settings[2]
        #Sharing our app's secret value
        client_secret = self.settings[1]

        #Creating client credential
        self.client_credential = ClientSecretCredential(tenant_id, client_id, client_secret)
        #Authentication for your app integration
        auth_provider = AzureIdentityAuthenticationProvider(self.client_credential) # type: ignore
        #Use the adapter once you are authenticated
        self.adapter = GraphRequestAdapter(auth_provider)
        #Use Graph over the new adapter
        self.app_client = GraphServiceClient(self.adapter)

    async def get_app_only_token(self):
        #Specify the scope of your app
        graph_scope = 'https://graph.microsoft.com/.default'
        #Provide the credential to get a token that it will be use in a subsequent API calls
        access_token = await self.client_credential.get_token(graph_scope)
        #Every time we called this function, return the token
        return access_token.token
    
    # function to retrieve user information as an example on how to call function by using the sdk
    async def get_users(self):
        query_params = UsersRequestBuilder.UsersRequestBuilderGetQueryParameters(
            # Only request specific properties
            select = ['displayName', 'id', 'mail'],
            # Get at most 25 results
            top = 25,
            # Sort by display name
            orderby= ['displayName']
        )
        request_config = UsersRequestBuilder.UsersRequestBuilderGetRequestConfiguration(
            query_parameters=query_params
        )

        users = await self.app_client.users.get(request_configuration=request_config)
        return users
    
    #This is for testing !! You can ommit at this time    
    async def get_callsNO(self):
        query_params = TeamworkRequestBuilder.TeamworkRequestBuilderGetQueryParameters(
            # Only request specific properties
            select = ['participants']
        )
        request_config = TeamworkRequestBuilder.TeamworkRequestBuilderGetRequestConfiguration(
            query_parameters=query_params
        )

        calls = await self.app_client.teamwork.get(request_configuration=request_config)
        return calls
    

    #   This function use a REST API from MS Graph (Get callRecord + call details) 
    # https://learn.microsoft.com/en-us/graph/api/callrecords-callrecord-get?view=graph-rest-1.0&tabs=http

    async def get_calls1(self, mitokeni): 
        callDetail = ''
        # This variable is used to store the content of each call
        var = ''
        # Pass the authorization value to the API call Method through a directory
        headers = {
            'Authorization' : 'Bearer ' + mitokeni
        }
        
        # Use it for API calls
        GRAPH_NDPOINT = 'https://graph.microsoft.com/v1.0/'
        idd = 'f65c041a-c772-4d8e-99c3-b6129526bbbf'
        ### idd = '9f28a21f-50ee-4bca-8940-999bb7089875'
        callid = 'd7eeea70-2400-4a26-b72b-e5e758b0f502'
        callid2 = '62945c20-0c4c-48ad-abff-209a347ac6ac'
        
        ## callid2 = 'MSpkMWQ0NjU4MC00Zjg2LTRlZDQtYWY4Mi03M2NkYmE5NzNiNGEqMCoqMTk6bWVldGluZ19ZemRpWWpBeE5EQXRZbVUwTWkwMFpHTTVMV0prWVRndE16VmlZek16WVRaa016UTVAdGhyZWFkLnYy'

        aa = "users/d1d46580-4f86-4ed4-af82-73cdba973b4a/onlineMeetings?$filter=JoinWebUrl%20eq%20'https%3A%2F%2Fteams.microsoft.com%2Fl%2Fmeetup-join%2F19%253ameeting_YzdiYjAxNDAtYmU0Mi00ZGM5LWJkYTgtMzViYzMzYTZkMzQ5%2540thread.v2%2F0%3Fcontext%3D%257b%2522Tid%2522%253a%25225bc0645b-7931-49d2-88b2-4bda33c52b66%2522%252c%2522Oid%2522%253a%2522d1d46580-4f86-4ed4-af82-73cdba973b4a%2522%257d'"
        ### expand2 = "?$top=1"

        # Variable which stores some datail for each call
        expand = '?$expand=sessions($expand=segments)'
        endpoint = GRAPH_NDPOINT + 'communications/callRecords/' + idd + expand
        #### filter = "?$startsWith(id,'f65c041a')"
        #### endpoint = GRAPH_NDPOINT + 'communications/callRecords' + filter

        # require_cols = [0, 3]
        # specify which column are you looking for in your report
        require_cols = [0]
        # List to store the values for each call
        ## callsIdList = []
        callsIdList = {}
        #Interact within the DataFrame to retrieve the infromation for all the listed calls
        flag4 = 0
        # only read specific columns from an excel file
        # required_df = pd.read_excel('ReportCalls.xlsx', usecols=require_cols)
        required_df = pd.read_excel('report title (31).xlsx', usecols=require_cols)
        # Create a DataFrame to manipulate all the data you get from the calls. For easier use
        df = pd.DataFrame(required_df)

        #Interact over the DataFrame
        for i in df['Conference Id']:
            # creating the resoirce path for the API call.
            endpoint2 = GRAPH_NDPOINT + 'communications/callRecords/' + i + expand
            
            # performing the call using the GET method to MS Graph. Which interacts with callRecords resource
            response = requests.get(endpoint2, headers=headers)
            #The expected response for the status is 200
            if response.status_code == 202:
                print('Email sent')
            else:
                #callDetail = response.content
                var = response.content
                #Store the content
                ##callsIdList.insert(flag4,var)    
                callsIdList[flag4] = var
            flag4 += 1
        '''response = requests.get(endpoint, headers=headers)
        if response.status_code == 202:
            print('Email sent')
        else:
            #callDetail = response.content
            var = response.content'''
        
        return callsIdList
    
    ### https://learn.microsoft.com/en-us/onedrive/developer/rest-api/getting-started/?view=odsp-graph-online
    ### Use sharepoint Graph API
    ### Authentication Scope  https://learn.microsoft.com/en-us/onedrive/developer/rest-api/getting-started/graph-oauth?view=odsp-graph-online
    ### This flow is useful for quickly obtaining an access token to use the OneDrive API in an interactive fashion.

    # Function to list Documents in a Site
    # Function to create a list in a particular site
    async def get_Sites(self, mitokeni): 
        callDetail = ''
        var = ''
        headers = {
            'Authorization' : 'Bearer ' + mitokeni,
            'Content-type': 'application/json; charset=utf-8'
        }
        
        GRAPH_NDPOINT = 'https://graph.microsoft.com/v1.0/'
        #endpoint = GRAPH_NDPOINT + 'sites'
        siteId = 't8vhz.sharepoint.com,57f371c9-91a9-4562-9d9b-048428fe829d,6d8eaf61-b3fe-467d-8c4e-e43690b221c7'
        documentsId = 'b!yXHzV6mRYkWdmwSEKP6CnWGvjm3-s31GjE7kNpCyIcd0JKQhQtoaRITx82hnCmEe'
        
        # endpoint = GRAPH_NDPOINT + 'sites/{0}/drive/{1}/'.format(siteId,documentsId)
        endpoint = GRAPH_NDPOINT + 'sites/{0}/lists'.format(siteId)
        body = {
                    "displayName": "Books",
                    "columns": [
                        {
                        "name": "Author",
                        "text": { }
                        },
                        {
                        "name": "PageCount",
                        "number": { }
                        }
                    ],
                    "list": {
                        "template": "genericList"
                    }
                }
        
        json_object = json.dumps(body)
        #response = requests.get(endpoint, headers=headers)
        response = requests.post(endpoint, headers=headers, data=json_object)
        if response.status_code == 202:
            print('Email sent')
        else:
            #callDetail = response.content
            var = response.content
        
        return var
    
    async def update_ListItem(self, mitokeni): 
        callDetail = ''
        var = ''
        headers = {
            'Authorization' : 'Bearer ' + mitokeni,
            'Content-type': 'application/json; charset=utf-8'
        }
        
        GRAPH_NDPOINT = 'https://graph.microsoft.com/v1.0/'
        #endpoint = GRAPH_NDPOINT + 'sites'
        siteId = 't8vhz.sharepoint.com,57f371c9-91a9-4562-9d9b-048428fe829d,6d8eaf61-b3fe-467d-8c4e-e43690b221c7'
        # listId = 'd0c42b6b-19eb-419a-896e-ad39f4e01dad'
        # endpoint = GRAPH_NDPOINT + 'sites/{0}/drive/{1}/'.format(siteId,documentsId)
        listId = 'd0c42b6b-19eb-419a-896e-ad39f4e01dad'
        endpoint = GRAPH_NDPOINT + 'sites/{0}/lists/{1}/items'.format(siteId,listId)
        body = {
                      "fields": {                  
                            "Title": "123123123okosfidsf",          
                            "startDateTime": "2023-10-31 22:42:09",
                            "endDateTime" : "2023-10-31 22:42:18",
                            "numberParticipants" : 2,
                            "userId" : "1",
                            "displayName" : "luis",
                            "streamDirection" : "MX_GDL",
                            "avJitter" : "123",
                            "maxJitter" : "10.10.23.45",
                            "avPacketLoss" : "456",
                            "maxPacketLoss" : "456",
                            "avRoundTrip" : "789",
                            "maxRoundTrip" : "789",
                            "callQuality" : "good",                                                        
                            "connectionType" : "unknown"
                       }
                }
        
        json_object = json.dumps(body)
        #response = requests.get(endpoint, headers=headers)
        response = requests.post(endpoint, headers=headers, data=json_object)
        if response.status_code == 202:
            print('Email sent')
        else:
            #callDetail = response.content
            var = response.content
        
        return var
    
    async def update_ListItem2(self, mitokeni, listFinal): 
        callDetail = ''
        var = ''
        headers = {
            'Authorization' : 'Bearer ' + mitokeni,
            'Content-type': 'application/json; charset=utf-8'
        }
        
        GRAPH_NDPOINT = 'https://graph.microsoft.com/v1.0/'
        #endpoint = GRAPH_NDPOINT + 'sites'
        siteId = 't8vhz.sharepoint.com,57f371c9-91a9-4562-9d9b-048428fe829d,6d8eaf61-b3fe-467d-8c4e-e43690b221c7'
        # listId = 'd0c42b6b-19eb-419a-896e-ad39f4e01dad'
        # endpoint = GRAPH_NDPOINT + 'sites/{0}/drive/{1}/'.format(siteId,documentsId)
        listId = 'd0c42b6b-19eb-419a-896e-ad39f4e01dad'
        endpoint = GRAPH_NDPOINT + 'sites/{0}/lists/{1}/items'.format(siteId,listId)
        for i in listFinal.values():
            print(i)

            body = {
                        "fields": {                  
                                "Title": i['callId'],          
                                "startDateTime": i['startDate'],
                                "endDateTime" : i['endDate'],
                                "numberParticipants" : i['numParticipants'],
                                "userId" : i['userId'],
                                "displayName" : i['displayName'],
                                "streamDirection" : i['ipLocation'],
                                "avJitter" : str(i['avJitter']),
                                "maxJitter" : i['ip'],
                                "avPacketLoss" : str(i['avPacket']),
                                "maxPacketLoss" : i['startTime'],
                                "avRoundTrip" : str(i['avRound']),
                                "maxRoundTrip" : i['endTime'],
                                "callQuality" : i['callQual'],                                                        
                                "connectionType" : i['connection']
                        }
                    }
            
            json_object = json.dumps(body)
            #response = requests.get(endpoint, headers=headers)
            response = requests.post(endpoint, headers=headers, data=json_object)
            '''if response.status_code == 202:
                print('Email sent')
            else:
                #callDetail = response.content
                var = response.content'''
            
            # return var


    async def get_List(self, mitokeni): 
        callDetail = ''
        var = ''
        headers = {
            'Authorization' : 'Bearer ' + mitokeni,
            'Content-type': 'application/json; charset=utf-8'
        }
        
        GRAPH_NDPOINT = 'https://graph.microsoft.com/v1.0/'
        #endpoint = GRAPH_NDPOINT + 'sites'
        siteId = 't8vhz.sharepoint.com,57f371c9-91a9-4562-9d9b-048428fe829d,6d8eaf61-b3fe-467d-8c4e-e43690b221c7'
        
        # endpoint = GRAPH_NDPOINT + 'sites/{0}/drive/{1}/'.format(siteId,documentsId)
        endpoint = GRAPH_NDPOINT + 'sites/{0}/lists/'.format(siteId)
        
        #response = requests.get(endpoint, headers=headers)
        response = requests.get(endpoint, headers=headers)
        if response.status_code == 202:
            print('Email sent')
        else:
            #callDetail = response.content
            var = response.content
        
        return var






    #The rest of the fucntions are for testing purposes using other reources through API calls
    async def get_onlineMeet(self, mitokeni): 
        callDetail = ''
        var = ''
        headers = {
            'Authorization' : 'Bearer ' + mitokeni
        }
        
        GRAPH_NDPOINT = 'https://graph.microsoft.com/v1.0/'
        endpoint = GRAPH_NDPOINT + 'subscriptions/'
        

        response = requests.get(endpoint, headers=headers)
        if response.status_code == 202:
            print('Email sent')
        else:
            #callDetail = response.content
            var = response.content
        
        return var

    async def get_onlineMeetDetails(self, mitokeni): 
        callDetail = ''
        var = ''
        headers = {
            'Authorization' : 'Bearer ' + mitokeni
        }
        
        GRAPH_NDPOINT = 'https://graph.microsoft.com/v1.0/'
        
        
        callid4 = "f65c041a-c772-4d8e-99c3-b6129526bbbf"
        callid5 = str(callid4)
        userId = 'lponduty2023@t8vhz.onmicrosoft.com'
        #### aa = "users/{userId}/onlineMeetings?$filter=joinMeetingIdSettings/joinMeetingId%20eq%20'{callid4}'"
        aa = "users/{0}/calendar/events?$select=subject,body,bodyPreview,organizer,attendees,start,end,location".format(userId)
        
        endpoint = GRAPH_NDPOINT + aa
        response = requests.get(endpoint, headers=headers)
        if response.status_code == 202:
            print('Email sent')
        else:
            #callDetail = response.content
            var = response.content
        
        return var

## Configure application access policy
    async def get_onlineMeetDetails2(self, mitokeni): 
        callDetail = ''
        var = ''
        headers = {
            'Authorization' : 'Bearer ' + mitokeni
        }
        
        GRAPH_NDPOINT = 'https://graph.microsoft.com/v1.0/'
        
        
        callid4 = "f65c041a-c772-4d8e-99c3-b6129526bbbf"
        meetingId = 'YzdiYjAxNDAtYmU0Mi00ZGM5LWJkYTgtMzViYzMzYTZkMzQ5'
        userId = 'LidiaH@t8vhz.onmicrosoft.com'
        #### aa = "users/{userId}/onlineMeetings?$filter=joinMeetingIdSettings/joinMeetingId%20eq%20'{callid4}'"
        aa = "users/d1d46580-4f86-4ed4-af82-73cdba973b4a/onlineMeetings?$filter=JoinWebUrl%20eq%20'https%3A%2F%2Fteams.microsoft.com%2Fl%2Fmeetup-join%2F19%253ameeting_YzdiYjAxNDAtYmU0Mi00ZGM5LWJkYTgtMzViYzMzYTZkMzQ5%2540thread.v2%2F0%3Fcontext%3D%257b%2522Tid%2522%253a%25225bc0645b-7931-49d2-88b2-4bda33c52b66%2522%252c%2522Oid%2522%253a%2522d1d46580-4f86-4ed4-af82-73cdba973b4a%2522%257d'"
        ### GET https://graph.microsoft.com/v1.0/users/dc17674c-81d9-4adb-bfb2-8f6a442e4622/onlineMeetings?$filter=JoinWebUrl%20eq%20'https%3A%2F%2Fteams.microsoft.com%2Fl%2Fmeetup-join%2F19%253ameeting_MGQ4MDQyNTEtNTQ2NS00YjQxLTlkM2EtZWVkODYxODYzMmY2%2540thread.v2%2F0%3Fcontext%3D%257b%2522Tid%2522%253a%2522909c6581-5130-43e9-88f3-fcb3582cde37%2522%252c%2522Oid%2522%253a%2522dc17674c-81d9-4adb-bfb2-8f6a442e4622%2522%257d'
        
        endpoint = GRAPH_NDPOINT + aa
        response = requests.get(endpoint, headers=headers)
        if response.status_code == 202:
            print('Email sent')
        else:
            #callDetail = response.content
            var = response.content
        
        return var

### Retrieve an online meeting by onlinemeetingid
    async def get_onlineMeetDetails3(self, mitokeni): 
        callDetail = ''
        var = ''
        headers = {
            'Authorization' : 'Bearer ' + mitokeni
        }
        
        GRAPH_NDPOINT = 'https://graph.microsoft.com/v1.0/'
        
        
        callid4 = "f65c041a-c772-4d8e-99c3-b6129526bbbf"
        meetingId = 'YzdiYjAxNDAtYmU0Mi00ZGM5LWJkYTgtMzViYzMzYTZkMzQ5'
        userId = 'LidiaH@t8vhz.onmicrosoft.com'
        
        ## aa = "communications/onlineMeetings/?$filter=VideoTeleconferenceId%20eq%20'287961081794'"
        aa = "users/d1d46580-4f86-4ed4-af82-73cdba973b4a/onlineMeetings/MSpkMWQ0NjU4MC00Zjg2LTRlZDQtYWY4Mi03M2NkYmE5NzNiNGEqMCoqMTk6bWVldGluZ19ZemRpWWpBeE5EQXRZbVUwTWkwMFpHTTVMV0prWVRndE16VmlZek16WVRaa016UTVAdGhyZWFkLnYy"
        ### GET https://graph.microsoft.com/v1.0/communications/onlineMeetings/?$filter=VideoTeleconferenceId%20eq%20'123456789'
        endpoint = GRAPH_NDPOINT + aa
        response = requests.get(endpoint, headers=headers)
        if response.status_code == 202:
            print('Email sent')
        else:
            #callDetail = response.content
            var = response.content
        
        return var


    async def create_onlineMeetSubs(self, mitokeni): 
        GRAPH_NDPOINT = 'https://graph.microsoft.com/v1.0/subscriptions/'
    
        headers = {
            'Authorization' : 'Bearer ' + mitokeni,
            'Content-type': 'application/json; charset=utf-8',
            'Host' : 'graph.microsoft.com',
            'Content-Length' : '199'
        }

        body = {
                    "changeType": "updated",
                    "notificationUrl": "https://webhook.azurewebsites.net/api/send/myNotifyClient",
                    "resource": "communications/callRecords",
                    "expirationDateTime":"2023-12-12T18:23:45.9356913Z"
                }
        
        json_object = json.dumps(body)
        # "clientState": "secretClientValue",
        # "latestSupportedTlsVersion": "v1_2"
        # https://learn.microsoft.com/en-us/graph/api/subscription-post-subscriptions?view=graph-rest-1.0&tabs=http
        
        # response = requests.get(chatsSend, headers=headers, json=body)
        response = requests.post(GRAPH_NDPOINT, headers=headers, data=json_object)
        if response.status_code == 201:
            print('Email sent')
        else:
            ### print('Email sent2')
            return response.content
            ### print(response.content)  
        
        '''
        txt = re.search("^averageAudioDegradation$", callDetail)

        if txt:
            print("YES! We have a match!")
        else:
            print("No match")
        '''
    
        

        

    # Retrieve the list of chats that the user is part of.
    # https://learn.microsoft.com/en-us/graph/api/chat-get?view=graph-rest-1.0&tabs=http
    # GET /me/chats
    # GET /users/{user-id | user-principal-name}/chats
    # Assign the next roles to your app regarding chat otherwise you get the following error
    # {"code":"Forbidden","message":"Missing role permissions on the request. 
    # API requires one of \'Chat.ReadBasic.All, Chat.Read.All, Chat.ReadWrite.All\'. 
    # Roles on the request \'Mail.ReadWrite, Directory.ReadWrite.All, CallRecords.Read.All, Directory.Read.All, User.Read.All, Mail.Send\'.","innerError":{"date":"2023-07-05T22:13:55","request-id":"6abbcf3a-4ea3-48f1-bb01-6cc04cf8a86f","client-request-id":"6abbcf3a-4ea3-48f1-bb01-6cc04cf8a86f"}}}'

    async def get_calls2(self, mitokeni): 
        headers = {
            'Authorization' : 'Bearer ' + mitokeni
        }
        
        GRAPH_NDPOINT = 'https://graph.microsoft.com/v1.0/'
        userid = 'd1d46580-4f86-4ed4-af82-73cdba973b4a'
        idd = 'users/' + userid + '/chats'
        
        chats = GRAPH_NDPOINT + idd        

        response = requests.get(chats, headers=headers)
        if response.status_code == 202:
            print('Email sent')
        else:
            print(response.content)  


    # Get messages for a particular ChatID 
    # https://learn.microsoft.com/en-us/graph/api/chat-post-messages?view=graph-rest-1.0&tabs=http  
    # Assign Teamwork.Migrate.All == Create chat and channel messages with anyone's identity and with any timestamp 
    # https://learn.microsoft.com/en-us/microsoftteams/platform/graph-api/import-messages/import-external-messages-to-teams
    async def get_calls3(self, mitokeni): 
        headers = {
            'Authorization' : 'Bearer ' + mitokeni,
            'Content-type': 'application/json'
        }

        body = {
                    "body": {
                        "content": "Hello world"
                    }
                }
        
        GRAPH_NDPOINT = 'https://graph.microsoft.com/v1.0/'
        chatId = '19:6841bba0-7d9d-4fa5-9d11-381d67dc9390_d1d46580-4f86-4ed4-af82-73cdba973b4a@unq.gbl.spaces'
        chatId2 = '19:d1d46580-4f86-4ed4-af82-73cdba973b4a_0c5cfdbb-596f-4d39-b557-5d9516c94107@unq.gbl.spaces'
        idd = 'chats/' + chatId + '/messages'
        
        chatsSend = GRAPH_NDPOINT + idd

        # response = requests.get(chatsSend, headers=headers, json=body)
        response = requests.get(chatsSend, headers=headers)
        if response.status_code == 202:
            print('Email sent')
        else:
            ### print('Email sent2')
            return response.content
            ### print(response.content)  

    async def get_callsUser(self, mitokeni):             
        varUser = ''
        headers = {
            'Authorization' : 'Bearer ' + mitokeni
        }
        
        GRAPH_NDPOINT = 'https://graph.microsoft.com/v1.0/'                            
        endpointUser = GRAPH_NDPOINT + 'users/'
        

        responseUser = requests.get(endpointUser, headers=headers)
        if responseUser.status_code == 202:
            print('Email sent')
        else:
            #callDetail = response.content
            varUser = responseUser.content        
            return varUser
    
    async def get_callsUser2(self, mitokeni, arra):   
        headers = {
                'Authorization' : 'Bearer ' + mitokeni
            }          
        
        arraUser = []
        flag = 0
        for i in arra:
            
            dictUser = {}
            GRAPH_NDPOINT = 'https://graph.microsoft.com/v1.0/'                            
            endpointUser = GRAPH_NDPOINT + 'users/' + i + '?%24select=country'
            countryUser = requests.get(endpointUser, headers=headers)
            dictUser['userid'] = i
            dictUser['country'] = countryUser

            arraUser[flag] = dictUser
            flag += 1
                
        return arraUser
        