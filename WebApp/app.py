
from flask import Flask
# from azure.storage.blob import BlobServiceClient

app = Flask(__name__)
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

# connect_str = config['AZURE_STORAGE_CONNECTION_STRING']
# blob_service_client = BlobServiceClient.from_connection_string(connect_str)
# container_client = blob_service_client.get_container_client(container=config['AZURE_STORAGE_CONTAINER_NAME'])
# blob_list = container_client.list_blobs()
# for blob in blob_list:
# 	print("\t" + blob.name)

from vehicle.views import vehicles_bp
from tracking.views import tracking_bp
from settings import config

if __name__ == '__main__':
	app.register_blueprint(vehicles_bp)
	app.register_blueprint(tracking_bp)
	app.run(debug=config['DEBUG_MODE'])