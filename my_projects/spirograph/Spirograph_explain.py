from manimlib.imports import *

class Gear_outline(VMobject):
    CONFIG = {
        'arc_segments': 4,
        'curve_segments': 6,
    }

    def __init__(self, pitch_circle_radius=2, tooth_hight=0.5, tooth_num=17, **kwargs):

        VMobject.__init__(self, **kwargs)
        self.pitch_circle_radius = pitch_circle_radius
        self.tooth_hight = tooth_hight
        self.tooth_num = tooth_num

        self.rb = self.pitch_circle_radius - self.tooth_hight/2
        self.pitch = self.pitch_circle_radius * 2 * PI / self.tooth_num
        theta_pitch = np.tan(np.arccos(self.rb/self.pitch_circle_radius)) - np.arccos(self.rb/self.pitch_circle_radius)
        theta_top = np.tan(np.arccos(self.rb/(self.rb + self.tooth_hight))) - np.arccos(self.rb/(self.rb + self.tooth_hight))
        alpha_max = np.arccos(self.rb/(self.rb + self.tooth_hight))


        alphas = np.linspace(0, alpha_max, self.curve_segments)
        curve01_radius = self.rb/np.cos(alphas)
        curve01_thetas = np.tan(alphas) - alphas - theta_pitch - TAU/self.tooth_num/2/2
        arc_top_thetas = np.linspace(theta_top - theta_pitch - TAU/self.tooth_num/2/2, -(theta_top - theta_pitch - TAU/self.tooth_num/2/2), self.arc_segments)
        curve02_radius = self.rb/np.cos(alphas)
        curve02_thetas = -curve01_thetas
        arc_bottom_thetas = np.linspace(theta_pitch + TAU/self.tooth_num/2/2, -(theta_pitch + TAU/self.tooth_num/2/2) + TAU/self.tooth_num, self.arc_segments)
        arc_top_radius = np.array([(self.rb + self.tooth_hight) for i in range(self.arc_segments)])
        arc_bottom_radius = np.array([self.rb for i in range(self.arc_segments)])
        part_01_thetas = np.concatenate((curve01_thetas, arc_top_thetas[1:-1], curve02_thetas[::-1], arc_bottom_thetas[1:-1]), axis=0)
        part_01_radius = np.concatenate((curve01_radius, arc_top_radius[1:-1], curve02_radius[::-1], arc_bottom_radius[1:-1]), axis=0)

        all_part_thetas = part_01_thetas
        all_part_radius = part_01_radius
        for i in range(1, self.tooth_num):
            all_part_thetas = np.concatenate((all_part_thetas, part_01_thetas + i * TAU/self.tooth_num), axis=0)
            all_part_radius = np.concatenate((all_part_radius, part_01_radius), axis=0)


        vertices = self.polar2xyz(all_part_radius, all_part_thetas)

        self.set_points_as_corners(
            [*vertices, vertices[0]]
        )

    def polar2xyz(self, r, theta):
        if type(theta) == np.ndarray:
            if type(r) == np.ndarray:

                return np.concatenate((np.cos(theta).reshape(-1, 1), np.sin(theta).reshape(-1, 1), theta.reshape(-1, 1) * 0), axis=1) * r.reshape(-1, 1)
            else:
                return np.concatenate((np.cos(theta).reshape(-1, 1), np.sin(theta).reshape(-1, 1), theta.reshape(-1, 1) * 0), axis=1) * r
        else:
            return np.array([np.cos(theta), np.sin(theta), 0]) * r

    def get_vertices(self):
        return self.get_start_anchors()

    def round_corners(self, radius=0.01):
        vertices = self.get_vertices()
        arcs = []
        for v1, v2, v3 in adjacent_n_tuples(vertices, 3):
            vect1 = v2 - v1
            vect2 = v3 - v2
            unit_vect1 = normalize(vect1)
            unit_vect2 = normalize(vect2)
            angle = angle_between_vectors(vect1, vect2)
            # Negative radius gives concave curves
            angle *= np.sign(radius)
            # Distance between vertex and start of the arc
            cut_off_length = radius * np.tan(angle / 2)
            # Determines counterclockwise vs. clockwise
            sign = np.sign(np.cross(vect1, vect2)[2])
            arc = ArcBetweenPoints(
                v2 - unit_vect1 * cut_off_length,
                v2 + unit_vect2 * cut_off_length,
                angle=sign * angle
            )
            arcs.append(arc)

        self.clear_points()
        # To ensure that we loop through starting with last
        arcs = [arcs[-1], *arcs[:-1]]
        for arc1, arc2 in adjacent_pairs(arcs):
            self.append_points(arc1.points)
            line = Line(arc1.get_end(), arc2.get_start())
            # Make sure anchors are evenly distributed
            len_ratio = line.get_length() / arc1.get_arc_length()
            line.insert_n_curves(
                int(arc1.get_num_curves() * len_ratio)
            )
            self.append_points(line.get_points())
        return self

class Spirograph(VGroup):

    CONFIG = {
        'radius_outer': 3.8,
        'radius_big': 3.5,
        'gear_color': [BLUE, YELLOW],
        'tooth_num_big': 59,
        'tooth_num_small': 29,
        'center_loc': LEFT * 3.,

        # 'dt': 1/25,
        'speed': TAU/360 * 2,
        'hole_radius': 0.09,
    }

    def __init__(self, **kwargs):

        VMobject.__init__(self, **kwargs)

        self.pitch = self.radius_big * 2 * PI / self.tooth_num_big
        self.tooth_hight = self.pitch * 0.6

        self.outer_circle = Circle(radius=self.radius_outer, fill_color=self.gear_color[0], fill_opacity=0.54, stroke_color=self.gear_color[0], stroke_width=2.25)
        self.outline_big = Gear_outline(pitch_circle_radius=self.radius_big, tooth_num=self.tooth_num_big, tooth_hight=self.tooth_hight,
                                        stroke_width=2.25, fill_opacity=1, fill_color=BLACK, stroke_color=self.gear_color[0])
        self.gear_big = VGroup(self.outer_circle, self.outline_big).move_to(self.center_loc)
        self.radius_small = self.pitch * self.tooth_num_small / 2 / PI
        self.outline_small = Gear_outline(pitch_circle_radius=self.radius_small, tooth_num=self.tooth_num_small, tooth_hight=self.tooth_hight,
                                          stroke_width=2.25, stroke_color=self.gear_color[1], fill_color=self.gear_color[1],
                                          fill_opacity=0.32).move_to(self.center_loc).shift(RIGHT * (self.radius_big-self.radius_small-0.01))

        self.hole_group = VGroup() # the tiny holes on the small gear
        # self.add_hole(ORIGIN)
        self.small_gear = VGroup(self.outline_small, self.hole_group)

        self.curves_group = VGroup() # put in the curves we wanna draw
        self.add(self.gear_big, self.small_gear, self.curves_group)

        self.small_gear_speed = -self.speed * self.tooth_num_big/self.tooth_num_small + self.speed

    def add_hole(self, loc, scale=1):

        hole = Circle(radius=self.hole_radius, color=self.gear_color[1], fill_color=BLACK, fill_opacity=1, stroke_width=1.8).scale(scale).move_to(self.outline_small.get_center() + loc)
        self.hole_group.add(hole)

    def add_hole_by_spiral(self, hole_num=13, min_radius=0.25, angle=PI * 3, delta_r=0.4):

        a, b = min_radius, np.log((self.radius_small-delta_r)/min_radius)/3/PI
        spiral_polar_r = lambda theta: a * np.exp(b * theta)
        theta = 0
        for i in range(hole_num):
            r = spiral_polar_r(theta)
            self.add_hole(r * (np.cos(theta) * RIGHT + np.sin(theta) * UP))
            theta += angle/(hole_num-1) * (1 + (5.5 - i) * 0.1)

    def add_hole_by_line(self, hole_num=7, delta_r=0.4):
        n = hole_num
        x = np.linspace(-(self.radius_small - delta_r), self.radius_small - delta_r, hole_num)

        for i in range(hole_num):
            self.add_hole(x[i] * RIGHT)

