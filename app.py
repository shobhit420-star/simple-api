import os

from flask import Flask
from flask_smorest import Api
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from db import db

import models

from resources.item import blp as ItemBlueprint
from resources.store import blp as StoreBlueprint
from resources.user import blp as UserBlueprint

def create_app(db_url=None):
    app = Flask(__name__)
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Stores REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config[
        "OPENAPI_SWAGGER_UI_URL"
    ] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URL", "sqlite:///data.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    # app.config["PROPAGATE_EXCEPTIONS"] = True
    db.init_app(app)
    migrate = Migrate(app, db)
    api = Api(app)

    app.config["JWT_SECRET_KEY"] = "shobhit"
    jwt = JWTManager(app)


    api.register_blueprint(ItemBlueprint)
    api.register_blueprint(StoreBlueprint)
    api.register_blueprint(UserBlueprint)

    return app





















# from flask import Flask, request
# import uuid
# from flask_smorest import abort
# app = Flask(__name__)

# from db import stores , items


# # stores = [{"name": "My Store", "items": [{"name": "my item", "price": 15.99}]}]




# @app.get("/store/<string:store_id>")
# def get_store(store_id):
#     try:
#         # Here you might also want to add the items in this store
#         # We'll do that later on in the course
#         return stores[store_id]
#     except KeyError:
#         abort(404,message="Store not found")

# @app.get("/store")
# def get_stores():
#     return {"stores": list(stores.values())}



# @app.post("/store")
# def create_store():
#     store_data = request.get_json()
#     if "name" not in store_data:
#         abort(
#             400,
#             message="Bad request. Ensure 'name' is included in the JSON payload.",
#         )
#     for store in stores.values():
#         if store_data["name"] == store["name"]:
#             abort(400, message=f"Store already exists.")

#     store_id = uuid.uuid4().hex
#     store = {**store_data, "id": store_id}
#     stores[store_id] = store

#     return store


# @app.post("/item")
# def create_item():
#     item_data = request.get_json()
#     # Here not only we need to validate data exists,
#     # But also what type of data. Price should be a float,
#     # for example.
#     if (
#         "price" not in item_data
#         or "store_id" not in item_data
#         or "name" not in item_data
#     ):
#         abort(
#             400,
#             message="Bad request. Ensure 'price', 'store_id', and 'name' are included in the JSON payload.",
#         )
#     for item in items.values():
#         if (
#             item_data["name"] == item["name"]
#             and item_data["store_id"] == item["store_id"]
#         ):
#             abort(400, message=f"Item already exists.")

#     item_id = uuid.uuid4().hex
#     item = {**item_data, "id": item_id}
#     items[item_id] = item

#     return item



# @app.get("/item")
# def get_all_items():
#     return "hello world"
#     # return {"items": list(items.values())} 




# @app.get("/item/<string:item_id>")
# def get_item(item_id):
#     try:

#         return items[item_id] ,
#     except KeyError:
#         return {"message": "Item not found"}, 404






# # deleting items 

# @app.delete("/item/<string:item_id>")
# def delete_item(item_id):
#     try:
#         del items[item_id]
#         return {"message": "Item deleted."}
#     except KeyError:
#         abort(404, message="Item not found.")







# # updating items 

# @app.put("/item/<string:item_id>")
# def update_item(item_id):
#     item_data = request.get_json()
#     # There's  more validation to do here!
#     # Like making sure price is a number, and also both items are optional
#     # You should also prevent keys that aren't 'price' or 'name' to be passed
#     # Difficult to do with an if statement...
#     if "price" not in item_data or "name" not in item_data:
#         abort(
#             400,
#             message="Bad request. Ensure 'price', and 'name' are included in the JSON payload.",
#         )
#     try:
#         item = items[item_id]
#         item |= item_data

#         return item
#     except KeyError:
#         abort(404, message="Item not found.")







# # deleting stores 

# @app.delete("/store/<string:store_id>")
# def delete_store(store_id):
#     try:
#         del stores[store_id]
#         return {"message": "Store deleted. lets giddy up"}
#     except KeyError:
#         abort(404, message="Store not found.")














