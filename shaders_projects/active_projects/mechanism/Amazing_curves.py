from manimlib.imports import *

def gcd(a, b):
    while (b!=0):
        temp = a % b
        a = b
        b = temp
    return a

def lcm(a, b):
    return a * b / gcd(a, b)

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
        'precision_factor': 5, # to determine the step_size of curve. step_size = total_time/self.precision_factor/1000
        'colorful_mode': False,
    }

    def construct(self):

        w = 1
        w_list = TAU/self.T[0] * w, TAU/self.T[1] * w, TAU/self.T[2] * w

        if self.rotate_or_not:
            t_total = lcm(lcm(self.T[0], self.T[1]), self.T[2])
            print('t_total: %.2f' % t_total)
            curve = ParametricCurve(t_func=lambda t: complex_to_R3(my_curve_rotate(t, self.r_list, w_list, self.phi_list, self.P_list)), t_min=0, t_max=t_total, color=BLUE_D, stroke_width=1.2, step_size=t_total/1000/self.precision_factor).set_height(7.2).move_to(ORIGIN)
        else:
            t_total = lcm(self.T[0], self.T[1])
            print('t_total: %.2f' % t_total)
            curve = ParametricCurve(t_func=lambda t: complex_to_R3(my_curve(t, self.r_list, w_list, self.phi_list, self.P_list)), t_min=0, t_max=t_total, color=BLUE_D, stroke_width=1.2, step_size=t_total/1000/self.precision_factor)#.set_height(6).move_to(ORIGIN)

        if self.colorful_mode:
            curves = CurvesAsSubmobjects(curve)
            # n = int(len(curves)/max(abs(self.T[0]), abs(self.T[1])))
            n = int(len(curves)/29)
            # n = int(len(curves)/51)
            print(n)

            colors = color_gradient([RED, BLUE, GREEN, YELLOW, ORANGE, RED], n)
            for i in range(len(curves)):
                curves[i].set_color(colors[int(i%n)])
            self.add(curves)
            self.play(ShowCreation(curves), run_time=25)
        else:
            self.add(curve)
            # self.play(ShowCreation(curve), run_time=25)

        self.wait(2)


class Curve_by_func_01(Show_Curve_by_func):

    CONFIG = {
        'camera_config': {
            'background_color': WHITE,
        },
        'P_list': [complex(-4, 2.5), complex(3, -1)],
        'r_list': [1.8, 1.5, 3., -1.5],
        'phi_list': [120 * DEGREES, 30 * DEGREES],
        'T': [26, -51, 65],
        'rotate_or_not': True,
        'precision_factor': 2,
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
        'precision_factor': 2,
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
        'precision_factor': 2,
    }


class Curve_by_func_04(Show_Curve_by_func):

    CONFIG = {
        'camera_config': {
            'background_color': WHITE,
        },
        'P_list': [complex(-5, 3.), complex(4, 2)],
        'r_list': [2.4, 1.2, 4.5, -3.6],
        'phi_list': [170 * DEGREES, -120 * DEGREES],
        'T': [23, 29, 23 * 5],
        'rotate_or_not': True,
        'precision_factor': 2,
    }


class Curve_by_func_05(Show_Curve_by_func):

    CONFIG = {
        'camera_config': {
            'background_color': WHITE,
        },
        'P_list': [complex(-2, 2.4), complex(4, -3.)],
        'r_list': [3.2, 1.5, 4.5, -3.2],
        'phi_list': [170 * DEGREES, -120 * DEGREES],
        'T': [31, 29, 31 * 5],
        'rotate_or_not': True,
        'precision_factor': 2,
    }


class Curve_by_func_01_colorful(Curve_by_func_01):

    CONFIG = {
        'colorful_mode': True,
    }

class Curve_by_func_02_colorful(Curve_by_func_02):

    CONFIG = {
        'colorful_mode': True,
    }

class Curve_by_func_03_colorful(Curve_by_func_03):

    CONFIG = {
        'colorful_mode': True,
    }

class Curve_by_func_04_colorful(Curve_by_func_04):

    CONFIG = {
        'colorful_mode': True,
    }

class Curve_by_func_05_colorful(Curve_by_func_05):

    CONFIG = {
        'colorful_mode': True,
    }

class Curve_by_func_colorful(Show_Curve_by_func):

    CONFIG = {
        'colorful_mode': True,
    }


