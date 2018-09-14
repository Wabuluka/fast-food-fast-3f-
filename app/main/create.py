from flask import Flask, jsonify
from . data import data


@app.route('/api/v1/orders', methods=['GET'])
@auth.login_required
def getOrders():
    return jsonify({'orders': orders})
    #return jsonify({'Orders': [make_public_task(order) for order in orders]})