class SpirographScene(Scene):

    CONFIG = {
        'total_hight': 7.2,
        'tooth_num_big': 72,
        'tooth_num_small': 48,
        'ratio_str': '3/2',
        'gear_color': [BLUE, YELLOW],
        'spirograph_loc': LEFT * 2.75,
        'rotate_speed': TAU/360 * 0.75,
        'run_time': 12,
        'dt': 1/60,
        'curve_stroke': 3.2,
    }

    def construct(self):

        self.temp_dot = []
        self.color_list = color_gradient([RED, ORANGE, YELLOW, GREEN, BLUE, PINK, RED], 320)
        self.color_pointer = 0

        self.spirograph = Spirograph(radius_outer=self.total_hight/2, radius_big=self.total_hight/2-0.32, center_loc=self.spirograph_loc,
                                tooth_num_big=self.tooth_num_big, tooth_num_small=self.tooth_num_small, speed=self.rotate_speed,
                                gear_color=self.gear_color)

        self.add_holes()
        self.add(self.spirograph)
        self.wait(0.4)
        self.add_parameter_info()
        self.start_draw()

    def add_holes(self):
        self.spirograph.hole_radius = 0.064
        self.spirograph.add_hole_by_line(hole_num=12, delta_r=0.275)

    def start_draw(self):
        self.spirograph.add_updater(self.draw_all_hole)
        self.wait(self.run_time)


    def draw_last_hole(self, spirograph, dt=1/60):
        dt=self.dt
        w1 = spirograph.speed
        R = np.array([[np.cos(-w1), -np.sin(-w1), 0],
                      [np.sin(-w1), np.cos(-w1), 0],
                      [0, 0, 1]])
        loc = spirograph.outline_small.get_center()
        loc_new = np.dot(loc-spirograph.center_loc, R) + spirograph.center_loc
        spirograph.small_gear.shift(loc_new-spirograph.outline_small.get_center())
        spirograph.small_gear.rotate(spirograph.small_gear_speed, about_point=spirograph.outline_small.get_center())

        self.temp_dot.append(spirograph.hole_group[-1].get_center())
        if len(self.temp_dot) > 2:
            self.temp_dot.remove(self.temp_dot[0])
        if len(self.temp_dot) == 2:
            spirograph.curves_group.add(Line(self.temp_dot[-1], self.temp_dot[-2], stroke_width=self.curve_stroke, color=self.color_list[int(self.color_pointer/20)%len(self.color_list)]))
        # self.add(Dot(spirograph.hole_group[-1].get_center()).scale(0.4).set_color(self.color_list[int(self.color_pointer/8)%len(self.color_list)]))
        self.color_pointer += 1

    def draw_all_hole(self, spirograph, dt=1/60):
        dt=self.dt
        w1 = spirograph.speed
        R = np.array([[np.cos(-w1), -np.sin(-w1), 0],
                      [np.sin(-w1), np.cos(-w1), 0],
                      [0, 0, 1]])
        loc = spirograph.outline_small.get_center()
        loc_new = np.dot(loc-spirograph.center_loc, R) + spirograph.center_loc
        spirograph.small_gear.shift(loc_new-spirograph.outline_small.get_center())
        spirograph.small_gear.rotate(spirograph.small_gear_speed, about_point=spirograph.outline_small.get_center())

        if self.temp_dot == []:
            self.temp_dot = [[] for i in range(len(spirograph.hole_group))]

        n = len(spirograph.hole_group)
        for i in range(n):
            self.temp_dot[i].append(spirograph.hole_group[i].get_center())
            if len(self.temp_dot[i]) > 2:
                self.temp_dot[i].remove(self.temp_dot[i][0])
            if len(self.temp_dot[i]) == 2:
                spirograph.curves_group.add(Line(self.temp_dot[i][-1], self.temp_dot[i][-2], stroke_width=self.curve_stroke, color=self.color_list[int(i/n * len(self.color_list))]))

        #         spirograph.curves_group.add(Line(self.temp_dot[i][-1], self.temp_dot[i][-2], stroke_width=2.4, color=self.color_list[int(self.color_pointer/20)%len(self.color_list)]))
        # self.color_pointer += 1

    def add_parameter_info(self):

        text_big_num = Text('定轮齿数：', font='新蒂小丸子体', color=self.gear_color[0]).scale(0.64).to_corner(UP * 2 + LEFT * 18)
        text_small_num = Text('动轮齿数：', font='新蒂小丸子体', color=self.gear_color[1]).scale(0.64).to_corner(UP * 4.5 + LEFT * 18)
        text_ratio = Text('齿数比：', font='新蒂小丸子体', color=average_color(*self.gear_color)).scale(0.64).to_corner(UP * 7 + LEFT * 18)
        big_num = Text('%d' % self.tooth_num_big, font='新蒂小丸子体', color=self.gear_color[0]).scale(0.64).next_to(text_big_num, RIGHT * 1.5)
        small_num = Text('%d' % self.tooth_num_small, font='新蒂小丸子体', color=self.gear_color[1]).scale(0.64).next_to(text_small_num, RIGHT * 1.5).align_to(big_num, LEFT)
        ratio = Text(self.ratio_str, font='新蒂小丸子体', color=average_color(*self.gear_color)).scale(0.64).next_to(text_ratio, RIGHT * 1.5)
        self.add(text_big_num, text_small_num)
        self.wait(0.2)
        self.play(FadeIn(big_num))
        self.play(FadeIn(small_num))
        self.wait(0.2)
        self.play(FadeIn(text_ratio), FadeIn(ratio), run_time=1.25)
        self.wait(0.5)

class Spirograph_explain(SpirographScene):

    CONFIG = {
        'tooth_num_big': 60,
        'tooth_num_small': 24,
        'ratio_str': '5/2',
        'rotate_speed': TAU/360 * 1.,
        'run_time': 18,
    }

    def construct(self):

        self.temp_dot = []
        self.color_list = color_gradient([RED, ORANGE, YELLOW, GREEN, BLUE, PINK, RED], 320)
        self.color_pointer = 0

        self.spirograph = Spirograph(radius_outer=self.total_hight/2 * 1.0, radius_big=self.total_hight/2-0.32, center_loc=self.spirograph_loc,
                                tooth_num_big=self.tooth_num_big, tooth_num_small=self.tooth_num_small, speed=self.rotate_speed,
                                gear_color=self.gear_color)

        self.spirograph.add_hole(RIGHT * 1.)

        self.pitch_big = Circle(radius=self.spirograph.radius_big, color=BLUE, stroke_width=3, fill_opacity=0).move_to(self.spirograph.outline_big.get_center())
        self.pitch_small = Circle(radius=self.spirograph.radius_small, color=YELLOW, stroke_width=3, fill_opacity=0).move_to(self.spirograph.outline_small.get_center())
        self.center_trace = Circle(radius=self.spirograph.radius_big-self.spirograph.radius_small, color=GREEN, stroke_width=2, fill_opacity=0).move_to(self.spirograph.outline_big.get_center())
        center = Dot(color=YELLOW).scale(1.2).move_to(self.pitch_small.get_center())
        arrow = VGroup(Arrow(self.spirograph.outer_circle.get_center(), self.spirograph.outline_small.get_center(), buff=0, color=GREEN),
                       Arrow(self.spirograph.outline_small.get_center(), self.spirograph.hole_group[-1].get_center(), buff=0, color=YELLOW))

        origin_dot = Dot(color=GREEN).scale(1.2).move_to(self.spirograph.outer_circle.get_center())
        def update_arrow(arr):
            arr.remove(arr[0])
            arr.remove(arr[0])
            arr.add(Arrow(self.spirograph.outer_circle.get_center(), self.spirograph.outline_small.get_center(), buff=0, color=GREEN),
                       Arrow(self.spirograph.outline_small.get_center(), self.spirograph.hole_group[-1].get_center(), buff=0, color=YELLOW))

        self.add(self.spirograph)
        self.wait(0.4)

        self.add_parameter_info()

        self.spirograph.add_updater(self.draw_last_hole)
        self.pitch_small.add_updater(lambda s: s.move_to(self.spirograph.outline_small.get_center()))
        center.add_updater(lambda c:c.move_to(self.spirograph.outline_small.get_center()))
        arrow.add_updater(update_arrow)
        self.wait(12)
        self.spirograph.remove_updater(self.draw_last_hole)
        # self.spirograph.outline_small.set_stroke()
        self.play(ShowCreation(self.pitch_big), ApplyMethod(self.spirograph.outer_circle.set_opacity, 0.2),
                  ApplyMethod(self.spirograph.outline_big.set_stroke, BLUE, 1.6, 0.2), run_time=1.6)
        self.play(ApplyMethod(self.spirograph.outline_small.set_opacity, 0.2), #ApplyMethod(self.spirograph.outline_small.set_stroke, opacity=0.2),
                  ShowCreation(self.pitch_small), run_time=1.6)
        self.wait(0.2)
        self.play(ShowCreation(self.center_trace), ShowCreation(center))
        self.wait(0.2)
        self.play(ShowCreation(arrow), ShowCreation(origin_dot))
        self.spirograph.add_updater(self.draw_last_hole)

        self.wait(12)

class Dashed_Circle(VGroup):

    CONFIG = {
        'arc_ratio': 0.6,
        'arc_num': 36,
        'arc_config':{
            'color': WHITE,
            'stroke_width': 2.5,
        },
    }

    def __init__(self, radius=1, center=ORIGIN, **kwargs):
        VGroup.__init__(self, **kwargs)
        theta = TAU/self.arc_num
        for i in range(self.arc_num):
            arc_i = Arc(radius=radius, angle=theta * self.arc_ratio, **self.arc_config)
            arc_i.rotate(theta * i, about_point=ORIGIN)
            self.add(arc_i)
        self.move_to(center)

class Before_Derivation(Scene):

    CONFIG = {
        'R': 3.6,
        'r': 3.6 * 2/5,
        'd': 3.6 * 2/5 * 0.6,
        'center': LEFT * 3,
        # 'R': 1.5 * 3.6,
        # 'r': 1.5 * 3.6 * 2/5,
        # 'd': 1.5 * 3.6 * 2/5 * 0.6,
        # 'center': LEFT * 4 + DOWN * 1.5,
        'defaul_font': '新蒂小丸子体',
    }

    def construct(self):

        self.theta = 0 * DEGREES

        center_b = Dot(color=BLUE).scale(1.25).move_to(self.center)
        center_y = Dot(color=YELLOW).move_to(self.center + RIGHT * (self.R - self.r))

        big_circle = Circle(radius=self.R, color=BLUE).move_to(self.center)
        small_circle = Circle(radius=self.r, color=YELLOW).move_to(self.center).shift(RIGHT * (self.R - self.r))
        dash_circle = Dashed_Circle(radius=self.d, center=self.center + RIGHT * (self.R - self.r)).set_color(YELLOW)

        vector_b = Arrow(self.center, self.center + RIGHT * (self.R - self.r), color=BLUE, buff=0)

        vector_y = Arrow(self.center + RIGHT * (self.R - self.r), self.center + RIGHT * (self.R - self.r + self.d), color=YELLOW, buff=0)
        line_y = Line(self.center + RIGHT * (self.R - self.r), self.center + RIGHT * self.R, color=YELLOW, buff=0, stroke_width=2.5)
        line_b = DashedLine(self.center, self.center + self.R * RIGHT, dash_length=0.12, positive_space_ratio=0.64).set_stroke(opacity=0)
        # self.add(self.big_circle, self.small_circle, self.dash_circle, self.vector_y, self.vector_b, self.line_y)

        self.blue_group = VGroup(center_b, big_circle, line_b, vector_b)
        self.yellow_group = VGroup(center_y, small_circle, dash_circle, line_y, vector_y)
        self.add(self.blue_group, self.yellow_group)

        # arc_01 = Arc(color=PINK, stroke_width=20)
        # arc_02 = Arc(color=ORANGE, stroke_width=20)
        # arc_opacity=0.8

        # def arc_updater_01(a1, dt):
        #     a1.become(Arc(arc_center=self.center, radius=self.R, angle=self.blue_group[-1].get_angle(),
        #                   color=PINK, stroke_width=20).set_stroke(opacity=arc_opacity))
        #
        # def arc_updater_02(a2, dt):
        #     a2.become(Arc(arc_center=self.yellow_group[0].get_center(), radius=self.r, start_angle=self.blue_group[-1].get_angle(),
        #                   angle=self.yellow_group[-1].get_angle() - self.blue_group[-1].get_angle(), color=ORANGE, stroke_width=20).set_stroke(opacity=arc_opacity))

        def yellow_updater(y_group, dt):
            y_group.rotate(self.theta, about_point=self.center)
            y_group.rotate(-self.R * self.theta/self.r, about_point=y_group[0].get_center())

        def blue_updater(b_group, dt):
            b_group.rotate(self.theta, about_point=self.center)

        self.yellow_group.add_updater(yellow_updater)
        self.blue_group.add_updater(blue_updater)
        # arc_01.add_updater(arc_updater_01)
        # arc_02.add_updater(arc_updater_02)
        # self.add(arc_01, arc_02)
        self.before_scale = VGroup(self.blue_group, self.yellow_group)

        self.wait(1)
        text_00 = Text('黄色动圆在蓝色定圆上做纯滚动', font=self.defaul_font).set_height(0.32)
        text_00.set_color_by_t2c({'黄色动圆': YELLOW, '蓝色定圆': BLUE})
        text_00.to_corner(RIGHT * 1.25 + UP * 1.25)
        self.play(Write(text_00), run_time=3)

        theta_tatal = 720 * DEGREES
        step = 360
        self.theta = theta_tatal/step
        self.wait(step/30 * 2)
        self.theta=0

        self.wait(1)

