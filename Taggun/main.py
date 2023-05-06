import requests
import base64

url = "https://app.nanonets.com/api/v2/OCR/FullText"

payload={'urls': ['MY_IMAGE_URL']}
files=[
  ('file',('FILE_NAME',open('FILE_PATH','rb'),'application/pdf'))
]
headers = {}

# TODO: generate API Key

# response = requests.request("POST", url, headers=headers, data=payload, files=files, auth=requests.auth.HTTPBasicAuth('REPLACE_API_KEY', ''))

# print(response.text)