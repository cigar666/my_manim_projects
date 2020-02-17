# this file need to do some changes to run on the new version of manim

from big_ol_pile_of_manim_imports import *

class Cardioid_by_Line(Scene):

    CONFIG = {
        'bg_color': WHITE,
        # 'circle_color': '#1514EA', # color blue
        # 'line_color': '#E71905', # color red
        'circle_color': BLUE, # color blue
        'line_color': RED, # color red
        'node_color': PINK,
        'line_width': 3,
        'node_num': 36,

        'show_node_id': True,

        'circle_r': 3.4,
        'node_r': 0.032,

        'circle_loc': LEFT * 2.5 + UP * 0.1,
    }

    def construct(self):

        bg_rect = Rectangle(fill_color=self.bg_color, fill_opacity=1).scale(20)
        self.add(bg_rect)
        self.wait(0.25)

        # self.anim()

        self.create_all()

        self.play(ShowCreation(self.circle), run_time=1.25)
        self.wait(0.4)

        for i in range(self.node_num):
            self.play(FadeInFromLarge(self.node_group[i]), run_time=0.04)
            if self.show_node_id:
                self.play(Write(self.node_id[i]), run_time=0.06)
        self.wait()


        zoom_in_scale = 3
        self.always_continually_update = True
        dt = 1/14.9

        for i in range(45):
            self.all_objects.scale_about_point(zoom_in_scale ** (1/45), self.node_group[-1].get_center())
            self.wait(dt)


        # draw_line

        text01 = TextMobject('node 1', '$\\to$', 'node 2', color=PINK, stroke_color=WHITE).scale(1.6).to_corner(UP * 2 + LEFT * 1.6)
        text01.set_color_by_tex_to_color_map({
            '$\\to$': RED_B,
        })
        text02 = TextMobject('node 2', '$\\to$', 'node 4', color=PINK, stroke_color=WHITE).scale(1.6).to_corner(UP * 2 + LEFT * 1.6)
        text02.set_color_by_tex_to_color_map({
            '$\\to$': RED_B,
        })
        text03 = TextMobject('node 3', '$\\to$', 'node 6', color=PINK, stroke_color=WHITE).scale(1.6).to_corner(UP * 2 + LEFT * 1.6)
        text03.set_color_by_tex_to_color_map({
            '$\\to$': RED_B,
        })
        text04 = TextMobject('node 4', '$\\to$', 'node 8', color=PINK, stroke_color=WHITE).scale(1.6).to_corner(UP * 2 + LEFT * 1.6)
        text04.set_color_by_tex_to_color_map({
            '$\\to$': RED_B,
        })

        self.play(Write(text01))
        self.wait(0.8)
        self.play(ShowCreation(self.line_group[0]))
        self.wait()

        self.play(ReplacementTransform(text01, text02))
        self.wait(0.8)
        self.play(ShowCreation(self.line_group[1]))
        self.wait()

        for i in range(15):
            self.all_objects.scale_about_point((1/zoom_in_scale) ** (1/45), self.node_group[-1].get_center())
            self.wait(dt)

        self.play(ReplacementTransform(text02, text03))
        self.wait(0.8)
        self.play(ShowCreation(self.line_group[2]))
        self.wait()

        self.play(ReplacementTransform(text03, text04))
        self.wait(0.8)
        self.play(ShowCreation(self.line_group[3]))
        self.wait()
        self.play(FadeOut(text04))

        for i in range(30):
            self.all_objects.scale_about_point((1/zoom_in_scale) ** (1/45), self.node_group[-1].get_center())
            self.wait(dt)

        text_i = TextMobject('node i', '$\\to$', '$node 2\\times i$', color=PINK, stroke_color=WHITE).scale(1.1).to_corner(UP * 2 + RIGHT * 1.5)
        text_i.set_color_by_tex_to_color_map({
            '$\\to$': RED_B,
        })
        text_i02 = TextMobject('2i大于n时则对n取余', color=PINK, stroke_color=WHITE)\
            .scale(0.9).next_to(text_i, DOWN * 0.7).align_to(text_i, LEFT)

        self.play(Write(text_i))
        self.wait(0.75)
        self.play(Write(text_i02))

        for i in range(4, self.node_num):
            self.play(ShowCreation(self.line_group[i]), run_time=0.25)
            self.wait(0.1)

        ## n = 18 to 36 to 64
        # self.node_num = 18
        # old_objs = self.all_objects
        # self.create_all()
        # self.play(ReplacementTransform(old_objs, self.all_objects))
        # self.wait()
        #
        # self.node_num = 36
        # old_objs = self.all_objects
        # self.create_all()
        # self.play(ReplacementTransform(old_objs, self.all_objects))
        # self.wait()
        #
        # self.node_num = 64
        # old_objs = self.all_objects
        # self.create_all()
        # self.play(ReplacementTransform(old_objs, self.all_objects))
        # self.wait()

        self.wait(2)

    def create_all(self):

        n = self.node_num
        self.circle = Circle(radius=self.circle_r, color=self.circle_color, stroke_width=2 * self.line_width).move_to(self.circle_loc)

        self.node_group = VGroup()
        self.node_id = VGroup()
        self.line_group = VGroup()
        delta_a = TAU / n

        for i in range(n):
            vector_i = np.array([-np.sin(delta_a * (i + 1) + TAU / 2), np.cos(delta_a * (i + 1) + TAU / 2), 0]) * self.circle_r
            node_i = Circle(radius=self.node_r, color=self.node_color, fill_color=self.node_color, fill_opacity=1).move_to(self.circle.get_center() + vector_i)

            self.node_group.add(node_i)
            if self.show_node_id:
                text_i = TextMobject('%d' % (i + 1), color=self.node_color).scale(0.36).move_to(self.circle.get_center() + vector_i * 1.06)
                self.node_id.add(text_i)

        for i in range(1, n+1):

            line_i = Line(self.node_group[i - 1].get_center(), self.node_group[(2 * i - 1) % n + 1 - 1].get_center(),
                          color=self.line_color, stroke_width=self.line_width)
            self.line_group.add(line_i)

        self.all_objects = VGroup(self.circle, self.node_group, self.node_id, self.line_group)

    def anim(self):
        self.create_all()

        self.play(ShowCreation(self.circle), run_time=1.25)
        self.wait(0.4)

        for i in range(self.node_num):
            self.play(FadeInFromLarge(self.node_group[i]), run_time=0.06)
            if self.show_node_id:
                self.play(Write(self.node_id[i]), run_time=0.1)
        self.wait()

        for i in range(self.node_num):
            self.play(ShowCreation(self.line_group[i]), run_time=0.2)
            self.wait(0.05)
        self.wait()

