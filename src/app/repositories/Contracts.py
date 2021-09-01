from ..models.Contract import Contract
from random import randint


class ContractRepository:
    def get_open_contracts(self):
        contracts = [
            Contract(1, 185),
            Contract(2, 34),
            Contract(3, 47),
            Contract(4, 33),
            Contract(5, 127),
            Contract(6, 101),
            Contract(7, 25),
            Contract(8, 62),
            Contract(9, 161)
        ]
        return contracts

    def get_renegotiated_contracts(self):
        return [3, 5, 7, 8]


contracts_repository_singleton = ContractRepository()
