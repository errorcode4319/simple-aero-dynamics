import numpy as np
import math 

import utils
from model import CylinderModel  


# 그리드 생성
X, Y = utils.create_mesh_grid(-1, 1, -1, 1, 0.05)

model = CylinderModel(X, Y)

model.add_uniform_flow(50)  # 균일 유동
model.add_source(100)       # 용출
model.add_vortex(100)       # 와류
model.add_doublet(30)       # 더블릿 

U, V = model.get_uv()

# 원점 속도 제거
U = np.where(((np.abs(X) < 0.01) & (np.abs(Y) < 0.01)), 0, U)
V = np.where(((np.abs(X) < 0.01) & (np.abs(Y) < 0.01)), 0, V)

utils.draw_vector_field(X, Y, U, V)