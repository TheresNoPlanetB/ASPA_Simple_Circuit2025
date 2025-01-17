# Import the necessary classes
from Bus import Bus
from Resistor import Resistor
from Load import Load
from VSource import Vsource

class Circuit:
    def __init__(self, name: str):
        # Initialize the circuit with a name and empty dictionaries for buses, resistors, and loads
        self.name = name  # Name of the circuit
        self.buses: dict[str, Bus] = {}  # Dictionary to store Bus objects
        self.resistors: dict[str, Resistor] = {}  # Dictionary to store Resistor objects
        self.loads: dict[str, Load] = {}  # Dictionary to store Load objects
        self.VSource = VSource
        self.i: float = 0.0  # Current flowing through the circuit, initially set to 0.0

    def add_bus(self, bus: Bus):
        """
        Adds a bus to the circuit.
        The bus is added to the buses dictionary with its name as the key.
        """
        self.buses[bus.name] = bus  # Add the Bus object to the buses dictionary

    def add_resistor_element(self, name: str, bus1: str, bus2: str, r: float):
        """
        Adds a resistor to the circuit.
        The resistor is created and added to the resistors dictionary with its name as the key.
        """
        resistor = Resistor(name, bus1, bus2, r)  # Create a Resistor object
        self.resistors[name] = resistor  # Add the Resistor object to the resistors dictionary

    def add_load_element(self, name: str, bus1: str, p: float, q: float):
        """
        Adds a load to the circuit.
        The load is created and added to the loads dictionary with its name as the key.
        """
        load = Load(name, bus1, p, q)  # Create a Load object
        self.loads[name] = load  # Add the Load object to the loads dictionary

    def add_vsource_element(self, name: str, bus1: str, v: float):
        """
        Adds a voltage source to the circuit.
        The voltage source is created and assigned to the vsource attribute.
        """
        self.vsource = Vsource(name, bus1, v)  # Create a Vsource object and assign it to the vsource attribute

    def set_i(self, i: float):
        """
        Updates the current flowing through the circuit.
        This method updates the i attribute with the provided value.
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

# Create a Circuit object
circuit = Circuit("Test Circuit")

# Add buses to the circuit
bus1 = Bus("Bus1")
bus2 = Bus("Bus2")
circuit.add_bus(bus1)
circuit.add_bus(bus2)

# Add a resistor to the circuit
circuit.add_resistor_element("R1", "Bus1", "Bus2", 10.0)

# Add a load to the circuit
circuit.add_load_element("L1", "Bus1", 5.0, 3.0)

# Add a voltage source to the circuit
circuit.add_vsource_element("V1", "Bus1", 120.0)

# Set the current flowing through the circuit
circuit.set_i(15.0)

# Print the nodal voltages
circuit.print_nodal_voltage()

# Print the circuit current
circuit.print_circuit_current()