class Derivation(Scene):

    CONFIG = {
        'R': 3.6,
        'r': 3.6 * 2/5,
        'd': 3.6 * 2/5 * 0.6,
        'center': LEFT * 3,
        # 'R': 1.5 * 3.6,
        # 'r': 1.5 * 3.6 * 2/5,
        # 'd': 1.5 * 3.6 * 2/5 * 0.6,
        # 'center': LEFT * 4 + DOWN * 1.5,
        'defaul_font': '新蒂小丸子体',
    }

    def construct(self):

        self.theta = 0 * DEGREES

        center_b = Dot(color=BLUE).scale(1.25).move_to(self.center)
        center_y = Dot(color=YELLOW).move_to(self.center + RIGHT * (self.R - self.r))

        big_circle = Circle(radius=self.R, color=BLUE).move_to(self.center)
        small_circle = Circle(radius=self.r, color=YELLOW).move_to(self.center).shift(RIGHT * (self.R - self.r))
        dash_circle = Dashed_Circle(radius=self.d, center=self.center + RIGHT * (self.R - self.r)).set_color(YELLOW)

        vector_b = Arrow(self.center, self.center + RIGHT * (self.R - self.r), color=BLUE, buff=0)

        vector_y = Arrow(self.center + RIGHT * (self.R - self.r), self.center + RIGHT * (self.R - self.r + self.d), color=YELLOW, buff=0)
        line_y = Line(self.center + RIGHT * (self.R - self.r), self.center + RIGHT * self.R, color=YELLOW, buff=0, stroke_width=2.5)
        line_b = DashedLine(self.center, self.center + self.R * RIGHT, dash_length=0.12, positive_space_ratio=0.64).set_stroke(opacity=0)
        # self.add(self.big_circle, self.small_circle, self.dash_circle, self.vector_y, self.vector_b, self.line_y)

        self.blue_group = VGroup(center_b, big_circle, line_b, vector_b)
        self.yellow_group = VGroup(center_y, small_circle, dash_circle, line_y, vector_y)
        self.add(self.blue_group, self.yellow_group)

        arc_01 = Arc(color=PINK, stroke_width=20)
        arc_02 = Arc(color=ORANGE, stroke_width=20)
        arc_opacity=0.8

        def arc_updater_01(a1, dt):
            a1.become(Arc(arc_center=self.center, radius=self.R, angle=self.blue_group[-1].get_angle(),
                          color=PINK, stroke_width=20).set_stroke(opacity=arc_opacity))

        def arc_updater_02(a2, dt):
            a2.become(Arc(arc_center=self.yellow_group[0].get_center(), radius=self.r, start_angle=self.blue_group[-1].get_angle(),
                          angle=self.yellow_group[-1].get_angle() - self.blue_group[-1].get_angle(), color=ORANGE, stroke_width=20).set_stroke(opacity=arc_opacity))

        def yellow_updater(y_group, dt):
            y_group.rotate(self.theta, about_point=self.center)
            y_group.rotate(-self.R * self.theta/self.r, about_point=y_group[0].get_center())

        def blue_updater(b_group, dt):
            b_group.rotate(self.theta, about_point=self.center)

        self.yellow_group.add_updater(yellow_updater)
        self.blue_group.add_updater(blue_updater)
        arc_01.add_updater(arc_updater_01)
        arc_02.add_updater(arc_updater_02)
        self.add(arc_01, arc_02)

        self.before_scale = VGroup(self.blue_group, self.yellow_group, arc_01, arc_02)

        self.wait(1)
        text_00 = Text('黄色动圆在蓝色定圆上做纯滚动', font=self.defaul_font).scale(0.4)
        text_00.set_color_by_t2c({'黄色动圆': YELLOW, '蓝色定圆': BLUE})
        text_00.to_corner(RIGHT * 1.25 + UP * 1.25)
        self.play(Write(text_00), run_time=3)
        self.wait(0.5)

        theta_tatal = 45 * DEGREES
        step = 120 * 2 #
        self.theta = theta_tatal/step
        self.wait(step/60)
        self.theta=0

        self.wait(1)

        text_01 = Text('所以：', font=self.defaul_font, color=WHITE).scale(0.4)
        text_01.to_corner(UP * 2.75).align_to(text_00, LEFT)
        self.play(Write(text_01), run_time=1)
        self.wait(0.5)

        text_02 = Text('橙色弧长 = 紫色弧长', font=self.defaul_font, color=WHITE).scale(0.4)
        text_02.set_color_by_t2c({'橙色弧长': ORANGE, '紫色弧长': PINK})
        text_02.next_to(text_01, RIGHT)
        text_h = text_01.get_height()
        self.play(Write(text_02))

        self.play(ApplyMethod(self.blue_group[-2].set_stroke, BLUE, 3, 1), run_time=1.6)
        self.wait(1)
        arc_01.clear_updaters(), arc_02.clear_updaters()

        ## scale and add annotations ##
        s = 1.75
        self.play(ApplyMethod(self.before_scale.scale_about_point, s, self.center + UP * 3.6 + RIGHT * 4.25), run_time=2)

        center_blue = self.blue_group[0].get_center()
        center_yellow = self.yellow_group[0].get_center()
        # line_R = DashedLine(center_blue, center_blue + self.R * RIGHT * s, dash_length=0.12, positive_space_ratio=0.64, stroke_width=3, color=PINK)
        vector_R = Arrow(center_blue, center_blue + self.R * RIGHT * s, buff=0, color=PINK)
        vector_r = Arrow(center_yellow, center_yellow + self.r * RIGHT * s, color=ORANGE, buff=0)

        arc_blue_01 = Arc(arc_center=center_blue, radius=0.6, angle=45*DEGREES, color=BLUE, stroke_width=8)
        arc_blue_01_2 = Arc(arc_center=center_blue, radius=0.3, angle=45*DEGREES, color=BLUE, stroke_width=60, stroke_opacity=0.4)
        arc_blue_02 = Arc(arc_center=center_yellow, radius=0.6, angle=45*DEGREES, color=BLUE, stroke_width=8)
        arc_blue_02_2 = Arc(arc_center=center_yellow, radius=0.3, angle=45*DEGREES, color=BLUE, stroke_width=60, stroke_opacity=0.4)
        arc_yellow = Arc(arc_center=center_yellow, radius=0.6, angle=self.yellow_group[-1].get_angle(), stroke_width=8, color=YELLOW)
        arc_yellow_2 = Arc(arc_center=center_yellow, radius=0.3, angle=self.yellow_group[-1].get_angle(), stroke_width=60, stroke_opacity=0.4, color=YELLOW)

        arc_orange = Arc(arc_center=center_yellow, radius=0.8, color=ORANGE, start_angle=self.blue_group[-1].get_angle(), # fill_color=BLUE, fill_opacity=0.25
                         angle=-self.blue_group[-1].get_angle()+self.yellow_group[-1].get_angle(), stroke_width=10)
        arc_orange_2 = Arc(arc_center=center_yellow, radius=0.4, color=ORANGE, start_angle=self.blue_group[-1].get_angle(), # fill_color=BLUE, fill_opacity=0.25
                         angle=-self.blue_group[-1].get_angle()+self.yellow_group[-1].get_angle(), stroke_opacity=0.4, stroke_width=80)

        angle_blue_1 = VGroup(arc_blue_01, arc_blue_01_2)
        angle_blue_2 = VGroup(arc_blue_02, arc_blue_02_2)
        angle_yellow = VGroup(arc_yellow, arc_yellow_2)
        angle_orange = VGroup(arc_orange, arc_orange_2)

        text_R = TexMobject('R', color=PINK).set_height(0.5).next_to(vector_R, DOWN * 0.01).shift(RIGHT * 2.25)
        text_r = TexMobject('r', color=ORANGE).set_height(0.4).next_to(vector_r, DOWN * 0.01).shift(RIGHT * 0.6)
        text_d = TexMobject('d', color=YELLOW).set_height(0.35).next_to(vector_y, LEFT * 0.4).shift(RIGHT * 0.24 + DOWN * 0.1)
        text_Rr = TexMobject('R-r', color=BLUE).set_height(0.4).rotate(vector_b.get_angle()).move_to(vector_b).shift(UP * 0.24 + LEFT * 0.24)


        formula_01 = TexMobject('\\Rightarrow\\,', '\\theta_{\\text{橙}}', '\\times', 'r', '=', '\\theta_{\\text{蓝}}', '\\times', 'R')
        scale_factor = 0.9 # text_h * 1.2/formula_01.get_height()
        formula_01.scale(scale_factor).to_corner(UP * 4.5).align_to(text_01, LEFT).shift(RIGHT * 0.5)
        formula_01.set_color_by_tex_to_color_map({
            '\\theta_{\\text{橙}}': ORANGE, 'r': ORANGE, '\\theta_{\\text{蓝}}': BLUE, 'R': PINK,
        })

        formula_02 = TexMobject('\\Rightarrow\\,', '\\theta_{\\text{橙}}', '=', '\\theta_{\\text{蓝}}', '\\times', '{R', '\\over', 'r')
        formula_02.scale(scale_factor).next_to(formula_01, DOWN * 1.1).align_to(text_01, LEFT).shift(RIGHT * 0.5)
        formula_02.set_color_by_tex_to_color_map({
            '\\theta_{\\text{橙}}': ORANGE, 'r': ORANGE, '\\theta_{\\text{蓝}}': BLUE, 'R': PINK, '\\over':WHITE,
        })

        formula_03 = TexMobject('\\Rightarrow\\,', '\\theta_{\\text{蓝}}', '\\times', '{R', '\\over', 'r}', '=', '\\theta_{\\text{橙}}', '=', '\\theta_{\\text{蓝}}', '+', '\\theta_{\\text{黄}}')
        formula_03.scale(scale_factor).next_to(formula_02, DOWN * 0.5).align_to(text_01, LEFT).shift(RIGHT * 0.5)
        formula_03.set_color_by_tex_to_color_map({
            '\\theta_{\\text{橙}}': ORANGE, 'r': ORANGE, '\\theta_{\\text{蓝}}': BLUE, 'R': PINK, '\\theta_{\\text{黄}}': YELLOW, '\\over':WHITE,
        })

        formula_04 = TexMobject('\\Rightarrow\\,', '\\theta_{\\text{黄}}', '=', '{R', '-', 'r', '\\over', 'r}', '\\theta_{\\text{蓝}}')
        formula_04.scale(scale_factor).next_to(formula_03, DOWN * 0.55).align_to(text_01, LEFT).shift(RIGHT * 0.5)
        formula_04.set_color_by_tex_to_color_map({
            '\\theta_{\\text{橙}}': ORANGE, 'r': ORANGE, '\\theta_{\\text{蓝}}': BLUE, 'R': PINK, '\\theta_{\\text{黄}}': YELLOW, '\\over':WHITE,
        })

        formula_01[0].set_color(WHITE), formula_02[0].set_color(WHITE), formula_03[0].set_color(WHITE), formula_04[0].set_color(WHITE)

        self.play(ShowCreation(vector_R))
        self.play(ShowCreation(vector_r))
        self.play(ShowCreation(text_R), ShowCreation(text_r), ShowCreation(text_d), ShowCreation(text_Rr))
        self.wait(0.2)
        self.play(ShowCreation(angle_blue_1), ShowCreation(angle_orange))

        self.wait()
        self.play(Write(formula_01[0]))
        self.wait(0.2)
        self.play(TransformFromCopy(arc_02, formula_01[1:4]))
        self.wait(0.4)
        self.play(Write(formula_01[4]))
        self.play(TransformFromCopy(arc_01, formula_01[5:8]))

        self.wait(1.5)
        self.play(TransformFromCopy(formula_01, formula_02), run_time=2)

        self.wait(2)
        self.play(Write(formula_03[0:7]), run_time=2)
        self.wait(0.25)
        self.play(TransformFromCopy(angle_orange[0], formula_03[7]), run_time=1.6)
        self.wait(0.25)
        self.play(Write(formula_03[8]), run_time=0.5)
        yellow_blue = VGroup(angle_blue_2, angle_yellow)
        self.play(ReplacementTransform(angle_orange, yellow_blue), run_time=1.2)
        self.wait(0.8)
        self.play(TransformFromCopy(VGroup(yellow_blue[0][0], yellow_blue[1][0]), formula_03[9:12]), run_time=1.6)
        self.wait(2)

        self.play(TransformFromCopy(formula_03, formula_04), run_time=2)
        self.wait(1)
        rect_g = SurroundingRectangle(formula_04[2:], color=GREEN)
        self.play(ShowCreation(rect_g), run_time=2)

        self.wait(5)

