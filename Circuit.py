# Import the necessary classes
from Bus import Bus
from Resistor import Resistor
from VSource import VSource
from Load import Load


class Circuit:
    """
    Represents a simple DC circuit consisting of buses, resistors, loads, and a voltage source.
    Provides functionality to manage components and perform power flow calculations.
    """

    def __init__(self, name: str):
        """
        Initializes a Circuit object with a name and empty dictionaries for circuit elements.
        :param name: Name of the circuit as a string.
        """
        self.name = name  # Circuit name
        self.buses: dict[str, Bus] = {}  # Stores Bus objects indexed by their names
        self.resistors: dict[str, Resistor] = {}  # Stores Resistor objects indexed by their names
        self.loads: dict[str, Load] = {}  # Stores Load objects indexed by their names
        self.vsource: VSource = VSource  # The single voltage source in the circuit
        self.i: float = 0.0  # Current flowing through the circuit

    def add_bus(self, bus: Bus):
        """
        Adds a bus to the circuit.
        :param bus: A Bus object to add.
        """
        self.buses[bus.name] = bus  # Add the Bus object to the dictionary
        print(f"Bus {bus.name} added to the circuit.")

    def add_resistor_element(self, name: str, bus1: str, bus2: str, r: float):
        """
        Adds a resistor between two buses in the circuit.
        :param name: Name of the resistor.
        :param bus1: The first bus connected to the resistor.
        :param bus2: The second bus connected to the resistor.
        :param r: Resistance value in ohms.
        """
        if bus1 in self.buses and bus2 in self.buses:
            resistor = Resistor(name, bus1, bus2, r)
            self.resistors[name] = resistor
            print(f"Resistor {name} added between buses {bus1} and {bus2} with R = {r} Ω.")
        else:
            print(f"Error: One or both buses ({bus1}, {bus2}) do not exist.")

    def add_load_element(self, name: str, bus1: str, p: float, voltage: float):
        """
        Adds a load connected to a single bus in the circuit.
        :param name: Name of the load.
        :param bus1: The bus to which the load is connected.
        :param p: Real power consumption in watts.
        :param voltage: Nominal operating voltage of the load in volts.
        """
        if bus1 in self.buses:
            load = Load(name, bus1, p, voltage)
            self.loads[name] = load
            print(f"Load {name} added to bus {bus1} with P = {p} W at {voltage} V.")
        else:
            print(f"Error: Bus {bus1} does not exist.")

    def add_vsource_element(self, name: str, bus1: str, v: float):
        """
        Adds a voltage source connected to a single bus.
        :param name: Name of the voltage source.
        :param bus1: The bus to which the voltage source is connected.
        :param v: Voltage value of the source in volts.
        """
        if bus1 in self.buses:
            self.vsource = VSource(name, bus1, v)
            print(f"Voltage source {name} added to bus {bus1} with V = {v} V.")
        else:
            print(f" ‼️ Error: Bus {bus1} does not exist for voltage source. ⚡️")

    def calculate_total_resistance(self) -> float:
        """
        Calculates the total resistance of the circuit assuming a series configuration.
        :return: Total resistance in ohms.
        """
        total_resistance = sum(resistor.r for resistor in self.resistors.values())
        return total_resistance

    def print_nodal_voltage(self):
        """
        Prints the voltages of all buses in the circuit.
        """
        for bus in self.buses.values():
            print(f"Bus {bus.name} voltage = {bus.v:.1f} V")

    def print_circuit_current(self):
        """
        Prints the current flowing through the circuit.
        """
        print(f"Circuit current = {self.i:.1f} A")

    def do_power_flow(self):
        """
        Solves the circuit by calculating bus voltages and circuit current.
        Assumes a voltage source at a bus and resistors connecting other buses.
        """
        if not self.vsource:
            print("Error: No voltage source defined in the circuit.")
            return

        # Calculate total resistance
        total_resistance = self.calculate_total_resistance()

        if total_resistance > 0:
            # Calculate current using Ohm's law: I = V / R
            self.i = self.vsource.v / total_resistance

            # Set voltage at bus A (source bus)
            source_bus = self.buses[self.vsource.bus1]
            source_bus.set_bus_v(self.vsource.v)

            # Calculate voltage drops across resistors and update bus voltages
            for resistor in self.resistors.values():
                if resistor.bus1 in self.buses and resistor.bus2 in self.buses:
                    bus1 = self.buses[resistor.bus1]
                    bus2 = self.buses[resistor.bus2]
                    voltage_drop = resistor.r * self.i  # Ohm's Law: V = IR
                    bus2.set_bus_v(bus1.v - voltage_drop)

            # Print results
            self.print_nodal_voltage()
            self.print_circuit_current()
        else:
            print(" ❗️Error: Total resistance must be greater than zero.")
