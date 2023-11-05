import os
from pyairtable import Api

API_TOKEN = 'patpQyRt1AX0n8eGS.b5eacd0c39dd0476476a7361f4d7a15a223f054cc1e6443a9580d26231b513d5'
db = Api(API_TOKEN)

airports = db.table('app66AlHq30vppBQp', 'Airports')
pairings = db.table('app66AlHq30vppBQp', 'Pairings')
users = db.table('app66AlHq30vppBQp','Users')

#for records in airports.iterate():
   # print(records)

#for records in users.iterate():
    #print(records)

def get_user(employee_id):
    db = Api(API_TOKEN)
    url = 'https://api.airtable.com/v0/app66AlHq30vppBQp/Users?filterByFormula=employee_id=' + value
    userinfo = db.request('get',url)
    return(userinfo)
    #print(url)
    
def get_pairing(pairing_id):
    db= Api(API_TOKEN)
    url = 'https://api.airtable.com/v0/app66AlHq30vppBQp/Pairings?filterByFormula=Pilot=' + value2
    userinfo = db.request('get',url)
    return(userinfo)