class Derivation_02(Scene):

    CONFIG = {
        'R': 3.5,
        'r': 3.5 * 2/5,
        'd': 3.5 * 2/5 * 0.95,
        # 'center': LEFT * 3,
        'defaul_font': '新蒂小丸子体',
    }

    def construct(self):

        text_01 = Text('蓝色向量和黄色向量的转角关系为（负号代表方向相反）：', font=self.defaul_font).set_height(0.5).to_corner(UP * 1.2 + LEFT * 1.2)
        text_01.set_color_by_t2c({'蓝色向量': BLUE, '黄色向量': YELLOW, '（负号代表方向相反）': RED})
        text_02 = Text('所以，两个向量可以表示为如下：', font=self.defaul_font).set_height(0.5).to_corner(UP * 5.2 + LEFT * 1.25)

        formula_01 = TexMobject('\\theta_{\\text{黄}}', '=', '-', '{R', '-', 'r', '\\over', 'r}', '\\theta_{\\text{蓝}}')
        formula_01.scale(1).next_to(text_01, DOWN * 1.).align_to(text_01, LEFT).shift(RIGHT * 0.8)
        formula_01.set_color_by_tex_to_color_map({
            '\\theta_{\\text{橙}}': ORANGE, 'r': ORANGE, '\\theta_{\\text{蓝}}': BLUE, 'R': PINK, '\\theta_{\\text{黄}}': YELLOW, '\\over':WHITE,
        })
        formula_01[2].set_color(RED)

        color_dict = {'R': PINK, 'd': YELLOW, 'r': ORANGE, '\\theta': BLUE, '\\over': WHITE}

        vect_b_x = TexMobject('x', '=', '(', 'R', '-', 'r', ')', '\\cos{', '\\theta}').scale(0.8)
        vect_b_y = TexMobject('y', '=', '(', 'R', '-', 'r', ')', '\\sin{', '\\theta}').scale(0.8).next_to(vect_b_x, DOWN * 0.8).align_to(vect_b_x, LEFT)
        vect_b_x.set_color_by_tex_to_color_map(color_dict)
        vect_b_y.set_color_by_tex_to_color_map(color_dict)

        formula_vect_b = VGroup(vect_b_x, vect_b_y)
        brace_b = Brace(formula_vect_b, LEFT)

        vect_y_x = TexMobject('x', '=', 'd', '\\cos{(', '{R', '-', 'r', '\\over', 'r}', '\\theta', ')}').scale(0.8)
        vect_y_y = TexMobject('y', '=', '-', 'd', '\\sin{(', '{R', '-', 'r', '\\over', 'r}', '\\theta', ')}').scale(0.8).next_to(vect_y_x, DOWN * 1.25).align_to(vect_y_x, LEFT)
        vect_y_x.set_color_by_tex_to_color_map(color_dict)
        vect_y_y.set_color_by_tex_to_color_map(color_dict)
        formula_vect_y = VGroup(vect_y_x, vect_y_y)
        brace_y = Brace(formula_vect_y, LEFT).scale(UP * 0.8 + RIGHT)

        formula_blue = VGroup(formula_vect_b, brace_b)
        formula_yellow = VGroup(formula_vect_y, brace_y)

        ## vectors
        dot_b = Dot(color=BLUE).scale(1.2)
        vector_b = Arrow(ORIGIN, self.R * (RIGHT * np.sqrt(2)/2 + UP * np.sqrt(2)/2), color=BLUE, buff=0)
        arc_b_01 = Arc(radius=0.6, angle=PI/4, color=BLUE, stroke_width=8)
        arc_b_02 = Arc(radius=0.3, angle=PI/4, color=BLUE, stroke_width=60, stroke_opacity=0.4)
        dash_b = DashedLine(ORIGIN, RIGHT * 2.5, color=BLUE, stroke_width=2.5, dash_length=0.12, positive_space_ratio=0.64)
        tex_Rr = TexMobject('R-r', color=BLUE).scale(0.8).rotate(PI/4).move_to(vector_b).shift((UP + LEFT) * 0.2 + (UP + RIGHT) * 0.2)
        tex_theta_b = TexMobject('\\theta_{\\text{蓝}}', '=', '\\theta').scale(0.8).next_to(arc_b_01, RIGHT * 0.2).shift(UP * 0.12)
        tex_theta_b[0].set_color(BLUE), tex_theta_b[-1].set_color(BLUE)
        group_b = VGroup(dot_b, vector_b, arc_b_01, arc_b_02, dash_b, tex_Rr, tex_theta_b).to_corner(LEFT * 2.5 + UP * 6.7)

        dot_y = Dot(color=YELLOW).scale(1.2)
        theta_y = -(self.R - self.r)/self.r * PI/4
        vector_y = Arrow(ORIGIN, self.d * (RIGHT * np.cos(theta_y) + UP * np.sin(theta_y)), color=YELLOW, buff=0)
        arc_y_01 = Arc(radius=0.6, angle=theta_y, color=YELLOW, stroke_width=8)
        arc_y_02 = Arc(radius=0.3, angle=theta_y, color=YELLOW, stroke_width=60, stroke_opacity=0.4)
        dash_y = DashedLine(ORIGIN, RIGHT * 2., color=YELLOW, stroke_width=2.5, dash_length=0.12, positive_space_ratio=0.64)
        tex_d = TexMobject('d', color=YELLOW).scale(0.75).next_to(vector_y, LEFT * 0.01).shift(RIGHT * 0.1 + DOWN * 0.25)
        tex_theta_y = TexMobject('\\theta_{\\text{黄}}', '=', '-', '{R', '-', 'r', '\\over', 'r}', '\\theta')\
            .scale(0.65).next_to(arc_y_01, RIGHT * 0.2).shift(DOWN * 0.24)
        tex_theta_y.set_color_by_tex_to_color_map(color_dict)
        tex_theta_y[0].set_color(YELLOW), tex_theta_y[-1].set_color(BLUE)

        group_y = VGroup(dot_y, vector_y, arc_y_01, arc_y_02, dash_y, tex_d, tex_theta_y).to_corner(RIGHT * 6.5 + UP * 7.6)

        self.play(Write(text_01), run_time=2)
        self.wait(0.25)
        self.play(Write(formula_01), run_time=1.8)
        self.wait(1.6)

        ##

        self.play(Write(text_02))
        self.wait(0.4)
        self.play(FadeIn(group_b), run_time=1.25)
        self.wait(0.5)

        formula_blue.next_to(group_b, DOWN * 0.75).align_to(formula_01, LEFT)
        formula_yellow.next_to(group_y, DOWN * 0.75)
        self.play(ShowCreation(formula_blue), run_time=1.8)
        self.wait(0.5)

        self.play(FadeIn(group_y), run_time=1.25)
        self.wait(0.5)
        self.play(ShowCreation(formula_yellow), run_time=1.8)
        self.wait(2.5)

        # add vector
        text_03 = Text('将两个旋转向量相加就得到了所需要的内旋轮线参数方程', font=self.defaul_font).set_height(0.56).to_corner(UP * 1.2 + LEFT * 1.2)
        #text_03.set_color_by_t2c('内旋轮线参数方程': PINK)
        self.play(FadeOut(text_01), FadeOut(formula_01), FadeOut(text_02))
        self.play(Write(text_03), run_time=2)
        self.wait(0.25)

        x_text = TexMobject('x', '=', '(', 'R', '-', 'r', ')', '\\cos{', '\\theta}', '+',
                            'd', '\\cos{(', '{R', '-', 'r', '\\over', 'r}', '\\theta', ')}')
        y_text = TexMobject('y', '=', '(', 'R', '-', 'r', ')', '\\sin{', '\\theta}', '-',
                            'd', '\\sin{(', '{R', '-', 'r', '\\over', 'r}', '\\theta', ')}')
        x_text.set_color_by_tex_to_color_map(color_dict)
        y_text.set_color_by_tex_to_color_map(color_dict)
        y_text.next_to(x_text, DOWN * 1.2).align_to(x_text, LEFT)

        para_func = VGroup(x_text, y_text)
        brace_pf = Brace(para_func, LEFT).scale(np.array([1, 0.72, 0])).shift(DOWN * 0.072)

        para_function = VGroup(para_func, brace_pf).to_corner(DOWN * 1.8 + LEFT * 2)

        junction_point = 2.4 * UP + 1 * LEFT
        self.play(ApplyMethod(group_y.shift, junction_point - dot_y.get_center()),
                  ApplyMethod(group_b.shift, junction_point - vector_b.get_end()), run_time=1.8)
        self.wait(0.2)
        self.play(ReplacementTransform(vect_b_x, x_text[0:9]),
                  ReplacementTransform(vect_b_y, y_text[0:9]),
                  ReplacementTransform(vect_y_x[2:], x_text[9:]),
                  ReplacementTransform(vect_y_y[2:], y_text[9:]),
                  FadeOut(brace_b), FadeOut(brace_y), FadeOut(vect_y_x[0:2]), FadeOut(vect_y_y[0:2]),
                  run_time=2.5)
        self.play(ShowCreation(brace_pf), run_time=1.5)
        self.wait(0.25)
        self.play(ApplyMethod(para_function.shift, RIGHT * 2.25), run_time=1.75)
        self.wait(0.5)
        self.play(ShowCreation(SurroundingRectangle(para_function, color=GREEN)), run_time=1.8)

        self.wait(5)

