class Resistor:
    def __init__(self, name: str, bus1: str, bus2: str, r: float):
        # Initialize the resistor with a name, two buses, and a resistance value
        self.name = name  # Name of the resistor
        self.bus1 = bus1  # First bus connected to the resistor
        self.bus2 = bus2  # Second bus connected to the resistor
        self.r = r  # Resistance value
        self.g = self.calc_g()  # Calculate conductance during initialization

    def calc_g(self) -> float:
        """
        Calculates the conductance value.
        Conductance is the reciprocal of resistance.
        Raises a ValueError if resistance is zero.
        """
        if self.r != 0:
            return 1 / self.r  # Conductance is the reciprocal of resistance
        else:
            raise ValueError("Resistance cannot be zero for conductance calculation.")

