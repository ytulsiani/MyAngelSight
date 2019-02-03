import requests
from pprint import pprint
# curl -i -H "Accept: application/json" -H "Content-Type: application/json" -H "Authorization: Bearer BWx/gfXk0RpFthUECBO0W0mKvyRCrVTdTkbxdv+DKT4=" https://developers.tsys.com/sandbox/rewards/00000022340/information
# curl -X POST -i -H "Accept: application/json" -H "Content-Type: application/json" -H "Authorization: Bearer BWx/gfXk0RpFthUECBO0W0mKvyRCrVTdTkbxdv+DKT4=" https://developers.tsys.com/sandbox/rewards/00000013815/redemption/directdeposit

account_id = "00000022340"
access_token = "BWx/gfXk0RpFthUECBO0W0mKvyRCrVTdTkbxdv+DKT4="


def get_tsys():
    headers = {"Authorization": "Bearer BWx/gfXk0RpFthUECBO0W0mKvyRCrVTdTkbxdv+DKT4=",
            "Content-Type" : "application/json",
            "Accept" : "application/json"}
    url = "https://developers.tsys.com/sandbox/rewards/{}/information".format(account_id)

    result = requests.get(url, headers=headers)
    pprint(result.json())

def post_tsys():
    url="https://developers.tsys.com/sandbox/rewards/{}/redemption/directdeposit".format("00000013815")

    headers = {"Authorization": "Bearer BWx/gfXk0RpFthUECBO0W0mKvyRCrVTdTkbxdv+DKT4=",
            "Content-Type" : "application/json",
            "Accept" : "application/json"}
    
    body = {
        "transferAccountInfo": {
            "routingNumber": "67867867868878",
            "accountType": "Savings",
            "accountNumber": "65765765675"
        },
        "rewardsValue": "10000"
    }

    result = requests.post(url, headers=headers)
    pprint(result.json())

if __name__=="__main__":
    # get_tsys()

    post_tsys()

    

