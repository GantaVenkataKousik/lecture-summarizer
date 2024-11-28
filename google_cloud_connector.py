import os
from google.cloud import storage
from google.cloud import aiplatform

def initialize_google_cloud():
    # Set the environment variable for the service account key
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./service-account-file.json"

    # Initialize Google Cloud Storage client
    storage_client = storage.Client()
    print("Google Cloud Storage client initialized.")

    # Initialize AI Platform client
    aiplatform.init(project='your-project-id', location='your-region')
    print("AI Platform client initialized.")

# Example function to upload a file to Google Cloud Storage
def upload_to_gcs(bucket_name, source_file_name, destination_blob_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)
    print(f"File {source_file_name} uploaded to {destination_blob_name}.")

# Example function to use AI Platform
def use_ai_platform():
    # Example code to interact with AI Platform
    pass

if __name__ == "__main__":
    initialize_google_cloud()
    # Call other functions as needed 