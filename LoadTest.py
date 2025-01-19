from Load import Load

if __name__ == "__main__":
    # *** Create a load connected to bus "B" with power values. ***
    load1 = Load("Load1", "B", 100.0, 50.0)  # P = 100 W, Q = 50 vars

    # *** Print the load to verify initialization. ***
    print(load1)  # Expected: Load Load1: Bus = B, P = 100.0 W, Q = 50.0 vars, G = 100.0000 S

    # *** Manually recalculate conductance and print the updated load object. ***
    load1.calc_g()
    print(load1)  # Should match the initial output.
