from pyzabbix import ZabbixAPI,ZabbixAPIException, ZabbixAPIObject
import requests
import os
import json

#define username and password

username = os.environ['ZABBIX_USERNAME']
password = os.environ['ZABBIX_PASSWORD']
zapi = ZabbixAPI("https://zabbix.tsworkz.com/zabbix")
zapi.login(username,password)
print("Connected to Zabbix API Version %s" % zapi.api_version())


# Define host parameters

host_name = os.environ['host_name']
host_group_id = 46 # ID of the host group the host will belong to
template_id = 11071 # IDs of the templates the host will use
tag_hostname = os.environ['tag_hostname']
tag_client_name = os.environ['tag_client_name']
marco_url = "https://blog-test.dev-tsworks.io"

# Create host
new_host = zapi.host.create(
    host=host_name,
    groups=[
        {
            "groupid": host_group_id
        }
    ],
    templates=[
        {
            "templateid": template_id
        }
    ],
    tags= [
            {
                "tag": "Host name",
                "value": tag_hostname
            },
            {
                "tag": "Client Name",
                "value": tag_client_name
            }
        ],
    macros=[
        {
            "macro": "{$TRIES.UNTIL.TRIGGER}",
            "value": "2"
        },
        {
            "macro": "{$URL}",
            "value": marco_url,
        }
    ]
)

print(f"New host ID: {new_host['hostids'][0]}")