class Cardioid_by_Circle(Scene):

    CONFIG = {
        'bg_color': WHITE,
        'circle_color': RED,
        'circle_num': 36,
        'circle_width': 3,
        # 'curve_color': RED_B,
        # 'curve_width': 4,
        'circle_r': 1.5,
        'circle_loc': LEFT * 2 + UP,
    }

    def construct(self):

        bg_rect = Rectangle(fill_color=self.bg_color, fill_opacity=1).scale(20)
        self.add(bg_rect)
        self.wait(0.25)

        self.create_all()

        self.play(FadeIn(self.circle))
        self.wait()

        # self.always_continually_update = True

        for i in range(self.circle_num):

            self.play(ReplacementTransform(self.r_group[i], self.r_group[i+1]), run_time=0.1)
            self.wait(0.15)
            self.play(ShowCreation(self.circles[i]), run_time=0.6)
            self.wait(0.25)
        self.play(FadeOut(self.r_group[-1]), FadeOut(self.circle))

        self.wait(2)

    def create_all(self):

        n = self.circle_num
        self.circle = Circle(radius=self.circle_r, color=BLUE, stroke_width=self.circle_width).move_to(self.circle_loc)

        self.circles = VGroup()

        delta_a = TAU / (n + 1)
        vector_0 = UP * self.circle_r

        r1 = Line(self.circle.get_center() + UP * self.circle_r, self.circle.get_center() + UP * self.circle_r, color=self.circle_color)
        r2 = Line(self.circle.get_center(), self.circle.get_center() + UP * self.circle_r, color=BLUE)

        self.r_group = VGroup(VGroup(r1, r2))

        for i in range(n):
            vector_i = np.array([np.sin(delta_a * (i + 1)), np.cos(delta_a * (i + 1)), 0]) * self.circle_r
            circle_i = Circle(radius=np.sqrt(sum((vector_i-vector_0) ** 2)), color=self.circle_color, stroke_width=self.circle_width).move_to(self.circle.get_center() + vector_i)
            self.circles.add(circle_i)

            r1_i = Line(self.circle.get_center() + UP * self.circle_r, self.circles[i].get_center(), color=self.circle_color)
            r2_i = Line(self.circle.get_center(), self.circles[i].get_center(), color=BLUE)
            self.r_group.add(VGroup(r1_i, r2_i))

class Cardioid_by_TwoCircles(Scene):

    CONFIG = {
        'bg_color': WHITE,
        'circle_color': BLUE,
        # 'circle_num': 36,
        'circle_width': 6,
        'curve_color': RED_B,
        'curve_width': 5,
        'circle_r': 1.25,
        'circle_loc': ORIGIN,
        'arrow_color': PINK,

        "parametric_function_step_size": 0.005,
        "slow_factor": 0.25,
        "draw_time": 4,
    }

    def construct(self):

        self.setup_scene()
        self.wait(0.4)

        self.play(FadeInFromLarge(self.origin), run_time=0.5)
        self.play(ShowCreation(self.circle_0), run_time=0.8)
        self.wait(0.2)
        self.play(ShowCreation(self.circle_1[0]), run_time=0.8)
        self.wait(0.2)
        self.play(ShowCreation(self.circle_1[1]), run_time=0.8)
        self.wait(0.8)
        self.always_continually_update = True

        dt = 1/29.9
        step_n = 160
        d_theta = -TAU/step_n
        self.line_group = VGroup()
        p_old = self.circle_1[2].get_center()

        # path = self.get_path()
        # broken_path = CurvesAsSubmobjects(path)
        # broken_path.curr_time = 0
        # broken_path.set_color(self.curve_color)

        # self.draw_path()

        for i in range(1, step_n + 1):
            self.circle_1.rotate_about_origin(d_theta)
            self.circle_1.rotate(d_theta)
            p_new = self.circle_1[2].get_center()
            line_i = Line(p_old, p_new, color=self.curve_color, stroke_width=self.curve_width)
            self.line_group.add(line_i)
            self.add(line_i)
            self.wait(dt)
            p_old = p_new

            # alpha = path.curr_time * self.get_slow_factor()
            # n_curves = len(path)
            # for a, sp in zip(np.linspace(0, 1, n_curves), path):
            #     b = alpha - a
            #     if b < 0:
            #         width = 0
            #     else:
            #         width = self.curve_width
            #     sp.set_stroke(width=width)
            # path.curr_time += dt
            self.wait(dt)

        self.wait(3)

    def setup_scene(self):
        bg_rect = Rectangle(fill_color=self.bg_color, fill_opacity=1).scale(20)
        self.add(bg_rect)
        self.wait(0.25)

        self.origin = Circle(radius=0.1, color=GREEN, fill_color=GREEN, fill_opacity=1)

        self.circle_0 = Circle(radius=self.circle_r, color=self.circle_color).move_to(self.circle_loc)
        self.circle_1 = VGroup(Circle(radius=self.circle_r, color=self.circle_color),
                               Vector(DOWN * self.circle_r, color=self.arrow_color),
                               Dot(DOWN * self.circle_r, color=self.arrow_color),
                               Vector(UP * self.circle_r, color=self.arrow_color),
                               Dot(UP * self.circle_r, color=self.arrow_color)).shift(self.circle_loc + 2 * UP * self.circle_r)
        self.two_cirlce = VGroup(self.circle_0, self.circle_1)

    def define_func(self):
        self.func = lambda t: self.circle_loc + np.array([(1 - np.sin(t)) * np.cos(t), (1 - np.sin(t)) * np.sin(t), 0]) * self.circle_r * 2

    def setup_slow_factor(self):
        self.slow_factor_tracker = ValueTracker(
            self.slow_factor
        )

    def get_slow_factor(self):
        return self.slow_factor_tracker.get_value()

    def get_path(self):
        self.define_func()
        path = ParametricFunction(
            self.func,
            t_min=0,
            t_max=2 * PI,
            color=self.curve_color,
            step_size=self.parametric_function_step_size
        )
        return path

    def draw_path(self):
        self.setup_slow_factor()
        path = self.get_path()
        broken_path = CurvesAsSubmobjects(path)
        broken_path.curr_time = 0

        def update_path(path, dt):
            alpha = path.curr_time * self.get_slow_factor()
            n_curves = len(path)
            for a, sp in zip(np.linspace(0, 1, n_curves), path):
                b = alpha - a
                if b < 0:
                    width = 0
                else:
                    width = self.curve_width
                sp.set_stroke(width=width)
            path.curr_time += dt
            return path

        broken_path.set_color(self.curve_color)
        broken_path.add_updater(update_path)
        return broken_path