class Curve_nr2r(Show_Curve_by_func):

    CONFIG = {
        'camera_config': {
            'background_color': WHITE,
        },
        'P_list': [complex(-4, 2.5), complex(3, -1)],
        'r_list': [4, 1, 6.4, -2.4],
        'phi_list': [120 * DEGREES, 30 * DEGREES],
        'T': [29, -31, 31 * 5],
        # 'rotate_or_not': True,
        'precision_factor': 2,
    }

    def construct(self):
        w = 1
        w_list = TAU/self.T[0] * w, TAU/self.T[1] * w, TAU/self.T[2] * w


        t_total = lcm(lcm(self.T[0], self.T[1]), self.T[2])
        print('t_total: %.2f' % t_total)
        curve_r = ParametricCurve(t_func=lambda t: complex_to_R3(my_curve_rotate(t, self.r_list, w_list, self.phi_list, self.P_list)), t_min=0, t_max=t_total, color=BLUE_D, stroke_width=1.2, step_size=t_total/1000/self.precision_factor).scale(0.6, about_point=ORIGIN)

        t_total = lcm(self.T[0], self.T[1])
        print('t_total: %.2f' % t_total)
        curve_nr = ParametricCurve(t_func=lambda t: complex_to_R3(my_curve(t, self.r_list, w_list, self.phi_list, self.P_list)), t_min=0, t_max=t_total, color=BLUE_D, stroke_width=1.2, step_size=t_total/1000/self.precision_factor).scale(0.6, about_point=ORIGIN)

        self.play(ShowCreation(curve_nr), run_time=6)
        self.wait()
        self.play(ReplacementTransform(curve_nr, curve_r), run_time=6)
        # self.play(ShowCreation(curve), run_time=40)
        self.wait(2)


class Curve_Transform(Show_Curve_by_func):

    CONFIG = {
        'camera_config': {
            'background_color': WHITE,
        },
        'P_list': [complex(-4, 2.5), complex(3, -1)],
        'r_list': [1.8, 1.5, 3., -1.5],
        'phi_list': [120 * DEGREES, 30 * DEGREES],
        'T': [22, -3 * 13, 55],
        'rotate_or_not': True,
        'rotate_or_not': True,
        'precision_factor': 1,
    }

    def construct(self):
        w = 1
        w_list = TAU/self.T[0] * w, TAU/self.T[1] * w, TAU/self.T[2] * w

        self.r_list[-1] += 3

        if self.rotate_or_not:
            t_total = lcm(lcm(self.T[0], self.T[1]), self.T[2])
            print('t_total: %.2f' % t_total)
            curve = ParametricCurve(t_func=lambda t: complex_to_R3(my_curve_rotate(t, self.r_list, w_list, self.phi_list, self.P_list)), t_min=0, t_max=t_total, color=BLUE_D, stroke_width=1.2, step_size=t_total/1000/self.precision_factor).set_height(7.2).move_to(ORIGIN)
            curve.add_updater(lambda c: c.become(ParametricCurve(t_func=lambda t: complex_to_R3(my_curve_rotate(t, self.r_list, w_list, self.phi_list, self.P_list)), t_min=0, t_max=t_total, color=BLUE_D, stroke_width=1.2, step_size=t_total/1000/self.precision_factor).set_height(7.2).move_to(ORIGIN)))
        else:
            t_total = lcm(self.T[0], self.T[1])
            print('t_total: %.2f' % t_total)
            curve = ParametricCurve(t_func=lambda t: complex_to_R3(my_curve(t, self.r_list, w_list, self.phi_list, self.P_list)), t_min=0, t_max=t_total, color=BLUE_D, stroke_width=1.2, step_size=t_total/1000/self.precision_factor)#.set_height(6).move_to(ORIGIN)
            curve.add_updater(lambda c: c.become(ParametricCurve(t_func=lambda t: complex_to_R3(my_curve(t, self.r_list, w_list, self.phi_list, self.P_list)), t_min=0, t_max=t_total, color=BLUE_D, stroke_width=1.2, step_size=t_total/1000/self.precision_factor)))
        self.add(curve)
        self.wait()

        time=2
        for i in range(self.camera.frame_rate * 8):
            self.r_list[-1] += -6/self.camera.frame_rate/8
            self.wait(1/self.camera.frame_rate)
            print('i = %d' % i)

        self.wait(2)
