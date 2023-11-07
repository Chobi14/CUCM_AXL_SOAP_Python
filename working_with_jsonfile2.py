import requests
# This Python module made to print data in a pretty way
from pprint import pprint
#To serialize the output. Then handle it as json structure
import json
# Converting a dict into DataFrame using pandas
import pandas as pd 
import xlsxwriter

from datetime import datetime

from functions_handlefile import funcSplitJitter, funcSplitDate, funcSplitPacket, funcSplitRound, funcCompareMetrics, funcFinalQuality
## f = open('sample2.json')
f = open('sampleNew.json')

# returns JSON object as
# a dictionary
data = json.load(f)

f.close()

lenCalls = len(data)
flag5 = 0
print("lencalls", lenCalls)


# Create a Pandas dataframe from some data. 
listId = []
listHeader = ["Id", "startDateTime", "endDateTime", "No. of Participants", "label", "StreamId", "Stream Direction", "Ave. Jitter", "Max. Jitter", "Ave. Packet Loss", "Max PAcket Loss: ", 
              "Average RoundTrip: ", "Max RoundTrip: ","Packet Utilization: ","averageRatioOfConcealedSamples: ", "maxRatioOfConcealedSamples","averAudio Degradation: "]
listStartDate = []
listEndDate = []
listParticipants = []
listUserID = []
listDisplayName= []
listLabel = []
listStream = []
listOutbound = []
listInbound = []
listAvJitter = []
listMaxJitter = []
listAvPacketLoss = []
listMaxPacketLoss = []
listAvRoundTrip = []
listMaxRoundTrip = []
listPacket = []
listAveRatio = []
listMaxRatio = []
listAvAudio = []
listLabel2 = []
listStream2 = []
listOutbound2 = []
listInbound2 = []
listAvJitter2 = []
listMaxJitter2 = []
listAvPacketLoss2 = []
listMaxPacketLoss2 = []
listAvRoundTrip2 = []
listMaxRoundTrip2 = []
listPacket2 = []
listAveRatio2 = []
listMaxRatio2 = []
listAvAudio2 = []

listConnection = []
listBand = []
listIp = []
listStartDatePar = []
listEndDatePar = []


while flag5 < lenCalls:

########################
# import pandas as pd 

  
# Create a Pandas dataframe from some data. 



########################

