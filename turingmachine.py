class TuringMachine:
    def __init__(self, tape="", blank_symbol=" ", initial_state="", final_states=None, transition_function=None, tape_symbols=None):
        self.tape = list(tape)
        self.blank_symbol = blank_symbol
        self.head_position = 0
        self.current_state = initial_state
        self.final_states = final_states if final_states is not None else set()
        self.transition_function = transition_function if transition_function is not None else {}
        self.tape_symbols = tape_symbols if tape_symbols is not None else set(tape)
        self.transitions_log = []

        # Add the blank symbol to the tape symbols
        self.tape_symbols.add(blank_symbol)

        # Verify the consistency of the transition function
        self._validate_transition_function()

    def _validate_transition_function(self):
        for (state, symbol), (new_state, new_symbol, direction) in self.transition_function.items():
            if symbol not in self.tape_symbols:
                raise ValueError(f"Symbol {symbol} in transition function not in tape symbols.")
            if new_symbol not in self.tape_symbols:
                raise ValueError(f"New symbol {new_symbol} in transition function not in tape symbols.")
            if direction not in {"L", "R", "S"}:
                raise ValueError(f"Direction {direction} in transition function is invalid.")

    def step(self):
        if self.current_state in self.final_states:
            return False
        current_symbol = self.tape[self.head_position]
        if (self.current_state, current_symbol) in self.transition_function:
            new_state, new_symbol, direction = self.transition_function[(self.current_state, current_symbol)]
            self.transitions_log.append((self.current_state, current_symbol, new_state, new_symbol, direction))
            #print(f"State: {self.current_state}, Read: {current_symbol}, Next State: {new_state}, Write: {new_symbol}, Move: {direction}")
            self.tape[self.head_position] = new_symbol
            self.current_state = new_state
            if direction == "R":
                self.head_position += 1
                if self.head_position == len(self.tape):
                    self.tape.append(self.blank_symbol)
            elif direction == "L":
                if self.head_position == 0:
                    self.tape.insert(0, self.blank_symbol)
                else:
                    self.head_position -= 1
            # No movement for direction 'S'
        else:
            raise Exception(f"No transition defined for state {self.current_state} and symbol {current_symbol}")
        return True

    def run(self):
        while self.current_state not in self.final_states:
            self.step()

    def get_tape(self):
        return "".join(self.tape).rstrip(self.blank_symbol)

    def get_head_position(self):
        return self.head_position

    def is_accepting(self):
        return self.current_state in self.final_states

    def print_transitions_log(self):
        print("\nTransitions Log:")
        for transition in self.transitions_log:
            print(
                f"State: {transition[0]}, Read: {transition[1]}, Next State: {transition[2]}, Write: {transition[3]}, Move: {transition[4]}")

    def get_decimal(self):
        tape = self.get_tape()
        return tape.count('1')