class Complex_form(Scene):

    CONFIG = {
        'defaul_font': '新蒂小丸子体',
    }

    def construct(self):
        color_dict_01 = {'R': PINK, 'd': YELLOW, 'r': ORANGE, '\\theta': BLUE, '\\over': WHITE,}

        color_dict = {'R': PINK, 'd': YELLOW, 'r': ORANGE, '\\theta': BLUE, '\\over': WHITE,
                      't': BLUE, 'e': GREEN, 'i': RED, '\\sin': WHITE, '\\cos': WHITE}
        x_text = TexMobject('x', '=', '(', 'R', '-', 'r', ')', '\\cos{', '\\theta}', '+',
                            'd', '\\cos{(', '{R', '-', 'r', '\\over', 'r}', '\\theta', ')}').scale(1.1)
        y_text = TexMobject('y', '=', '(', 'R', '-', 'r', ')', '\\sin{', '\\theta}', '-',
                            'd', '\\sin{(', '{R', '-', 'r', '\\over', 'r}', '\\theta', ')}').scale(1.1)
        x_text.set_color_by_tex_to_color_map(color_dict_01)
        y_text.set_color_by_tex_to_color_map(color_dict_01)
        y_text.next_to(x_text, DOWN * 0.9).align_to(x_text, LEFT)

        para_func = VGroup(x_text, y_text)
        brace_pf = Brace(para_func, LEFT).scale(np.array([1, 0.72, 0])).shift(DOWN * 0.072)
        para_function = VGroup(para_func, brace_pf).to_corner(UP * 2.6 + LEFT * 2.25)

        text_01 = Text('内旋轮线参数方程：', font=self.defaul_font).set_height(0.56).to_corner(LEFT * 1.5 + UP * 1.25)
        text_02 = Text('通过欧拉公式我们很容易得出其复数形式：', font=self.defaul_font).set_height(0.56).to_corner(LEFT * 1.5 + UP * 8.4)
        text_01.set_color_by_t2c({'参数方程': ORANGE})
        text_02.set_color_by_t2c({'欧拉公式': BLUE, '复数形式': PINK})

        complex_form = TexMobject('f(', 't', ')=', 'x(', 't', ')', '+', 'y(', 't', ')', 'i', '=', '(', 'R', '-', 'r', ')',
                                  'e^{', 't', 'i}', '+', 'd', 'e^{', '-', '{R', '-', 'r', '\\over', 'r}', 't', 'i}').scale(1.2)
        complex_form.set_color_by_tex_to_color_map(color_dict)
        complex_form.to_corner(LEFT * 2.25 + UP * 10.2)

        self.play(Write(text_01), run_time=1.5)
        self.wait(0.5)
        self.play(ShowCreation(para_function), run_time=3.2)
        self.wait(4)
        self.play(Write(text_02), run_time=2.4)
        self.wait(1.8)
        self.play(Write(complex_form), run_time=3)
        self.wait()
        self.play(ShowCreation(SurroundingRectangle(complex_form[12:], color=GREEN)), run_time=1.6)
        self.wait(8)

class Rotate_anim(Rotating):
    CONFIG = {
        "axis": OUT,
        "radians": TAU,
        "run_time": 10,
        "rate_func": linear,
        "about_point": ORIGIN,
        "about_edge": None,
    }

class Angle(VGroup):

    CONFIG = {
        'radius': 1,
        'color': RED,
        'opacity': 0.4,
        'stroke_width': 10,
        # 'below_180': True,
    }

    def __init__(self, A, O, B, **kwargs):

        VMobject.__init__(self, **kwargs)
        OA, OB = A-O, B-O
        theta = np.angle(complex(*OA[:2])/complex(*OB[:2])) # angle of OB to OA

        self.add(Arc(start_angle=Line(O,B).get_angle(), angle=theta, radius=self.radius/2,
                     stroke_width=100 * self.radius, color=self.color).set_stroke(opacity=self.opacity).move_arc_center_to(O))
        self.add(Arc(start_angle=Line(O,B).get_angle(), angle=theta, radius=self.radius,
                     stroke_width=self.stroke_width, color=self.color).move_arc_center_to(O))

class EulerFormula_04(Scene):

    CONFIG = {
        # 'camera_config': {'background_color': WHITE}
    }

    def construct(self):

        formula = TexMobject('\\mathbf{e', '^{i', 't', '}=', '\\cos{', 't', '}+', 'i', '\\sin', '{t}}',
                             color=WHITE, background_stroke_color=BLACK, background_stroke_width=2).set_height(1.)

        formula.set_color_by_tex_to_color_map({'i': ORANGE, 't': BLUE, 'e': GREEN, '\\sin': YELLOW_D, '\\cos': YELLOW_D}).shift(DOWN * 1.8)
        formula[-2].set_color(YELLOW_D)

        arrow_x = Arrow(LEFT * 2.35, RIGHT * 2.6, color=GRAY, buff=0, max_tip_length_to_length_ratio=0.05)
        arrow_y = Arrow(DOWN * 2.35, UP * 2.6, color=GRAY, buff=0, max_tip_length_to_length_ratio=0.05)
        circle = Circle(color=RED_D, stroke_width=8).scale(2)
        group_1 = VGroup(arrow_x, arrow_y, circle).shift(UP * 1.2)

        dot_o = Dot(ORIGIN, color=GRAY).set_height(0.2)
        dot_p = Dot(np.sqrt(3) * RIGHT + UP, color=RED_D).set_height(0.25)
        line_1 = Line(dot_o.get_center(), dot_p.get_center(), color=RED_D, stroke_width=8)
        line_2 = Line(dot_o.get_center(), dot_p.get_center()*RIGHT + RIGHT * 0.035, color=YELLOW_D, stroke_width=10)
        line_3 = Line(dot_p.get_center()*RIGHT + DOWN * 0.035, dot_p.get_center(), color=YELLOW_D, stroke_width=10)
        group_2 = VGroup(line_1, line_2, line_3, dot_o, dot_p).shift(UP * 1.2)

        tex_i_1 = TexMobject('\\mathbf{i}', color=ORANGE, background_stroke_color=ORANGE, background_stroke_width=1.2).scale(0.8)
        tex_i_2 = TexMobject('\\mathbf{-i}', color=ORANGE, background_stroke_color=ORANGE, background_stroke_width=1.2).scale(0.8)
        tex_i_1.shift(UP * 2.2 + RIGHT * 0.275)
        tex_i_2.shift(DOWN * 2.2 + RIGHT * 0.275)

        tex_1_1 = TexMobject('\\mathbf{1}', color=WHITE, background_stroke_color=WHITE, background_stroke_width=1.2).scale(0.8)
        tex_1_2 = TexMobject('\\mathbf{-1}', color=WHITE, background_stroke_color=WHITE, background_stroke_width=1.2).scale(0.8)
        tex_1_1.shift(RIGHT * 2.25 + DOWN * 0.275)
        tex_1_2.shift(LEFT * 2.35 + DOWN * 0.275)

        tex_cos = TexMobject('\\mathbf{\\cos{', 't}}', color=YELLOW_D, background_stroke_color=BLACK, background_stroke_width=1).scale(0.8)
        tex_sin = TexMobject('\\mathbf{\\sin{', 't}}', color=YELLOW_D, background_stroke_color=BLACK, background_stroke_width=1).scale(0.8)
        tex_cos[1].set_color(BLUE)
        tex_sin[1].set_color(BLUE)
        tex_cos.next_to(line_2, DOWN * 0.8)
        tex_sin.next_to(line_3, RIGHT * 1.25)

        tex_group = VGroup(tex_1_1, tex_1_2, tex_i_1, tex_i_2).shift(UP * 1.2)

        self.add(group_1, group_2, tex_group, tex_cos, tex_sin)
        self.wait()

        angle_t = Angle(dot_o.get_center() + RIGHT, dot_o.get_center(), dot_o.get_center() + RIGHT * np.sqrt(3)/2 + UP * 0.5, color=BLUE, radius=0.75, stroke_width=8)
        text_t = TexMobject('\\mathbf{t}', color=BLUE).next_to(angle_t, RIGHT * 0.6).shift(UP * 0.1)

        self.play(ShowCreation(angle_t), Write(text_t), run_time=1)
        self.play(Write(formula))

        self.wait(10)

class Rotate_eit(Scene):

    def construct(self):

        def get_angle_new(vect):
            if vect.get_angle() >= 0:
                return vect.get_angle()
            else:
                return vect.get_angle() + PI * 2


        s = 2.75
        cp = ComplexPlane().scale(s)
        cp.add_coordinates(0, 1, 2, 3, 4, -1, -2, -3, -4)
        cp.add_coordinates(1j, 2j, -1j, -2j)

        color_dict = {'e': GREEN, 'i': RED, 't': BLUE, '\\times': WHITE, 'rad': BLUE}
        # text_eit = TexMobject('e^', '{i', 't}').scale(1.2).set_color_by_tex_to_color_map(color_dict)
        # times_eit = TexMobject('\\times', 'e^', '{i', 't}', color=WHITE).scale(2).set_color_by_tex_to_color_map(color_dict)
        # times_eit[0].set_color(WHITE)

        ## part 1 ##
        self.vector_2 = Arrow(ORIGIN, cp.c2p(1, 0), buff=0, color=BLUE)
        self.dot_2 = Dot(cp.c2p(1, 0), color=YELLOW).scale(1.5)
        self.rotate_2 = VGroup(self.vector_2, self.dot_2)
        text_2 = TexMobject('e^', '{i', 't}').scale(1.5).set_color_by_tex_to_color_map(color_dict).next_to(self.dot_2, RIGHT * 0.2 + UP * 0.2)

        arc_2 = Arc(radius=cp.c2p(1, 0)[1], color=GREEN, stroke_width=6)

        text_t = TexMobject('t', '=', '00.00', 'rad').set_color_by_tex_to_color_map(color_dict).scale(1.8).to_corner(LEFT * 1.2 + UP * 1.2)
        bg = SurroundingRectangle(text_t, color=YELLOW, fill_color=BLACK, fill_opacity=0.64)
        t_num = DecimalNumber(0, num_decimal_places=2, color=YELLOW).set_height(text_t.get_height()).move_to(text_t[2])
        show_t = VGroup(bg, text_t[0:2], t_num, text_t[-1])
        t_num.add_updater(lambda t: t.set_value(get_angle_new(self.vector_2)))

        arc_2.add_updater(lambda a: a.become(Arc(radius=1*s, angle=get_angle_new(self.vector_2), color=GREEN, stroke_width=6)))
        text_2.add_updater(lambda t: t.next_to(self.dot_2, RIGHT * 0.2 + UP * 0.2))


        ## part 2 ##


        ## anim ###

        self.play(ShowCreation(cp), run_time=1.5)
        self.wait(1)

        # anim part 1 #
        self.play(ShowCreation(self.vector_2))
        self.play(ShowCreation(self.dot_2))

        self.wait(0.8)

        self.play(Write(text_2), run_time=1.5)
        self.wait(0.5)
        self.add(arc_2)
        self.play(FadeIn(show_t), run_time=1.5)
        self.wait(0.5)
        self.play(Rotate_anim(self.rotate_2))
        # anim part 2 #

        #self.play()

        self.wait(5)