# Iterating through the json
# list
# print(data.keys())
    l = str(flag5)
    print(data[l]['id'],'\n',data[l]['startDateTime'],'\n',data[l]['endDateTime'])    
    print("# of participants: ",len(data[l]['participants']))    

    flag = 0

    for i in data[l]['sessions']:
        # print(i.keys())
        # print(i['caller']['userAgent']['platform'],'\n',i['caller']['identity']['user']['displayName'],'\n')
        print("UserID: ",i['segments'][flag]['caller']['identity']['user']['id'],"\n displayName: ",i['segments'][flag]['caller']['identity']['user']['displayName'])
        listId.append(data[l]['id'])
        listStartDate.append(data[l]['startDateTime'])
        listEndDate.append(data[l]['endDateTime'])
        listParticipants.append(len(data[l]['participants']))
        listUserID.append(i['segments'][flag]['caller']['identity']['user']['id'])        
        listDisplayName.append(i['segments'][flag]['caller']['identity']['user']['displayName'])
        print(i['segments'][flag].keys())

        listStartDatePar.append(i['startDateTime'])
        listEndDatePar.append(i['endDateTime'])

        flag2 = 0
        for j in i['segments'][flag2]['media']:
            print(j.keys())
            if j['label'] == "main-audio":
                print("Label: ",j['label'],'\n',"Stream ID: ",j['streams'][0]['streamId'],'\n',"Stream Direction: ",j['streams'][0]['streamDirection'],'\n',"Avergae Jitter: ",j['streams'][0]['averageJitter'],'\n',"Max Jitter: ",j['streams'][0]['maxJitter'],'\n',"Aver Packet Loss: ",j['streams'][0]['averagePacketLossRate'],'\n',"Max PAcket Loss: ",j['streams'][0]['maxPacketLossRate'],'\n',"Average RoundTrip: ",j['streams'][0]['averageRoundTripTime'],'\n',"Max RoundTrip: ",j['streams'][0]['maxRoundTripTime'],'\n',"Packet Utilization: ",j['streams'][0]['packetUtilization'],'\n',"averageRatioOfConcealedSamples: ",j['streams'][0]['averageRatioOfConcealedSamples'],'\n',"maxRatioOfConcealedSamples",j['streams'][0]['maxRatioOfConcealedSamples'],'\n',"averAudio Degradation: ",j['streams'][0]['averageAudioDegradation'])
                listConnection.append(j['callerNetwork']['connectionType'])
                listBand.append(j['callerNetwork']['wifiBand'])
                listIp.append(j['callerNetwork']['ipAddress'])
                listLabel.append(j['label'])
                listStream.append(j['streams'][0]['streamId'])
                listOutbound.append(j['streams'][0]['streamDirection'])
                listAvJitter.append(j['streams'][0]['averageJitter'])
                listMaxJitter.append(j['streams'][0]['maxJitter'])
                listAvPacketLoss.append(j['streams'][0]['averagePacketLossRate'])
                listMaxPacketLoss.append(j['streams'][0]['maxPacketLossRate'])
                listAvRoundTrip.append(j['streams'][0]['averageRoundTripTime'])
                listMaxRoundTrip.append(j['streams'][0]['maxRoundTripTime'])
                listPacket.append(j['streams'][0]['packetUtilization'])
                listAveRatio.append(j['streams'][0]['averageRatioOfConcealedSamples'])
                listMaxRatio.append(j['streams'][0]['maxRatioOfConcealedSamples'])
                listAvAudio.append(j['streams'][0]['averageAudioDegradation'])
                print("Label: ",j['label'],'\n',"Stream ID: ",j['streams'][1]['streamId'],'\n',"Inbound Network: ",j['streams'][1]['streamDirection'],'\n',"Avergae Jitter: ",j['streams'][1]['averageJitter'],'\n',"Max Jitter: ",j['streams'][1]['maxJitter'],'\n',"Aver Packet Loss: ",j['streams'][1]['averagePacketLossRate'],'\n',"Max PAcket Loss: ",j['streams'][1]['maxPacketLossRate'],'\n',"Average RoundTrip: ",j['streams'][1]['averageRoundTripTime'],'\n',"Max RoundTrip: ",j['streams'][1]['maxRoundTripTime'],'\n',"Packet Utilization: ",j['streams'][1]['packetUtilization'],'\n',"averageRatioOfConcealedSamples: ",j['streams'][1]['averageRatioOfConcealedSamples'],'\n',"maxRatioOfConcealedSamples",j['streams'][1]['maxRatioOfConcealedSamples'],'\n',"averAudio Degradation: ",j['streams'][1]['averageAudioDegradation'])
                print("IP: ",j['callerNetwork']['ipAddress'],"\n Connection type: ",j['callerNetwork']['connectionType'])
                listLabel2.append(j['label'])
                listStream2.append(j['streams'][1]['streamId'])
                listOutbound2.append(j['streams'][1]['streamDirection'])
                listAvJitter2.append(j['streams'][1]['averageJitter'])
                listMaxJitter2.append(j['streams'][1]['maxJitter'])
                listAvPacketLoss2.append(j['streams'][1]['averagePacketLossRate'])
                listMaxPacketLoss2.append(j['streams'][1]['maxPacketLossRate'])
                listAvRoundTrip2.append(j['streams'][1]['averageRoundTripTime'])
                listMaxRoundTrip2.append(j['streams'][1]['maxRoundTripTime'])
                listPacket2.append(j['streams'][1]['packetUtilization'])
                listAveRatio2.append(j['streams'][1]['averageRatioOfConcealedSamples'])
                listMaxRatio2.append(j['streams'][1]['maxRatioOfConcealedSamples'])
                listAvAudio2.append(j['streams'][1]['averageAudioDegradation'])

            
            flag2 += 1
        flag2 = 0
    flag5 += 1


