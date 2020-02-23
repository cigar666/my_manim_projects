from manimlib.imports import *

class Mobius_Strip(SpecialThreeDScene):
    CONFIG = {
        "default_angled_camera_position": {
            "phi": 66 * DEGREES,
            "theta": -60 * DEGREES,
            "distance": 50,
            },
        'camera_config': {'background_color': WHITE},
    }
    def construct(self):
        self.set_camera_to_default_position()
        R, r = 3.2, 0.8
        mobius_surface = ParametricSurface(lambda u, v: R * np.array([np.cos(u), np.sin(u), 0])
                                                + v * np.cos(u/2) * np.array([np.cos(u), np.sin(u), 0])
                                                + v * np.sin(u/2) * OUT,
                                           u_min=0, u_max=TAU, v_min=-r, v_max=r, resolution=(80, 16),
                                           checkerboard_colors=None, stroke_color=PINK, stroke_opacity=0.6,
                                           stroke_width=1.2, fill_color=BLUE, fill_opacity=0.8)
        mobius_edge = ParametricFunction(lambda t: R * np.array([np.cos(t), np.sin(t), 0])
                                         + r * np.cos(t/2) * np.array([np.cos(t), np.sin(t), 0])
                                         + r * np.sin(t/2) * OUT,
                                         t_min=0, t_max=TAU * 2, color=RED, stroke_width=10, stroke_opacity=0.5)
        h = 0.08
        ball_path = lambda t: R * np.array([np.cos(t), np.sin(t), 0] + h * np.sin(-t/2) * np.array([np.cos(t), np.sin(t), 0]) + h * np.cos(t/2) * OUT)
        ball = Sphere(checkerboard_colors=None, fill_color=RED).set_height(0.48)
        self.time = 0
        def update_ball(b, dt):
            self.time += dt/2
            b.move_to(ball_path(self.time))

        self.play(ShowCreation(mobius_surface), run_time=2)
        self.wait(1)
        self.play(ShowCreation(mobius_edge), run_time=2.5)
        self.play(FadeOut(mobius_edge), run_time=1.5)
        self.wait()
        ball.add_updater(update_ball)
        self.add(ball)
        self.wait(20)

class Cut_Mobius_Strip(SpecialThreeDScene):
    CONFIG = {
        "default_angled_camera_position": {
            "phi": 72 * DEGREES,
            "theta": -64 * DEGREES,
            "distance": 50,
            },
        'camera_config': {'background_color': WHITE},
    }
    def construct(self):
        self.set_camera_to_default_position()
        R, r = 2.5, 0.8
        mobius_cut = ParametricSurface(lambda u, v: R * np.array([np.cos(u), np.sin(u), 0])
                                                + v * np.cos(u/2) * np.array([np.cos(u), np.sin(u), 0])
                                                + v * np.sin(u/2) * OUT,
                                       u_min=0, u_max=TAU * 2, v_min=0, v_max=r, resolution=(80, 12),
                                       checkerboard_colors=None, stroke_color=PINK, stroke_opacity=0.8,
                                       stroke_width=1.5, fill_color=BLUE, fill_opacity=0.75)

        mobius_cut_02 = ParametricSurface(lambda u, v: R * np.array([np.cos(u), np.sin(u), 0])
                                                + v * np.cos(u/2) * np.array([np.cos(u), np.sin(u), 0])
                                                + v * np.sin(u/2) * OUT,
                                          u_min=0, u_max=TAU * 2, v_min=0 + r * 0.5, v_max=r * 1.5, resolution=(80, 12),
                                          checkerboard_colors=None, stroke_color=PINK, stroke_opacity=0.8,
                                          stroke_width=1.5, fill_color=BLUE, fill_opacity=0.75)


        band_new = ParametricSurface(lambda u, v: R * 2 * np.array([np.cos(u), np.sin(u), 0])
                                                + v * np.cos(u) * np.array([np.cos(u), np.sin(u), 0])
                                                + v * np.sin(u) * OUT,
                                       u_min=0, u_max=TAU, v_min=-r/2, v_max=r/2, resolution=(80, 12),
                                       checkerboard_colors=None, stroke_color=PINK, stroke_opacity=0.8,
                                       stroke_width=1.5, fill_color=BLUE, fill_opacity=0.75)


        # mobius_edge = ParametricFunction(lambda t: R * np.array([np.cos(t), np.sin(t), 0])
        #                                         + r * np.cos(t/2) * np.array([np.cos(t), np.sin(t), 0])
        #                                         + r * np.sin(t/2) * OUT,
        #                                  t_min=0, t_max=TAU * 2, color=RED, stroke_width=10, stroke_opacity=0.5)
        # h = 0.09
        # ball_path = lambda t: R * np.array([np.cos(t), np.sin(t), 0] + h * np.sin(-t/2) * np.array([np.cos(t), np.sin(t), 0]) + h * np.cos(t/2) * OUT)
        # ball = Sphere(checkerboard_colors=None, fill_color=RED).set_height(0.48)
        # self.time = 0
        # def update_ball(b, dt):
        #     self.time+=dt
        #     b.move_to(ball_path(self.time))

        # self.play(ShowCreation(mobius_cut))
        self.add(mobius_cut)
        self.wait(1)
        self.play(ReplacementTransform(mobius_cut, mobius_cut_02), run_time=4)
        self.wait(0.2)
        self.play(ReplacementTransform(mobius_cut_02, band_new), run_time=4)
        # self.play(ShowCreation(mobius_edge))
        # self.wait()
        # ball.add_updater(update_ball)
        # self.add(ball)
        self.wait(5)

