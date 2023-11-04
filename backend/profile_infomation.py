import os
from pyairtable import Api

API_TOKEN = 'patpQyRt1AX0n8eGS.b5eacd0c39dd0476476a7361f4d7a15a223f054cc1e6443a9580d26231b513d5'
db = Api(API_TOKEN)

airports = db.table('app66AlHq30vppBQp', 'Airports')
pairings = db.table('app66AlHq30vppBQp', 'Pairings')

for records in airports.iterate():
    print(records)


def getThis(paramater):
    return "hello"