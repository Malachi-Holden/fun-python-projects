"""
This is a program for running a turing machine. It is very old and may or may not work.
I plan to redesign it soon
"""

class State:
    def __init__(self, ruleNone, rule1, rule2):
        """

        :param ruleNone: a tuple (return, state, movement) telling what number to place down, what state to go to next,
        and where to move next if turing reads None
        :param rule1: a tuple (return, state, movement) telling what number to place down, what state to go to next,
        and where to move next if turing reads 1
        :param rule2: a tuple (return, state, movement) telling what number to place down, what state to go to next,
        and where to move next if turing reads 2
        """
        self.rules = {None: ruleNone, 1: rule1, 2: rule2}

    def __eq__(self, other):
        if self.rules == other.rules:
            return True
        return False

class Turing:
    def __init__(self):
        """
        The 0th state should always be the halting state. When the machine reaches this state, it will stop.
        """
        self.tape = {0: None}
        self.position = 0
        self.state = 1
        self.rules = {0: State((0, 0, 0), (0, 0, 0), (0, 0, 0))}  # number for state: state

    def update(self, state_number, state):
        """
        Adds a new state to the list of states
        :param state_number: a positive integer
        :param state: a State object
        :return: None
        """
        self.rules[state_number] = state

    def step(self):
        if self.position in self.tape.keys():
            current_value = self.tape[self.position]
        else:
            current_value = None
        current_position = self.position
        current_state = self.rules[self.state]

        self.tape[current_position] = current_state.rules[current_value][0]
        self.position += current_state.rules[current_value][2]
        self.state = current_state.rules[current_value][1]

    def run(self):
        while self.state != 0:
            self.step()


class Machine:
    def __init__(self, instructions):
        """

        :param instructions: a string, the name of a file with instructions
        """
        file = open(instructions, "r")
        raw_instructions = file.read()
        instructions_by_state = raw_instructions.split("\n")
        self.states = []
        for state_line in instructions_by_state:
            code = state_line.split(" ")
            self.states.append(State((int(code[0]), code[1], code[2]), (code[3], code[4], code[5]), (code[6], code[7], code[8])))










if __name__ == "__main__":
    turing = Turing()
    state1 = State((1, 2, 1), (1, 2, 1), (1, 2, 1))
    state2 = State((1, 3, 1), (1, 3, 1), (1, 3, 1))
    state3 = State((1, 4, 1), (1, 4, 1), (1, 4, 1))
    state4 = State((1, 0, 0), (1, 0, 0), (1, 0, 0))
    turing.update(1, state1)
    turing.update(2, state2)
    turing.update(3, state3)
    turing.update(4, state4)
    print(turing.tape, turing.position, turing.state)
    turing.run()
    print(turing.tape, turing.position, turing.state)
