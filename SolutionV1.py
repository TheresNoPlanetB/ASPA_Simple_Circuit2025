from Circuit import Circuit

class Solution:
    def __init__(self, circuit):
        """
        Initialize the Solution object with a Circuit object.
        """
        self.circuit = circuit

    def do_power_flow(self):
        """
        Solves the circuit by finding bus voltages and circuit current.
        Assumes a voltage source at Bus A with known resistances connecting Bus A to Bus B.
        """
        if not self.circuit.vsource or len(self.circuit.resistors) < 1:
            print("Error: Circuit must have at least one voltage source and one resistor.")
            return

        # Total circuit resistance
        total_resistance = self.circuit.calculate_total_resistance()

        # Calculate the circuit current using Ohm's law: I = V / R
        if total_resistance > 0:
            total_voltage = self.circuit.vsource.v
            circuit_current = total_voltage / total_resistance
            self.circuit.i = circuit_current

            # Set voltage at bus A
            bus_a = self.circuit.buses[self.circuit.vsource.bus1]
            bus_a.set_bus_v(total_voltage)

            # Calculate voltage at bus B
            for resistor in self.circuit.resistors.values():
                if resistor.bus2 in self.circuit.buses:
                    voltage_drop = resistor.r * circuit_current  # Voltage drop across resistor
                    bus_b = self.circuit.buses[resistor.bus2]
                    bus_b.set_bus_v(bus_a.v - voltage_drop)


            # Print final voltages and current
            self.circuit.print_nodal_voltage()
            self.circuit.print_circuit_current()
        else:
            print("Error: Total resistance must be greater than zero.")


# Main Script
if __name__ == "__main__":
    # Initialize circuit
    circuit = Circuit("Simple DC Circuit")

    # Add buses
    circuit.add_bus(Bus("A"))
    circuit.add_bus(Bus("B"))

    # Add voltage source (100V at Bus A)
    circuit.add_vsource_element("V1", "A", 100.0)

    # Add resistor (5 ohms between A and B)
    circuit.add_resistor_element("R1", "A", "B", 5.0)

    # Initialize solution and calculate power flow
    solution = Solution(circuit)
    solution.do_power_flow()