class Gear(VGroup):

    CONFIG = {
        'g_color': BLUE,
        'g_R': 3.,
        'g_r': 1.2,
        'g_h': 0.6,
        'g_stroke': 4,
        'teeth_num': 17,
    }

    def init_gear(self):
        self.g_m = 2 * PI * self.g_R / self.teeth_num

        r0 = self.g_R - self.g_h / 2
        phi_m = np.sqrt((self.g_R / r0) ** 2 - 1)
        phi_t = np.sqrt(((r0 + self.g_h) / r0) ** 2 - 1)

        d_theta = TAU / self.teeth_num / 2

        self.add(Circle(radius=self.g_r, stroke_width=self.g_stroke, color=self.g_color))

        for i in range(self.teeth_num):

            p1 = np.array([r0, 0])
            p2 = np.array([r0 * (np.cos(phi_m) + phi_m * np.sin(phi_m)), r0 * (np.sin(phi_m) - phi_m * np.cos(phi_m))])
            p3 = np.array([r0 * (np.cos(phi_t) + phi_t * np.sin(phi_t)), r0 * (np.sin(phi_t) - phi_t * np.cos(phi_t))])
            arc_1 = self.create_arc_ppp(p1, p2, p3, stroke_width=self.g_stroke, color=self.g_color)

            a = np.arctan(p2[1]/p2[0])

            p2 = np.array([r0 * (np.cos(phi_m) + phi_m * np.sin(phi_m)), -r0 * (np.sin(phi_m) - phi_m * np.cos(phi_m))])
            p3 = np.array([r0 * (np.cos(phi_t) + phi_t * np.sin(phi_t)), -r0 * (np.sin(phi_t) - phi_t * np.cos(phi_t))])

            arc_2 = self.create_arc_ppp(p3, p2, p1, stroke_width=self.g_stroke, color=self.g_color).rotate_about_origin(d_theta + 2 * a)

            line01 = Line(arc_1.get_all_points()[-1], arc_2.get_all_points()[0], stroke_width=self.g_stroke, color=self.g_color)

            line02 = Line(arc_2.get_all_points()[-1], Point(arc_1.get_all_points()[0]).rotate_about_origin(d_theta * 2).get_center(),
                          stroke_width=self.g_stroke, color=self.g_color)

            self.add(VGroup(arc_1, line01, arc_2, line02).rotate_about_origin(d_theta * i * 2))

    def create_arc_ppp(self, p1, p2, p3, **kwargs):
        a = np.array([[p1[0], p1[1], 1], [p2[0], p2[1], 1], [p3[0], p3[1], 1]])
        b = np.array([-(p1[0] ** 2 + p1[1] ** 2), -(p2[0] ** 2 + p2[1] ** 2), -(p3[0] ** 2 + p3[1] ** 2)])
        x = np.linalg.solve(a, b)
        center = np.array([-x[0]/2, -x[1]/2, 0])
        radius = np.sqrt(x[0] ** 2 / 4 + x[1] ** 2 / 4 - x[2])
        l_13 = np.sqrt((p1[0] - p3[0]) ** 2 + (p1[1] - p3[1]) ** 2)
        theta = np.arcsin(l_13 / 2 / radius) * 2
        start_a = np.arctan((p1[1] - center[1])/(p1[0] - center[0]))
        return Arc(radius=radius, start_angle=start_a, angle=theta, **kwargs).shift(center)

class Test_gear(Scene):

    def construct(self):
        gear = Gear()

        # p1 = UP
        # p2 = (UP + RIGHT) * np.sqrt(2) / 2
        # p3 = RIGHT
        # arc = gear.create_arc_ppp(p3, p2, p1, stroke_width=4, color=YELLOW)
        # self.play(ShowCreation(Circle()))
        # self.play(ShowCreation(arc), run_time=2)

        gear.init_gear()
        self.play(ShowCreation(gear), run_time=10)
        self.wait(4)

