
"""
    State class
        takes in name, two input symbols and transitions on those inputs
"""

class State:
    def __init__(self, name, a, b, on_a_go_to, on_b_go_to):
        self.name = name
        self.a = a
        self.b = b
        self.transitions = {self.a:on_a_go_to, self.b:on_b_go_to}

    # def init(self):
    #     self.transitions[self.a] = self.name 
    #     self.transitions[self.b] = self.name 

    def transition(self, input):
        return self.transitions[input]

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def set_transition(self, input, state):
        self.transitions[input] = state

    def print_info(self):
        print("{}\t{}\t{}".format(self.name, self.transitions[self.a], self.transitions[self.b]))  



""" Tests """
# state = State("A", 0, 1, "B", "C")
# state.transition(1)
# state.transition(0)
# state.print_info()


# state = State(1, "a", "b", 2, 5)
# state.transition("b")
# state.transition("a")
# state.print_info()