class Mobius_Strip_heartshape(SpecialThreeDScene):

    CONFIG = {
        "default_angled_camera_position": {
            "phi": 30 * DEGREES,
            "theta": -80 * DEGREES,
            "distance": 50,
            },
        'camera_config': {'background_color': WHITE},
    }

    def construct(self):

        self.set_camera_to_default_position()

        heart_curve_func = lambda t: (16 * np.sin(t) ** 3 * RIGHT + (13 * np.cos(t) - 5 * np.cos(2 * t) - 3 * np.cos(3 * t)
                                      - np.cos(4 * t)) * UP + np.sin(t) * (1 - abs(-t/PI)) ** 2 * 8 * OUT) * 0.2
        r = 0.5
        heart_shape_mobius = ParametricSurface(lambda u, v: heart_curve_func(u) + v * np.cos(u/2) * np.array([np.cos(u), np.sin(u), 0])
                                                + v * np.sin(-u/2) * OUT,
                                               u_min=-PI, u_max=PI, v_min=-r, v_max=r, resolution=(80, 12),
                                               checkerboard_colors=None, stroke_color=PINK, stroke_opacity=0.8,
                                               stroke_width=1.5, fill_color=average_color(RED, PINK), fill_opacity=0.8)

        heart_curve = ParametricFunction(heart_curve_func, t_min=-PI, t_max=PI, color=RED, stroke_width=10, stroke_opacity=0.9)

        # self.play(ShowCreation(heart_curve))
        # self.wait()

        self.play(ShowCreation(heart_shape_mobius))
        self.wait()

        heart_shape_mobius.add_updater(lambda m, dt: m.rotate(1 * DEGREES, axis=UP))

        self.wait(40)

