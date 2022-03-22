import sys

class FSA:
    def __init__(self, fsa_def_file_name):
        self.fsa_tokens = []
        self.fsa_def_file_name = fsa_def_file_name
        self.read()

    def read(self):
        with open(self.fsa_def_file_name) as fsa_file:
            content = fsa_file.readline()
        print('the FSA: ' + content)
        global tokens
        tokens = content.split(';')

    def show_tokens(self):
        for i in range(0,len(tokens)-1):
            print('token - ' + tokens[i])

fsa_def_file_name = sys.argv[1]
fsa = FSA(fsa_def_file_name)
fsa.show_tokens()