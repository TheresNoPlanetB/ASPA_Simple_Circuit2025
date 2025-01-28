class Load:
    """
    Represents a load in a simple circuit. A load is connected to a bus and consumes power (P) and reactive power (Q).
    """

    def __init__(self, name: str, bus1: str, p: float, voltage: float):
        """
        Initializes a Load object with name, connected bus, and power consumption. 
        :param name: Name of the load as a string.
        :param bus1: The bus to which the load is connected.
        :param p: Real power consumed by the load in watts.
        :param q: Reactive power consumed by the load in vars.
        """
        self.name = name  #  Load name, e.g., "Load1". 
        self.bus1 = bus1  #  Name of the bus to which this load is connected. 
        self.p = p  #  Real power consumed by the load (watts). 
        self.voltage = voltage  #  Reactive power consumed by the load (vars).
        self.g = 0.0  #  Conductance of the load, to be calculated using calc_g(). 

        #  Calculate the conductance upon initialization. 
        self.calc_g()


    def calc_g(self):
        """
        Calculates the conductance (G) of the load using the formula: G = P / (V^2),
        assuming voltage V is provided during use. Defaults to V = 1.0 p.u. for initialization. 
        """
        if self.voltage != 0:
            self.g = self.p/(self.voltage ** 2)
        else:
            self.g = 0.0  # Avoid division by zero.


    def __str__(self):
        """
        Returns a readable string representation of the Load object.
        :return: A string in the format "Load {name}: Bus = {bus1}, P = {p} W, Q = {q} vars, G = {g} S".
        """
        return (
            f"Load {self.name}: Bus = {self.bus1}, P = {self.p} W, Q = {self.q} vars, "
            f"G = {self.g:.4f} S"
        )
