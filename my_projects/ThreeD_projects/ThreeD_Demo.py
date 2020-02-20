from manimlib.imports import *

class Test_camera(ThreeDScene):

    def construct(self):

        axes = ThreeDAxes()
        cube_yellow = Cube(fill_color=YELLOW, stroke_width=2, stroke_color=WHITE)
        sphere_blue = Sphere(fill_color=BLUE, checkerboard_colors=None).shift(OUT * 2)
        cube_green = Cube(fill_color=GREEN).scale([2, 0.5, 0.5]).shift(RIGHT * 3.25)

        phi_0, theta_0 = 0, 0 # 起始角度
        phi, theta = 60 * DEGREES, -120 * DEGREES # 目标角度

        self.set_camera_orientation(phi=phi_0, theta=theta_0)
        self.add(axes, cube_yellow, sphere_blue, cube_green)
        self.wait()
        dt = 1/15
        delta_phi, delta_theta = (phi - phi_0) / 30, (theta - theta_0) / 60
        for i in range(30):
            phi_0 += delta_phi
            self.set_camera_orientation(phi=phi_0, theta=theta_0)
            self.wait(dt)
        for i in range(60):
            theta_0 += delta_theta
            self.set_camera_orientation(phi=phi_0, theta=theta_0)
            self.wait(dt)
        self.wait(2)

class Curve_3D_test(SpecialThreeDScene):
    CONFIG = {
        "default_angled_camera_position": {
            "phi": 65 * DEGREES, # Angle off z axis
            "theta": -60 * DEGREES, # Rotation about z axis
            "distance": 50,
            "gamma": 0,  # Rotation about normal vector to camera
            },
        }
    def construct(self):
        self.set_camera_to_default_position()
        r = 2 # radius
        w = 4
        circle = ParametricFunction(lambda t: r * complex_to_R3(np.exp(1j * w * t)),
                                    t_min=0, t_max=TAU * 1.5, color=RED, stroke_width=8)
        spiral_line = ParametricFunction(lambda t: r * complex_to_R3(np.exp(1j * w * t)) + OUT * t,
                                    t_min=0, t_max=TAU * 1.5, color=PINK, stroke_width=8)
        circle.shift(IN * 2.5), spiral_line.shift(IN * 2.5)

        self.add(axes, circle)
        self.wait()
        self.play(TransformFromCopy(circle, spiral_line, rate_func=there_and_back), run_time=4)
        self.wait(2)

class Surface_test_01(SpecialThreeDScene):
    CONFIG = {
        "default_angled_camera_position": {
            "phi": 65 * DEGREES, # Angle off z axis
            "theta": -60 * DEGREES, # Rotation about z axis
            "distance": 50,
            "gamma": 0,  # Rotation about normal vector to camera
            },
        }
    def construct(self):
        self.set_camera_to_default_position()
        axes = self.get_axes()
        # create surface: z = sin(x ^ 2 + y ^ 2)
        surface = ParametricSurface(lambda u, v: np.array([u, v, np.sin(u ** 2 + v ** 2)]),
                                    u_min=-4, u_max=4, v_min=-4, v_max=4, resolution=(120, 120))
        self.add(axes, surface)
        self.wait(5)

class Surface_test_02(SpecialThreeDScene):
    CONFIG = {
        "default_angled_camera_position": {
            "phi": 65 * DEGREES, # Angle off z axis
            "theta": -60 * DEGREES, # Rotation about z axis
            "distance": 50,
            "gamma": 0,  # Rotation about normal vector to camera
            },
        }
    def construct(self):
        self.set_camera_to_default_position()
        axes = self.get_axes()
        w = 1
        surface_01 = ParametricSurface(lambda u, v: v * complex_to_R3(np.exp(1j * w * u)),
                                       u_min=0, u_max=TAU, v_min=1, v_max=3, checkerboard_colors=None,
                                       fill_color=BLUE_B, fill_opacity=0.8, stroke_color=BLUE_A, resolution=(60, 10))
        surface_02 = ParametricSurface(lambda u, v: v * complex_to_R3(np.exp(1j * w * u)) + OUT * u/PI * 2,
                                       u_min=0, u_max=TAU, v_min=1, v_max=3, checkerboard_colors=None,
                                       fill_color=BLUE_D, fill_opacity=0.8, stroke_color=BLUE_A, resolution=(60, 10))
        self.add(axes, surface_01)
        self.wait()
        self.play(TransformFromCopy(surface_01, surface_02, rate_func=linear), run_time=5)
        self.wait(2)

