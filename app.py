import os
from flask import Flask 
from azure.cosmos import CosmosClient

app = Flask(_name_)

url = os.environ.get("COSMOS_ENDPOINT")
key = os.environ.get("AZURE_COSMOS_CONNECTION_STRING")
client = CosmosClient(url,credential=key)
database = client.get_database_client("v-db")
container = database.get_container_client("v_container")

@app.route("/")
def fello():
  item = container.read_item(item="1", partition_key="1")
  item['count'] += 1
  container.upsert_item(item)
  
  return f"<h1>Welcome!</h1><p>You are visitor number: {item['count']}</p>"
