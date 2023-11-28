class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """


    def __init__(self, start):
        """Constructor for SerialGenerator class, accepts "start" value passed
        into the intial Class instance and assigns it to a variable. Also
        creates a count property at value "start-1".
        """

        self.start = start
        self.count = start-1

    def __repr__(self):
        """repr for SerialGenerator class.
        """

        return f"<SelfGenerate start={self.start} count={self.count}"

    def generate(self):
        """generate method for instances of SerialGenerator class. Increments
        the self.count property and returns it.
        """

        self.count += 1
        return self.count

    def reset(self):
        """reset method for instances of SerialGenerator class. Resets the
        self.count property to self.start -1.
        """

        self.count = self.start - 1