class Set_surface_color_test(SpecialThreeDScene):
    CONFIG = {
        "default_angled_camera_position": {
            "phi": 65 * DEGREES, # Angle off z axis
            "theta": -60 * DEGREES, # Rotation about z axis
            "distance": 50,
            "gamma": 0,  # Rotation about normal vector to camera
            },
        }
    def construct(self):
        self.set_camera_to_default_position()
        ##################################################################################
        # 下面这个是我们将要绘制的曲面方程，我们将渲染默认的曲面，以及曲面的线框图及上色后的曲面 #
        # R = sqrt(x ^ 2 + y ^ 2) + eps, z = sin(R) / R * 8 - 2                          #
        ##################################################################################
        R = lambda x, y: np.sqrt(x ** 2 + y ** 2) + 1e-8
        # surface_origin 为默认的展示方式，仅更改了resolution（也就是u, v方向的分段数）
        surface_origin = ParametricSurface(lambda u, v: np.array([u, v, 8 * np.sin(R(u, v))/R(u, v) - 2]),
                                           u_min=-8, u_max=8, v_min=-8, v_max=8, resolution=(50, 50)).scale(0.5)
        # surface_frame为线框图
        surface_frame = surface_origin.copy().set_fill(color=BLUE, opacity=0)
        # colored_frame和colored_surface为上色后的曲面线框图和上色后的曲面
        r = np.linspace(1e-8, 8 * np.sqrt(2), 1000)
        z = (8 * np.sin(r)/r - 2) / 2
        z_l = max(z) - min(z)
        colors = color_gradient([BLUE_E, YELLOW, RED], 100)
        colored_frame = surface_frame.copy()
        colored_surface = surface_origin.copy()
        for ff, fs in zip(colored_frame, colored_surface):
            f_z = ff.get_center()[-1]
            ff.set_color(colors[int((f_z-min(z))/z_l * 90)])
            fs.set_color(colors[int((f_z-min(z))/z_l * 90)])
        ## 下面是几种曲面的效果展示 ##
        self.add(surface_origin)
        self.wait()
        self.play(ReplacementTransform(surface_origin, surface_frame), run_time=2)
        self.wait()
        self.play(ReplacementTransform(surface_frame, colored_frame), run_time=2)
        self.wait()
        self.play(ReplacementTransform(colored_frame, colored_surface), run_time=2)
        self.wait(2)

class Surface_by_rotate(SpecialThreeDScene):
    CONFIG = {
        "default_angled_camera_position": {
            "phi": 65 * DEGREES, # Angle off z axis
            "theta": -60 * DEGREES, # Rotation about z axis
            "distance": 50,
            "gamma": 0,  # Rotation about normal vector to camera
            },
        }
    def construct(self):
        self.set_camera_to_default_position()
        axes = self.get_axes()
        ## 方法一：通过旋转矩阵实现旋转 ##
        ## 注：可使用manim中有的旋转矩阵，不用自己写 ##
        curve_01 = lambda x: np.array([x, 0, x ** 2/4]) # z = x ** 2 / 4
        surface_func = lambda u, v: np.dot(curve_01(v), rotation_matrix(u, OUT).T) # 将z(v)绕z轴旋转u度得到的曲面
        surface_by_rotate_01 = ParametricSurface(surface_func, u_min=0, u_max=TAU, v_min=0, v_max=3,
                                                checkerboard_colors=None, fill_color=YELLOW_D, fill_opacity=0.8,
                                                stroke_color=WHITE, stroke_width=2.5)
        ## 方法二：通过复数 ##
        # np.exp(1j * w * u)为旋转复数，其中w控制快慢
        theta = PI / 4 # 直线夹角
        curve_02 = lambda y: np.array([1, y, y * np.tan(theta)]) # 一条直线，单叶双曲线的母线
        w = 1
        surface_func_02 = lambda u, v: complex_to_R3(complex(*curve_02(v)[0:2]) * np.exp(1j * w * u)) + curve_02(v)[-1] * OUT
        surface_by_rotate_02 = ParametricSurface(surface_func_02, u_min=0, u_max=TAU, v_min=-2, v_max=2,
                                                 checkerboard_colors=None, fill_color=BLUE, fill_opacity=0.8,
                                                stroke_color=WHITE, stroke_width=2.5)
        self.add(axes)
        self.wait()
        self.play(ShowCreation(surface_by_rotate_01))
        self.wait(2)
        self.play(ReplacementTransform(surface_by_rotate_01, surface_by_rotate_02))
        self.wait(2)

class Surface_generated_by_rotating(SpecialThreeDScene):
    CONFIG = {
        "default_angled_camera_position": {
            "phi": 65 * DEGREES, # Angle off z axis
            "theta": -60 * DEGREES, # Rotation about z axis
            "distance": 50,
            "gamma": 0,  # Rotation about normal vector to camera
            },
        }
    def construct(self):

        self.set_camera_to_default_position()
        axes = self.get_axes()
        self.var_theta = 0.01

        theta = PI / 4 # 直线夹角
        line_func = lambda y: np.array([1, y, y * np.tan(theta)]) # 母直线

        line = ParametricFunction(line_func, t_min=-2, t_max=2, stroke_color=ORANGE, stroke_width=6)
        surface_func = lambda u, v: complex_to_R3(complex(*line_func(v)[0:2]) * np.exp(1j * u)) + line_func(v)[-1] * OUT
        surface_by_rotate = ParametricSurface(surface_func, u_min=0, u_max=self.var_theta, v_min=-2, v_max=2,
                                              checkerboard_colors=None, fill_color=BLUE, fill_opacity=0.8,
                                              stroke_color=WHITE, stroke_width=2.5)

        d_theta = 2 * DEGREES # the rotation angle in each frame
        def update_surface(s, dt):
            s.become(ParametricSurface(surface_func, u_min=0, u_max=self.var_theta, v_min=-2, v_max=2,
                                       checkerboard_colors=None, fill_color=BLUE, fill_opacity=0.8,
                                       stroke_color=WHITE, stroke_width=2.5))
            # TODO 此处的ParametricSurface中添加resolution的更新，使分段数在一开始不至于过密

            self.var_theta += d_theta

        line.add_updater(lambda l, dt: l.rotate(d_theta, about_point=ORIGIN))
        surface_by_rotate.add_updater(update_surface)

        self.add(axes, line, surface_by_rotate)
        self.wait(12)







