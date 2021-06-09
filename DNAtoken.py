import requests
import json

base_url = "https://dcloud-dna-center-inst-rtp.cisco.com/dna/"
auth_endpoint = "system/api/v1/auth/token"

user = 'devnetuser'
password = '@@@@'

auth_response = requests.post(url="https://sandboxdnac2.cisco.com/dna/system/api/v1/auth/token", auth=(user, password)).json()

token = auth_response['Token']

headers = {
    "x-auth-token": token,
    "Accept": "application/json",
    "Content-Type": "application/json"
}

