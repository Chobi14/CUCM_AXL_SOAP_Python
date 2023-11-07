from datetime import datetime

#Funtion to work with the list of values for start and end dateTime. Cahnge the format to datetime
def funcSplitDate(listStartDate):
    listDatePar = []
    bul = 0
    for i in listStartDate:
        x = listStartDate[bul].split("T")
        y = x[1].split(".")
        
        date_string_3 = x[0] + " " + y[0]
        
        format_3 = "%Y-%m-%d %H:%M:%S"
        date_3 = datetime.strptime(date_string_3, format_3)
        listDatePar.append(date_3)
        bul += 1
    return listDatePar

def funcSplitDate2(listStartDate):    
    listDatePar = {}
    bul = 0
    for i in listStartDate:        
        x = listStartDate[bul].split("T")
        y = x[1].split(".")
        # z = x[0].split("-")
        # zz = z[1] + "/" + z[2] + "/" + z[0]
        listDatePar[bul] = {            
            "deit" : x[0],
            "taim" : y[0]
        }
        bul += 1
    return listDatePar
#Funtion to work with the list of values fro Jitter and convert it to the correct value
def funcSplitJitter(listAvJitterM):
    flag = 0
    s = "None"
    for i in listAvJitterM:
        if i == None:
            #listAvJitterM[flag] = str(s)           
            listAvJitterM[flag] = "None"          
        elif '.' in i:
            x = i.split(".")
            y = x[1].split("S")
            z = int(y[0])
            listAvJitterM[flag] = z
        else:
            listAvJitterM[flag] = 0
        flag += 1
    return listAvJitterM

#Funtion to work with the list of values from Packet and convert it to the correct value
def funcSplitPacket(listAvPacketLossM):
    flag = 0
    for i in listAvPacketLossM:
        if i == None:
            listAvPacketLossM[flag] = "None"
        elif i == 0:
            listAvPacketLossM[flag] = 0.00
        else:
            y = listAvPacketLossM[flag] * 100
            z = round(y,2)
            listAvPacketLossM[flag] = z
        flag += 1
    return listAvPacketLossM

#Funtion to work with the list of values from roundTrip and convert it to the correct value
def funcSplitRound(listAvRoundM):
    flag = 0
    for i in listAvRoundM:
        if i == None:
            listAvRoundM[flag] = "None"            
        elif '.' in i:
            x = i.split(".")
            y = x[1].split("S")
            z = int(y[0])
            listAvRoundM[flag] = z
        else:
            listAvRoundM[flag] = 0
        flag += 1
    return listAvRoundM

#Funtion to compare metrics and just set the final value in a new list
def funcCompareMetrics(lst1, lst2, lst3):
    flag = 0
    passw = "None"
    listFinalJitter = []
    for i in lst1:
        print(flag)
        print(type(lst2[flag]))
        print(type(lst3[flag]))

        if ((lst2[flag] == "None") and (lst3[flag] == "None")):
            #listFinalJitter[flag] = '-'
            listFinalJitter.append(passw)
        elif (lst2[flag] == "None"):
            #listFinalJitter[flag] = listAvJitterM2[flag]
            listFinalJitter.append(lst3[flag])
        elif (lst3[flag] == "None"):
            #listFinalJitter[flag] = listAvJitterM[flag]
            listFinalJitter.append(lst2[flag])
        else:
            print("entra")
            print(lst2[flag])
            print(lst3[flag])
            if (lst2[flag] >= lst3[flag]):
                #listFinalJitter[flag] = listAvJitterM[flag]
                listFinalJitter.append(lst2[flag])
            else:
                #listFinalJitter[flag] = listAvJitterM2[flag]
                listFinalJitter.append(lst3[flag])        
        flag += 1
    return listFinalJitter

#Funtion to set the status of the call based on the final metrics
def funcFinalQuality(lst1, lst2, lst3, lst4):
    flag = 0
    g = "good"
    p = "poor"
    u = "unclassified"
    listFinaCallQuality = []
    for i in lst1:
        print(flag)
        print(type(lst2[flag]))
        print(type(lst3[flag]))
        print(type(lst4[flag]))
        j = "good"
        if ((lst2[flag] == "None") and (lst3[flag] == "None") and (lst4[flag] == "None")):
            print("un")
            listFinaCallQuality.append(u)
        else:
            a = lst2[flag]
            if(a == "None"):
                a = 0
            b = lst3[flag]
            if(b == "None"):
                b = 0
            c = lst4[flag]
            if(c == "None"):
                c = 0
            
            if (a < 130):
                print("paso1")
                if (b < 1):
                    print("paso2")
                    if (c < 500):
                        print("paso3")
                        listFinaCallQuality.append(g)
                    else:
                        listFinaCallQuality.append(p)
                else:
                    listFinaCallQuality.append(p)
            else:
                listFinaCallQuality.append(p)
            


            '''if ((lst2[flag] < 130) or (lst2[flag] is not int)):
                print("paso1")
                if ((lst3[flag] < 1) or (lst3[flag] is not int)):
                    print("paso2")
                    if ((lst4[flag] < 500) or (lst4[flag] is not int)):
                        print("paso3")
                        listFinaCallQuality.append(g)
                    else:
                        listFinaCallQuality.append(p)
                else:
                    listFinaCallQuality.append(p)
            else:
                listFinaCallQuality.append(p)'''
        print(listFinaCallQuality[flag])
        flag += 1
    return listFinaCallQuality


# function to determine if the coneection is either wired or wireless.For wireless calls get at what frecuency

def funcConnection(lst1, lst2, lst3):
    listFinalConnection = []
    flag = 0
    for i in lst1:
        a = lst2[flag] + " " + lst3[flag]
        listFinalConnection.append(a)
        flag += 1
    return listFinalConnection