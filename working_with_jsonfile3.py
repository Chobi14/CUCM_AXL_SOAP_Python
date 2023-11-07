import requests
# This Python module made to print data in a pretty way
from pprint import pprint
#To serialize the output. Then handle it as json structure
import json
# Converting a dict into DataFrame using pandas
import pandas as pd 
import xlsxwriter
from datetime import datetime
from functions_handlefile import funcSplitJitter, funcSplitDate, funcSplitPacket, funcSplitRound, funcCompareMetrics, funcFinalQuality, funcConnection, funcSplitDate2
## f = open('sample2.json')

def funcWorkFile():
    f = open('sampleNew4.json')
    

    # returns JSON object as
    # a dictionary
    data = json.load(f)

    f.close()

    lenCalls = len(data)
    flag5 = 0
    print("lencalls", lenCalls)


    # Create a Pandas dataframe from some data. 
    listId = []
    listParticipants = []
    listUserID = []
    listDisplayName= []
    listAvJitter = []
    listAvPacketLoss = []
    listAvRoundTrip = []
    listAvJitter2 = []
    listAvPacketLoss2 = []
    listAvRoundTrip2 = []

    listConnection = []
    listBand = []
    listIp = []
    listStartDatePar = []
    listEndDatePar = []

    while flag5 < lenCalls:
        l = str(flag5)
        if "error" in data[l]:
            print("errora")
        else:
            #print(data[l]['id'],'\n',data[l]['startDateTime'],'\n',data[l]['endDateTime'])    
            #print("# of participants: ",len(data[l]['participants']))    

            flag = 0

            for i in data[l]['sessions']:
                
                listId.append(data[l]['id'])
                listParticipants.append(str(len(data[l]['participants'])))
                listUserID.append(i['segments'][flag]['caller']['identity']['user']['id'])        
                listDisplayName.append(i['segments'][flag]['caller']['identity']['user']['displayName'])
                
                listStartDatePar.append(i['startDateTime'])
                listEndDatePar.append(i['endDateTime'])

                flag2 = 0
                for j in i['segments'][flag2]['media']:
                    
                    if j['label'] == "main-audio":                
                        ###########################################################################################
                        listConnection.append(j['callerNetwork']['connectionType'])
                        listBand.append(j['callerNetwork']['wifiBand'])
                        ###########################################################################################
                        listIp.append(j['callerNetwork']['ipAddress'])                
                        listAvJitter.append(j['streams'][0]['averageJitter'])                
                        listAvPacketLoss.append(j['streams'][0]['averagePacketLossRate'])                
                        listAvRoundTrip.append(j['streams'][0]['averageRoundTripTime'])                                
                        listAvJitter2.append(j['streams'][1]['averageJitter'])                
                        listAvPacketLoss2.append(j['streams'][1]['averagePacketLossRate'])                
                        listAvRoundTrip2.append(j['streams'][1]['averageRoundTripTime'])               
                    
                    flag2 += 1
                flag2 = 0
        flag5 += 1


    # Create a Pandas dataframe from some data. 
    print("lllllllllllllllllllllllllllllllllllllllllllllllllll")
    listFinalStartDateM = funcSplitDate2(listStartDatePar)
    listFinalEndDateM = funcSplitDate2(listEndDatePar)
    print("lllllllllllllllllllllllllllllllllllllllllllllllllll")
    listAvJitterM = funcSplitJitter(listAvJitter)
    listAvJitterM2 = funcSplitJitter(listAvJitter2)
    print("lllllllllllllllllllllllllllllllllllllllllllllllllll")
    listAvPackteM = funcSplitPacket(listAvPacketLoss)
    listAvPackteM2 = funcSplitPacket(listAvPacketLoss2)
    print("lllllllllllllllllllllllllllllllllllllllllllllllllll")
    listAvRoundM = funcSplitRound(listAvRoundTrip)
    listAvRoundM2 = funcSplitRound(listAvRoundTrip2)
    print("lllllllllllllllllllllllllllllllllllllllllllllllllll")


    flag = 0
    for i in listBand:
        if i == "frequency50GHz":
            listBand[flag] = "5Ghz"
        elif i == "frequency24GHz":
            listBand[flag] = "2.4Ghz"
        else:
            listBand[flag] = "-"
        flag += 1

        

    listFinalConnection = funcConnection(listId, listConnection, listBand)
    print("***********************************")
    print("***********************************")
    listFinalJitter = funcCompareMetrics(listId, listAvJitterM, listAvJitterM2)
    print("***********************************")
    print("***********************************")
    listFinalPacket = funcCompareMetrics(listId, listAvPackteM, listAvPackteM2)
    print("***********************************")
    print("***********************************")
    listFinalRound = funcCompareMetrics(listId, listAvRoundM, listAvRoundM2)
    print("***********************************")
    print("***********************************")
    listCallQuality = funcFinalQuality(listId, listFinalJitter, listFinalPacket, listFinalRound)


    Location = {
        "NSA_MX_GDL_Connect" : {
            "startRange" : "10.0.0.0",
            "endRange" : "10.10.254.254",
            "nameLoc" : "NSA_MX_GDL_Connect"
        },"NSA_MX_GDL_Labs" : {
            "startRange" : "10.20.0.0",
            "endRange" : "10.30.254.254",
            "nameLoc" : "NSA_MX_GDL_Labs"
        }, "NSA_MX_IRP_Plant1" : {
            "startRange" : "10.50.0.0",
            "endRange" : "10.70.254.254",
            "nameLoc" : "NSA_MX_IRP_Plant1"
        }, "NSA_US_NTV_Plant1" : {
            "startRange" : "20.0.0.0",
            "endRange" : "20.10.254.254",
            "nameLoc" : "NSA_US_NTV_Plant1"
        }, "NSA_BR_SP_Plant4" : {
            "startRange" : "30.0.0.0",
            "endRange" : "30.40.254.254",
            "nameLoc" : "NSA_BR_SP_Plant4"
        }, "APAC_IN_GUR_Corporate" : {
            "startRange" : "40.0.0.0",
            "endRange" : "40.30.254.254",
            "nameLoc" : "APAC_IN_GUR_Corporate"
        }, "EMEA_GER_LIP_Plant2" : {
            "startRange" : "50.0.0.0",
            "endRange" : "50.45.254.254",
            "nameLoc" : "EMEA_GER_LIP_Plant2"
        }
    }

    listLocation = []
    unk = "unknown"
    non = "None"
    for i in listIp:
        band = 0
        for j in Location.values():         
            if (i == None):  
                listLocation.append(non)
                band = 1          
                break
            else:
                if ((i > j['startRange']) and (i < j['endRange'])):                
                    listLocation.append(j['nameLoc'])
                    band = 1
                    break 
                else:
                    continue
        if band == 0:
            listLocation.append(unk)

    flag = 0
    for i in listIp:
        if i == None:
            listIp[flag] = "None"
        flag += 1

    dictFinal = {}

    print("aaaaaaaaaaaaaaaaaaaaaa")
    flag = 0
    for i in listId:
        dictFinal[flag] = {
            "callId" : listId[flag],
            "startDate" : listFinalStartDateM[flag]['deit'],
            "endDate" : listFinalEndDateM[flag]['deit'],
            "startTime" : listFinalStartDateM[flag]['taim'],
            "endTime" : listFinalEndDateM[flag]['taim'],
            "numParticipants" : listParticipants[flag],
            "userId" : listUserID[flag],
            "displayName" : listDisplayName[flag],
            "avJitter" : listFinalJitter[flag],
            "avPacket" : listFinalPacket[flag],
            "avRound" : listFinalRound[flag],
            "connection" : listFinalConnection[flag],
            "callQual" : listCallQuality[flag],
            "ip" : listIp[flag],
            "ipLocation" : listLocation[flag]
        }
        flag += 1

    '''for i in dictFinal.values():
        print(type(i))
        print(i)'''
    return dictFinal

# varistas = funcWorkFile()
# print(varistas)