class Rotate_eit_3D(ThreeDScene):

    def construct(self):

        self.t = 0
        pass

class Rotate_eiwt(Scene):

    def construct(self):

        color_dict = {'e': GREEN, 'i': RED, 't': BLUE, '\\times': WHITE, 'rad': BLUE, '\\omega': PINK,
                   '1': PINK, '0.1': PINK, '10': PINK, '-2': PINK, 'z': YELLOW}
        self.theta = 1.5 * DEGREES

        def create_eiwt(loc, w, r=1.2):

            dot = Dot(loc, color=BLUE).scale(1.2)
            vect = Arrow(loc, loc+RIGHT*r, color=PINK, buff=0)
            circle = Circle(radius=r, color=YELLOW, stroke_width=2).move_to(loc)
            dot_y = Dot(loc+RIGHT*r, color=YELLOW) # .add_updater(lambda d: d.move_to(vect.get_end()))
            return VGroup(circle, dot, vect, dot_y)

        self.loc_list = [LEFT * 4.5 + UP * 0.25, LEFT * 1.5 + UP * 0.25, RIGHT * 1.5 + UP * 0.25, RIGHT * 4.5 + UP * 0.25]
        self.w_list = [1, 0.1, 10, -2]

        self.rotate_vects = VGroup()

        v_1 = create_eiwt(self.loc_list[0], self.w_list[0])
        v_1.add_updater(lambda v, dt: v.rotate(self.theta * self.w_list[0], about_point=self.loc_list[0]))
        v_2 = create_eiwt(self.loc_list[1], self.w_list[1])
        v_2.add_updater(lambda v, dt: v.rotate(self.theta * self.w_list[1], about_point=self.loc_list[1]))
        v_3 = create_eiwt(self.loc_list[2], self.w_list[2])
        v_3.add_updater(lambda v, dt: v.rotate(self.theta * self.w_list[2], about_point=self.loc_list[2]))
        v_4 = create_eiwt(self.loc_list[3], self.w_list[3])
        v_4.add_updater(lambda v, dt: v.rotate(self.theta * self.w_list[3], about_point=self.loc_list[3]))

        text = Text('不同角速度对应的的旋转情况', font='新蒂小丸子体').set_height(0.6)
        text.set_color_by_t2c({'角速度': PINK})
        text.to_corner(LEFT * 1.5 + UP * 1.5)

        formula_01 = TexMobject('z', '=', 'e^{', 'i', '\\omega', 't}').set_color_by_tex_to_color_map(color_dict).set_height(1.)
        formula_01.next_to(text, RIGHT * 1.5).shift(UP * 0.2)

        self.wait()
        self.play(Write(text), run_time=2.5)
        self.wait(0.5)
        self.play(Write(formula_01), run_time=1.5)

        self.rotate_vects.add(v_1, v_2, v_3, v_4)
        self.add(self.rotate_vects)

        # text_1 = TexMobject('e^', '{i', '(', '1', 't', ')}').set_color_by_tex_to_color_map(color_dict).next_to(self.rotate_vects[0], DOWN * 4)
        # text_2 = TexMobject('e^', '{i', '(', '0.1', 't', ')}').set_color_by_tex_to_color_map(color_dict).next_to(self.rotate_vects[1], DOWN * 4)
        # text_3 = TexMobject('e^', '{i', '(', '10', 't', ')}').set_color_by_tex_to_color_map(color_dict).next_to(self.rotate_vects[2], DOWN * 4)
        # text_4 = TexMobject('e^', '{i', '(', '-2', 't', ')}').set_color_by_tex_to_color_map(color_dict).next_to(self.rotate_vects[3], DOWN * 4)

        text_1 = TexMobject('e^', '{i', '1', 't}').set_height(0.8).set_color_by_tex_to_color_map(color_dict).next_to(self.rotate_vects[0], DOWN * 2.8)
        text_2 = TexMobject('e^', '{i', '0.1', 't}').set_height(0.8).set_color_by_tex_to_color_map(color_dict).next_to(self.rotate_vects[1], DOWN * 2.8)
        text_3 = TexMobject('e^', '{i', '10', 't}').set_height(0.8).set_color_by_tex_to_color_map(color_dict).next_to(self.rotate_vects[2], DOWN * 2.8)
        text_4 = TexMobject('e^', '{i', '(', '-2', ')', 't}').set_height(0.8).set_color_by_tex_to_color_map(color_dict).next_to(self.rotate_vects[3], DOWN * 2.8)


        self.play(Write(text_1))
        self.play(Write(text_2))
        self.play(Write(text_3))
        self.play(Write(text_4))


        self.wait(15)

class Rotate_part_1(Scene):

    def construct(self):

        def get_angle_new(vect):
            if vect.get_angle() >= 0:
                return vect.get_angle()
            else:
                return vect.get_angle() + PI * 2


        s = 1.8
        cp = ComplexPlane().scale(s)
        cp.add_coordinates(0, 1, 2, 3, 4, -1, -2, -3, -4)
        cp.add_coordinates(1j, 2j, -1j, -2j)

        color_dict = {'e': GREEN, 'i': RED, 't': BLUE, '\\times': WHITE, 'rad': BLUE}
        text_eit = TexMobject('e^', '{i', 't}').scale(1.2).set_color_by_tex_to_color_map(color_dict)
        times_eit = TexMobject('\\times', 'e^', '{i', 't}', color=WHITE).scale(2).set_color_by_tex_to_color_map(color_dict)
        # times_eit[0].set_color(WHITE)

        ## part 1 ##
        self.vector_2 = Arrow(ORIGIN, cp.c2p(2, 0), buff=0, color=BLUE)
        self.dot_2 = Dot(cp.c2p(2, 0), color=YELLOW).scale(1.5)
        self.rotate_2 = VGroup(self.vector_2, self.dot_2)
        text_2 = TexMobject('z', '=', '2', color=YELLOW).next_to(self.dot_2, RIGHT * 0.2 + UP * 0.2)
        text_2[1].set_color(WHITE)

        times_eit_2 = times_eit.copy().to_corner(RIGHT * 2.5 + UP * 2)
        text_eit_2 = text_eit.copy().next_to(text_2, RIGHT * 0.25).shift(UP * 0.1)
        text_group_2 = VGroup(text_2, text_eit_2)

        arc_2 = Arc(radius=cp.c2p(2, 0)[1], color=GREEN, stroke_width=6)

        text_t = TexMobject('t', '=', '00.00', 'rad').set_color_by_tex_to_color_map(color_dict).scale(1.8).to_corner(LEFT * 1.5 + UP * 1.5)
        bg = SurroundingRectangle(text_t, color=YELLOW, fill_color=BLACK, fill_opacity=0.64)
        t_num = DecimalNumber(0, num_decimal_places=2, color=YELLOW).set_height(text_t.get_height()).move_to(text_t[2])
        show_t = VGroup(bg, text_t[0:2], t_num, text_t[-1])
        t_num.add_updater(lambda t: t.set_value(get_angle_new(self.vector_2)))

        arc_2.add_updater(lambda a: a.become(Arc(radius=2*s, angle=get_angle_new(self.vector_2), color=GREEN, stroke_width=6)))
        text_2.add_updater(lambda t: t.next_to(self.dot_2, RIGHT * 0.2 + UP * 0.2))
        text_eit_2.add_updater(lambda t:t.next_to(text_2, RIGHT * 0.25).shift(UP * 0.1))

        ## part 2 ##


        ## anim ###

        self.play(ShowCreation(cp), run_time=1.5)
        self.wait(1)

        # anim part 1 #
        self.play(ShowCreation(self.vector_2))
        self.play(ShowCreation(self.dot_2))

        self.wait(0.8)

        self.play(Write(text_2))
        self.wait(0.6)
        self.play(Write(times_eit_2), run_time=1.2)
        self.wait(0.25)
        self.play(ShowCreationThenDestruction(SurroundingRectangle(times_eit_2).set_color(GREEN)), run_time=1.5)
        self.wait(0.25)
        self.play(ReplacementTransform(times_eit_2, text_eit_2), run_time=1.6)
        self.wait(0.5)
        self.add(arc_2)
        self.play(FadeIn(show_t))
        self.wait(0.75)
        self.play(Rotate_anim(self.rotate_2))
        # anim part 2 #

        #self.play()

        self.wait(5)

