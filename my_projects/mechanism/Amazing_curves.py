from manimlib.imports import *
from my_manim_projects.my_projects.mechanism.basic_component import lcm

func_rotate = lambda t, r0=1, w0=1, phi_0=0, P0=0+0*1j: r0 * np.exp(1j * (w0 * t + phi_0)) + P0

def my_curve(t, r_list, w_list, phi_list, P_list):

    AC, CD = r_list[2], r_list[3]
    get_A = lambda t_: func_rotate(t_, r_list[0], w_list[0], phi_list[0], P_list[0])
    get_B = lambda t_: func_rotate(t_, r_list[1], w_list[1], phi_list[1], P_list[1])
    get_D = lambda t_: np.sqrt(AC ** 2 + CD ** 2) * np.exp(1j * (np.angle(get_B(t_) - get_A(t_)) + np.angle(AC + 1j * CD))) + get_A(t_)
    return get_D(t)

def my_curve_rotate(t, r_list, w_list, phi_list, P_list):

    AC, CD = r_list[2], r_list[3]
    get_A = lambda t_: func_rotate(t_, r_list[0], w_list[0], phi_list[0], P_list[0])
    get_B = lambda t_: func_rotate(t_, r_list[1], w_list[1], phi_list[1], P_list[1])
    get_D = lambda t_: (np.sqrt(AC ** 2 + CD ** 2) * np.exp(1j * (np.angle(get_B(t_) - get_A(t_)) + np.angle(AC + 1j * CD))) + get_A(t_)) * np.exp(w_list[2] * t * 1j)
    return get_D(t)

class Show_Curve_by_func(Scene):

    CONFIG = {
        'camera_config': {
            'background_color': WHITE,
        },
        'P_list': [complex(-4, 2.5), complex(3, -1)],
        'r_list': [1.6, 1.2, 5, -1],
        'phi_list': [120 * DEGREES, 30 * DEGREES],
        'T': [22, -3 * 17, 44],
        'rotate_or_not': True,
        # 'total_time': 11 * 21,
        # 'scale_factor': 1.6,
        'precision_factor': 5, # different from the precision_factor in other class
    }

    def construct(self):

        w = 1
        w_list = TAU/self.T[0] * w, TAU/self.T[1] * w, TAU/self.T[2] * w

        # curve_A = ParametricFunction(function=lambda t: complex_to_R3(func_rotate(t, self.r_list[0], w_list[0], self.phi_list[0], self.P_list[0])), t_min=0, t_max=t_total, color=RED)
        # curve_B = ParametricFunction(function=lambda t: complex_to_R3(func_rotate(t, self.r_list[1], w_list[1], self.phi_list[1], self.P_list[1])), t_min=0, t_max=t_total, color=PINK)

        if self.rotate_or_not:
            t_total = lcm(lcm(self.T[0], self.T[1]), self.T[2])
            print('t_total: %.2f' % t_total)
            curve = ParametricFunction(function=lambda t: complex_to_R3(my_curve_rotate(t, self.r_list, w_list, self.phi_list, self.P_list)), t_min=0, t_max=t_total, color=BLUE_D, stroke_width=1.2, step_size=t_total/1000/self.precision_factor).set_height(7.2).move_to(ORIGIN)
        else:
            t_total = lcm(self.T[0], self.T[1])
            print('t_total: %.2f' % t_total)
            curve = ParametricFunction(function=lambda t: complex_to_R3(my_curve(t, self.r_list, w_list, self.phi_list, self.P_list)), t_min=0, t_max=t_total, color=BLUE_D, stroke_width=1.2, step_size=t_total/1000/self.precision_factor)#.set_height(6).move_to(ORIGIN)

        self.add(curve)
        # self.play(ShowCreation(curve), run_time=50)
        self.wait(2)


class Curve_by_func_01(Show_Curve_by_func):

    CONFIG = {
        'camera_config': {
            'background_color': WHITE,
        },
        'P_list': [complex(-4, 2.5), complex(3, -1)],
        'r_list': [1.8, 1.5, 3., -1.5],
        'phi_list': [120 * DEGREES, 30 * DEGREES],
        'T': [22, -3 * 13, 55],
        'rotate_or_not': True,
        # 'total_time': 11 * 21,
        # 'scale_factor': 1.6,
        'precision_factor': 4, # different from the precision_factor in other class
    }


class Curve_by_func_02(Show_Curve_by_func):

    CONFIG = {
        'camera_config': {
            'background_color': WHITE,
        },
        'P_list': [complex(-4, 2.5), complex(3, -1)],
        'r_list': [4, 1, 6.4, -2.4],
        'phi_list': [120 * DEGREES, 30 * DEGREES],
        'T': [29, -31, 31 * 8],
        'rotate_or_not': True,
        # 'total_time': 11 * 21,
        # 'scale_factor': 1.6,
        'precision_factor': 2, # different from the precision_factor in other class
    }


class Curve_by_func_03(Show_Curve_by_func):

    CONFIG = {
        'camera_config': {
            'background_color': WHITE,
        },
        'P_list': [complex(-4, 2.5), complex(3, -1)],
        'r_list': [4, 1, 6.4, -2.4],
        'phi_list': [120 * DEGREES, 30 * DEGREES],
        'T': [29, -31, 31 * 5],
        'rotate_or_not': True,
        # 'total_time': 11 * 21,
        # 'scale_factor': 1.6,
        'precision_factor': 2, # different from the precision_factor in other class
    }
