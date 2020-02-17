from manimlib.imports import *

class Hypocycloid(VMobject):

    CONFIG = {
        'R': 3,
        'r': 1,
        'd': 0.5,
        'theta_max': TAU,
        'stroke_width': 2,
    }

    def __init__(self, **kwargs):

        VMobject.__init__(self, **kwargs)

        t = np.linspace(0, self.theta_max, 400 + 400 * int(np.sqrt(self.theta_max/TAU)))
        curve_points = self.parameter_func(t)
        self.set_points_as_corners(
            [*curve_points]
        )

    def parameter_func(self, t):
        R, r, d = self.R, self.r, self.d
        x, y = (R-r) * np.cos(t) + d * np.cos((R-r) * t/r), (R-r) * np.sin(t) - d * np.sin((R-r) * t/r)
        return np.concatenate((x.reshape(-1, 1), y.reshape(-1, 1), x.reshape(-1, 1) * 0), axis=1)

class Hypocycloid_cluster(Scene):

    def construct(self):

        R = 3.6
        r = R * 3/4
        d = np.linspace(0, r * 0.99, 20)

        curve_group = VGroup()
        color_list = color_gradient([RED, ORANGE, YELLOW, GREEN, BLUE, PINK], len(d))

        circle_big = Circle(radius=R, color=BLUE, fill_opacity=0)
        circle_small = Circle(radius=r, color=BLUE, fill_opacity=0).shift((R-r) * RIGHT)

        for i in range(len(d)):
            curve_i = Hypocycloid(R=R, r=r, d=d[i], theta_max=r/(R-r) * TAU, stroke_width=1.6, color=color_list[i])
            curve_group.add(curve_i)

        self.add(circle_big)
        self.wait()
        self.add(curve_group)
        self.wait(2)

class Generate_Hypocycloid(Scene):

    def construct(self):

        R = 3.6
        r = R * 1/3
        d = r * 0.75

        circle_big = Circle(radius=R, color=BLUE)

        circle_small = Circle(radius=r, color=YELLOW)

        arrow = Arrow(ORIGIN, d * RIGHT, buff=0, color=YELLOW)
        dot = Dot(d * RIGHT, color=RED)
        center_small = Dot().shift((R-r)*RIGHT)
        n = 60
        arc_i = Arc(radius=R-r, angle=TAU/2/n, color=GREEN, stroke_width=2)
        circle_dash = VGroup()
        for i in range(n):
            circle_dash.add(arc_i.copy().rotate_about_origin(i * TAU/n))

        rotate_group = VGroup(circle_small, arrow, dot).shift((R-r)*RIGHT)
        temp = []

        theta = TAU * r/(R-r)
        speed = TAU/360 * 1
        Matrix_R = np.array([[np.cos(-speed), -np.sin(-speed), 0],
                      [np.sin(-speed), np.cos(-speed), 0],
                      [0, 0, 1]])

        def rotate_and_plot(rotate_g, dt):

            loc = rotate_g[0].get_center()
            loc_new = np.dot(loc, Matrix_R)

            rotate_g.shift(loc_new - rotate_g[0].get_center())
            rotate_g.rotate(-speed * (R-r)/r, about_point=rotate_g[0].get_center())

            # self.add(dot.copy().scale(0.4))
            temp.append(dot.get_center())
            if len(temp) >= 2:
                self.add(Line(temp[-1], temp[-2], color=ORANGE, stroke_width=2.5))

            return rotate_g


        self.add(circle_big, circle_dash, rotate_group)

        # self.wait(0.6)
        # self.play(ShowCreation(dot))
        # self.wait(0.4)
        # self.play(ShowCreation(arrow))
        self.wait(0.2)

        # rotate_group.add_updater(update_movement)
        rotate_group.add_updater(rotate_and_plot)


        self.wait(theta/speed/30 + 2)

