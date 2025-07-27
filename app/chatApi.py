import requests
import json
 


class CTAPI:
    def __init__(self): 
        
        # cloud chatwoot shoubo@chinatourism
        self.cloud_url = f"https://app.chatwoot.com/api/v1/accounts/93650/conversations/"
        self.cloud_access_token ="WSFc9wQsRPVNS7GeNBumK4Tp"
        self.cloud_account_id = "93650"

        # self-host 本机Admin-shoubo   MuspfaBBdvmah2sMi84AvCZ3  
        self.host_url = f"https://seemingly-deep-polecat.ngrok-free.app/api/v1/accounts/2/conversations/"
        self.host_access_token ="MuspfaBBdvmah2sMi84AvCZ3"
        self.host_account_id = "2"

        self.cloud_headers = {
            'Content-Type': 'application/json',
            'api_access_token': self.cloud_access_token
            }
        
        self.host_headers = {
            'Content-Type': 'application/json',
            'api_access_token': self.host_access_token
            }

        # vpn-veee
        self.proxies = {'https': '127.0.0.1:15236'}
        
    def create_msg_card(self,conversationID): 
        print("entering api card:", conversationID,type(conversationID))

        payload = json.dumps({
        "content_attributes": {
            "items": [
            {
                "description": "Nike Shoe 8.0",
                "title": "Nike Shoes 8.0",
                "actions": [
                {
                    "uri": "https://chinatourismgroup.com",
                    "text": "View More",
                    "type": "link"
                },
                {
                    "payload": "ITEM_SELECTED",
                    "text": "Add to cart",
                    "type": "postback"
                }
                ],
                "media_url": "https://assets.ajio.com/medias/sys_master/root/hdb/h9a/13582024212510/-1117Wx1400H-460345219-white-MODEL.jpg"
            }
            ]
        },
        "content_type": "cards",
        "content": "card message",
        "private": False
        }) 
        url = self.cloud_url + str(conversationID) + "/messages"
        print(url)
        # response = requests.request("POST", url, headers=self.cloud_headers, data=payload,proxies=self.proxies) 
        response = requests.request("POST", url, headers=self.cloud_headers, data=payload) 
        print(response.text)

    def create_msg_article(self,conversationID): 
        print("entering api article:", conversationID,type(conversationID))

        payload = json.dumps({
            "content": "articles",
            "content_type": "article",
            "content_attributes": {
                "items": [
                    { "title": "Product Operation Guide", "description": "Comprehensive guide for product line and operation ", "link": "https://www.chinatourismgroup.com" },
                { "title": "Product Quotation for 2024", "description": "Pricing books for 2024", "link": "https://www.chinatourismgroup.com" }
                ]
            },
            "private":False
        }) 
        url = self.cloud_url + str(conversationID) + "/messages"
        print(url)
        # response = requests.request("POST", url, headers=self.cloud_headers, data=payload,proxies=self.proxies )
        response = requests.request("POST", url, headers=self.cloud_headers, data=payload)

        print(response.text)

    def create_msg_select(self,conversationID): 
        print("entering api select:", conversationID,type(conversationID))

        payload = json.dumps( {
            "content": " ",
            "content_type": "input_select",
            "content_attributes": {
                "items": [
                    { "title": "Product Related Issues", "value": "Sales" },
                    { "title": "Quotation & Pricing", "value": "Sales" },
                    { "title": "Shipment Status & Payment", "value": "AfterSale" },
                    { "title": "Others", "value": "Sales" }
                ]
            },
            "private":False
        }) 
        url = self.cloud_url + str(conversationID) + "/messages"
        print(url)
        # response = requests.request("POST", url, headers=self.cloud_headers, data=payload,proxies=self.proxies )
        response = requests.request("POST", url, headers=self.cloud_headers, data=payload)

        print(response.text)

    def create_msg_link(self,conversationID): 
        print("entering api links:", conversationID,type(conversationID))

        payload = json.dumps({
            "content": "articles",
            "content_type": "article",
            "content_attributes": {
                "items": [
                    { "title": "WKS Product Price List (2024-IV-101)", "description": "", "link": "https://www.chinatourismgroup.com/index/price-101-2024new.pdf" } 
                ]
            },
            "private":False
        }) 
        url = self.cloud_url + str(conversationID) + "/messages"
        print(url)
        # response = requests.request("POST", url, headers=self.cloud_headers, data=payload,proxies=self.proxies )
        response = requests.request("POST", url, headers=self.cloud_headers, data=payload)

        print(response.text)