class Rotate_part_2(Scene):

    def construct(self):

        def get_angle_new(vect):
            if vect.get_angle() >= 0:
                return vect.get_angle()
            else:
                return vect.get_angle() + PI * 2

        self.t = 0

        s = 1.8
        s_new = 1.25
        cp = ComplexPlane().scale(s)
        cp.add_coordinates(0, 1, 2, 3, 4, 5, -1, -2, -3, -4, -5)
        cp.add_coordinates(1j, 2j, 3j, -1j, -2j, -3j)

        color_dict = {'e': GREEN, 'i': RED, 't': BLUE, '\\times': WHITE, 'rad': BLUE, 'z': YELLOW, '2': GREEN, '\\cos': YELLOW}
        text_eit = TexMobject('e^', '{i', 't}').scale(1.2).set_color_by_tex_to_color_map(color_dict)
        times_eit = TexMobject('\\times', 'e^', '{i', 't}', color=WHITE).scale(2).set_color_by_tex_to_color_map(color_dict)
        # times_eit[0].set_color(WHITE)

        ## part 1 ##

        ## part 2 ##
        self.vector_g = Arrow(ORIGIN, cp.c2p(2, 0), buff=0, color=GREEN)
        self.vector_y = Arrow(cp.c2p(2, 0), cp.c2p(3, 0), buff=0, color=YELLOW)
        self.dot_y = Dot(cp.c2p(3, 0), color=YELLOW).scale(1.25)
        self.dot_y.add_updater(lambda d: d.move_to(self.vector_y.get_end()))
        self.vectors = VGroup(self.vector_g, self.vector_y, self.dot_y)

        text_z = TexMobject('z', '=', '2', '+', '\\cos{', '5', 't}').set_color_by_tex_to_color_map(color_dict)
        text_z_02 = TexMobject('z', '=', '(', '2', '+', '\\cos{', '5', 't}', ')').set_color_by_tex_to_color_map(color_dict)
        text_z.next_to(self.dot_y, LEFT + UP * 0.6)
        text_z_02.next_to(self.dot_y, LEFT + UP * 0.6)

        times_eit_2 = times_eit.copy().to_corner(RIGHT * 2.5 + UP * 2)
        text_eit_2 = text_eit.copy().next_to(text_z_02, RIGHT * 0.25).shift(UP * 0.16)
        text_group_2 = VGroup(text_z_02, text_eit_2)
        text_z_02.add_updater(lambda t: t.next_to(self.vector_g.get_end(), UP * 0.6))
        text_eit_2.add_updater(lambda t: t.next_to(text_z_02, RIGHT * 0.25).shift(UP * 0.1))

        text_t = TexMobject('t', '=', '00.00', 'rad').set_color_by_tex_to_color_map(color_dict).scale(1.8).to_corner(LEFT * 1.35 + UP * 1.35)
        bg = SurroundingRectangle(text_t, color=YELLOW, fill_color=BLACK, fill_opacity=0.64)
        t_num = DecimalNumber(0, num_decimal_places=2, color=YELLOW).set_height(text_t.get_height()).move_to(text_t[2]).shift(LEFT * 0.24)
        show_t = VGroup(bg, text_t[0:2], t_num, text_t[-1])
        t_num.add_updater(lambda t: t.set_value(self.t))

        self.path = VGroup()


        def update_by_cos(vect_y, dt):
            self.t += dt
            vect_y.become(Arrow(cp.c2p(2, 0), cp.c2p(2 + np.cos(self.t * 5), 0), buff=0, color=YELLOW))

        def update_vectors(vects, dt):
            p1_old = cp.c2p(2 * np.cos(self.t), 2 * np.sin(self.t))
            p2_old = p1_old * (2 + np.cos(self.t * 5))/2
            self.t += dt
            p0 = ORIGIN
            p1 = cp.c2p(2 * np.cos(self.t), 2 * np.sin(self.t))
            p2 = p1 * (2 + np.cos(self.t * 5))/2
            vects[0].become(Arrow(p0, p1, buff=0, color=GREEN))
            vects[1].become(Arrow(p1, p2, buff=0, color=YELLOW))
            vects[2].move_to(p2)
            line_i = Line(p2_old, p2, color=YELLOW, stroke_width=2.5)
            self.path.add(line_i)

        ## anim ###

        self.play(ShowCreation(cp), run_time=1.5)
        self.wait(1)
        self.add(self.path)

        # anim part 1 #

        # anim part 2 #
        self.play(ShowCreation(self.vector_g), ShowCreation(self.vector_y), ShowCreation(self.dot_y), run_time=1.5)
        self.wait()
        self.play(Write(text_z), run_time=1.5)
        self.wait()
        self.vector_y.add_updater(update_by_cos)
        self.wait(4)

        self.play(Write(times_eit_2), run_time=2.01)
        self.wait(0.25)
        self.play(ShowCreationThenDestruction(SurroundingRectangle(times_eit_2).set_color(GREEN)), run_time=2.25)
        self.wait(0.25)
        self.play(ReplacementTransform(times_eit_2, text_eit_2), ReplacementTransform(text_z, text_z_02), run_time=2.5)
        self.wait(0.25)

        self.vector_y.clear_updaters()
        self.play(ApplyMethod(cp.scale_about_point, s_new/s, ORIGIN),
                  ApplyMethod(self.vectors.scale_about_point, s_new/s, ORIGIN), run_time=1.2)
        self.t=0
        self.play(FadeIn(show_t), run_time=1.5)

        self.vectors.add_updater(update_vectors)
        self.wait(15)

class Rotate_part_3(Scene):

    def construct(self):

        def get_angle_new(vect):
            if vect.get_angle() >= 0:
                return vect.get_angle()
            else:
                return vect.get_angle() + PI * 2

        self.t = 0

        s = 1.8
        s_new = 1.25
        cp = ComplexPlane().scale(s)
        cp.add_coordinates(0, 1, 2, 3, 4, 5, -1, -2, -3, -4, -5)
        cp.add_coordinates(1j, 2j, 3j, -1j, -2j, -3j)

        color_dict = {'e': GREEN, 'i': RED, 't': BLUE, '\\times': WHITE, 'rad': BLUE, 'z': YELLOW, '2': GREEN, '\\cos': YELLOW}

        text_eit = TexMobject('e^', '{i', 't}').scale(1.2).set_color_by_tex_to_color_map(color_dict)
        times_eit = TexMobject('\\times', 'e^', '{i', 't}', color=WHITE).scale(2).set_color_by_tex_to_color_map(color_dict)

        # times_eit[0].set_color(WHITE)

        ## part 1 ##

        ## part 2 ##
        self.vector_g = Arrow(ORIGIN, cp.c2p(2, 0), buff=0, color=GREEN)
        self.vector_y = Arrow(cp.c2p(2, 0), cp.c2p(3, 0), buff=0, color=YELLOW)
        self.dot_y = Dot(cp.c2p(3, 0), color=YELLOW).scale(1.25)
        self.dot_y.add_updater(lambda d: d.move_to(self.vector_y.get_end()))
        self.vectors = VGroup(self.vector_g, self.vector_y, self.dot_y)

        text_z = TexMobject('z', '=', '2', '+', 'e^{', 'i', '5', 't}').set_color_by_tex_to_color_map(color_dict)
        text_z_02 = TexMobject('z', '=', '(', '2', '+', 'e^{', 'i', '5', 't}', ')').set_color_by_tex_to_color_map(color_dict)
        text_z.next_to(self.dot_y, LEFT + UP * 0.6)
        text_z_02.next_to(self.dot_y, LEFT + UP * 0.6)

        times_eit_2 = times_eit.copy().to_corner(RIGHT * 2.5 + UP * 2)
        text_eit_2 = text_eit.copy().next_to(text_z, RIGHT * 0.25).shift(UP * 0.16)
        text_group_2 = VGroup(text_z_02, text_eit_2)
        text_z_02.add_updater(lambda t: t.next_to(self.vector_g.get_end(), UP * 0.6))
        text_eit_2.add_updater(lambda t: t.next_to(text_z_02, RIGHT * 0.25).shift(UP * 0.1))

        text_t = TexMobject('t', '=', '00.00', 'rad').set_color_by_tex_to_color_map(color_dict).scale(1.8).to_corner(LEFT * 1.35 + UP * 1.35)
        bg = SurroundingRectangle(text_t, color=YELLOW, fill_color=BLACK, fill_opacity=0.64)
        t_num = DecimalNumber(0, num_decimal_places=2, color=YELLOW).set_height(text_t.get_height()).move_to(text_t[2]).shift(LEFT * 0.24)
        show_t = VGroup(bg, text_t[0:2], t_num, text_t[-1])
        t_num.add_updater(lambda t: t.set_value(self.t))

        self.path = VGroup()


        def update_by_rotate(vect_y, dt):
            self.t += dt
            vect_y.become(Arrow(cp.c2p(2, 0), cp.c2p(2 + np.cos(self.t * 5), np.sin(self.t * 5)), buff=0, color=YELLOW))

        def update_vectors(vects, dt):
            p1_old = cp.c2p(2 * np.cos(self.t), 2 * np.sin(self.t))
            p2_old = p1_old + cp.c2p(np.cos(self.t * 6), np.sin(self.t * 6))
            self.t += dt
            p0 = ORIGIN
            p1 = cp.c2p(2 * np.cos(self.t), 2 * np.sin(self.t))
            p2 = p1 + cp.c2p(np.cos(self.t * 6), np.sin(self.t * 6))
            vects[0].become(Arrow(p0, p1, buff=0, color=GREEN))
            vects[1].become(Arrow(p1, p2, buff=0, color=YELLOW))
            vects[2].move_to(p2)
            line_i = Line(p2_old, p2, color=YELLOW, stroke_width=2.5)
            self.path.add(line_i)

        ## anim ###

        self.play(ShowCreation(cp), run_time=1.5)
        self.wait(1)
        self.add(self.path)

        # anim part 1 #

        # anim part 2 #
        self.play(ShowCreation(self.vector_g), ShowCreation(self.vector_y), ShowCreation(self.dot_y), run_time=1.5)
        self.wait()
        self.play(Write(text_z), run_time=1.5)
        self.wait()
        self.vector_y.add_updater(update_by_rotate)
        self.wait(4)

        self.play(Write(times_eit_2), run_time=2.)
        self.wait(0.25)
        self.play(ShowCreationThenDestruction(SurroundingRectangle(times_eit_2).set_color(GREEN)), run_time=2.25)
        self.wait(0.25)
        self.play(ReplacementTransform(times_eit_2, text_eit_2), ReplacementTransform(text_z, text_z_02), run_time=2.48)
        self.wait((0.25))

        self.vector_y.clear_updaters()
        self.play(ApplyMethod(cp.scale_about_point, s_new/s, ORIGIN),
                  ApplyMethod(self.vectors.scale_about_point, s_new/s, ORIGIN), run_time=1.2)
        self.t=0
        self.play(FadeIn(show_t), run_time=1.5)

        self.vectors.add_updater(update_vectors)
        self.wait(15)

