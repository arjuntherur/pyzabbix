from pyzabbix import ZabbixAPI,ZabbixAPIException, ZabbixAPIObject
import requests

zapi = ZabbixAPI("https://zabbix.tsworkz.com/zabbix")
zapi.login("tswadmin", "MyHeart@2023")
print("Connected to Zabbix API Version %s" % zapi.api_version())


# Define host parameters
host_name = "Test Host"
visible_name = "Zabbix Automation test"
host_group_id = 46 # ID of the host group the host will belong to
template_id = 11071 # IDs of the templates the host will use
tag_hostname = "Ghost"
tag_client_name = "Arackal"
marco_url = "https://blog-test.dev-tsworks.io"
macro_description = "blog test"

# Create host
new_host = zapi.host.create(
    host=host_name,
    name=visible_name,
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
            "description": macro_description
        }
    ]
)

print(f"New host ID: {new_host['hostids'][0]}")



