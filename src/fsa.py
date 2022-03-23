import sys

class FiniteStateAutomata:

    def __init__(self, def_file_name, string_file_name):
        self.tokens = []
        self._read_def_file(def_file_name)

    def _read_def_file(self, def_file_name):
        with open(def_file_name) as fsa_file:
            content = fsa_file.readline()
        self.tokens = content.split(';')

    # temporary testing function
    def show_tokens(self):
        for i in range(0,len(self.tokens)-1):
            print('token - ' + self.tokens[i])

fsa_def_file_name = sys.argv[1]
fsa_string_file_name = sys.argv[2]

fsa = FiniteStateAutomata(fsa_def_file_name, fsa_string_file_name)
fsa.show_tokens()