class Cardioid_by_TwoGears(Scene):

    CONFIG = {
        'bg_color': WHITE,
        'gear_color': BLUE,
        'gear_stroke': 3,
        'curve_color': RED_B,
        'curve_width': 5,

        'gear_r': 1.25,
        'gear_loc': ORIGIN,
        'arrow_color': PINK,

        "parametric_function_step_size": 0.005,
        "slow_factor": 0.25,
        "draw_time": 4,
    }

    def construct(self):

        self.setup_scene()
        self.wait(0.4)

        self.play(FadeInFromLarge(self.origin), run_time=0.5)
        self.play(ShowCreation(self.gear_0), run_time=1.6)
        self.wait(0.2)

        self.play(ShowCreation(self.gear_1[-1]), run_time=0.4)
        self.wait(0.2)
        self.play(ShowCreation(self.orbit), run_time=1)
        self.wait(0.25)

        self.play(ShowCreation(self.gear_1[0]), run_time=1.6)
        self.wait(0.2)
        self.play(ShowCreation(self.gear_1[1]), run_time=0.8)
        self.wait(0.8)
        self.always_continually_update = True

        dt = 1/30
        step_n = 240
        d_theta = -TAU/step_n
        self.line_group = VGroup()
        p_old = self.gear_1[2].get_center()

        # path = self.get_path()
        # broken_path = CurvesAsSubmobjects(path)
        # broken_path.curr_time = 0
        # broken_path.set_color(self.curve_color)

        # self.draw_path()

        for i in range(1, step_n + 1):
            self.gear_1.rotate_about_origin(d_theta)
            self.gear_1.rotate(d_theta)
            p_new = self.gear_1[2].get_center()
            line_i = Line(p_old, p_new, color=self.curve_color, stroke_width=self.curve_width)
            self.line_group.add(line_i)
            self.add(line_i)
            self.wait(dt)
            p_old = p_new

            # alpha = path.curr_time * self.get_slow_factor()
            # n_curves = len(path)
            # for a, sp in zip(np.linspace(0, 1, n_curves), path):
            #     b = alpha - a
            #     if b < 0:
            #         width = 0
            #     else:
            #         width = self.curve_width
            #     sp.set_stroke(width=width)
            # path.curr_time += dt
            self.wait(dt)

        self.wait(3)

    def setup_scene(self):
        bg_rect = Rectangle(fill_color=self.bg_color, fill_opacity=1).scale(20)
        self.add(bg_rect)
        self.wait(0.25)

        self.origin = Circle(radius=0.1, color=GREEN, fill_color=GREEN, fill_opacity=1)

        self.orbit = VGroup()
        orbit_n = 36
        d_a = TAU / orbit_n / 2
        for i in range(orbit_n):
            self.orbit.add(Arc(radius=self.gear_r * 2, angle=d_a, color=GREEN, stroke_width=2.5).rotate_about_origin(d_a * 2 * i))


        g_0 = Gear(g_R=self.gear_r, g_r=0.4, g_h=0.25, g_color=self.gear_color, g_stroke=self.gear_stroke)
        g_1 = Gear(g_R=self.gear_r, g_r=0.4, g_h=0.25, g_color=self.gear_color, g_stroke=self.gear_stroke)
        g_0.init_gear()
        g_1.init_gear()
        self.gear_0 = g_0.move_to(self.gear_loc).rotate(TAU / 6 / g_0.teeth_num + PI / 2)
        g_1.rotate(-TAU / 3 / g_0.teeth_num * 1.04 - PI / 2)

        self.gear_1 = VGroup(g_1.move_to(self.gear_loc),
                             Vector(DOWN * self.gear_r, color=self.arrow_color),
                             Dot(DOWN * self.gear_r, color=self.arrow_color),
                             Vector(UP * self.gear_r, color=self.arrow_color),
                             Dot(UP * self.gear_r, color=self.arrow_color),
                             Circle(radius=0.1, color=GREEN, fill_color=GREEN, fill_opacity=1)).shift(self.gear_loc + 2 * UP * self.gear_r)
        self.two_cirlce = VGroup(self.gear_0, self.gear_1)

    def define_func(self):
        self.func = lambda t: self.gear_loc + np.array([(1 - np.sin(t)) * np.cos(t), (1 - np.sin(t)) * np.sin(t), 0]) * self.gear_r * 2

    def setup_slow_factor(self):
        self.slow_factor_tracker = ValueTracker(
            self.slow_factor
        )

    def get_slow_factor(self):
        return self.slow_factor_tracker.get_value()

    def get_path(self):
        self.define_func()
        path = ParametricFunction(
            self.func,
            t_min=0,
            t_max=2 * PI,
            color=self.curve_color,
            step_size=self.parametric_function_step_size
        )
        return path

    def draw_path(self):
        self.setup_slow_factor()
        path = self.get_path()
        broken_path = CurvesAsSubmobjects(path)
        broken_path.curr_time = 0

        def update_path(path, dt):
            alpha = path.curr_time * self.get_slow_factor()
            n_curves = len(path)
            for a, sp in zip(np.linspace(0, 1, n_curves), path):
                b = alpha - a
                if b < 0:
                    width = 0
                else:
                    width = self.curve_width
                sp.set_stroke(width=width)
            path.curr_time += dt
            return path

        broken_path.set_color(self.curve_color)
        broken_path.add_updater(update_path)
        return broken_path

