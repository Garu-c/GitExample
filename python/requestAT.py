import requests
import json


class MakeApiCall:
    
    def get_data(self, api, parameters):
        response = requests.get(api, params=parameters)
        if response.status_code == 200:
            print("sucessfully fetched the data")
            self.formatted_print(response.json())
        else:
            print(
                f"Hello person, there's a {response.status_code} error with your request")

    def formatted_print(self, obj):
        text = json.dumps(obj, sort_keys=True, indent=4)
        print(text)

    def __init__(self, api):  
        parameters = {
        "ApiIntegrationCode" : "C64GP2XSDWM2OLS3FVC4LEIRKNV",
        "UserName:" : "btlb5qsqfmagjpb@AIRPOWER.COM.BR",
        "Secret" : "0r_Q@Cj4Ny5V~Fn98XLdvt3YG",
        "Content-Type" : "application/json"
        }
        self.get_data(api, parameters)

if __name__ == "__main__":
    api_call = MakeApiCall("https://webservices3.autotask.net/atservicesrest/v1.0/tickets/query?search=         {%22filter%22:[\
    {%22op%22:%22contains%22,%22field%22:%22title%22,%22value%22:%22ZURICH%22},\
    {%22op%22:%22contains%22,%22field%22:%22title%22,%22value%22:%22Uplink%20status%20changed%22},\
    {%22op%22:%22noteq%22,%22field%22:%22status%22,%22value%22:5}]}")