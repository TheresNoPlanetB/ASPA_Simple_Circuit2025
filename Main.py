# Import the necessary classes and Solution class
from Circuit import Circuit
from Bus import Bus
from Solution import Solution

# Define the circuit
circuit = Circuit("Simple DC Circuit for Project One with the class Advanced Power System Analysis")

# Add buses A and B
circuit.add_bus(Bus("A"))
circuit.add_bus(Bus("B"))

# Voltage source Va connected at bus A with 100 V
circuit.add_vsource_element("Va", "A", 100.0)

# Resistor Rab connected between buses A and B with 5 Ohms
circuit.add_resistor_element("Rab", "A", "B", 5.0)

# Load Lb connected to bus B with power of 2000 W and nominal voltage of 100 V (constant impedance model)
load_power = 2000  # in watts
nominal_voltage = 100  # in volts
load_resistance = (nominal_voltage ** 2) / load_power  # Calculate load resistance
circuit.add_load_element("Lb", "B", load_power, nominal_voltage)  # Reactive power is zero for resistive load

# Create a solution object and simulate the circuit
solution = Solution(circuit)
solution.do_power_flow()

# Display the calculated nodal voltages and circuit current
circuit.print_nodal_voltage()
circuit.print_circuit_current()