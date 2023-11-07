# REFERENCE
## https://learn.microsoft.com/en-us/graph/tutorials/python-app-only?tabs=aad&tutorial-step=2

# Important

# The Microsoft Graph SDK for Python is currently in preview and should not be used in production. During this period breaking changes are expected to happen. This tutorial was written with version 1.0.0a2.

# MSAL

###
'''For validation and debugging purposes only, you can decode app-only access tokens using Microsoft's online token parser at https://jwt.ms. 
This can be useful if you encounter token errors when calling Microsoft Graph. 
For example, verifying that the role claim in the token contains the expected Microsoft Graph permission scopes.'''
###


# For running asyncio threading
import asyncio
# It is a method to read from config files
import configparser
# To read the exceptions that the program can raise during its execution using MS Graph SDK
from msgraph.generated.models.o_data_errors.o_data_error import ODataError
# Reading the Class Graph
from graph import Graph
# We use requests library to make API calls to M365 tenant
import requests
# This Python module made to print data in a pretty way
from pprint import pprint
#To serialize the output. Then handle it as json structure
import json

#APP ID for the app registartion that we already created
### clientId = '485311ac-2cc8-48f3-8433-86147d8c0d4d'
appID = '485311ac-2cc8-48f3-8433-86147d8c0d4d'
#Client Secret of the app that is loaded by default
SecretID_app = 'mn88Q~QBEMlKmyWLcVOYh2Q815Wtkyd7VORs4cRO'

#Look for your tenant ID in AAD - 
tenantId = '5bc0645b-7931-49d2-88b2-4bda33c52b66'


# Creating an array while I am trying to figure out how I can read the config file
arr = [appID,SecretID_app,tenantId]

async def main():
    print('CQD at Hella\n')

    # Load settings
    # azure_settings = config['Azure']
    # Trying to parse the intial settings to read it from an specific config file
    # It is not working, I skipped it for now
    # config = configparser.ConfigParser()
    # config.read(['config.cfg', 'config.dev.cfg'])
    
    
    # graph: Graph = Graph(loadding the intial parameters by passing it through our API)
    graph: Graph = Graph(arr)

    # Creating a variable to store our token for future API calls using requests as authentication
    mitoken = ''

    try:
        # Retrieving our APP's token for future API calls
        print("---")
        mitoken = await display_access_token(graph)
        # Method to retrieve a list of users using the MS Graph SDK
        print("---")
        # await list_users(graph)
        # Use REST API to get Microsoft Graph services
        print("---")
        await make_graph_call(graph, mitoken)

        # Print the token as doubel check
        print("---")
        ### print("el token: " + mitoken)
    
    # If an error raised, handle it to avoid your code be iunterrupted
    except ODataError as odata_error:
            print('Error:')
            if odata_error.error:
                # Print the error for debugging
                print(odata_error.error.code, odata_error.error.message)

# Function to authenticate, then get the token
async def display_access_token(graph: Graph):
    token = await graph.get_app_only_token()    
    return token    

# Get users in my organization
#Get call details by using the Call ID
async def make_graph_call(graph: Graph, mitoken):
    # TODO
    calls_page = await graph.get_callsUser(mitoken)

    #get the output call type
    print(type(calls_page))
    jout = json.loads(calls_page.decode('utf-8'))
    # print(jout,'\n================\n')
    ### pprint(jout)
    ### print(jout.keys(),'\n================\n')
    ### print(jout['sessions'][0].keys(),'\n================\n')
    # Serializing json
    json_object = json.dumps(jout, indent=4)
    
    # Writing to sample.json
    with open("sampleUser.json", "w") as outfile:
        outfile.write(json_object)
    
    

    ### print(calls_page, '\n================\n')


    # Output each users's details


# Run main
asyncio.run(main())