# Create a Pandas dataframe from some data. 
'''
dataframe = pd.DataFrame( {'CallId': listId, 'StarDateTime' : listStartDate, 'StarDateTime' : listStartDate, 'EndDateTime' : listEndDate, '# of Participants' : listParticipants, 
                           'UserID' : listUserID, 'DisplayName' : listDisplayName, 'label' : listLabel, 'Stream' : listStream, 'Stream Direction' : listOutbound, 'Av Jitter' : listAvJitter, 
                           'Max Jitter' : listMaxJitter, 'Av Packet Loss' : listAvPacketLoss, 'Max Packet Loss' : listMaxPacketLoss, 'Av Round Trip' : listAvRoundTrip, 
                           'Max Round Trip' : listMaxRoundTrip, 'Packet Utilization' : listPacket, 'Av Ratio' : listAveRatio, 'Max Ratio' : listMaxRatio, 'Av Audio Degradation' : listAvAudio,
                           'label2' : listLabel2, 'Stream2' : listStream2, 'Stream Direction2' : listOutbound2, 'Av Jitter2' : listAvJitter2, 
                           'Max Jitter2' : listMaxJitter2, 'Av Packet Loss2' : listAvPacketLoss2, 'Max Packet Loss2' : listMaxPacketLoss2, 'Av Round Trip2' : listAvRoundTrip2, 
                           'Max Round Trip2' : listMaxRoundTrip2, 'Packet Utilization2' : listPacket2, 'Av Ratio2' : listAveRatio2, 'Max Ratio2' : listMaxRatio2, 'Av Audio Degradation2' : listAvAudio2}) 
'''
print("lllllllllllllllllllllllllllllllllllllllllllllllllll")
listStartDateM = funcSplitDate(listStartDatePar)
for i in listStartDateM:
    print(i)
    print(type(i))


listEndDateM = funcSplitDate(listEndDatePar)
for i in listEndDateM:
    print(i)
    print(type(i))

'''listDatePar = []
bul = 0
for i in listStartDate:
    x = listStartDate[bul].split("T")
    y = x[1].split(".")
    
    date_string_3 = x[0] + " " + y[0]
    
    format_3 = "%Y-%m-%d %H:%M:%S"
    date_3 = datetime.strptime(date_string_3, format_3)
    listDatePar.append(date_3)   
    print(date_3)
    print(type(date_3))
    bul += 1'''

print(type(listAvRoundTrip[0]))
print(type(listAvJitter[0]))
print("lllllllllllllllllllllllllllllllllllllllllllllllllll")
listAvJitterM = funcSplitJitter(listAvJitter)
for i in listAvJitterM:
    print(i)
    print(type(i))

listAvJitterM2 = funcSplitJitter(listAvJitter2)
for i in listAvJitterM2:
    print(i)
    print(type(i))

print("lllllllllllllllllllllllllllllllllllllllllllllllllll")

listAvPackteM = funcSplitPacket(listAvPacketLoss)
for i in listAvPackteM:
    print(i)
    print(type(i))

listAvPackteM2 = funcSplitPacket(listAvPacketLoss2)
for i in listAvPackteM2:
    print(i)
    print(type(i))

print("lllllllllllllllllllllllllllllllllllllllllllllllllll")


print("lllllllllllllllllllllllllllllllllllllllllllllllllll")
listAvRoundM = funcSplitRound(listAvRoundTrip)
for i in listAvRoundM:
    print(i)
    print(type(i))

listAvRoundM2 = funcSplitRound(listAvRoundTrip2)
for i in listAvRoundM2:
    print(i)
    print(type(i))

print("lllllllllllllllllllllllllllllllllllllllllllllllllll")

for i in listConnection:
    print(i)
    print(type(i))

flag = 0
for i in listBand:
    if i == "frequency50GHz":
        listBand[flag] = "5Ghz"
    elif i == "frequency24GHz":
        listBand[flag] = "2.4Ghz"
    else:
        pass

for i in listBand:
    print(i)
    print(type(i))

for i in listIp:
    print(i)
    print(type(i))

for i in listStartDatePar:
    print(i)
    print(type(i))

for i in listEndDatePar:
    print(i)
    print(type(i))

