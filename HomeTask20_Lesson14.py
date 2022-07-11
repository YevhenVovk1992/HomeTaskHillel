"""
    Реализовать класс счетчика. В классе реализовать:

        установкe максимального и минимального значений (так же начального значения счётчика) при инициализации
        увеличения счетчика на 1
        возвращения текущего значения счётчика
        методы сравнения и равенства двух счетчиков
"""


class Counter:

    def __init__(self, start: int, stop: int, step=1):
        self.start = start
        self.stop = stop
        self.step = step
        self.current = start

    def increase(self):
        if self.current < self.stop:
            self.current += self.step
            return self.current
        else:
            return 'Out of the range'

    def get_current(self) -> int:
        return self.current

    def __str__(self) -> str:
        return f'Counter value {self.current}'

    def __eq__(self, other) -> bool:
        return self.current == other.current

    def __gt__(self, other) -> bool:
        return self.current > other.current

    def __ge__(self, other) -> bool:
        return self.current >= other.current


# Create two object of the class Counter
counter_1 = Counter(0, 3)
counter_2 = Counter(1, 5)
print(counter_1)
print(counter_2)

# Counter comparison
print('Are counters equal: ', counter_2 == counter_1)
counter_1.increase()

# Display counter values on the screen
print(counter_1.get_current())
print(counter_2.get_current())

# Count counters
print('Increment the counter: ', end=' ')
print(counter_1.increase(), end=', ')
print(counter_1.increase(), end=', ')
print(counter_1.increase())

# Counter comparison
print('counter_1 is biggest than counter_2: ', counter_1 > counter_2)