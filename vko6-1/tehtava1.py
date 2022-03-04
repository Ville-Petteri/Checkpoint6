import requests
import json

import os
from azure.identity import AzureCliCredential
from azure.mgmt.storage import StorageManagementClient
from azure.storage.blob import BlobServiceClient
from azure.storage.blob import BlobClient


#haetaan subscription id ympäristömuuttujasta ja luodaan credential olio
credential = AzureCliCredential()
subscription_id = os.environ["SUBSCRIPTION_ID"]



def GetAndWrite():
    #haetaan data urlista ja tallennetaan se json muodossa data muuttujaan
    tiedosto=requests.get('https://2ri98gd9i4.execute-api.us-east-1.amazonaws.com/dev/academy-checkpoint2-json')
    data = tiedosto.json()

    #Avataan tai luodaan ja avataan tiedosto checkpoint.txt kirjoitamista varten
    #käydään datan items arvot läpi yksi kerrallaan ja haetaan sieltä avaimen parameter osoittama alkio ja kirjoitetaan se tiedostoon
    with open("checkpoint.txt", "w") as tiedosto:
        for i in data["items"]:
            tiedosto.write(i['parameter']+"\n")

#funktio luo uuden containerin olemassa olevaan storage accountiin, containerin nimi annetaan parametrina
def GreateBlobContainer(BCname,RGname,Storagename):
        storage_client = StorageManagementClient(credential,subscription_id)
        storage_client.blob_containers.create(
        RGname,
        Storagename,
        BCname,
        {}
        )
#funtio luo yhteuden containeriin ympäristömuuttujassa olevan connection stringin avulla ja lataa sinne parametrina annetun tiedoston
def uploadfiletocontainer(tiedosto,container):
    connection_string = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
    BlobServiceClient.from_connection_string(connection_string)
    blob = BlobClient.from_connection_string(connection_string, container, tiedosto)
    with open(tiedosto, "rb") as data:
        blob.upload_blob(data)


#funktioiden suoritus
GetAndWrite()
GreateBlobContainer("checkpointcontainer","ville-petteritestiRG","villepetteristorage")
uploadfiletocontainer("checkpoint.txt","checkpointcontainer")
    

