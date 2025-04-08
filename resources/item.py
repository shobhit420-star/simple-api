import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import ItemSchema , ItemUpdateSchema
from models import ItemModel
from db import db 
from sqlalchemy.exc import SQLAlchemyError

# from db import items

blp = Blueprint("Items", __name__, description="Operations on items")


@blp.route("/item/<string:item_id>")
class Item(MethodView):


# <><><><><><><><><><><><><><><><><><><><><
    @blp.response(200, ItemSchema)
    def get(self, item_id):
        item = ItemModel.query.get_or_404(item_id)
        return item






# <><><><><><><><><><><><><><><><><><><><><
    def delete(self, item_id):
        item = ItemModel.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return {"message": "Item deleted."}





# <><><><><><><><><><><><><><><><><><><><><



# shobhit here we have also managed to get the abstracted validation using  marshmallow , remember that the url 
# arguement always come at the last     
    '''
    Order of parameters
    Be careful here since we've now got item_data and item_id. The URL arguments come in at the end. 
    The injected arguments are passed first, so item_data goes before item_id in our function signature.
    '''
    @blp.arguments(ItemUpdateSchema)
    @blp.response(200, ItemSchema)
    def put(self, item_data,item_id):

        item = ItemModel.query.get(item_id)
        if item:
            item.price = item_data["price"]
            item.name = item_data["name"]
        else:
            item = ItemModel(id=item_id, **item_data)

        db.session.add(item)
        db.session.commit()

        return item









#______________________________________________________________________________------------------___________________-----------------____________________


@blp.route("/item")
class ItemList(MethodView):

    @blp.response(200, ItemSchema(many=True))
    def get(self):
        return ItemModel.query.all()
    



    # post method <><><><><><><><><><><><


    @blp.arguments(ItemSchema)
    @blp.response(201, ItemSchema)
    def post(self,item_data):

        item = ItemModel(**item_data)  # ** here means that when we recieve data from clients it gets unpacked 
        try:
            db.session.add ( item)
            db.session.commit()


        except SQLAlchemyError:
            abort(500, message = 'error occured while inserting the data')


       
        return item