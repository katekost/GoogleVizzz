from google.cloud import vision
from google.cloud.vision import types
from google.oauth2 import service_account

# Authentification with Services Account Key
# We need to create key on App Engine Project and download .json

credentials = service_account.Credentials.from_service_account_file('nth-avatar-119019-1d8f80012b95.json')

# Create Connection

vision_client = vision.ImageAnnotatorClient(credentials=credentials)

# Transform image to binary code

with io.open(file_name,'rb') as image_file:
    cnt = image_file.read()

img = types.Image(content=cnt)

# Get the service responce
response = vision_client.label_detection(image=img,  max_results=10)

# Print the detected objects
labels = response.label_annotations
