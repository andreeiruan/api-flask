from flask.json import jsonify
from app import app
from flask import request
from ..useCases.contracts_usecase import Contracts
from ..useCases.combine_orders_usecase import Orders
from ..repositories.Contracts import contracts_repository_singleton
from ..repositories.Orders import orders_repository_singleton


@app.route('/open_contracts', methods=['GET'])
def get_open_contracts():
    open_contracts = contracts_repository_singleton.get_open_contracts()
    open_contracts_dicts = list(
        map(lambda c: {'id': c.id, 'debt': c.debt}, open_contracts))
    renegotiated_contracts = contracts_repository_singleton.get_renegotiated_contracts()
    top_n = request.args.get('top_n')
    top_n_open_contracts = Contracts().get_top_N_open_contracts(
        open_contracts, renegotiated_contracts, top_n)
    return jsonify({'top_n_open_contracts': top_n_open_contracts, 'open_contracts': open_contracts_dicts, 'renegotiated_contracts': renegotiated_contracts}), 200


@app.route('/combined_orders', methods=['GET'])
def calculate_minimum_trips():
    requests = orders_repository_singleton.get_daily_orders()
    n_max = orders_repository_singleton.get_maximum_travel_value()
    response = Orders().combine_orders(requests, n_max)
    return jsonify(response), 200
