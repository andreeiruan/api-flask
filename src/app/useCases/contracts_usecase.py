class Contracts:        
    def get_top_N_open_contracts(self, open_contracts, renegotiated_contracts, top_n):
        """
        Method that searches the account holders' unnegotiated debts 
        and returns a list sorting from the largest to the smallest debtor,
        limiting the number of contracts for the return.

        Args:
            open_contracts (list): List of open contracts.
            renegotiated_contracts (list): List of contract identifiers already renegotiated.
            top_n (int): Number of contracts to return

        Returns:
            [list]: List with identifiers of contracts not renegotiated and ordered from largest to smallest.
        """
        open_contracts.sort(key=lambda contract: contract.debt, reverse=True)        
        unrenegotiated_contracts = list(filter(lambda contract: contract.id not in renegotiated_contracts, open_contracts))
        id_contracts_unrenegotiated = [c.id for c in unrenegotiated_contracts]        
        return id_contracts_unrenegotiated[0: int(top_n)]


