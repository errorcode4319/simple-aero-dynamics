import numpy as np 
import math 
import matplotlib.pyplot as plt

# R이 0인 지점에 대한 예외처리를 위해 일부 로직의 분모항에 더해줌 
EPSILON = 1e-10

def create_mesh_grid(x_min, x_max, y_min, y_max, step = 1):
    X, Y = np.meshgrid(
        np.arange(x_min, x_max + step, step),
        np.arange(y_min, y_max + step, step))
    return X, Y



def draw_vector_field(X, Y, U, V):
    # 벡터 크기 계산
    magnitude = np.sqrt(U**2 + V**2) + EPSILON 

    U = U / (magnitude)
    V = V / (magnitude)

    fig, ax = plt.subplots()
    # magnitude(크기)를 C 인자로 전달, cmap으로 색상 지정
    quiver = ax.quiver(
        X, Y, U, V, magnitude, 
        angles='xy', scale_units='xy', 
        cmap='coolwarm', 
        # scale=2, 
        # width=0.005 
    )
    fig.colorbar(quiver, ax=ax)  # 색상바 추가
    ax.set_xlim(X[0][0], X[0][-1])
    ax.set_ylim(Y[0][0], Y[-1][0])
    plt.show()


def create_polar_field(X, Y):
    R = np.sqrt(X**2 + Y**2)
    C = np.arctan2(Y, X)


def conv_velocity_polar2cartesian(R, C, V_r, V_c):
    U = V_r * np.cos(C) - V_c * np.sin(C)
    V = V_r * np.sin(C) + V_c * np.cos(C)
    return U, V


# 용출 (strength: 용출 강도)
def source(R, C, strength):
    V_r = strength / (2 * math.pi * R + EPSILON)   
    V_c = C * 0.0
    
    # R == 0인 지점에 대한 예외처리
    V_r = np.where((R == 0), 0, V_r)
    
    return conv_velocity_polar2cartesian(R, C, V_r, V_c)


# 용입 (용출과 동일한 로직 사용)
def sink(R, C, strength):
    return source(R, C, -strength)


# 와류 (circulation: 순환강도 Γ)
def vortex(R, C, circulation):
    V_r = R * 0.0
    V_c = -circulation / (2 * math.pi * R + EPSILON)
    
    # R == 0인 지점에 대한 예외처리
    V_c = np.where((R == 0), 0, V_c)
    
    return conv_velocity_polar2cartesian(R, C, V_r, V_c)


# 더블릿 (moment: 더블릿 모멘트 K)
def doublet(R, C, moment): 
    V_r = (-moment * np.cos(C)) / (2 * math.pi * (R**2) + EPSILON)
    V_c = (-moment * np.sin(C)) / (2 * math.pi * (R**2) + EPSILON)
    
    # R == 0인 지점에 대한 예외처리
    V_r = np.where((R == 0), 0, V_r)
    V_c = np.where((R == 0), 0, V_c)

    return conv_velocity_polar2cartesian(R, C, V_r, V_c)