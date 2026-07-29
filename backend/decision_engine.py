from products import products

class DecisionEngine:

    def __init__(self):
        self.last_state = None
        self.state_count = 0
        self.cart = []
        self.essential_index = 0
        self.relaxed_index = 0

    def process_prediction(self, state):

        # Same prediction again
        if state == self.last_state:
            self.state_count += 1
        else:
            self.last_state = state
            self.state_count = 1

        # Need 5 consecutive predictions
        if self.state_count == 5:

            if state == "Concentration":

                if self.essential_index < len(products["Concentration"]):

                    item = products["Concentration"][self.essential_index]
                    self.cart.append(item)
                    self.essential_index += 1

                    return f"Added {item['name']}"

            else:

                if self.relaxed_index < len(products["Relaxed"]):

                    item = products["Relaxed"][self.relaxed_index]
                    self.cart.append(item)
                    self.relaxed_index += 1

                    return f"Added {item['name']}"

        return None