class Mobius_to_Heartshape(SpecialThreeDScene):

    CONFIG = {
        "default_angled_camera_position": {
            "phi": 50 * DEGREES,
            "theta": -80 * DEGREES,
            "distance": 50,
            },
        'camera_config': {'background_color': WHITE},
    }

    def construct(self):

        self.set_camera_to_default_position()

        heart_curve_func = lambda t: (16 * np.sin(t) ** 3 * RIGHT + (13 * np.cos(t) - 5 * np.cos(2 * t) - 3 * np.cos(3 * t) - np.cos(4 * t)) * UP + np.sin(t) * (1 - abs(-t/PI)) ** 2 * 8 * OUT) * 0.21

        # heart_curve = ParametricFunction(heart_curve_func, t_min=-PI, t_max=PI, color=RED, stroke_width=10, stroke_opacity=0.9)

        r = 0.5
        heart_shape_mobius = ParametricSurface(lambda u, v: heart_curve_func(u) + v * np.cos(u/2) * np.array([np.cos(u), np.sin(u), 0])
                                                + v * np.sin(-u/2) * OUT,
                                               u_min=-PI, u_max=PI, v_min=-r, v_max=r, resolution=(80, 12),
                                               checkerboard_colors=None, stroke_color=PINK, stroke_opacity=0.6,
                                               stroke_width=1.5, fill_color=average_color(RED, PINK), fill_opacity=0.8)
        R = 3.6
        mobius_surface = ParametricSurface(lambda u, v: R * np.array([np.cos(u), np.sin(u), 0])
                                                + v * np.cos(u/2) * np.array([np.cos(u), np.sin(u), 0])
                                                + v * np.sin(u/2) * OUT,
                                           u_min=-PI/2, u_max=-PI/2 + TAU, v_min=-r, v_max=r, resolution=(80, 10),
                                           checkerboard_colors=None, stroke_color=PINK, stroke_opacity=0.6,
                                           stroke_width=1.5, fill_color=BLUE, fill_opacity=0.8).rotate(PI, axis=UP)

        heart_shape_mobius.move_to(mobius_surface)

        # self.play(ShowCreation(heart_curve))
        # self.wait()

        self.add(mobius_surface)
        self.wait()
        self.play(ReplacementTransform(mobius_surface, heart_shape_mobius), run_time=4)

        self.wait(1.)

        rotate_right = lambda m, dt: m.rotate(0.25 * DEGREES, axis=RIGHT)
        rotate_up = lambda m, dt: m.rotate(0.25 * DEGREES, axis=UP)
        heart_shape_mobius.add_updater(rotate_right)
        self.wait(2.5)
        heart_shape_mobius.remove_updater(rotate_right)

        # heart_shape_mobius.add_updater(rotate_up)

        self.wait(5)

class Test(Scene):

    def construct(self):

        f = np.array([1, 1, 2, 3, 5, 8, 13, 21, 34, 55]) * 0.1

        arcs = VGroup()
        for i in range(len(f)):
            arc_i = Arc(radius=f[i], color=RED)
            arcs.add(arc_i)
        # self.play(ShowCreation(arcs))
        # self.wait(0.5)
        for i in range(len(f)):
            arcs[i:].rotate(PI/2, about_point=ORIGIN)
            # self.wait(0.15)
        for i in range(1, len(f)):
            # self.play(arcs[i].shift, arcs[i-1].get_end()-arcs[i].get_start())
            arcs[i].shift(arcs[i-1].get_end()-arcs[i].get_start())
            # self.wait(0.1)

        for arc in arcs:
            self.play(ShowCreation(arc))
            # self.wait(0.1)

        self.wait(2)

