import argparse
import os
from azure.storage.blob import BlobClient
from azure.storage.blob import BlobServiceClient




#parsitaan komentoriviargumentistä talteen Rivimäärä-muuttuja
parser = argparse.ArgumentParser()
parser.add_argument("Rivimäärä", type=int, help="Tulostettavien rivien määrä")
args = parser.parse_args()





#ladataan tehtävässä 1 upattu tiedosto
def downloadfile(containername,filename):
    connection_string = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
    BlobServiceClient.from_connection_string(connection_string)
    blob = BlobClient.from_connection_string(connection_string,containername, filename)
    with open(filename, "wb") as my_blob:
        blob_data = blob.download_blob()
        blob_data.readinto(my_blob)

downloadfile("checkpointblob","checkpoint.txt")
