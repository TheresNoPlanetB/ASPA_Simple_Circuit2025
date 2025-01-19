from VSource import Vsource

if __name__ == "__main__":
    # *** Create a voltage source named "V1" connected to bus "A" with 12 volts. ***
    vsource1 = Vsource("V1", "A", 12.0)

    # *** Print the voltage source to verify its initialization. ***
    print(vsource1)  # Expected: Vsource V1: Bus = A, V = 12.0 V
