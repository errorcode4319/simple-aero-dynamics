import numpy as np
import utils 


class CylinderModel:

    def __init__(self, X, Y):
        self.X = X 
        self.Y = Y
        self.R = np.sqrt(X**2 + Y**2)
        self.C = np.arctan2(Y, X)
        self.U = X * 0.0
        self.V = Y * 0.0

    def reset(self):
        self.U = X * 0.0
        self.V = Y * 0.0

    def add_uniform_flow(self, velocity):
        self.U = self.U + velocity 
        return self 

    def add_sink(self, strength):
        self._run_calc_func(utils.sink, strength)
        return self 

    def add_source(self, strength):
        self._run_calc_func(utils.source, strength)
        return self 

    def add_vortex(self, circulation):
        self._run_calc_func(utils.vortex, circulation)
        return self 
        
    def add_doublet(self, moment):
        self._run_calc_func(utils.doublet, moment)
        return self 

    def get_uv(self):
        return self.U, self.V 

    def _run_calc_func(self, func, *args):
        U_offset, V_offset = func(self.R, self.C, *args)
        self.U = self.U + U_offset
        self.V = self.V + V_offset