class Derivation_by_complex(Scene):

    CONFIG = {
        'R': 3.2,
        'r': 3.2 * 3/5,
        'd': 3.2 * 3/5 * 0.4,
        'center': LEFT * 3.4 + UP * 0.25,
        'defaul_font': '新蒂小丸子体',
    }

    def construct(self):

        d_theta = -0.25 * DEGREES

        gear_b = Gear_outline(pitch_circle_radius=self.R, tooth_hight=0.275, tooth_num=40, stroke_color=BLUE, stroke_opacity=0.32).shift(self.center)
        gear_y = Gear_outline(pitch_circle_radius=self.r, tooth_hight=0.275, tooth_num=24, stroke_color=YELLOW, stroke_opacity=0.32).shift(RIGHT * (self.R - self.r) + self.center)

        circle_b = Circle(radius=self.R, color=BLUE).shift(self.center)
        circle_y = Circle(radius=self.r, color=YELLOW).shift(RIGHT * (self.R - self.r) + self.center)

        dot_b = Dot(self.center, color=BLUE).scale(1.2)
        self.dot_y = Dot(self.center, color=YELLOW).scale(1.2).move_to(circle_y)

        gear_b.add_updater(lambda g, dt: g.rotate(d_theta))
        gear_y.add_updater(lambda g, dt: g.move_to(self.dot_y).rotate(d_theta * self.R/self.r))

        self.dots = VGroup()
        self.path = VGroup()

        arrow_p = Arrow(self.center, self.center + self.R * np.sqrt(2)/2 * (LEFT + DOWN), buff=0, color=PINK)
        arrow_o = Arrow(self.center + RIGHT * (self.R - self.r), self.center + RIGHT * (self.R - self.r)
                        + self.r * np.sqrt(2)/2 * (LEFT + DOWN), buff=0, color=ORANGE)

        text_R  =TexMobject('R', color=PINK).next_to(arrow_p.get_end(), UP * 2.75 + RIGHT * 0.4)
        text_r = TexMobject('r', color=ORANGE).next_to(arrow_o.get_end(), UP * 2.25 + RIGHT * 0.3)

        self.add(gear_b, circle_b, dot_b, arrow_p, gear_y, circle_y, self.dot_y, arrow_o)

        text_01 = Text('在两圆相切处线速度相等,\n\n若蓝色圆的角速度为1， 则：', font=self.defaul_font).set_height(1.25).to_corner(RIGHT * 3.6 + UP * 1.25)
        text_01.set_color_by_t2c({'蓝色圆': BLUE, '1': BLUE, '线速度相等': GREEN})

        color_dict = {'v': GREEN, '1': BLUE, 'R': PINK, 'r': ORANGE, '\\omega_{\\text{黄}}': YELLOW,
                      '\\over': WHITE, '\\therefore': WHITE, 'e^': GREEN, 'd': YELLOW, 't': BLUE, 'i': RED}
        formula_01 = TexMobject('v', '=', '1', '\\times', 'R', '=', '\\omega_{\\text{黄}}', '\\times', 'r')
        formula_01.set_color_by_tex_to_color_map(color_dict)
        formula_01[6].set_color(YELLOW)
        formula_01.next_to(text_01, DOWN * 1.5).align_to(text_01, LEFT).shift(RIGHT * 0.25)

        arrow_v = Arrow(self.center + self.R * RIGHT, self.center + self.R * RIGHT + DOWN * 3.2, color=GREEN, stroke_width=4)

        formula_02 = TexMobject('\\therefore\\,', '\\omega_{\\text{黄}}', '=', '{R', '\\over', 'r}', color=WHITE)
        formula_02.set_color_by_tex_to_color_map(color_dict)
        formula_02[1].set_color(YELLOW)
        formula_02.next_to(formula_01, DOWN * 1).align_to(formula_01, LEFT)

        text_02 = Text('黄色圆上的任意一点的轨迹为：', font=self.defaul_font).set_height(0.52)
        text_02.set_color_by_t2c({'黄色圆': YELLOW})
        text_02.next_to(formula_02, DOWN).align_to(text_01, LEFT)

        formula_03 = TexMobject('g(', 't', ')', '=', 'R', '-', 'r', '+', 'd', 'e^{', '-', '{R', '\\over', 'r}', 't', 'i}')
        formula_03.set_color_by_tex_to_color_map(color_dict)
        formula_03[0].set_color(YELLOW), formula_03[2].set_color(YELLOW)
        formula_03.next_to(text_02, DOWN * 1.25).align_to(formula_01, LEFT)

        self.arrow_Rr = Arrow(self.center, self.center + RIGHT * (self.R - self.r), color=BLUE, buff=0)
        self.arrow_d = Arrow(self.center + RIGHT * (self.R - self.r), self.center + RIGHT * (self.R - self.r + self.d), color=YELLOW, buff=0)
        self.dot_y_new = Dot(color=YELLOW).move_to(self.center + RIGHT * (self.R - self.r))
        self.dot_d = Dot(color=YELLOW).move_to(self.arrow_d.get_end())
        self.rotate_y = VGroup(self.arrow_d, self.dot_d, self.dot_y_new)

        ## anim ##

        self.wait(1.5)
        self.play(Write(text_R), Write(text_r))
        self.wait()
        self.play(Write(text_01), run_time=3)

        self.wait()

        self.play(ShowCreation(arrow_v), run_time=1.5)
        self.wait(0.5)
        self.play(ReplacementTransform(arrow_v, formula_01[0]), run_time=1.25)
        self.wait(0.25)
        self.play(Write(formula_01[1:]), run_time=3)

        self.wait()

        self.play(Write(formula_02), run_time=2.5)
        self.wait(1.5)

        self.play(Write(text_02))

        self.wait()
        self.play(Write(formula_03[0:4]), run_time=1.5)
        self.wait(0.25)
        self.play(ShowCreation(self.arrow_Rr))
        self.play(ShowCreation(self.rotate_y))
        self.rotate_y.add_updater(lambda r: r.shift(self.dot_y.get_center() - r[2].get_center()).rotate(d_theta * self.R/self.r, about_point=self.dot_y.get_center()))
        self.wait(0.25)
        self.play(TransformFromCopy(self.arrow_Rr, formula_03[4:7]), run_time=1.5)
        self.play(Write(formula_03[7]))
        self.wait(0.4)
        self.play(TransformFromCopy(self.rotate_y, formula_03[8:]), run_time=1.5)
        self.wait(0.5)
        self.play(FadeOut(arrow_p), FadeOut(arrow_o), FadeOut(text_R), FadeOut(text_r), run_time=2)
        self.play(FadeOut(text_01), FadeOut(formula_01), FadeOut(formula_02), run_time=1.2)
        self.play(ApplyMethod(text_02.to_corner, UP * 1.25), ApplyMethod(formula_03.shift, UP * 4))

        ## add reverse rotate ##

        text_03 = Text('给所有对象添加一个逆时针的\n\n'
                       '公转（转速为1），则蓝色圆\n\n'
                       '变为静止，黄色圆绕其纯滚动', font=self.defaul_font).set_height(1.9)
        text_03.set_color_by_t2c({'蓝色圆': BLUE, '黄色圆': YELLOW})
        text_03.next_to(formula_03, DOWN).align_to(text_02, LEFT)

        text_04 = Text('则，动点的轨迹为：', font=self.defaul_font).set_height(0.42)
        text_04.set_color_by_t2c({'动点': YELLOW})
        text_04.next_to(text_03, DOWN * 0.75).align_to(text_03, LEFT)

        formula_04 = TexMobject('f(', 't', ')', '=', 'g(', 't', ')', 'e^', '{i', 't}').scale(0.95).next_to(text_04, DOWN * 0.95).align_to(formula_03, LEFT)
        formula_04.set_color_by_tex_to_color_map({'f(': YELLOW, ')': YELLOW, 'g(': YELLOW, 'e': GREEN, 'i': RED, 't': BLUE})

        formula_05 = TexMobject('f(', 't', ')', '=(', 'R', '-', 'r', '+', 'd', 'e^{', '-', '{R', '\\over', 'r}', 't', 'i}', ')', 'e^', '{i', 't}').scale(0.9)
        formula_05[0].set_color(YELLOW), formula_05[2].set_color(YELLOW)
        formula_05.set_color_by_tex_to_color_map(color_dict)
        formula_05.next_to(formula_04, DOWN * 0.9).align_to(formula_03, LEFT)

        formula_06 = TexMobject('f(', 't', ')', '=(', 'R', '-', 'r', ')', 'e^', '{i', 't}', '+', 'd', 'e^{', '-', '{R', '-', 'r', '\\over', 'r}', 't', 'i}').scale(0.9)
        formula_06[0].set_color(YELLOW), formula_06[2].set_color(YELLOW)
        formula_06.set_color_by_tex_to_color_map(color_dict)
        formula_06.next_to(formula_05, DOWN * 1).align_to(formula_03, LEFT)


        self.play(Write(text_03), run_time=4.5)
        self.wait(0.2)
        gear_b.clear_updaters()
        gear_y.clear_updaters()
        gear_y.add_updater(lambda g, dt: g.move_to(self.dot_y).rotate(d_theta * (self.R-self.r)/self.r))

        self.dot_y.add_updater(lambda d: d.rotate(-d_theta, about_point=self.center))
        self.arrow_Rr.add_updater(lambda a: a.rotate(-d_theta, about_point=self.center))
        # self.dots.add_updater(lambda d: d.add(Dot(self.dot_d.get_center())))
        circle_y.add_updater(lambda c: c.move_to(self.dot_y))
        self.wait(0.25)
        self.add(self.path)
        # print(len(self.dots))

        self.point = self.dot_d.get_center()
        def update_path(path):
            p_old = self.point
            p_new = self.dot_d.get_center()
            path.add(Line(p_old, p_new, stroke_width=2, color=YELLOW))
            self.point = p_new

        # self.path.add_updater(lambda p: p.add(Line(self.dots[-1].get_center(), self.dots[-2].get_center(), stroke_width=2, color=YELLOW)))
        self.path.add_updater(update_path)

        self.wait(0.5)
        self.play(Write(text_04), run_time=1.5)
        self.wait(0.25)
        self.play(Write(formula_04[0:4]), run_time=1)
        self.wait(0.2)
        self.play(TransformFromCopy(formula_03[0:3], formula_04[4:7]), run_time=2.5)
        self.wait(0.25)
        self.play(Write(formula_04[7:]), run_time=1.5)
        self.play(WiggleOutThenIn(formula_04[7:]))
        self.wait()
        
        self.play(TransformFromCopy(formula_04, formula_05), run_time=2.5)
        self.wait(2)
        self.play(TransformFromCopy(formula_05, formula_06), run_time=2.5)
        self.wait(0.5)
        self.play(ShowCreation(SurroundingRectangle(formula_06, color=GREEN)), run_time=2)
        self.wait(1.)
        d_theta = -0.25 * DEGREES * 1.2
        self.wait(1.)
        d_theta = -0.25 * DEGREES * 1.2 ** 2
        self.wait(1.)
        d_theta = -0.25 * DEGREES * 1.2 ** 3
        self.wait(1.)
        d_theta = -0.25 * DEGREES * 1.2 ** 4
        self.wait(1.)
        d_theta = -0.25 * DEGREES * 1.2 ** 5
        self.wait(1.)
        d_theta = -0.25 * DEGREES * 1.2 ** 6
        self.wait(1.)
        d_theta = -0.25 * DEGREES * 1.2 ** 7
        self.wait(1.)
        d_theta = -0.25 * DEGREES * 1.2 ** 8

        self.wait(20)


class Hello_World(Scene):

    def construct(self):
        text = TexMobject('hello\\ world！',color=RED)
        self.play(ShowCreation(text))
        self.wait(5)






