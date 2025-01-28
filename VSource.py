class VSource:
    """
    Represents a voltage source in a simple circuit. A voltage source maintains
    a fixed voltage between two buses.
    """

    def __init__(self, name: str, bus1: str, v: float):
        """
        Initializes a VSource object with name, connected bus, and voltage.
        :param name: Name of the voltage source as a string.
        :param bus1: The name of the bus connected to the positive terminal of the source.
        :param v: Voltage value of the source in volts.
        """
        self.name = name  # Name of the voltage source, e.g., "V1".
        self.bus1 = bus1  # Bus connected to the positive terminal of the voltage source.
        self.v = v  # Voltage maintained by the voltage source in volts.

    def __str__(self):
        """
        Returns a readable string representation of the VSource object.
        :return: A string in the format "VSource {name}: Bus = {bus1}, V = {v} V".
        """
        return f"VSource {self.name}: Bus = {self.bus1}, V = {self.v} V"
