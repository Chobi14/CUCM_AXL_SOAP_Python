# REFERENCE
## https://learn.microsoft.com/en-us/graph/tutorials/python-app-only?tabs=aad&tutorial-step=2

# Important

# The Microsoft Graph SDK for Python is currently in preview and should not be used in production. During this period breaking changes are expected to happen. This tutorial was written with version 1.0.0a2.

###
'''For validation and debugging purposes only, you can decode app-only access tokens using Microsoft's online token parser at https://jwt.ms. 
This can be useful if you encounter token errors when calling Microsoft Graph. 
For example, verifying that the role claim in the token contains the expected Microsoft Graph permission scopes.'''
###

import asyncio
import configparser
from msgraph.generated.models.o_data_errors.o_data_error import ODataError
from graph import Graph
import requests


clientId = '485311ac-2cc8-48f3-8433-86147d8c0d4d'
clientSecret = 'llT8Q~YtY1JNvG4ond-y6fXyE5p0UB8pNM~x6dzR'
tenantId = '5bc0645b-7931-49d2-88b2-4bda33c52b66'

arr = [clientId,clientSecret,tenantId]

async def main():
    print('Python Graph App-Only Tutorial\n')

    # Load settings
    config = configparser.ConfigParser()
    config.read(['config.cfg', 'config.dev.cfg'])
    
    # azure_settings = config['Azure']
    # graph: Graph = Graph(azure_settings)
    graph: Graph = Graph(arr)

    choice = -1

    while choice != 0:
        print('Please choose one of the following options:')
        print('0. Exit')
        print('1. Display access token')
        print('2. List users')
        print('3. Make a Graph call')

        try:
            choice = int(input())
        except ValueError:
            choice = -1

        try:
            if choice == 0:
                print('Goodbye...')
            elif choice == 1:
                await display_access_token(graph)
            elif choice == 2:
                await list_users(graph)
            elif choice == 3:
                await make_graph_call(graph)
            else:
                print('Invalid choice!\n')
        except ODataError as odata_error:
            print('Error:')
            if odata_error.error:
                print(odata_error.error.code, odata_error.error.message)

async def display_access_token(graph: Graph):
    token = await graph.get_app_only_token()
    print('App-only token:', token, '\n')

async def list_users(graph: Graph):
    users_page = await graph.get_users()

    # Output each users's details
    if users_page and users_page.value:
        for user in users_page.value:
            print('User:', user.display_name)
            print('  ID:', user.id)
            print('  Email:', user.mail)

        # If @odata.nextLink is present
        more_available = users_page.odata_next_link is not None
        print('\nMore users available?', more_available, '\n')

async def make_graph_call(graph: Graph):
    # TODO
    return

# Run main
asyncio.run(main())