class Double_heart(SpecialThreeDScene):

    CONFIG = {
        "default_angled_camera_position": {
            "phi": 15 * DEGREES,
            "theta": -85 * DEGREES,
            "distance": 50,
            },
        'camera_config': {'background_color': WHITE},
    }

    def construct(self):

        self.set_camera_to_default_position()

        heart_curve_func = lambda t: (16 * np.sin(t) ** 3 * RIGHT + (13 * np.cos(t) - 5 * np.cos(2 * t) - 3 * np.cos(3 * t) - np.cos(4 * t)) * UP + np.sin(t) * (1 - abs(-t/PI)) ** 2 * 15 * OUT) * 0.2
        heart_curve_func_02 = lambda t: (16 * np.sin(t) ** 3 * RIGHT + (13 * np.cos(t) - 5 * np.cos(2 * t) - 3 * np.cos(3 * t) - np.cos(4 * t)) * UP + np.sin(-t) * (1 - abs(-t/PI)) ** 2 * 15 * OUT) * 0.2

        r = 0.25
        heart_shape_mobius = ParametricSurface(lambda u, v: heart_curve_func(u) + v * np.cos(u/2) * np.array([np.cos(u), np.sin(u), 0])
                                                + v * np.sin(-u/2) * OUT,
                                               u_min=-PI, u_max=PI, v_min=-r, v_max=r, resolution=(80, 12),
                                               checkerboard_colors=None, stroke_color=RED, stroke_opacity=0.8,
                                               stroke_width=0.8, fill_color=average_color(RED, PINK), fill_opacity=0.9)
        heart_shape_mobius_02 = ParametricSurface(lambda u, v: heart_curve_func_02(u) + v * np.cos(u/2) * np.array([np.cos(u), np.sin(u), 0])
                                                + v * np.sin(-u/2) * OUT,
                                                  u_min=-PI, u_max=PI, v_min=-r, v_max=r, resolution=(80, 12),
                                                  checkerboard_colors=None, stroke_color=RED, stroke_opacity=0.8,
                                                  stroke_width=0.8, fill_color=average_color(RED, PINK), fill_opacity=0.9)
        heart_shape_mobius.scale(0.85)
        heart_shape_mobius.shift(LEFT * 2)
        heart_shape_mobius_02 = heart_shape_mobius.copy().rotate(PI, axis=UP, about_point=ORIGIN)
        heart_shape_mobius.rotate(15*DEGREES, axis=UP).shift(IN * 0.1)
        heart_shape_mobius_02.rotate(15*DEGREES, axis=UP).shift(OUT * 0.1)

        hearts = VGroup(heart_shape_mobius_02, heart_shape_mobius).move_to(ORIGIN)

        self.add(heart_shape_mobius, heart_shape_mobius_02)

        self.wait()
        heart_shape_mobius.add_updater(lambda h, dt: h.rotate(-1 * DEGREES, axis=UP, about_point=ORIGIN))
        heart_shape_mobius_02.add_updater(lambda h, dt: h.rotate(-1 * DEGREES, axis=UP, about_point=ORIGIN))

        self.wait(25)

