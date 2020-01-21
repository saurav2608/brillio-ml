# Read the wine-quality csv file from the URL
import pandas as pd
import logging
import os
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
container_name = 'data'
blob_service_client = BlobServiceClient.from_connection_string(connect_str)
source_file_name = 'semantic_layer/final_data.csv'

with open('~/data_trg/df.csv) as my_blob:
    blob_data = blob_downlaod_client.download_blob()
    blob_data.readinto(my_blob)