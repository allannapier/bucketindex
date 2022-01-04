# bucketindex
Indexes files in a azure storage bucket and creates metadata for each file

Metadata will be things like document type (Document, Image File etc) and the category of the document (invoice, menu, order form, certificate etc)

This indexing script can be used as a building block for a document management system.

In order to run it you have to have set your Azure Connection string on the machine that will be running the script, instructions here https://docs.microsoft.com/en-us/azure/storage/blobs/storage-quickstart-blobs-python

Then update the settings.py file with your host address and container_id (container is Azures word for a bucket)

To Do:

Currently this just works with Azure but the plan is to make it work with all the major clouds, S3, Google Cloud and Wasabi so you can choose your storage provider or even use multiple clouds.

The range of categories needs to be increased to improve categorisation.

Add the ability to read the file contents to figure out more categories for the file using AI
