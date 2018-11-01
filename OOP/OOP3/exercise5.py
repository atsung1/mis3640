class Coffee:
    """represents a coffee order
    
    attributes: shots of espresso, extras (milk, syrup, sweetener), whipped cream servings
    """
    def __init__(self, shots=1, extra=[], whip=0): 
        self.shots = shots
        self.extra = extra
        self.whip = whip

    def __str__(self):
        return '{} espresso shots with {} and {} serving(s) of whipped cream'.format(self.shots, self.extra, self.whip)

    def __eq__(self, other):
        return self.shots == other.shots

    def add_shot(self, num=1):
        self.shots += num
        return self

    def add_to_order(self, obj):
        self.extra.append(obj)
        return self

def main():
    a = Coffee(1, ['pumpkin spice', 'matcha'], 1)
    b = Coffee(2, ['pumpkin spice', 'matcha'], 1)
    print(a)
    print(b)
    print(a == b)
    print(a.add_shot(2))
    print(a.add_to_order('vanilla syrup'))


if __name__ == '__main__':
        main()