class FourierCirclesScene(Scene):

    CONFIG = {
        "n_circles": 10,
        "big_radius": 2,
        "colors": [
            BLUE_D,
            BLUE_C,
            BLUE_E,
            GREY_BROWN,
        ],
        "circle_style": {
            "stroke_width": 2,
        },
        "arrow_config": {
            # "buff": 0,
            "max_tip_length_to_length_ratio": 0.35,
            "tip_length": 0.15,
            "max_stroke_width_to_length_ratio": 10,
            "stroke_width": 2,
        },
        "use_vectors": True,
        "base_frequency": 1,
        "slow_factor": 0.25,
        "center_point": ORIGIN,
        "parametric_function_step_size": 0.001,
    }

    def setup(self):
        self.slow_factor_tracker = ValueTracker(
            self.slow_factor
        )

    def get_slow_factor(self):
        return self.slow_factor_tracker.get_value()

    #
    def get_freqs(self):
        n = self.n_circles
        all_freqs = list(range(n // 2, -n // 2, -1))
        all_freqs.sort(key=abs)
        return all_freqs

    def get_coefficients(self):
        return [complex(0) for x in range(self.n_circles)]

    def get_color_iterator(self):
        return it.cycle(self.colors)

    def get_circles(self, freqs=None, coefficients=None):
        circles = VGroup()
        color_iterator = self.get_color_iterator()
        self.center_tracker = VectorizedPoint(self.center_point)

        if freqs is None:
            freqs = self.get_freqs()
        if coefficients is None:
            coefficients = self.get_coefficients()

        last_circle = None
        for freq, coefficient in zip(freqs, coefficients):
            if last_circle:
                center_func = last_circle.get_start
            else:
                center_func = self.center_tracker.get_location
            circle = self.get_circle(
                coefficient=coefficient,
                freq=freq,
                color=next(color_iterator),
                center_func=center_func,
            )
            circles.add(circle)
            last_circle = circle
        return circles

    def get_circle(self, coefficient, freq, color, center_func):
        radius = abs(coefficient)
        phase = np.log(coefficient).imag
        circle = Circle(
            radius=radius,
            color=color,
            **self.circle_style,
        )
        line_points = (
            circle.get_center(),
            circle.get_start(),
        )
        if self.use_vectors:
            circle.radial_line = Arrow(
                *line_points,
                **self.arrow_config,
            )
        else:
            circle.radial_line = Line(
                *line_points,
                color=BLUE,
                **self.circle_style,
            )
        circle.add(circle.radial_line)
        circle.freq = freq
        circle.phase = phase
        circle.rotate(phase)
        circle.coefficient = coefficient
        circle.center_func = center_func
        circle.add_updater(self.update_circle)
        return circle

    def update_circle(self, circle, dt):
        circle.rotate(
            self.get_slow_factor() * circle.freq * dt * TAU
        )
        circle.move_to(circle.center_func())
        return circle

    def get_rotating_vectors(self, circles):
        return VGroup(*[
            self.get_rotating_vector(circle)
            for circle in circles
        ])

    def get_rotating_vector(self, circle):
        vector = Vector(RIGHT, color=BLUE_E)
        vector.add_updater(lambda v, dt: v.put_start_and_end_on(
            circle.get_center(),
            circle.get_start(),
        ))
        circle.vector = vector
        return vector

    def get_circle_end_path(self, circles, color=GOLD):
        coefs = [c.coefficient for c in circles]
        freqs = [c.freq for c in circles]
        center = circles[0].get_center()

        path = ParametricFunction(
            lambda t: center + reduce(op.add, [
                complex_to_R3(
                    coef * np.exp(TAU * 1j * freq * t)
                )
                for coef, freq in zip(coefs, freqs)
            ]),
            t_min=0,
            t_max=1,
            color=color,
            step_size=self.parametric_function_step_size,
        )
        return path

    # TODO, this should be a general animated mobect
    def get_drawn_path(self, circles, stroke_width=2, **kwargs):
        path = self.get_circle_end_path(circles, **kwargs)
        broken_path = CurvesAsSubmobjects(path)
        broken_path.curr_time = 0

        def update_path(path, dt):
            alpha = path.curr_time * self.get_slow_factor()
            n_curves = len(path)
            for a, sp in zip(np.linspace(0, 1, n_curves), path):
                b = alpha - a
                if b < 0:
                    width = 0
                else:
                    width = stroke_width * (1 - (b % 1))
                sp.set_stroke(width=width)
            path.curr_time += dt
            return path

        broken_path.set_color(RED_C)
        broken_path.add_updater(update_path)
        return broken_path

    def get_y_component_wave(self,
                             circles,
                             left_x=1,
                             color=PINK,
                             n_copies=2,
                             right_shift_rate=5):
        path = self.get_circle_end_path(circles)
        wave = ParametricFunction(
            lambda t: op.add(
                right_shift_rate * t * LEFT,
                path.function(t)[1] * UP
            ),
            t_min=path.t_min,
            t_max=path.t_max,
            color=color,
        )
        wave_copies = VGroup(*[
            wave.copy()
            for x in range(n_copies)
        ])
        wave_copies.arrange(RIGHT, buff=0)
        top_point = wave_copies.get_top()
        wave.creation = ShowCreation(
            wave,
            run_time=(1 / self.get_slow_factor()),
            rate_func=linear,
        )
        cycle_animation(wave.creation)
        wave.add_updater(lambda m: m.shift(
            (m.get_left()[0] - left_x) * LEFT
        ))

        def update_wave_copies(wcs):
            index = int(
                wave.creation.total_time * self.get_slow_factor()
            )
            wcs[:index].match_style(wave)
            wcs[index:].set_stroke(width=0)
            wcs.next_to(wave, RIGHT, buff=0)
            wcs.align_to(top_point, UP)
        wave_copies.add_updater(update_wave_copies)

        return VGroup(wave, wave_copies)

    def get_wave_y_line(self, circles, wave):
        return DashedLine(
            circles[-1].get_start(),
            wave[0].get_end(),
            stroke_width=1,
            dash_length=DEFAULT_DASH_LENGTH * 0.5,
        )

    # Computing Fourier series
    def get_coefficients_of_path(self, path, n_samples=10000, freqs=None):
        if freqs is None:
            freqs = self.get_freqs()
        dt = 1 / n_samples
        ts = np.arange(0, 1, dt)
        samples = np.array([
            path.point_from_proportion(t)
            for t in ts
        ])
        samples -= self.center_point
        complex_samples = samples[:, 0] + 1j * samples[:, 1]

        result = []
        for freq in freqs:
            riemann_sum = np.array([
                np.exp(-TAU * 1j * freq * t) * cs
                for t, cs in zip(ts, complex_samples)
            ]).sum() * dt
            result.append(riemann_sum)

        return result

class Curves_by_Fourier(FourierCirclesScene):

    CONFIG = {
        'bg_color': WHITE,
        "n_circles": 20,
        "center_point": ORIGIN,
        "slow_factor": 0.2,
        "run_time": 8,
        # "tex": "\\Sigma",
        "start_drawn": False,

        "colors": [
            BLUE_A,

            BLUE_D,
        ],

    }

    def construct(self):

        bg_rect = Rectangle(fill_color=self.bg_color, fill_opacity=1).scale(20)
        self.add(bg_rect)
        self.wait(0.25)

        cardioid = [self.curve_func(i * 2 * PI / 120) for i in range(120)]
        path = self.my_path(cardioid)
        coefs = self.get_coefficients_of_path(path)

        circles = self.get_circles(coefficients=coefs)
        for k, circle in zip(it.count(1), circles):
            circle.set_stroke(width=max(
                1 / np.sqrt(k),
                1,
            ))

        # approx_path = self.get_circle_end_path(circles)
        drawn_path = self.get_drawn_path(circles)
        if self.start_drawn:
            drawn_path.curr_time = 1 / self.slow_factor

        self.add(path)
        self.add(circles)
        self.add(drawn_path)
        self.wait(self.run_time)

    def curve_func(self, t):
        # return np.array([2*np.sin(t)-np.sin(2*t), 2*np.cos(t)-np.cos(2*t), 0]) * 2 + UP
        return np.array([16 * np.sin(t) ** 3, 13 * np.cos(t) - 5 * np. cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t), 0]) + UP * 1.6

    def my_path(self, point_list):

        my_path = Polygon(*point_list)
        my_path.set_height(5)
        my_path.shift(RIGHT)
        path = my_path.family_members_with_points()[0]
        path.set_fill(opacity=0)
        path.set_stroke(WHITE, 1)

        return path

class Curve_by_RotatingVectors_2v(Scene):

    CONFIG = {
        'bg_color': WHITE,
        'circle_color': BLUE,
        'circle_num': 2,
        'circle_width': 3.6,
        'curve_color': RED_B,
        'curve_width': 4,

        'scale_all': 1.2,

        'arrow_color': PINK,

        'center_loc': ORIGIN,

        "arrow_config": {
            "buff": 0,
            "max_tip_length_to_length_ratio": 0.35,
            "tip_length": 0.15,
            "max_stroke_width_to_length_ratio": 10,
            "stroke_width": 2,
        },

        'dt': 1/29.9,
        'run_time': 16,
        'speed': 1,

    }

    def construct(self):

        bg_rect = Rectangle(fill_color=self.bg_color, fill_opacity=1).scale(20)
        self.add(bg_rect)
        self.wait(0.25)

        f_list = [1, 2]
        a_list = [2, 1]
        p_list = [0, PI]
        self.setup_all(f_list, a_list, p_list)
        self.circle_arrow_anim()
        self.wait(2)


    def set_frequency(self, f_list):
        self.frequency_list = np.array(f_list[0: self.circle_num])

    def set_amplitude(self, a_list):
        self.amplitude_list = np.array(a_list[0: self.circle_num]) * self.scale_all

    def set_phase(self, p_list):
        if p_list == 0:
            self.phase_list = np.array([0 for i in range(self.circle_num)])
        else:
            self.phase_list = np.array(p_list[0: self.circle_num])

    def curve_func(self, t):
        return self.circle_loc + np.array([(1 - np.sin(t)) * np.cos(t), (1 - np.sin(t)) * np.sin(t), 0])

    def setup_all(self, f_list, a_list, p_list):
        self.set_frequency(f_list)
        self.set_amplitude(a_list)
        self.set_phase(p_list)

        n = self.circle_num
        self.center_list = np.zeros((n + 1, 3)) + self.center_loc

        for i in range(n):
            v_i = np.array([np.sin(self.phase_list[i]), np.cos(self.phase_list[i]), 0]) * self.amplitude_list[i]
            self.center_list[i + 1: n + 2] += v_i

        self.always_continually_update = True

    def set_arrow(self):
        self.arrows = VGroup()

        for i in range(self.circle_num):
            # print('i = %d' % i)
            arrow_i = Vector(self.center_list[i+1] - self.center_list[i], color=self.arrow_color, **self.arrow_config).shift(self.center_list[i])
            #.put_start_and_end_on(self.center_list[i], self.center_list[i+1])
            # print(type(arrow_i))
            self.arrows.add(arrow_i)
            # print(len(self.arrows))

    def arrow_anim(self):
        self.set_arrow()
        self.play(ShowCreation(self.arrows), run_time=1.2)
        # self.play(ShowCreation(self.arrows.get_family()[0]), run_time=1.2)
        self.wait(0.5)
        n = self.circle_num
        dt = 1/14.9
        step_n = 120
        speed = 1
        d_theta = 2 * PI / step_n / n * speed

        for j in range(step_n + 1):
            print('center_points:')
            print(self.center_list)
            self.center_list = np.zeros((n + 1, 3)) + self.center_loc
            for i in range(self.circle_num):
                v_i = np.array([np.sin(self.phase_list[i] + d_theta * j * self.frequency_list[i]), np.cos(self.phase_list[i] + d_theta * j * self.frequency_list[i]), 0]) * self.amplitude_list[i]
                self.center_list[i + 1: n + 2] += v_i
                self.arrows[i].put_start_and_end_on(self.center_list[i], self.center_list[i+1])
            self.wait(dt)
        self.wait(0.25)

    def set_circles(self):
        self.circles = VGroup()
        for i in range(self.circle_num):
            circle_i = Circle(radius=self.amplitude_list[i], color=self.circle_color, stroke_width=self.circle_width).move_to(self.center_list[i])
            self.circles.add(circle_i)

    def circle_arrow_anim(self):

        self.set_arrow()
        self.set_circles()

        self.play(ShowCreation(self.arrows[1]), ShowCreation(self.circles[1]), run_time=0.8)
        #self.wait(0.5)
        c1 = Circle(radius=1 * self.scale_all, color=self.circle_color, stroke_width=self.circle_width)
        self.play(ShowCreation(c1), run_time=0.8)
        self.wait(0.6)

        n = self.circle_num
        dt = self.dt
        step_n = int(self.run_time/dt)
        speed = self.speed
        d_theta = 4 * PI / step_n * speed
        self.lines = VGroup()

        line_start = self.center_list[-1]
        # line_end = self.center_list[-1]
        for j in range(step_n + 1):
            print('center_points:')
            print(self.center_list)
            self.center_list = np.zeros((n + 1, 3)) + self.center_loc
            for i in range(self.circle_num):
                v_i = np.array([np.sin(self.phase_list[i] + d_theta * j * self.frequency_list[i]), np.cos(self.phase_list[i] + d_theta * j * self.frequency_list[i]), 0]) * self.amplitude_list[i]
                self.center_list[i + 1: n + 2] += v_i
                self.arrows[i].put_start_and_end_on(self.center_list[i], self.center_list[i+1])
                self.circles[i].move_to(self.center_list[i])
            line_end = self.center_list[-1]
            line_j = Line(line_start, line_end, color=self.curve_color, stroke_width=self.curve_width)
            self.lines.add(line_j)
            self.add(line_j)
            line_start = self.center_list[-1]
            self.wait(dt)
            if j == int(step_n/2):
                self.play(ShowCreation(self.circles[0]), ShowCreation(self.arrows[0]), run_time=1)
                self.play(FadeOut(c1), run_time=1)
                self.wait(0.9)
            # elif j > int(step_n/2):

        self.wait(0.25)

class Curve_by_RotatingVectors(Scene):

    CONFIG = {
        'bg_color': WHITE,
        'circle_color': BLUE,
        'circle_num': 14,
        'circle_width': 1.,
        'curve_color': RED_B,
        'curve_width': 4,

        'scale_all': 5,

        'arrow_color': PINK,

        'center_loc': ORIGIN,

        "arrow_config": {
            "buff": 0,
            "max_tip_length_to_length_ratio": 0.35,
            "tip_length": 0.15,
            "max_stroke_width_to_length_ratio": 10,
            "stroke_width": 2,
        },

        'dt': 1/29,
        'run_time': 32,
        'speed': 1,

        # 'f_list': [1, 2],
        # 'a_list': [2, 1],
        # 'p_list': [0, PI],

    }

    def construct(self):

        bg_rect = Rectangle(fill_color=self.bg_color, fill_opacity=1).scale(20)
        self.add(bg_rect)
        self.wait(0.25)

        self.setup_all()
        self.anim_follow_EndPoint()
        self.wait(2)

    def set_frequency(self, f_list):
        self.frequency_list = np.array(f_list[0: self.circle_num])

    def set_amplitude(self, a_list):
        self.amplitude_list = np.array(a_list[0: self.circle_num]) * self.scale_all

    def set_phase(self, p_list):
        if p_list == 0:
            self.phase_list = np.array([0 for i in range(self.circle_num)])
        else:
            self.phase_list = np.array(p_list[0: self.circle_num])

    def curve_func(self, t):
        return np.array([16 * np.sin(t) ** 3, 13 * np.cos(t) - 5 * np. cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t), 0]) + UP * 1.6

    def curve_complex_func(self, t):
        return complex(self.curve_func(t)[0], self.curve_func(t)[1])

    def get_freqs(self):
        n = self.circle_num
        all_freqs = list(range(n // 2, -n // 2, -1))
        all_freqs.sort(key=abs)
        return all_freqs

    def get_coefficients_of_path(self, path, n_samples=10000, freqs=None):
        if freqs is None:
            freqs = self.get_freqs()
        dt = 1 / n_samples
        ts = np.arange(0, 1, dt)
        samples = np.array([
            path.point_from_proportion(t)
            for t in ts
        ])
        samples -= self.center_loc
        complex_samples = samples[:, 0] + 1j * samples[:, 1]

        result = []
        for freq in freqs:
            riemann_sum = np.array([
                np.exp(-TAU * 1j * freq * t) * cs
                for t, cs in zip(ts, complex_samples)
            ]).sum() * dt
            result.append(riemann_sum)

        return result

    def my_path(self, point_list):

        my_path = Polygon(*point_list)
        my_path.set_height(5.6)
        my_path.shift(UP)
        path = my_path.family_members_with_points()[0]
        path.set_fill(opacity=0)
        path.set_stroke(WHITE, 1)

        return path

    def setup_all(self):

        sample_n = 100
        path = [self.curve_func(i * 2 * PI/sample_n) for i in range(sample_n)]
        my_path = self.my_path(path)
        self.frequency_list = self.get_freqs()
        amplitudes = self.get_coefficients_of_path(my_path)
        self.amplitude_list = [abs(a) for a in amplitudes]

        self.phase_list = np.log(amplitudes).imag - PI / 2
        # self.phase_list = [0 for a in amplitudes]
        print('phase:', self.phase_list)

        n = self.circle_num
        self.center_list = np.zeros((n + 1, 3)) + self.center_loc

        for i in range(n):
            v_i = np.array([np.sin(self.phase_list[i]), np.cos(self.phase_list[i]), 0]) * self.amplitude_list[i]
            self.center_list[i + 1: n + 2] += v_i

        self.always_continually_update = True

    def set_arrow(self):
        self.arrows = VGroup()

        for i in range(self.circle_num):
            # print('i = %d' % i)
            arrow_i = Vector(self.center_list[i+1] - self.center_list[i], color=self.arrow_color, **self.arrow_config).shift(self.center_list[i])
            #.put_start_and_end_on(self.center_list[i], self.center_list[i+1])
            # print(type(arrow_i))
            self.arrows.add(arrow_i)
            # print(len(self.arrows))

    def arrow_anim(self):
        self.set_arrow()
        self.play(ShowCreation(self.arrows), run_time=1.2)
        # self.play(ShowCreation(self.arrows.get_family()[0]), run_time=1.2)
        self.wait(0.5)
        n = self.circle_num
        dt = 1/14.9
        step_n = 120
        speed = 1
        d_theta = 2 * PI / step_n / n * speed

        for j in range(step_n + 1):
            print('center_points:')
            print(self.center_list)
            self.center_list = np.zeros((n + 1, 3)) + self.center_loc
            for i in range(self.circle_num):
                v_i = np.array([np.sin(self.phase_list[i] + d_theta * j * self.frequency_list[i]), np.cos(self.phase_list[i] + d_theta * j * self.frequency_list[i]), 0]) * self.amplitude_list[i]
                self.center_list[i + 1: n + 2] += v_i
                self.arrows[i].put_start_and_end_on(self.center_list[i], self.center_list[i+1])
            self.wait(dt)
        self.wait(0.25)

    def set_circles(self):
        self.circles = VGroup()
        for i in range(self.circle_num):
            circle_i = Circle(radius=self.amplitude_list[i], color=self.circle_color, stroke_width=self.circle_width).move_to(self.center_list[i])
            self.circles.add(circle_i)

    def circle_arrow_anim(self):

        self.set_arrow()
        self.set_circles()

        # self.play(ShowCreation(self.arrows), ShowCreation(self.circles), run_time=1.8)

        for i in range(self.circle_num):
            self.play(FadeInFromLarge(self.arrows[i]), FadeInFromLarge(self.circles[i]), run_time=0.32)

        #self.wait(0.5)
        # c1 = Circle(radius=1 * self.scale_all, color=self.circle_color, stroke_width=self.circle_width)
        # self.play(ShowCreation(c1), run_time=0.8)
        self.wait()

        n = self.circle_num
        dt = self.dt
        step_n = int(self.run_time/dt)
        speed = self.speed
        d_theta = 4 * PI / step_n * speed
        self.lines = VGroup()

        line_start = self.center_list[-1]
        # line_end = self.center_list[-1]
        for j in range(step_n + 1):
            print('center_points:')
            print(self.center_list)
            self.center_list = np.zeros((n + 1, 3)) + self.center_loc
            for i in range(self.circle_num):
                # print('i = %d' % i)
                v_i = np.array([np.sin(self.phase_list[i] + d_theta * j * self.frequency_list[i]), np.cos(self.phase_list[i] + d_theta * j * self.frequency_list[i]), 0]) * self.amplitude_list[i]
                self.center_list[i + 1: n + 2] += v_i
                self.arrows[i].put_start_and_end_on(self.center_list[i], self.center_list[i+1])
                self.circles[i].move_to(self.center_list[i])
            line_end = self.center_list[-1]
            line_j = Line(line_start, line_end, color=self.curve_color, stroke_width=self.curve_width)
            self.lines.add(line_j)
            self.add(line_j)
            line_start = self.center_list[-1]
            self.wait(dt)
            # if j == int(step_n/2):
            #     self.play(ShowCreation(self.circles[0]), ShowCreation(self.arrows[0]), run_time=1)
            #     self.play(FadeOut(c1), run_time=1)
            #     self.wait(0.9)
            # elif j > int(step_n/2):

        self.wait(0.25)

    def anim_follow_EndPoint(self):

        self.set_arrow()
        self.set_circles()

        self.add(self.arrows, self.circles)

        # move_vector = ORIGIN - self.center_list[-1]
        # self.arrows.shift(move_vector)
        # self.circles.shift(move_vector)

        n = self.circle_num
        dt = self.dt
        step_n = int(self.run_time/dt)
        speed = self.speed
        d_theta = 4 * PI / step_n * speed
        self.lines = VGroup()

        line_start = self.center_list[-1]

        s = 5

        for j in range(step_n + 1):
            print('center_points:')
            print(self.center_list)
            self.center_list = np.zeros((n + 1, 3)) + self.center_loc
            for i in range(self.circle_num):
                # print('i = %d' % i)
                v_i = np.array([np.sin(self.phase_list[i] + d_theta * j * self.frequency_list[i]), np.cos(self.phase_list[i] + d_theta * j * self.frequency_list[i]), 0]) * self.amplitude_list[i]
                self.center_list[i + 1: n + 2] += v_i
                self.arrows[i].put_start_and_end_on(self.center_list[i], self.center_list[i+1])
                self.circles[i].move_to(self.center_list[i])
            line_end = self.center_list[-1]
            line_j = Line(line_start, line_end, color=self.curve_color, stroke_width=self.curve_width)

            move_vector = ORIGIN - self.center_list[-1]
            self.arrows.shift(move_vector)
            self.circles.shift(move_vector)
            self.lines.shift(line_start - line_end)
            line_j.shift(move_vector)

            self.lines.add(line_j)
            self.add(line_j)

            self.arrows.scale_about_point(s, ORIGIN)
            self.circles.scale_about_point(s, ORIGIN)
            self.lines.scale_about_point(s, ORIGIN)

            self.wait(dt)

            self.arrows.scale_about_point(1/s, ORIGIN)
            self.circles.scale_about_point(1/s, ORIGIN)
            self.lines.scale_about_point(1/s, ORIGIN)

            line_start = self.center_list[-1]

        self.wait(0.25)

class Other_heart_curves(Scene):

    CONFIG = {
        'bg_color': WHITE,

        'title_color': BLACK,
        'title_scale': 1.1,
        'title_loc': UP * 0.85 + LEFT * 1.,

        'func_color': RED_D,
        'func_scale': 0.72,
        'func_loc': 12 * LEFT + UP * 3,

        'image_path': 'my_code\\images\\',
    }

    def construct(self):

        bg_rect = Rectangle(fill_color=self.bg_color, fill_opacity=1).scale(20)
        self.add(bg_rect)
        self.wait(0.25)

        title = TextMobject('其他由方程生成的心形曲线：', color=self.title_color).scale(self.title_scale).to_corner(self.title_loc)

        func_1_title = TextMobject('参数方程：', color=BLACK).scale(self.func_scale).to_corner(self.func_loc)
        func_1_1 = TextMobject('$x = 16sin^{3}(t)$', color=self.func_color).scale(self.func_scale).to_corner(self.func_loc + UP * 1.2)
        func_1_2 = TextMobject('$y = 13cos(t)-5cos(2t)-2cos(3t)-cos(4t)$', color=self.func_color).scale(self.func_scale).to_corner(self.func_loc + UP * 1.2 * 2)

        func_1 = VGroup(func_1_title, func_1_1, func_1_2).scale(0.85).to_corner(RIGHT * 0.72 + UP * 2.8)

        func_2_title = TextMobject('函数关系式：', color=BLACK).scale(self.func_scale).to_corner(self.func_loc)
        func_2_1 = TextMobject('$y=(cos(200x) \\sqrt{cos(x)} + \\sqrt{| x|}-0.7)(4-x^{2})^{0.01}$', color=self.func_color).scale(self.func_scale).to_corner(self.func_loc + UP * 1.2)

        func_2 = VGroup(func_2_title, func_2_1).scale(0.78).to_corner(RIGHT * 0.56 + UP * 2.8)

        func_3_title = TextMobject('隐式曲线：', color=BLACK).scale(self.func_scale).to_corner(self.func_loc)
        func_3_1 = TextMobject('$5x^{2}-6| x| y +5y^{2}=128$', color=self.func_color).scale(self.func_scale).to_corner(self.func_loc + UP * 1.2)

        func_3 = VGroup(func_3_title, func_3_1).to_corner(RIGHT + UP * 2.8)

        func_4_title = TextMobject('隐式曲线：', color=BLACK).scale(self.func_scale).to_corner(self.func_loc)
        func_4_1 = TextMobject('$x^{2} + 2(\\frac{3}{5} \\sqrt[3]{x^{2}} - y)^{2} = 1$', color=self.func_color).scale(self.func_scale).to_corner(self.func_loc + UP * 1.2)

        func_4 = VGroup(func_4_title, func_4_1).to_corner(RIGHT + UP * 2.8)

        func_5_title = TextMobject('极坐标方程：', color=BLACK).scale(self.func_scale).to_corner(self.func_loc)
        func_5_1 = TextMobject('$\\rho= \\frac{sin(\\theta)\\sqrt{| cos(\\theta)|}}{sin(\\theta) + \\frac{7}{5}} - 2sin(t) + 2$', color=self.func_color).scale(self.func_scale).to_corner(self.func_loc + UP * 1.2)

        func_5 = VGroup(func_5_title, func_5_1).to_corner(RIGHT + UP * 2.8)

        images = Group()

        for i in range(5):
            file_name = self.image_path + 'curve_0' + str(i+1) + '.png'
            image_i = ImageMobject(file_name).scale(3.).shift(DOWN * 0.4 + LEFT * 2.5)
            images.add(image_i)

        ##########
        ## anim ##
        ##########

        self.play(Write(title))
        self.wait(0.6)

        # func_3
        self.play(FadeIn(images[2]))
        self.wait(0.25)
        self.play(Write(func_3[0]))
        self.wait(0.4)
        self.play(Write(func_3[1]))
        self.wait(3)
        self.play(FadeOut(func_3), FadeOut(images[2]))
        self.wait(0.25)

        # func_4
        self.play(FadeIn(images[3]))
        self.wait(0.25)
        self.play(Write(func_4[0]))
        self.wait(0.4)
        self.play(Write(func_4[1]))
        self.wait(3)
        self.play(FadeOut(func_4), FadeOut(images[3]))
        self.wait(0.25)

        # func_5
        self.play(FadeIn(images[4]))
        self.wait(0.25)
        self.play(Write(func_5[0]))
        self.wait(0.4)
        self.play(Write(func_5[1]))
        self.wait(3)
        self.play(FadeOut(func_5), FadeOut(images[4]))
        self.wait(0.25)

        # func_1
        self.play(FadeIn(images[0]))
        self.wait(0.25)
        self.play(Write(func_1[0]))
        self.wait(0.4)
        self.play(Write(func_1[1]))
        self.wait(0.4)
        self.play(Write(func_1[2]))
        self.wait(3)
        self.play(FadeOut(func_1), FadeOut(images[0]))
        self.wait(0.25)

        # func_2
        self.play(FadeIn(images[1]))
        self.wait(0.25)
        self.play(Write(func_2[0]))
        self.wait(0.4)
        self.play(Write(func_2[1]))
        self.wait(3)

        self.wait()

