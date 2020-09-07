class Store:
    def __init__(self, name, categories):
        # attributes
        self.name = name
        self.categories = categories

    def __str__(self):
        ret =f'\n{self.name}\n'

        for i, c in enumerate(self.categories):
            ret += '' + str(i+1) + ': '+ c.name + '\n'
        ret += '' + str(i+2) + ': Exit\n'

        return ret
    def __repr__(self):
        return f'Store({self.name}, {self.categories})'
