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

#funktio lukee ladatun tiedoston listaan, tiedoston nimi annetaan parametrina
#listasta valitaan komentoriviparametrin mukainen rivimäärä
#valitun mittainen lista järjestetään ensisijaisesti pituuden, toissijaisesti aakkosjärjestyksen mukaan
#järjestetyt alkiot tulostetaan yksi kerrallaan omille riveilleen
def CutSortAndPrint(filename):
    readlist=[]
    cutlist=[]
    sortedlist=[]
    with open(filename) as file:
        for rivi in file:
            rivi=rivi.replace("\n","")
            readlist.append(rivi)

    cutlist=readlist[0:args.Rivimaara]
    sortedlist=sorted(cutlist,key=lambda x: (len(x),x))

    for i in sortedlist:
        print(i)


#funktioiden suoritus
downloadfile("checkpointcontainer","checkpoint.txt")
CutSortAndPrint("checkpoint.txt")
