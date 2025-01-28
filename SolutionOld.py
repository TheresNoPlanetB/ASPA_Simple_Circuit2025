"""This seeks to serve as a models and solves a DC circuit with a voltage
source, a series resistor, and a load resistor connected between buses A and B. The program
should calculate and display the voltage at each bus and the current flowing through the circuit.
"""

# Import the necessary classes
from Circuit import Circuit

class Solution:
    def __init__(self, circuit: Circuit):
        """
        Initialize the Solution object with a Circuit object.
        """
        self.circuit = circuit

    def do_power_flow(self):
        """
        Solves the circuit by finding bus voltages and circuit current.
        First, calculate the current using element conductance values,
        then determine the voltage at bus B.
        """
        total_conductance = 0.0
        for resistor in self.circuit.resistors.values():
            total_conductance += resistor.g  # Sum the conductances

        if total_conductance > 0:
            # Calculate the total current using Ohm's law
            total_voltage = self.circuit.vsource.v if self.circuit.vsource else 0
            self.circuit.i = total_voltage * total_conductance  # I = V * G

            # Calculate the voltage at bus B
            bus_a_voltage = self.circuit.vsource.v if self.circuit.vsource else 0
            voltage_drop = self.circuit.i / total_conductance  # V = I / G
            for resistor in self.circuit.resistors.values():
                if resistor.bus2 in self.circuit.buses:
                    bus_b = self.circuit.buses[resistor.bus2]
                    bus_b.v = bus_a_voltage - voltage_drop

            # Print the results
            self.circuit.print_nodal_voltage()
            self.circuit.print_circuit_current()
        else:
            print("Error: Total conductance is zero. Check your circuit configuration.")
