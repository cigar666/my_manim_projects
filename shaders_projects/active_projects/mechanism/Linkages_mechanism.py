from manimlib.imports import *
from my_projects.active_projects.mechanism.basic_component import *

class Four_bar_linkage(Scene):

    def construct(self):

        O1, O2 = LEFT * 2 + DOWN, RIGHT * 2. + DOWN

        dot_O1 = Dot(O1, color=PINK)
        dot_O2 = Dot(O2, color=PINK)
        bar_1 = Bar(O1, 140 * DEGREES, 1., color=ORANGE)
        bar_2 = Bar(O2, 80 * DEGREES, 2.7, color=BLUE)
        bar_3 = Rod(bar_1.get_end(), bar_2.get_end(), end_type=[2, 2], color=BLUE)
        bars = VGroup(bar_1, bar_2, bar_3)
        t = ValueTracker(140 * DEGREES)
        w = 1

        # ## 两个updater都不太行，在摇杆接近死点时经常不收敛 ##
        # def update_bars(b):
        #     err = 1e-3
        #     b[0].reposition_by_angle(t.get_value() * w)
        #     print(t.get_value() * w / PI * 180)
        #
        #     # b[2].reposition_by_angle(angle=None, start=b[0].get_end())
        #     b[2].reposition(b[0].get_end(), b[2].get_end())
        #     print('theta=%.2f, error=%.5f' % (t.get_value() / PI * 180, get_norm(b[1].get_end() - b[2].get_end())))
        #     while get_norm(b[1].get_end() - b[2].get_end()) > err:
        #         b[1].reposition(b[1].get_start(), b[2].get_end())
        #         b[2].reposition(b[0].get_end(), b[1].get_end())
        #         print('theta=%.2f, error=%.5f' % (t.get_value() / PI * 180, get_norm(b[1].get_end() - b[2].get_end())))

        def update_bars(b):
            def l_new():
                return get_norm(b[1].get_end() - b[0].get_end())
            err = 1e-3
            delta_theta = 2 * DEGREES
            a0 = 0.8
            l = b[2].get_rod_length()

            b[0].reposition_by_angle(t.get_value() * w)
            d_l = abs(l_new() - l)
            print('theta=%.2f, error=%.5f' % (t.get_value() / PI * 180, d_l))
            while d_l > err:
                if d_l < err * 50:
                    a0 = 0.6
                # elif d_l < err * 15:
                #     a0 = 0.5
                elif d_l < err * 5:
                    a0 = 0.4

                b[1].rotate_about_start(delta_theta)
                d_l_new = abs(l_new() - l)

                if d_l_new < d_l:
                    delta_theta *= a0
                    d_l = d_l_new
                else:
                    delta_theta *= -1
                    d_l = d_l_new
                print('theta=%.2f, error=%.5f' % (t.get_value() / PI * 180, d_l))
            b[2].reposition(b[0].get_end(), b[1].get_end())

        bars.add_updater(update_bars)

        self.add(dot_O1, dot_O2, bars, t)
        self.wait()
        # self.play(t.set_value, 4 * 500 * DEGREES, rate_func=linear, run_time=20)
        t.add_updater(lambda t, dt: t.increment_value(2 * DEGREES))
        self.wait(20)

class Four_bar_linkage_draw(Scene):

    def construct(self):

        grid_n = 4
        dots = VGroup(*[Dot(RIGHT * i + UP * j, color=BLUE).scale(0.5) for i in range(grid_n + 1) for j in range(grid_n + 1)])
        lines = VGroup(*([Line(ORIGIN, UP * grid_n, stroke_color=BLUE_B, stroke_width=1).shift(i * RIGHT) for i in range(grid_n + 1)] +
                         [Line(ORIGIN, RIGHT * grid_n, stroke_color=BLUE_B, stroke_width=1).shift(i * UP) for i in range(grid_n + 1)]))
        grid = VGroup(dots, lines)

        O1, O2 = LEFT * 2 + DOWN * 2.5, RIGHT * 2. + DOWN * 2.5

        dot_O1 = Dot(O1, color=PINK)
        dot_O2 = Dot(O2, color=PINK)
        bar_1 = Bar(O1, 140 * DEGREES, 1., color=YELLOW)
        bar_2 = Bar(O2, 80 * DEGREES, 2.7, color=BLUE)
        bar_3 = Rod(bar_1.get_end(), bar_2.get_end(), end_type=[2, 2], color=BLUE)

        grid.rotate_about_origin(bar_3.get_angle()).scale(bar_3.get_rod_length()/grid_n, about_point=ORIGIN).shift(bar_3.get_start())

        bars = VGroup(bar_1, bar_2, bar_3)
        t = ValueTracker(140 * DEGREES)
        w = 1

        def update_bars(b):
            err = 1e-3
            b[0].reposition_by_angle(t.get_value() * w)
            print(t.get_value() * w / PI * 180)

            # b[2].reposition_by_angle(angle=None, start=b[0].get_end())
            b[2].reposition(b[0].get_end(), b[2].get_end())
            print('theta=%.2f, error=%.5f' % (t.get_value() / PI * 180, get_norm(b[1].get_end() - b[2].get_end())))
            while get_norm(b[1].get_end() - b[2].get_end()) > err:
                b[1].reposition(b[1].get_start(), b[2].get_end())
                b[2].reposition(b[0].get_end(), b[1].get_end())
                print('theta=%.2f, error=%.5f' % (t.get_value() / PI * 180, get_norm(b[1].get_end() - b[2].get_end())))

        bars.add_updater(update_bars)
        paths = VGroup(*[TracedPath(dot.get_center, stroke_color=BLUE_B, stroke_width=1.5) for dot in dots])
        self.add(dot_O1, dot_O2, bars, t, paths)
        self.wait()
        bar_3.add(grid)
        self.play(ShowCreation(grid), run_time=1.5)
        self.wait(0.5)
        self.play(t.set_value, 1 * 500 * DEGREES, rate_func=linear, run_time=25)
        # t.add_updater(lambda t, dt: t.increment_value(2 * DEGREES))
        # self.wait(30)
        self.wait(2)

