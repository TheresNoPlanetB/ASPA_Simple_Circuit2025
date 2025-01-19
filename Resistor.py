class Resistor:
    """
    Represents a resistor in a simple circuit. The resistor connects two buses
    and introduces resistance and conductance into the circuit.
    """

    def __init__(self, name: str, bus1: str, bus2: str, r: float):
        """
        *** Initializes a Resistor object with name, connected buses, and resistance. ***
        :param name: Name of the resistor as a string.
        :param bus1: The name of the first bus connected to the resistor.
        :param bus2: The name of the second bus connected to the resistor.
        :param r: Resistance of the resistor in ohms.
        """
        self.name = name  # *** Name of the resistor, e.g., "R1". ***
        self.bus1 = bus1  # *** Name of the first connected bus. ***
        self.bus2 = bus2  # *** Name of the second connected bus. ***
        self.r = r  # *** Resistance in ohms. ***
        self.g = 0.0  # *** Conductance, to be calculated using calc_g(). ***

        # *** Calculate the conductance upon initialization. ***
        self.calc_g()

    def calc_g(self):
        """
        *** Calculates the conductance (G) of the resistor using the formula: G = 1 / R. ***
        """
        if self.r != 0:
            self.g = 1 / self.r
        else:
            self.g = 0.0  # Avoid division by zero.

    def __str__(self):
        """
        *** Returns a human-readable string representation of the Resistor object. ***
        :return: A string in the format "Resistor {name}: Buses = {bus1}-{bus2}, R = {r} Ω, G = {g} S".
        """
        return (
            f"Resistor {self.name}: Buses = {self.bus1}-{self.bus2}, "
            f"R = {self.r} Ω, G = {self.g:.4f} S"
        )
