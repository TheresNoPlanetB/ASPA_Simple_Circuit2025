# Import the Bus class
from Bus import Bus

# Create a Bus object
bus1 = Bus("Bus1")

# Set the voltage at the bus
bus1.set_bus_v(120.0)

# Print the bus details to verify
print(f"Bus Name: {bus1.name}")
print(f"Bus Voltage: {bus1.v} V")
