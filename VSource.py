class Vsource:
    def __init__(self, name: str, bus1: str, v: float):
        # Initialize the voltage source with a name, a bus, and a voltage value
        self.name = name  # Name of the voltage source
        self.bus1 = bus1  # Bus connected to the voltage source
        self.v = v  # Voltage value of the source

    def set_v(self, v: float):
        """
        Sets the voltage value of the source.
        This method updates the voltage attribute 'v' with the provided value.
        """
        self.v = v  # Update the voltage value of the source

if