class Mobius_Properties(SpecialThreeDScene):
    CONFIG = {
        "default_angled_camera_position": {
            "phi": 72 * DEGREES,
            "theta": -64 * DEGREES,
            "distance": 50,
            },
        'camera_config': {'background_color': WHITE},
    }
    def construct(self):
        self.set_camera_to_default_position()
        R, r = 2.5, 0.8
        mobius_cut = ParametricSurface(lambda u, v: R * np.array([np.cos(u), np.sin(u), 0])
                                                + v * np.cos(u/2) * np.array([np.cos(u), np.sin(u), 0])
                                                + v * np.sin(u/2) * OUT,
                                       u_min=0, u_max=TAU * 2, v_min=0, v_max=r, resolution=(80, 12),
                                       checkerboard_colors=None, stroke_color=PINK, stroke_opacity=0.8,
                                       stroke_width=1.5, fill_color=BLUE, fill_opacity=0.75)

        mobius_cut_02 = ParametricSurface(lambda u, v: R * np.array([np.cos(u), np.sin(u), 0])
                                                + v * np.cos(u/2) * np.array([np.cos(u), np.sin(u), 0])
                                                + v * np.sin(u/2) * OUT,
                                          u_min=0, u_max=TAU * 2, v_min=0 + r * 0.5, v_max=r * 1.5, resolution=(80, 12),
                                          checkerboard_colors=None, stroke_color=PINK, stroke_opacity=0.8,
                                          stroke_width=1.5, fill_color=BLUE, fill_opacity=0.75)


        band_new = ParametricSurface(lambda u, v: R * 2 * np.array([np.cos(u), np.sin(u), 0])
                                                + v * np.cos(u) * np.array([np.cos(u), np.sin(u), 0])
                                                + v * np.sin(u) * OUT,
                                       u_min=0, u_max=TAU, v_min=-r/2, v_max=r/2, resolution=(80, 12),
                                       checkerboard_colors=None, stroke_color=PINK, stroke_opacity=0.8,
                                       stroke_width=1.5, fill_color=BLUE, fill_opacity=0.75)


        # mobius_edge = ParametricFunction(lambda t: R * np.array([np.cos(t), np.sin(t), 0])
        #                                         + r * np.cos(t/2) * np.array([np.cos(t), np.sin(t), 0])
        #                                         + r * np.sin(t/2) * OUT,
        #                                  t_min=0, t_max=TAU * 2, color=RED, stroke_width=10, stroke_opacity=0.5)
        # h = 0.09
        # ball_path = lambda t: R * np.array([np.cos(t), np.sin(t), 0] + h * np.sin(-t/2) * np.array([np.cos(t), np.sin(t), 0]) + h * np.cos(t/2) * OUT)
        # ball = Sphere(checkerboard_colors=None, fill_color=RED).set_height(0.48)
        # self.time = 0
        # def update_ball(b, dt):
        #     self.time+=dt
        #     b.move_to(ball_path(self.time))

        # self.play(ShowCreation(mobius_cut))
        self.add(mobius_cut)
        self.wait(1)
        self.play(ReplacementTransform(mobius_cut, mobius_cut_02), run_time=4)
        self.wait(0.2)
        self.play(ReplacementTransform(mobius_cut_02, band_new), run_time=4)
        # self.play(ShowCreation(mobius_edge))
        # self.wait()
        # ball.add_updater(update_ball)
        # self.add(ball)
        self.wait(5)

class Create_Mobius(SpecialThreeDScene):

    CONFIG = {
        "default_angled_camera_position": {
            "phi": 45 * DEGREES,
            "theta": -60 * DEGREES,
            "distance": 200,
            },
        'camera_config': {'background_color': WHITE},
    }

    def construct(self):
        self.set_camera_to_default_position()
        R, r = 2.4, 0.6

        band = ParametricSurface(lambda u, v: PI/2 * u * RIGHT + v * UP + R * UP,
                                 u_min=PI, u_max=-PI, v_min=-r, v_max=r, resolution=(80, 16),
                                 checkerboard_colors=None, stroke_color=PINK, stroke_opacity=0.6,
                                 stroke_width=1.5, fill_color=BLUE, fill_opacity=0.8)
        twisted_band = ParametricSurface(lambda u, v: PI/2 * u * RIGHT + v * np.cos(u/2) * UP + R * UP
                                                + v * np.sin(u/2) * OUT,
                                 u_min=PI, u_max=-PI, v_min=-r, v_max=r, resolution=(80, 16),
                                 checkerboard_colors=None, stroke_color=PINK, stroke_opacity=0.6,
                                 stroke_width=1.5, fill_color=BLUE, fill_opacity=0.8)

        mobius_half = ParametricSurface(lambda u, v: 2 * R * np.array([np.cos(u/2), np.sin(u/2), 0])
                                                + v * np.cos(u/2) * np.array([np.cos(u/2), np.sin(u/2), 0])
                                                + v * np.sin(u/2) * OUT,
                                        u_min=-PI/6, u_max=-PI/6 + TAU, v_min=-r, v_max=r, resolution=(80, 16),
                                        checkerboard_colors=None, stroke_color=PINK, stroke_opacity=0.6,
                                        stroke_width=1.5, fill_color=BLUE, fill_opacity=0.8)

        mobius_surface = ParametricSurface(lambda u, v: R * np.array([np.cos(u), np.sin(u), 0])
                                                + v * np.cos(u/2) * np.array([np.cos(u), np.sin(u), 0])
                                                + v * np.sin(u/2) * OUT,
                                           u_min=-PI/2, u_max=-PI/2 + TAU, v_min=-r, v_max=r, resolution=(80, 16),
                                           checkerboard_colors=None, stroke_color=PINK, stroke_opacity=0.6,
                                           stroke_width=1.5, fill_color=BLUE, fill_opacity=0.8)

        self.play(ShowCreation(band), run_time=1.2)
        self.wait()
        self.play(ReplacementTransform(band, twisted_band), run_time=2)

        self.wait()
        self.play(ReplacementTransform(twisted_band, mobius_half), run_time=2)
        self.play(ReplacementTransform(mobius_half, mobius_surface), run_time=2)
        # twisted_band.add_updater(update_band)
        # for i in range(60):
        #     self.w *= np.log(1/1e-3)/np.log(60)
        #     self.wait(1/15)
        self.wait(4)

