import math

x = 0.0003145
y = x * 100
z = round(y,2)

print(z)
print(type(y))

x = 0.0
if(x == 0):
    print("true")
else:
    print("false")



x = "10.54.0.0"
print(type(x))
y = "10.53.254.254"
z = "10.55.254.254"

if ((x >= y) and (x <= z)):
    print("in")
else:
    print("out")

a = 1
b = "None"

if (b is not int):
    print("entra")
else:
    print("fuera")

dictTest = {
    "0": {
        "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#communications/callRecords(sessions(segments()))/$entity",
        "id": "266d71bc-3b63-4bc8-9726-70b6139430dc",
        "version": 1,
        "type": "groupCall",
        "modalities": [
            "audio"
        ],
        "lastModifiedDateTime": "2023-10-31T23:05:39.6861863Z",
        "startDateTime": "2023-10-31T22:42:09.5508716Z",
        "endDateTime": "2023-10-31T22:47:39.569309Z",
    },
    "1": {
        "error": {
            "code": "NotFound",
            "message": "Could not find the requested call record. Records about calls or online meetings that started more than 30 days ago are not available.",
            "innerError": {
                "date": "2023-11-03T18:31:42",
                "request-id": "a42062a8-06ad-4055-b586-e8d540889a4d",
                "client-request-id": "a42062a8-06ad-4055-b586-e8d540889a4d"
            }
        }
    }
}

for i in dictTest.values():
    if "error" in i:
        print("hay")
    else: 
        print("no hay")