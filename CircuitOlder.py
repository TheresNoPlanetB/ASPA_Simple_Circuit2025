# Import the necessary classes
from Bus import Bus
from Resistor import Resistor
from VSource import VSource

class Circuit:
    """
    Represents a simple electrical circuit consisting of buses, resistors, and a voltage source.
    """

    def __init__(self, name: str):
        """
        Initializes the Circuit object with a name and empty dictionaries for buses and resistors.
        :param name: Name of the circuit.
        """
        self.name = name  # Name of the circuit
        self.buses: dict[str, Bus] = {}  # Dictionary to store Bus objects
        self.resistors: dict[str, Resistor] = {}  # Dictionary to store Resistor objects
        self.vsource: VSource = None  # VSource object, initially set to None
        self.i: float = 0.0  # Current flowing through the circuit, initially set to 0.0

    def add_bus(self, bus: Bus):
        """
        Adds a bus to the circuit.
        The bus is added to the buses dictionary with its name as the key.
        :param bus: Bus object to be added.
        """
        self.buses[bus.name] = bus  # Add the Bus object to the buses dictionary

    def add_resistor_element(self, name: str, bus1: str, bus2: str, r: float):
        """
        Adds a resistor to the circuit.
        The resistor is created and added to the resistors dictionary with its name as the key.
        :param name: Name of the resistor.
        :param bus1: Name of the first bus connected to the resistor.
        :param bus2: Name of the second bus connected to the resistor.
        :param r: Resistance of the resistor in ohms.
        """
        if bus1 in self.buses and bus2 in self.buses:
            resistor = Resistor(name, bus1, bus2, r)  # Create a Resistor object
            self.resistors[name] = resistor  # Add the Resistor object to the resistors dictionary
        else:
            print(f"Error: One or both buses ({bus1}, {bus2}) do not exist.")

    def add_vsource_element(self, name: str, bus1: str, v: float):
        """
        Adds a voltage source to the circuit.
        The voltage source is created and assigned to the vsource attribute.
        :param name: Name of the voltage source.
        :param bus1: Name of the bus connected to the positive terminal of the source.
        :param v: Voltage value of the source in volts.
        """
        if bus1 in self.buses:
            self.vsource = VSource(name, bus1, v)  # Create a VSource object and assign it to the vsource attribute
        else:
            print(f"Error: Bus {bus1} does not exist for voltage source.")

    def set_i(self, i: float):
        """
        Updates the current flowing through the circuit.
        This method updates the i attribute with the provided value.
        :param i: Current value to set for the circuit.
        """
        self.i = i  # Update the current flowing through the circuit

    def print_nodal_voltage(self):
        """
        Prints the voltages at all buses.
        Iterates through the buses dictionary and prints the voltage of each bus.
        """
        for bus in self.buses.values():
            print(f"Bus {bus.name}: Voltage = {bus.v} V")  # Print the voltage of each bus

    def print_circuit_current(self):
        """
        Prints the current flowing through the circuit.
        """
        print(f"Circuit current: {self.i} A")  # Print the current flowing through the circuit

    def calculate_total_resistance(self):
        """
        Calculates the total resistance of the circuit.
        This is a simplified version considering only resistors in series.
        :return: Total resistance of the circuit.
        """
        total_resistance = 0.0
        for resistor in self.resistors.values():
            total_resistance += resistor.r  # Assuming series circuit for simplicity
        return total_resistance

    def do_power_flow(self):
        """
        Solves for the voltages at each bus and the current in the circuit using power flow analysis.
        """
        total_resistance = self.calculate_total_resistance()
        if total_resistance > 0:
            # Using Ohm's law to compute voltage across the entire circuit based on total resistance
            total_voltage = self.vsource.v if self.vsource else 0
            self.i = total_voltage / total_resistance  # Simplified for series resistors

            # Assuming the voltage at the first bus is the source voltage
            if self.vsource:
                first_bus = self.buses[self.vsource.bus1]
                first_bus.v = self.vsource.v

            # Update the voltage at each bus based on the current and resistances
            for resistor in self.resistors.values():
                if resistor.bus1 in self.buses and resistor.bus2 in self.buses:
                    bus1 = self.buses[resistor.bus1]
                    bus2 = self.buses[resistor.bus2]
                    voltage_drop = self.i * resistor.r
                    bus2.v = bus1.v - voltage_drop

            # Print the results
            self.print_nodal_voltage()
            self.print_circuit_current()
        else:
            print("Error: Total resistance is zero. Check your circuit configuration.")

# Example usage:
# Create a Circuit object
circuit = Circuit("Test Circuit")

# Add buses A and B
circuit.add_bus(Bus("A"))
circuit.add_bus(Bus("B"))

# Add resistor and voltage source
circuit.add_resistor_element("R1", "A", "B", 5.0)
circuit.add_vsource_element("V1", "A", 100.0)

# Perform power flow analysis
circuit.do_power_flow()