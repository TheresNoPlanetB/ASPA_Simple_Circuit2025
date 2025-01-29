class Solution:
    def __init__(self, circuit):
        """
        Initialize a Solution object.
        :param circuit: The Circuit object to solve
        """
        self.circuit = circuit

    def do_power_flow(self):
        """
        Solve the power flow of the circuit.
        Calculate nodal voltages and circuit current.
        """
        # Fetch key components
        vsource = self.circuit.vsource
        resistor = next(iter(self.circuit.resistors.values()))
        load = next(iter(self.circuit.loads.values()))

        # Set voltage at bus A based on the voltage source
        self.circuit.buses[vsource.bus1].set_bus_v(vsource.v)

        # Calculate total conductance of the resistor and load
        total_g = 1 /((1/ resistor.g) + (1/load.g)) # Total conductance

        # Calculate voltage at bus B
        vb = vsource.v / (1 + (resistor.g / load.g))  # Voltage divider formula
        self.circuit.buses[load.bus1].set_bus_v(vb)

        # Calculate circuit current
        self.circuit.i = vb * total_g

