import requests
import json


url = 'https://api.digitalocean.com/v2/domains'

class DigitalOceanAPI:
    
    def __init__(self,token):
        self.token = token

    def get_all_domains(self):
        headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer '+ self.token
        }

        payload={}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text)


    def create_domain(self,domain,ip):

        headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer '+ self.token
        }
        payload = json.dumps({
          "name": domain,
          "ip_address": ip
        })

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)



if __name__ == "__main__":

    token = 'dop_v1_5c6a65d56ea77dfa28d6147f3b7c4ca7018984b8d41739e5b828c7100dbf7651'

    # domain_list = [
    # 'barkatdesigningplanet.com',
    # 'chasingsunsets.in',
    # ]

    do_api = DigitalOceanAPI(token)
    do_api.get_all_domains()


    # do_api.create_domain('ganjalust.con')
    # # create_domain_record_A()
    # # do_api.create_subdomain('1872102','demo12','jurasystems.in')
    # # create_domain_CNAME_record()