'''flag = 0
passw = "None"
for i in listId:
    print(flag)
    print(type(listAvJitterM[flag]))
    print(type(listAvJitterM2[flag]))

    if ((listAvJitterM[flag] == "None") and (listAvJitterM2[flag] == "None")):
        #listFinalJitter[flag] = '-'
        listFinalJitter.append(passw)
    elif (listAvJitterM[flag] == "None"):
        #listFinalJitter[flag] = listAvJitterM2[flag]
        listFinalJitter.append(listAvJitterM2[flag])
    elif (listAvJitterM2[flag] == "None"):
        #listFinalJitter[flag] = listAvJitterM[flag]
        listFinalJitter.append(listAvJitterM[flag])
    else:
        print("entra")
        print(listAvJitterM[flag])
        print(listAvJitterM2[flag])
        if (listAvJitterM[flag] >= listAvJitterM2[flag]):
            #listFinalJitter[flag] = listAvJitterM[flag]
            listFinalJitter.append(listAvJitterM[flag])
        else:
            #listFinalJitter[flag] = listAvJitterM2[flag]
            listFinalJitter.append(listAvJitterM2[flag])        
    flag += 1'''


print("***********************************")
for i in listAvJitterM:
    print(i)
    print(type(i))

for i in listAvJitterM2:
    print(i)
    print(type(i))
print("***********************************")
listFinalJitter = funcCompareMetrics(listId, listAvJitterM, listAvJitterM2)
for i in listFinalJitter:
    print(i)
    print(type(i))
print("***********************************")
for i in listAvPacketLoss:
    print(i)
    print(type(i))

for i in listAvPacketLoss2:
    print(i)
    print(type(i))
print("***********************************")
listFinalPacket = funcCompareMetrics(listId, listAvPacketLoss, listAvPacketLoss2)
for i in listFinalPacket:
    print(i)
    print(type(i))

print("***********************************")
for i in listAvRoundTrip:
    print(i)
    print(type(i))

for i in listAvRoundTrip2:
    print(i)
    print(type(i))
print("***********************************")
listFinalRound = funcCompareMetrics(listId, listAvRoundTrip, listAvRoundTrip2)
for i in listFinalRound:
    print(i)
    print(type(i))

print("***********************************")
print("***********************************")
print("***********************************")
listCallQuality = funcFinalQuality(listId, listFinalJitter, listFinalPacket, listFinalRound)
for i in listCallQuality:
    print(i)
    print(type(i))
# Create a Pandas Excel writer  
# object using XlsxWriter as the engine.  
#writer_object = pd.ExcelWriter("Example_header.xlsx", 
                                #engine ='xlsxwriter') 


'''writer_object = pd.ExcelWriter("newCallsFile.xlsx", 
                                engine ='xlsxwriter') 
   
# Write a dataframe to the worksheet.  
# we turn off the default header 
# and skip one row because we want 
# to insert a user defined header there. 
dataframe.to_excel(writer_object, sheet_name ='Sheet1',  
                          startrow = 1, header = False) 
   
# Create xlsxwriter workbook object . 
workbook_object = writer_object.book 
   
# Create xlsxwriter worksheet object 
worksheet_object = writer_object.sheets['Sheet1'] 
   
# Create a new Format object to formats cells  
# in worksheets using add_format() method . 
   
# here we create a format object for header. 
header_format_object = workbook_object.add_format({ 
                                'bold': True, 
                                'italic' : True, 
                                'text_wrap': True, 
                                'valign': 'top', 
                                'font_color': 'red', 
                                'border': 2}) 
   
# Write the column headers with the defined format. 
for col_number, value in enumerate(dataframe.columns.values): 
    worksheet_object.write(0, col_number + 1, value,  
                              header_format_object) 
   
# Close the Pandas Excel writer  
# object and output the Excel file.  
writer_object._save() 

f1 = open('sampleUser.json')

# returns JSON object as
# a dictionary
data = json.load(f1)

f1.close()

# Iterating through the json
# list
print(data.keys())
varUserMail = []
flag4 = 0
for i in data['value']:
    varUserMail.insert(flag4,i['mail'])
    flag4 += 1

for i in varUserMail:
    print(i)
'''    
    


    
'''if ((listAvJitterM[flag] == "None") and (listAvJitterM2[flag] == "None") and (listAvPackteM[flag] == "None") and (listAvPackteM2[flag] == "None") and (listAvRoundM[flag] == "None") and (listAvRoundM[flag] == "None")):
        listCallQuality[flag] = "Unclassified"'''