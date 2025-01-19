# Import the necessary classes

from Circuit import Circuit

# Define the Bus class for completeness
class Bus:
    def __init__(self, name: str):
        self.name = name
        self.v: float = 0.0

    def __str__(self):
        return f"Bus {self.name}: Voltage = {self.v} V"

# Create an instance of the Circuit class
circuit = Circuit("Test Circuit")

# Add buses to the circuit
circuit.add_bus(Bus("Bus1"))
circuit.add_bus(Bus("Bus2"))

# Add resistor to the circuit
circuit.add_resistor_element("R1", "Bus1", "Bus2", 10.0)

# Add voltage source to the circuit
circuit.add_vsource_element("V1", "Bus1", 10.0)

# Perform power flow analysis
circuit.do_power_flow()

# Verify the results
circuit.print_nodal_voltage()
circuit.print_circuit_current()
