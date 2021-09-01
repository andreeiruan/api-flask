from ..models import Contract
from contracts_usecase import Contracts

constracts = [
    Contract(1, 100),
    Contract(2, 45),
    Contract(3, 25),
    Contract(4, 65),
    Contract(5, 12),
    Contract(6, 89)
]
actual_open_contracts = Contracts(
).get_top_N_open_contracts(constracts, [4], 4)
expected_contracts = [1, 6, 2, 3]
assert expected_contracts == actual_open_contracts

constracts = [
    Contract(1, 1),
    Contract(2, 2),
    Contract(3, 3),
    Contract(4, 4),
    Contract(5, 5)
]
renegotiated = [3]
top_n = 3
actual_open_contracts = Contracts().get_top_N_open_contracts(
    constracts, renegotiated, top_n)
expected_open_contracts = [5, 4, 2]
assert expected_open_contracts == actual_open_contracts
