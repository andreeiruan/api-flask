class Orders:
    def combine_orders(self, requests, n_max):
        """Method that combines travel requests compared and matching travel
        values ​​with the maximum allowable value per trip.

        Args:
            requests (list): List with value for each trip.
            n_max (int): Maximum value of a combined trip.

        Returns:
            int: Returns the size of the combined travel request list.
        """
        return_requests = requests.copy()
        combined_requests = []
        while len(requests) > 0:
            if len(requests) == 1:
                combined_requests.append((requests[request - 1], 0))
                del(requests[request - 1])
            else:
                for request in range(0, len(requests) - 1):
                    for r in range(request + 1, len(requests) - 1):
                        value = requests[request]
                        del(requests[request])
                        summed_below_maximum = list(
                            filter(lambda re: re + value <= n_max, requests))
                        if len(summed_below_maximum) == 0:
                            combined_requests.append((value, 0))
                        else:
                            del_index = requests.index(
                                max(summed_below_maximum))
                            combined_requests.append(
                                (value, max(summed_below_maximum)))
                            del(requests[del_index])
                            break
                    break
        return {'combined_orders': len(combined_requests), 'requests': return_requests}
