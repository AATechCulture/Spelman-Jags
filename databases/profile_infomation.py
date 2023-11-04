import os
from pyairtable import Api

db = Api(os.environ['patpQyRt1AX0n8eGS.d9a9dcf4bb1239000fcbbf2dd92bf0dba8e68d9dc955c7f221f0b71665592564'])
airports = db.table('Airports')

for records in airports.iterate():
    print(records)
