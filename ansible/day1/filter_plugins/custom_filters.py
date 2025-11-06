def subtract(pair):
    a, b = pair
    return a - b

class FilterModule(object):
    def filters(self):
        return {
            'subtract': subtract,
        }
