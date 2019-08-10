class Counter():
    def __init__(self, counter):
        self.counter = counter
        self.initial_counter = counter

    def next(self):
        if self.counter == 100:
            self.counter = 0
        else:
            self.counter += 1
        return self.counter

    def reset(self):
        self.counter = self.initial_counter
        return self.counter


# Case 1
counter = Counter(1)
assert counter.next() == 2

# Case 2
counter = Counter(100)
assert counter.next() == 0

# Case 3
counter = Counter(50)
counter.next()
assert counter.reset() == 50
