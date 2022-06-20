import json


def store_client_json(client):
    with open(r'C:\Users\alejo\PycharmProjects\pythonProject1\src\db\client_db.json', 'w') as store_file:
        json.dump(client, store_file)
        print('clients stored')
