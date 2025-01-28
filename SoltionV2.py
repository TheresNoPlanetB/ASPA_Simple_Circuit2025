# Import the necessary classes
from Circuit import Circuit


class Solution:
    """
    Represents the solution for a DC circuit. This class computes the circuit's power flow,
    including the current and voltage at each bus, using Ohm's law and nodal voltage analysis.
    """

    def __init__(self, circuit: Circuit):
        """
        Initializes the Solution object with a Circuit object.

        :param circuit: An instance of the Circuit class representing the DC circuit to solve.
        """
        self.circuit = circuit

    def do_power_flow(self):
        """
        Solves the circuit by calculating bus voltages and the circuit current.
        Assumes:
        - A voltage source is connected to one bus.
        - Resistors are connected in series between buses.

        :raises ValueError: If no voltage source or resistors are defined in the circuit.
        """
        if not self.circuit.vsource:
            raise ValueError("Error: No voltage source defined in the circuit.")

        if len(self.circuit.resistors) < 1:
            raise ValueError("Error: No resistors defined in the circuit.")

        # Calculate total resistance for a series circuit
        total_resistance = self.circuit.calculate_total_resistance()

        if total_resistance > 0:
            # Calculate the current using Ohm's law: I = V / R
            total_voltage = self.circuit.vsource.v
            circuit_current = total_voltage / total_resistance
            self.circuit.set_i(circuit_current)  # Update current in the circuit

            # Set voltage at the source bus
            source_bus = self.circuit.buses[self.circuit.vsource.bus1]
            source_bus.set_bus_v(total_voltage)

            # Update voltages across all buses based on voltage drops
            for resistor in self.circuit.resistors.values():
                if resistor.bus1 in self.circuit.buses and resistor.bus2 in self.circuit.buses:
                    bus1 = self.circuit.buses[resistor.bus1]
                    bus2 = self.circuit.buses[resistor.bus2]
                    voltage_drop = circuit_current * resistor.r  # Ohm's law: V = IR
                    bus2.set_bus_v(bus1.v - voltage_drop)

            # Print final results
            self.circuit.print_nodal_voltage()
            self.circuit.print_circuit_current()
        else:
            raise ValueError("Error: Total resistance must be greater than zero.")
