
class Bus:
    """
    Represents a bus in a simple circuit. A bus serves as a node where
    electrical components such as resistors, loads, and voltage sources connect.
    """

    def __init__(self, name: str):
        """
        *** Initializes a Bus object with a name and a default voltage. ***
        :param name: A unique name for the bus (e.g., "A", "B").
        """
        self.name = name  # *** The unique identifier for this bus. ***
        self.v = 0.0  # *** Initialize voltage at the bus to 0.0 volts. ***

    def set_bus_v(self, bus_v: float):
        """
        *** Updates the voltage at this bus. ***
        :param bus_v: The voltage value to set for this bus.
        """
        self.v = bus_v  # *** Set the voltage to the provided value. ***

    def __str__(self):
        """
        *** Returns a human-readable string representation of the bus,
        showing its name and current voltage. ***
        :return: A string in the format "Bus {name}: Voltage = {v} V".
        """
        return f"Bus {self.name}: Voltage = {self.v} V"
