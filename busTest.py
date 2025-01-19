# Import the Bus class
from Bus import Bus

if __name__ == "__main__":
    # *** Create a new bus object named "A". ***
    bus1 = Bus("A")

    # *** Print the initial state of the bus (Voltage should be 0.0). ***
    print(bus1)  # Output: Bus A: Voltage = 0.0 V

    # *** Update the voltage of the bus to 12.0 volts. ***
    bus1.set_bus_v(12.0)

    # *** Print the updated state of the bus. ***
    print(bus1)  # Output: Bus A: Voltage = 12.0 V
