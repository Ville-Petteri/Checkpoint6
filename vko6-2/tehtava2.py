import argparse
import os
from azure.storage.blob import BlobClient
from azure.storage.blob import BlobServiceClient




#parsitaan komentoriviargumentistä talteen Rivimäärä-muuttuja
parser = argparse.ArgumentParser()
parser.add_argument("Rivimaara", type=int, help="Tulostettavien rivien määrä")
args = parser.parse_args()





#ladataan tehtävässä 1 upattu tiedosto. 
# Yhteys containeriin luodaan ympäristömuuttujassa olevan connection strigin avulla. Containerin ja tiedoston nimet annetaan parametreina
def downloadfile(containername,filename):
    connection_string = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
    BlobServiceClient.from_connection_string(connection_string)
    blob = BlobClient.from_connection_string(connection_string,containername, filename)
    with open(filename, "wb") as my_blob:
        blob_data = blob.download_blob()
        blob_data.readinto(my_blob)

def CutSortAndPrint(filename):
    readlist=[]
    cutlist=[]
    with open(filename) as file:
        for rivi in file:
            rivi=rivi.replace("\n","")
            readlist.append(rivi)

    cutlist=readlist[0:args.Rivimaara]
    print(cutlist)

#lajiteltu=sorted(alkulista,key=lambda x: (len(x),x))



downloadfile("checkpointcontainer","checkpoint.txt")
CutSortAndPrint("checkpoint.txt")
