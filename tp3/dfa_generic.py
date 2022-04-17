"""Deterministic finite automata"""

class DFA:


    def __init__(self):
        """Initialize automata"""
        self.Q = self.populate_states()
        self.SIGMA = self.populate_alphabet()
        self.DELTA = self.populate_transition_function()
        self.START_STATE, self.ACCEPT_STATES = self.set_start_accept()
        self.CURRENT_STATE = None


    def set_start_accept(self):
        """Takes user input for START_STATE and ACCEPT_STATE"""
        while(True):
            start = input("Enter the start state: ")
            accept = input("Enter the accept states: ").split()
            
            if (start in self.Q) and (set(accept).issubset(set(self.Q))): #.issubset: Return True if all items in set "accept" are present in set "Q"
                return start, accept
            else:
                print("Enter the start state and the acceptance states: {}.\nAcceptance states should be a valid subset of Q!!\n".format(self.Q))


    def populate_states(self):
        """Takes user input for states (Q)"""
        Q_input = input("Enter list of states separated by spaces: ").split()
        print("STATES : {}".format(Q_input))
        return Q_input
    

    def populate_alphabet(self):
        """Takes user input for alphabet/symbols (SIGMA)"""
        SIGMA_input = input("Enter input alphabet separated by spaces: ").split()
        print("ALPHABET : {}".format(SIGMA_input))
        return SIGMA_input


    def populate_transition_function(self):
        """Creates the transition function (Q X SIGMA -> Q) and prints it out"""
        transition_dict = {el : {el_2 : 'REJECT' for el_2 in self.SIGMA} for el in self.Q}

        for key, dict_value in transition_dict.items():
            print("Enter transitions for state {}. If required, use 'REJECT'.".format(key))

            for input_alphabet, transition_state in dict_value.items():
                transition_dict[key][input_alphabet] = input("CURRENT STATE : {}\tINPUT ALPHABET : {}\tNEXT STATE : ".format(key, input_alphabet))
        
        print("\nTRANSITION FUNCTION Q X SIGMA -> Q")
        print("CURRENT STATE\tINPUT ALPHABET\tNEXT STATE")
        for key, dict_value in transition_dict.items():
            for input_alphabet, transition_state in dict_value.items():
                print("{}\t\t{}\t\t{}".format(key, input_alphabet, transition_state))

        return transition_dict


    def run_state_transition(self, input_symbol):
        """Takes in current state and goes to next state based on input symbol."""
        if (self.CURRENT_STATE == 'REJECT'):
            return False
        print("CURRENT STATE : {}\tINPUT SYMBOL : {}\t NEXT STATE : {}".format(self.CURRENT_STATE, input_symbol, self.DELTA[self.CURRENT_STATE][input_symbol]))
        self.CURRENT_STATE = self.DELTA[self.CURRENT_STATE][input_symbol]
        return self.CURRENT_STATE


    def check_if_accept(self):
        """Checks if the current state is one of the accept states."""
        if self.CURRENT_STATE in self.ACCEPT_STATES:
            return True
        else:
            return False


    def run_machine(self, in_string):
        """Run the machine on input string"""
        self.CURRENT_STATE = self.START_STATE
        for ele in in_string:
            check_state = self.run_state_transition(ele)
            #Check if new state is not REJECT
            if (check_state == 'REJECT'):
                return False
        return self.check_if_accept()


if __name__ == "__main__":
    check = True
    print("\nDeterministic finite automata")
    machine = DFA()
    while(check):
        choice = int(input("\nEnter Choice:\n1. Replace Automata\n2. Run Automata on input string\n3. Exit\nEnter choice : "))
        if (choice == 1):
            machine = DFA()
        elif (choice == 2):
            input_string = list(input("Enter the input string : "))
            print("ACCEPTED" if machine.run_machine(input_string) else "REJECTED")
        elif (choice == 3):
            exit()  
        else:
            check = False