class Hypocycloid_transfrom(Scene):

    def construct(self):

        R = 3.6

        r_list = np.array([1/2, 1/3, 2/3, 1/4, 3/4, 1/5, 2/5, 3/5, 4/5,
                           1/6, 5/6, 1/7, 2/7, 3/7, 4/7, 5/7, 6/7,
                           1/8, 3/8, 5/8, 7/8, 1/9, 8/9]) * R
        str_list = ['1/2', '1/3', '2/3', '1/4', '3/4', '1/5', '2/5', '3/5', '4/5', '1/6', '5/6',
                    '1/7', '2/7', '3/7', '4/7', '5/7', '6/7', '1/8', '3/8', '5/8', '7/8', '1/9', '8/9']
        # cycle_list = [1, 2, 1, 3, 1, 4, 3, 2, 1,
        #               5, 1, 6, 5, 4, 3, 2, 1,
        #               7, 5, 3, 1, 8, 1]
        cycle_list = [1, 2, 2, 3, 3, 4, 3, 3, 4,
                      5, 5, 6, 5, 4, 4, 5, 6,
                      7, 5, 5, 7, 8, 8]
        d_list = [np.linspace(0, r_list[0] * 0.98, 15), # 1/2
                  np.linspace(0, r_list[1] * 0.98, 10), # 1/3
                  np.linspace(0, r_list[2] * 0.98, 20), # 2/3
                  np.linspace(0, r_list[3] * 0.98, 8 + 3), # 1/4
                  np.linspace(0, r_list[4] * 0.98, 24), # 3/4
                  np.linspace(0, r_list[5] * 0.98, 6 + 3), # 1/5
                  np.linspace(0, r_list[6] * 0.98, 12 + 1), # 2/5
                  np.linspace(0, r_list[7] * 0.98, 18), # 3/5
                  np.linspace(0, r_list[8] * 0.98, 24), # 4/5
                  np.linspace(0, r_list[9] * 0.98, 5 + 3), # 1/6
                  np.linspace(0, r_list[10] * 0.98, 25), # 5/6
                  np.linspace(0, r_list[11] * 0.98, 4 + 3), # 1/7
                  np.linspace(0, r_list[12] * 0.98, 8 + 1), # 2/7
                  np.linspace(0, r_list[13] * 0.98, 12), # 3/7
                  np.linspace(0, r_list[14] * 0.98, 16), # 4/7
                  np.linspace(0, r_list[15] * 0.98, 20), # 5/7
                  np.linspace(0, r_list[16] * 0.98, 24), # 6/7
                  np.linspace(0, r_list[17] * 0.98, 4 + 3), # 1/8
                  np.linspace(0, r_list[18] * 0.98, 12), # 3/8
                  np.linspace(0, r_list[19] * 0.98, 20), # 5/8
                  np.linspace(0, r_list[20] * 0.98, 27), # 7/8
                  np.linspace(0, r_list[21] * 0.98, 3 + 2), # 1/9
                  np.linspace(0, r_list[22] * 0.98, 28), # 8/9
                  ]
        circle_big = Circle(radius=R+0.025, color=BLUE, fill_opacity=0, stroke_width=8)

        all_curve = VGroup()
        for j in range(len(r_list)):
            curve_j = VGroup()
            color_list = color_gradient([RED, ORANGE, YELLOW, GREEN, BLUE, PINK], len(d_list[j]))

            for i in range(len(d_list[j])):
                curve_i = Hypocycloid(R=R, r=r_list[j], d=d_list[j][i], theta_max=cycle_list[j] * TAU, stroke_width=2., color=color_list[i])
                curve_j.add(curve_i)

            all_curve.add(curve_j)

        self.add(circle_big)

        text_group = VGroup()
        for i in range(len(r_list)):
            text_i = Text(str_list[i][::-1], font='Comic Sans MS', color=GREEN).scale(0.9).to_corner(RIGHT * 2.4 + UP * 1.8)
            text_group.add(text_i)

        self.wait(0.5)
        self.play(FadeInFromLarge(text_group[0]), run_time=0.6)
        self.play(FadeIn(all_curve[0]), run_time=1)
        self.wait(1.5)
        for i in range(len(r_list)-1):
            self.play(ReplacementTransform(text_group[i], text_group[i+1]),
                      ReplacementTransform(all_curve[i], all_curve[i+1]),
                      run_time=1)
            self.wait(2)

        self.wait(4)

class Hypocycloid_transfrom_02(Scene):

    def construct(self):

        R = 3.6

        r_list = np.array([1/9, 2/9, 4/9, 5/9, 7/9, 8/9]) * R
        str_list = ['1/9', '2/9', '4/9', '5/9', '7/9', '8/9']
        # cycle_list = [1, 2, 1, 3, 1, 4, 3, 2, 1,
        #               5, 1, 6, 5, 4, 3, 2, 1,
        #               7, 5, 3, 1, 8, 1]
        cycle_list = [8, 7, 5, 5, 7, 8]
        d_list = [np.linspace(0, r_list[0] * 0.98, 4 + 2), # 3/7
                  np.linspace(0, r_list[1] * 0.98, 4 * 2 + 1), # 4/7
                  np.linspace(0, r_list[2] * 0.98, 4 * 4), # 5/7
                  np.linspace(0, r_list[3] * 0.98, 4 * 5 - 1), # 6/7
                  np.linspace(0, r_list[4] * 0.98, 4 * 7 - 2), # 1/8
                  np.linspace(0, r_list[5] * 0.98, 4 * 8 - 3), # 3/8
                  ]
        circle_big = Circle(radius=R+0.025, color=BLUE, fill_opacity=0, stroke_width=8)

        all_curve = VGroup()
        for j in range(len(r_list)):
            curve_j = VGroup()
            color_list = color_gradient([RED, ORANGE, YELLOW, GREEN, BLUE, PINK], len(d_list[j]))

            for i in range(len(d_list[j])):
                curve_i = Hypocycloid(R=R, r=r_list[j], d=d_list[j][i], theta_max=cycle_list[j] * TAU, stroke_width=2., color=color_list[i])
                curve_j.add(curve_i)

            all_curve.add(curve_j)

        self.add(circle_big)

        text_group = VGroup()
        for i in range(len(r_list)):
            text_i = Text(str_list[i][::-1], font='Comic Sans MS', color=GREEN).scale(0.9).to_corner(RIGHT * 2.4 + UP * 1.8)
            text_group.add(text_i)

        self.wait(0.5)
        self.play(FadeInFromLarge(text_group[0]), run_time=0.6)
        self.play(FadeIn(all_curve[0]), run_time=1)
        self.wait(1.5)
        for i in range(len(r_list)-1):
            self.play(ReplacementTransform(text_group[i], text_group[i+1]),
                      ReplacementTransform(all_curve[i], all_curve[i+1]),
                      run_time=1)
            self.wait(2)

        self.wait(4)