class Cut_heart(SpecialThreeDScene):

    CONFIG = {
        "default_angled_camera_position": {
            "phi": 72 * DEGREES,
            "theta": -64 * DEGREES,
            "distance": 50,
            },
        'camera_config': {'background_color': WHITE},
    }

    def construct(self):
        
        self.set_camera_to_default_position()

        heart_curve_func = lambda t: (16 * np.sin(t) ** 3 * RIGHT + (13 * np.cos(t) - 5 * np.cos(2 * t) - 3 * np.cos(3 * t)
                                  - np.cos(4 * t)) * UP + np.sin(t) * (1 - abs(-t/PI)) ** 2 * 8 * OUT) * 0.2
        r = 0.5
        heart_shape_mobius = ParametricSurface(lambda u, v: heart_curve_func(u) + v * np.cos(u/2) * np.array([np.cos(u), np.sin(u), 0])
                                             + v * np.sin(-u/2) * OUT,
                                            u_min=-PI, u_max=PI, v_min=-r, v_max=r, resolution=(80, 12),
                                            checkerboard_colors=None, stroke_color=PINK, stroke_opacity=0.8,
                                            stroke_width=1.5, fill_color=average_color(RED, PINK), fill_opacity=0.8)

        heart_curve = ParametricFunction(heart_curve_func, t_min=-PI, t_max=PI, color=RED, stroke_width=10, stroke_opacity=0.9)

class Spiral_Curve_test(Scene):

    def construct(self):

        F = lambda n: (((1 + np.sqrt(5))/2) ** n - ((1 - np.sqrt(5))/2) ** n)/np.sqrt(5)
        F_int = lambda t: F(int(t))
        P_n = lambda t: F_int(t) * 1j ** (int(t)-1)
        Q_n = lambda t: F_int(t+1) * 1j ** (int(t)-1)
        P_minus_Q = [(P_n(i)-Q_n(i)) for i in range(100)]
        # print(P_minus_Q)
        # for i in range(1, 10):
        #     print('i =', i)
        #     print(F_int(i))
        #     print(sum(P_minus_Q[1:i]))
        r0 = 0.1
        self.mytime = 0
        spiral = ParametricFunction(lambda t: r0 * complex_to_R3(F_int(t) * np.exp(1j * PI /2 * (t-2)) + sum(P_minus_Q[1:int(t)])),
                                    t_min=1, t_max=1.0001, color=RED, stroke_width=2., stroke_opacity=1, step_size=0.01)
        def update_spiral(sp, dt):
            self.mytime += 1/30 * 2
            sp.become(ParametricFunction(lambda t: r0 * complex_to_R3(F_int(t) * np.exp(1j * PI /2 * (t-2)) + sum(P_minus_Q[1:int(t)])),
                                    t_min=1, t_max=1 + self.mytime, color=RED, stroke_width=2., stroke_opacity=1, step_size=0.01))

        self.add(spiral)
        spiral.add_updater(update_spiral)
        self.wait(5)
        spiral.suspend_updating()
        self.wait(2)





