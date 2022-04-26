""" 
    *** Deterministic Finite Automata - DFA
    *** Awet Thon
    *** 20-03-2022
"""
import State
class DynamicStateMachine:
    def __init__(self,name="Dynamic State Machine"):
        self.name = name
        self.current_state = None
        self.initial_state = None
        self.final_states = []
        self.language = None
        self.states_dict = {}

    def insert_state(self, key, state):
        self.states_dict[key] = state

    def print_info(self):
        print("TRANSACTION TABLE")
        print("{}\t{}\t{}".format("STATE", "ON A", "ON B"))
        for state in self.states_dict.values():
            state.print_info()
 
    def transition(self, input):
        next_state = self.states_dict[self.current_state].transition(input)
        print("Current State: {}\tInput: {}\tNext State: {}".format(self.current_state, input, next_state) )
        self.current_state = next_state

    def is_final_state(self):
        return self.current_state in self.final_states 

    def set_initial_state(self,state):
        if state in self.states_dict:
            self.current_state = self.initial_state = state
        else:
            print("Error In Setting Initial State: Unknown state: '{}'".format(state))     

    def set_final_state(self, state):
        state = str(state)
        if state in self.states_dict:
            self.final_states.append(state)  
        else:
            print("Error In Setting Final State: Unknown state: '{}'".format(state))      

    def init(self):
        self.read()

        """ set first state as initial state and last state as final state """
        k = list(self.states_dict.keys())
        self.set_initial_state(k[0])
        self.set_final_state(k[len(k)-1])

    # initialize states and their transitions using data from transition table
    def read(self,filename="table2.txt"):
        input_a, input_b = "", ""
        with open(filename, 'r') as f:
            for line in f:
                line = line.strip()
                if line.startswith("#"):
                    _, input_a, input_b = tuple(line.split())
                elif len(line) > 0:
                    state, on_a, on_b = tuple(line.split())
                    self.insert_state(state, State.State(state,input_a, input_b, on_a, on_b))
        f.close()

    """TODO MINIMIZE DFA STATES"""
    def minimize(self):
        states = [state for state in self.states_dict]
        f_states = []
        non_f_states = []
        for state in states:
            if state in self.final_states:
                # print("Found final state: {}".format(state))
                f_states.append(state)
            else:
                non_f_states.append(state)    

        
    
machine = DynamicStateMachine()
machine.init()
machine.print_info()
machine.set_final_state(5)
machine.set_final_state(6)


input = [ "a","b", "a", "b","b","a", "b","a", "a", "b"]
i = 0

while i < len(input):
    machine.transition(input[i])
    i += 1
if machine.is_final_state():
    print("current state: {}".format(machine.current_state))
    print("final state: {}".format(machine.final_states))
    print(input)
    print("String accepted")
else:
    print("current state: {}".format(machine.current_state))
    print("final state: {}".format(machine.final_states))
    print(input)
    print("String rejected")        