class Hypocycloid_transfrom_03(Scene):

    def construct(self):

        R = 3.6

        r_list = np.array([5/13, 11/27, 17/41, 19/39, 21/53, 37/91]) * R
        str_list = ['13/5', '27/11', '41/17', '39/19', '53/21', '91/37']
        # cycle_list = [1, 2, 1, 3, 1, 4, 3, 2, 1,
        #               5, 1, 6, 5, 4, 3, 2, 1,
        #               7, 5, 3, 1, 8, 1]
        cycle_list = [8, 16, 26, 20, 32, 54]
        d_list = [np.linspace(0, r_list[0] * 0.98, 3), # 3/7
                  np.linspace(0, r_list[1] * 0.98, 3), # 4/7
                  np.linspace(0, r_list[2] * 0.98, 3), # 5/7
                  np.linspace(0, r_list[3] * 0.98, 3), # 6/7
                  np.linspace(0, r_list[4] * 0.98, 3), # 1/8
                  np.linspace(0, r_list[5] * 0.98, 3), # 3/8
                  ]
        circle_big = Circle(radius=R+0.025, color=BLUE, fill_opacity=0, stroke_width=8)

        all_curve = VGroup()
        for j in range(len(r_list)):
            curve_j = VGroup()
            color_list = color_gradient([RED, ORANGE, YELLOW, GREEN, BLUE, PINK], len(d_list[j]))

            for i in range(len(d_list[j])):
                curve_i = Hypocycloid(R=R, r=r_list[j], d=d_list[j][i], theta_max=cycle_list[j] * TAU, stroke_width=1.8, color=color_list[i])
                curve_j.add(curve_i)

            all_curve.add(curve_j)

        self.add(circle_big)

        text_group = VGroup()
        for i in range(len(r_list)):
            text_i = Text(str_list[i], font='Comic Sans MS', color=GREEN).scale(0.9).to_corner(RIGHT * 2.4 + UP * 1.8)
            text_group.add(text_i)

        self.wait(0.5)
        self.play(FadeInFromLarge(text_group[0]), run_time=0.6)
        self.play(FadeIn(all_curve[0]), run_time=1)
        self.wait(2.4)
        for i in range(len(r_list)-1):
            self.play(ReplacementTransform(text_group[i], text_group[i+1]),
                      ReplacementTransform(all_curve[i], all_curve[i+1]),
                      run_time=1)
            self.wait(2.2)

        self.wait(4)

class Quote_intro(Scene):

    def construct(self):

        text = TexMobject('Knowledge', '\\ is a pleasure,', 'while', '\\ curiosity', '\\ is the germination of', '\\ knowledge', '——\\ Francis\\ Bacon')
        text.set_color_by_tex_to_color_map({
            'Knowledge': BLUE,
            '\\ curiosity': YELLOW,
            '\\ knowledge': BLUE,
            '——\\ Francis\\ Bacon': RED,
        })

        text[0:2].to_corner(LEFT * 2 + UP * 1.6)
        text[2:6].next_to(text[0], DOWN).shift(RIGHT * 5.2)
        text[6].next_to(text[2], DOWN * 1.4).align_to(text[5], RIGHT)

        rect_y = Rectangle(color=YELLOW, height=3.6, width=5.4, stroke_width=6).to_corner(DOWN * 2.75 + LEFT * 2.25)
        rect_b = Rectangle(color=BLUE, height=3.6, width=5.4, stroke_width=6).to_corner(DOWN * 2.75 + RIGHT * 2.25)

        # self.play(Write(text), run_time=2.)
        self.play(FadeIn(text[0:2]))
        self.wait(0.1)
        self.play(FadeIn(text[2:6]))
        self.wait(0.2)
        self.play(Write(text[-1]))
        self.wait()
        self.play(ShowCreation(rect_y))

        self.wait(2.5)
        self.play(ShowCreation(rect_b))

        self.wait(5)

# class Rotate_test(Scene):
#
#     def construct(self):
#         center = Dot(color=GREEN)
#
#         circle = Circle().scale(2).shift(RIGHT * 2)
#         self.add(center, circle)
#         # def update_circle(c, dt):
#         #     circle.rotate(TAU/360, about_point=ORIGIN)
#         # circle.add_updater(update_circle)
#
#         circle.add_updater(lambda c, dt: c.rotate(TAU/360, about_point=ORIGIN))
#
#         self.wait(10)
