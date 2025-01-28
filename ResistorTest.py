from Resistor import Resistor

if __name__ == "__main__":
    # Create a resistor connecting buses "A" and "B" with resistance 10 ohms.
    resistor1 = Resistor("R1", "A", "B", 10.0)

    #  Print the resistor to verify initialization.
    print(resistor1)  # Expected: Resistor R1: Buses = A-B, R = 10.0 Ω, G = 0.1000 S

    #  Manually recalculate conductance and print the updated resistor object.
    resistor1.calc_g()
    print(resistor1)  # Should match the initial output.
