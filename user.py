class User:
    def __init__(self, first_name, last_name):
        self.fn = first_name
        self.ln = last_name
        

    def prfirst_name(self):
        print(self.fn)

    def prlast_name(self):
        print(self.ln)

    def prAll_name(self):
        print(self.fn, self.ln)