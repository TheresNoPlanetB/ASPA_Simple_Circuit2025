class Load:
    def __init__(self, name: str, bus1: str, p: float, q: float):
        # Initialize the load with a name, a bus, and power values
        self.name = name  # Name of the load
        self.bus1 = bus1  # Bus connected to the load
        self.p = p  # Active power value
        self.q = q  # Reactive power value
        self.g = self.calc_g()  # Calculate conductance during initialization

    def calc_g(self) -> float:
        """
        Calculates the conductance value.
        Conductance is the reciprocal of the sum of active and reactive power.
        Raises a ValueError if the sum of active and reactive power is zero.
        """
        if (self.p + self.q) != 0:
            return 1 / (self.p + self.q)  # Conductance is the reciprocal of the sum of active and reactive power
        else:
            raise ValueError("The sum of active and reactive power cannot be zero for conductance calculation.")
