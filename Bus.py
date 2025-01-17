
class Bus:
    def __init__(self, name: str):
        # Initialize the bus with a name and set the default voltage to 0.0
        self.name = name  # Name of the bus
        self.v = float  # Voltage at the bus, no default

    def set_bus_v(self, bus_v: float):
        """
        Sets the voltage at the bus.
        This method updates the voltage attribute 'v' with the provided value.
        """
        self.v = bus_v  # Update the voltage at the bus