class Five_bar_linkage(Scene):

    CONFIG = {
        'camera_config': {
            'background_color': WHITE,
        },
    }

    def construct(self):

        O1, O2 = LEFT * 3.4 + DOWN * 1.5, RIGHT * 0.8 + DOWN * 1.5
        dot_O1 = Dot(O1, color=PINK).set_plot_depth(-1)
        dot_O2 = Dot(O2, color=PINK).set_plot_depth(-1)

        init_angle_1, init_angle_2 = 140 * DEGREES, 30 * DEGREES
        bar_1 = Bar(O1, init_angle_1, 1.25, color=YELLOW)
        bar_2 = Bar(O2, init_angle_2, 0.75, color=RED)
        bar_3 = Bar(bar_1.get_end(), 30 * DEGREES, 5, end_type=[2, 2], color=BLUE_D)
        bar_4 = Rod(bar_2.get_end(), bar_3.get_end(), end_type=[2, 1], color=BLUE_D)
        bar_5 = Bar(0.15 * bar_4.get_start() + 0.85 * bar_4.get_end(), bar_4.get_angle() - PI/2, 1.8, end_type=[1, 1], color=BLUE_D)
        bar_4.add(bar_5)
        bars = VGroup(bar_1, bar_2, bar_3, bar_4)
        t = ValueTracker(0)
        T0, T1, T2 = 19, 16, 24
        w0 = 1
        w1 = w0 * T0/T1

        def update_bars(b):
            err = 1e-3
            b[0].reposition_by_angle(t.get_value() * w0 + init_angle_1)
            b[1].reposition_by_angle(t.get_value() * w1 + init_angle_2)

            # b[2].reposition_by_angle(angle=None, start=b[0].get_end())
            # b[3].reposition_by_angle(angle=None, start=b[1].get_end())
            b[2].reposition(b[0].get_end(), b[3].get_end())
            b[3].reposition(b[1].get_end(), b[2].get_end())
            print('theta=%.2f, error=%.5f' % (t.get_value() / PI * 180, get_norm(b[2].get_end() - b[3].get_end())))
            while get_norm(b[2].get_end() - b[3].get_end()) > err:
                b[2].reposition(b[0].get_end(), b[3].get_end())
                b[3].reposition(b[1].get_end(), b[2].get_end())
                print('theta=%.2f, error=%.5f' % (t.get_value() / PI * 180, get_norm(b[2].get_end() - b[3].get_end())))

        rotate_time = 90

        path = TracedPath(bar_5.get_end, stroke_color=BLUE_D, stroke_width=1.6)
        self.add(bars, dot_O1, dot_O2, path)
        bars.add_updater(update_bars)
        path.add_updater(lambda p: p.rotate_about_origin(abs(T0/T2 * lcm(T2, T1) * TAU) /self.camera.frame_rate/rotate_time))

        self.play(t.set_value, abs(lcm(T2, T1)) * 360 * DEGREES, rate_func=linear, run_time=rotate_time)
        # self.play(t.set_value, abs(T1 * 360 * DEGREES), rate_func=linear, run_time=rotate_time)
        path.clear_updaters()
        self.wait(2)


class Five_bar_draw_01(Scene):


    CONFIG = {
        'camera_config': {
            'background_color': WHITE,
        },
    }

    def construct(self):

        O1, O2 = LEFT * 2 + DOWN * 2., RIGHT * 2 + DOWN * 2.
        dot_O1 = Dot(O1, color=PINK).set_plot_depth(-1)
        dot_O2 = Dot(O2, color=PINK).set_plot_depth(-1)
        l1, l2, l3 = 1.2, 1, 4
        init_angle_1, init_angle_2 = 140 * DEGREES, 30 * DEGREES
        bar_1 = Bar(O1, init_angle_1, l1, color=YELLOW)
        bar_2 = Bar(O2, init_angle_2, l2, color=RED)

        bar_3 = Bar(bar_1.get_end(), 30 * DEGREES, l3, end_type=[2, 2], color=BLUE_D)
        bar_4 = Rod(bar_2.get_end(), bar_3.get_end(), end_type=[2, 1], color=BLUE_D)

        self.add(dot_O1, dot_O2, bar_1, bar_2, bar_3, bar_4)
        self.wait()


class Draw_straight_line(Scene):

    def construct(self):

        pass

