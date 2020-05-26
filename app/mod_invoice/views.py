from flask import Blueprint, jsonify, request
from marshmallow import ValidationError
from app.database import db
from app.mod_invoice.models import Order, OrderSchema

#order = Blueprint('order', __name__)

#order_schema = OrderSchema()
#orders_schema = OrderSchema(many=True)


#@order.route('/orders/', methods=['GET'])
#def get_orders():
#    orders = Order.query.all()
#    result = orders_schema.dump(orders)
#    return jsonify({'orders': result})


#@order.route('/orders/<int:pk>')
#def get_order():
#    return 'Get order'


#@order.route('/orders/', methods=['POST'])
#def new_order():
#    json_data = request.get_json()
#    if not json_data:
#        return jsonify({'message': 'No input data provided'}), 400
    # Validate and deserialize input
#    try:
#        data = order_schema.load(json_data)
#    except ValidationError as err:
#        return jsonify(err.messages), 422

#    db.session.add(data.data)
#    db.session.commit()
#    result = order_schema.dump(Order.query.get(data.data.id))
#    return jsonify({
#        'message': 'Created new quote.',
#        'order': result,
#    })


#@order.route('/orders/', methods=['PUT'])
#def update_order():
#    return 'Update order'


#@order.route('/orders/', methods=['DELETE'])
#def delete_order():
#    return 'Delete order'
