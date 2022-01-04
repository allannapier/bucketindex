import os
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__
import pathlib
import settings

filetypes = {
    "pdf" : "Document",
    "doc" : "Document",
    "docx" : "Document",
    "txt" : "Text File",
    "bmp" : "Image",
    "jpg" : "Image",
    "png" : "Image",
    "jpeg" : "Image",
    "html" : "Web Page",
    "htm" : "Web Page",
    "php" : "Web Page",
    "js" : "Javascript file",
    "py" : "Python Script",

}

filenames = {
    "invoice" : "Invoice",
    "order" : "Order",
    "logo" : "Logo",
    "menu" : "Menu",
    "certificate" : "Certificate"
}



class indexfiles:

    def __init__(self):
        self.HOST = settings.azure_host
        self.CONTAINER_ID = settings.azure_container_id
        #aetup blob access
        self.connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
        self.blob_service_client = BlobServiceClient.from_connection_string(self.connect_str)
        self.container_name = 'files'
        self.container_client = self.blob_service_client.get_container_client(self.container_name)
        

    def get_file_info(self,file):
    
        file1 = {
            "id":file,
            "filename": "uploads/salesorder1.pdf",
            "sizeMB": "1.6",
            "lastModified": "",
            "Category": "pdf file"
        }

        return file1

    def generate_metadata(self,filename):
        metadata = []
        #generate metadata based on file type
        file_extension = pathlib.Path(filename).suffix
        for key in filetypes:
            if key in file_extension:
                metadata.append(filetypes[key])
        
        #lets examine the filename to get an idea on the type of document it may be

        for key in filenames:
            if key in filename.lower():
                metadata.append(filenames[key])

        return metadata


    def get_bucket_files(self):
        blob_list = self.container_client.list_blobs()
        for blob in blob_list:
            fileinfo = self.get_file_info("SalesOrder1")
            metadata = self.generate_metadata(blob.name)
            x=0
            for entry in metadata:
                blob.metadata[x] = entry
                x = x + 1
            print("\t" + blob.name, blob.metadata)
            

run1 = indexfiles()
run1.get_bucket_files()
