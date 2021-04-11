from manimlib.imports import *
from my_projects.my_utils.boolean_operation import VGroup_

get_angle = lambda c: np.angle(-c) + PI if not c/abs(c) == 1 else 0
convert_angle = lambda a: a if a>=0 else a + TAU

class Apple_logo(VGroup):

    CONFIG = {
        'scale': 0.25,
        'logo_color': RED_D,
        'logo_stroke': 8,
        'coord_center': DOWN * 1.25,
        'assistent_lines_config': {
            'stroke_width': 2,
            'stroke_color': GREY,
        },
        'key_lines_config': {
            'stroke_width': 2.5,
            'stroke_color': GREY_E,
        },
        'step_size': 0.02,
        'create_shape': True,

    }

    def __init__(self, **kwargs):

        VGroup.__init__(self, **kwargs)
        self.set_key_lines()
        self.set_outline()
        if self.create_shape:
            self.set_logo_shape()

    def set_key_lines(self):

        s = self.scale
        center = self.coord_center
        self.c1 = Circle(arc_center=center+ORIGIN, radius=1/2*s, **self.key_lines_config)
        self.c5_r = Circle(arc_center=center+3*s*RIGHT, radius=5/2*s, **self.key_lines_config)
        self.c5_l = Circle(arc_center=center+3*s*LEFT,  radius=5/2*s, **self.key_lines_config)
        # self.c5_l = self.c5_r.copy().flip()
        self.c8_d = Circle(arc_center=center + s * 5.77 * DOWN, radius=8/2*s, **self.key_lines_config)
        self.c13  = Circle(arc_center=center + s * 4.73 * UP, radius=13/2*s, **self.key_lines_config)
        self.c8_r = Circle(arc_center=center + s * ( 3.48 * RIGHT + 7.69 * UP),
                           radius=8/2*s, **self.key_lines_config)
        self.c8_l = Circle(arc_center=center + s * (-3.48 * RIGHT + 7.69 * UP),
                           radius=8/2*s, **self.key_lines_config)
        self.c3_r = Circle(arc_center=center + s * ( 5.9 * RIGHT + 2.75 * UP),
                           radius=3/2*s, **self.key_lines_config)
        self.c3_l = Circle(arc_center=center + s * (-5.9 * RIGHT + 2.75 * UP),
                           radius=3/2*s, **self.key_lines_config)
        self.c24_r = Circle(arc_center=center + s * ( 3.89 * RIGHT + 6.54 * UP),
                           radius=24/2*s, **self.key_lines_config)
        self.c24_l = Circle(arc_center=center + s * (-3.89 * RIGHT + 6.54 * UP),
                           radius=24/2*s, **self.key_lines_config)


        self.c12_r = Circle(arc_center=center + s * ( 2.11 * RIGHT + 6.23 * UP),
                           radius=12/2*s, **self.key_lines_config)
        self.c12_l = Circle(arc_center=center + s * (-2.11 * RIGHT + 6.23 * UP),
                           radius=12/2*s, **self.key_lines_config)
        self.c8_u = Circle(arc_center=center + s * 14.89 * UP, radius=8/2*s, **self.key_lines_config)
        self.c8_01 = Circle(arc_center=center + s * (8.82 * RIGHT + 6.23 * UP),
                            radius=8/2*s, **self.key_lines_config)
        self.c8_02 = Circle(arc_center=center + s * (3.61 * RIGHT + 12.23 * UP),
                            radius=8/2*s, **self.key_lines_config)
        self.c8_03 = Circle(arc_center=center + s * (-0.46 * RIGHT + 15.69 * UP),
                            radius=8/2*s, **self.key_lines_config)

        self.key_lines = VGroup(self.c1, self.c5_r, self.c5_l,
                                self.c8_d, self.c13,
                                self.c8_r, self.c8_l,
                                self.c3_r, self.c3_l,
                                self.c24_r, self.c24_l,
                                self.c12_r, self.c12_l,
                                self.c8_u,
                                self.c8_01,
                                self.c8_02, self.c8_03,
                                )
        self.key_lines_center = VGroup(* [Dot(c.get_center(), stroke_color=self.key_lines_config['stroke_color'],
                                              radius=self.key_lines_config['stroke_width']/100) for c in self.key_lines])
        return self

    def set_outline(self):
        s = self.scale
        center = self.coord_center
        # kp_list = [[7.41, 2.49, 0], [4.81, -1.72, 0], [1.85, -2.22, 0], [-1.85, -2.22, 0], [-4.81, 1.72, 0], [-8.1, 5.91, 0],
        #            [-6.22, 10.6, 0], [-1.74, 11.29, 0], [1.74, 11.29, 0], [6.22, 10.6, 0], [6.95, 9.77, 0], [-0.37, 11.87, 0], [3.42, 16.22, 0]]
        kp_list = [[6.95, 9.77, 0], [6.22, 10.6, 0], [1.74, 11.29, 0], [-1.74, 11.29, 0], [-6.22, 10.6, 0], [-8.1, 5.91, 0],
                   [-4.81, -1.72, 0], [-1.85, -2.22, 0], [1.85, -2.22, 0], [4.81, -1.72, 0], [7.41, 2.49, 0], [-0.35, 11.69, 0], [3.5, 16.23, 0]]

        self.key_angles = np.array([10.62, 69, -51.5, 69, 49.77, 40.52, 73.94, -54.97, 73.94, 23.77, -131.51, 96.09, -96.09]) * DEGREES
        self.key_radius = np.array([12/2, 8/2, 8/2, 8/2, 12/2, 24/2, 5/2, 8/2, 5/2, 24/2, 8/2]) * s
        self.key_points = np.array(kp_list) * s + center
        n = len(kp_list)
        self.outline_by_arcs = VGroup_(step_size=self.step_size)
        for i in range(n-2):
            p1, p2 = self.key_points[i], self.key_points[(i+1) % (n-2)]
            arc_i = ArcBetweenPoints(p1, p2, angle=self.key_angles[i], radius=self.key_radius[i], stroke_color=self.logo_color, stroke_width=self.logo_stroke)
            self.outline_by_arcs.add(arc_i)
        arc_1 = ArcBetweenPoints(self.key_points[-2], self.key_points[-1], angle=self.key_angles[-2], radius=self.key_radius[-2], stroke_color=self.logo_color, stroke_width=self.logo_stroke)
        arc_2 = ArcBetweenPoints(self.key_points[-2], self.key_points[-1], angle=self.key_angles[-1], radius=self.key_radius[-1], stroke_color=self.logo_color, stroke_width=self.logo_stroke)

        self.outline_by_arcs.add(arc_1, arc_2)
        return self

    def set_logo_shape(self):
        s = self.scale
        center = self.coord_center
        self.outline_by_arcs.get_all_outline_points()
        self.shape_1 = self.outline_by_arcs.get_shape(center=center + s * (-3.89 * RIGHT + 6.54 * UP), fill_color=self.logo_color, fill_opacity=1, stroke_color=self.logo_color, stroke_width=self.logo_stroke)
        self.shape_2 = self.outline_by_arcs.get_shape(center=center + s * (1.52 * RIGHT + 14.05 * UP), fill_color=self.logo_color, fill_opacity=1, stroke_color=self.logo_color, stroke_width=self.logo_stroke)
        # shape_1.set_fill(self.logo_color, 1).set_stroke(self.logo_color, self.logo_stroke, 1)
        # shape_2.set_fill(self.logo_color, 1).set_stroke(self.logo_color, self.logo_stroke, 1)
        self.add(self.shape_1, self.shape_2)
        return self

# from my_projects.others.BooleanOperationsOnPolygons import PolygonIntersection, PolygonUnion, PolygonSubtraction
#
# class PolygonBooleanTest(Scene):
#     def construct(self):
#         pol1 = RegularPolygon(9).scale(2).shift(LEFT)
#         pol2 = RegularPolygon(9).scale(2).shift(RIGHT)
#         start = time.perf_counter()
#         boolpol = PolygonSubtraction(
#             PolygonUnion(pol1, pol2), PolygonIntersection(pol1, pol2)
#         ).set_stroke(color=YELLOW, width=0).set_fill(color=YELLOW, opacity=0.5)
#         end = time.perf_counter()
#         print(end - start)
#         self.add(pol1, pol2, boolpol)
#
#         '''
#         pol1 = RegularPolygon(16).scale(2)
#         pol2 = Circle().stretch(1.2, 1).stretch(0.8, 0)
#         pol3 = RegularPolygon(5).scale(2).shift(LEFT*0.9)
#         pol4 = RegularPolygon(3).stretch(3, 1).shift(LEFT)
#         pol5 = Ellipse().scale(0.6).shift(LEFT).stretch(2, 0)
#         #start = time.perf_counter()
#         boolpol = PolygonSubtraction(
#             PolygonUnion(
#                 PolygonIntersection(
#                     PolygonSubtraction(
#                         pol1, pol2), pol3), pol4), pol5) \
#             .set_stroke(color=YELLOW, width=0).set_fill(color=YELLOW, opacity=0.5)
#         #end = time.perf_counter()
#         #print(end - start)#0.49910769999999993
#         self.add(pol1, pol2, pol3, pol4, pol5, boolpol)
#         '''
#

class Compass(VGroup):

    CONFIG = {
        'stroke_color': GREY_E,
        'fill_color': WHITE,
        'stroke_width': 2,
        'leg_length': 3,
        'leg_width': 0.12,
        'r': 0.2,
        'depth_test': True,
    }

    def __init__(self, span=2.5,  **kwargs):

        VGroup.__init__(self, **kwargs)
        self.span = span
        self.create_compass()


    # def create_compass_old(self):
    #
    #     s, l, r = self.span, self.leg_length, self.r
    #     theta = np.arcsin(s/2/l)
    #     arc = Arc(start_angle=-PI/2 + theta, angle=TAU-theta*2, radius=r, stroke_color=self.stroke_color, stroke_width=self.stroke_width*4)
    #     dot = Dot(color=self.stroke_color).set_height(self.stroke_width*8/100)
    #     leg_01 = Line(arc.get_center(), arc.get_center() + complex_to_R3(l * np.exp(1j * (-PI/2-theta))), stroke_color=self.stroke_color, stroke_width=self.stroke_width)
    #     leg_02 = Line(arc.get_center(), arc.get_center() + complex_to_R3(l * np.exp(1j * (-PI/2+theta))), stroke_color=self.stroke_color, stroke_width=self.stroke_width * 1)
    #     leg_11 = Line(arc.get_center(), arc.get_center() + complex_to_R3((l - r * 0.8) * np.exp(1j * (-PI/2-theta))), stroke_color=self.stroke_color, stroke_width=self.stroke_width * 4)
    #     leg_12 = Line(arc.get_center(), arc.get_center() + complex_to_R3((l - r * 0.8) * np.exp(1j * (-PI/2+theta))), stroke_color=self.stroke_color, stroke_width=self.stroke_width * 4)
    #     pen_point = Dot(color=self.stroke_color).set_height(self.stroke_width * 1/125).move_to(leg_02.get_end())
    #     leg_1, leg_2 = VGroup(leg_01, leg_11),  VGroup(leg_02, leg_12, pen_point)
    #     head = Line(UP * r, UP * (r + r * 1), stroke_color=self.stroke_color, stroke_width=self.stroke_width * 4)
    #
    #     self.add(arc, dot, head, leg_1, leg_2)
    #     self.move_to(ORIGIN)
    #
    #     return self

    def create_compass(self):

        s, l, r, w = self.span, self.leg_length, self.r, self.leg_width
        self.theta = np.arcsin(s/2/l)

        self.c = Circle(radius=r, fill_color=self.fill_color, fill_opacity=1, stroke_color=self.stroke_color, stroke_width=self.stroke_width*5)
        c2 = Circle(radius=r+self.stroke_width*5/100/2, fill_opacity=0, stroke_color=self.fill_color, stroke_width=self.stroke_width)

        self.leg_1 = Polygon(ORIGIN, l * RIGHT, (l-w*np.sqrt(3)) * RIGHT + w * DOWN, w * DOWN,
                             stroke_width=0, stroke_color=self.fill_color, fill_color=self.stroke_color,
                             fill_opacity=1).rotate(-PI/2-self.theta, about_point=self.c.get_center())
        self.leg_2 = Polygon(ORIGIN, l * RIGHT, (l-w*np.sqrt(3)) * RIGHT + w * UP, w * UP,
                             stroke_width=0, stroke_color=self.fill_color, fill_color=self.stroke_color,
                             fill_opacity=1).rotate(-PI/2+self.theta, about_point=self.c.get_center())


        # self.leg_1, self.leg_2 = VGroup(leg_01, leg_11),  VGroup(leg_02, leg_12, pen_point)
        h = Line(UP * r, UP * (r + r * 1.8), stroke_color=self.stroke_color, stroke_width=self.stroke_width*6)

        self.head = VGroup(h, self.c, c2)
        self.add(self.leg_1, self.leg_2, self.head)
        self.move_to(ORIGIN)

        return self

    def get_niddle_tip(self):
        return self.leg_1.get_vertices()[1]

    def get_pen_tip(self):
        return self.leg_2.get_vertices()[1]

    def move_niddle_tip_to(self, pos):
        self.shift(pos-self.get_niddle_tip())
        return self

    def rotate_about_niddle_tip(self, angle=PI/2):
        self.rotate(angle=angle, about_point=self.get_niddle_tip())

    def get_span(self):
        # return self.span 如果进行了缩放而self.span没变会有问题
        return get_norm(self.get_pen_tip() - self.get_niddle_tip())

    def set_span(self, s):
        self.span = s
        l, r, w = self.leg_length, self.r, self.leg_width
        theta_new, theta_old = np.arcsin(s/2/l), self.theta
        sign = np.sign(get_angle(R3_to_complex(self.leg_2.get_vertices()[1] - self.leg_2.get_vertices()[0])) - get_angle(R3_to_complex(self.leg_1.get_vertices()[1] - self.leg_1.get_vertices()[0])))
        rotate_angle = 2 * (theta_new - theta_old) * sign
        self.leg_2.rotate(rotate_angle, about_point=self.c.get_center())
        self.theta=theta_new
        self.head.rotate(rotate_angle/2, about_point=self.c.get_center())
        self.rotate_about_niddle_tip(-rotate_angle/2)
        return self

    def set_compass(self, center, pen_tip):
        self.move_niddle_tip_to(center)
        self.set_span(get_norm(pen_tip - center))
        self.rotate_about_niddle_tip(np.angle(R3_to_complex(pen_tip - center)) - np.angle(R3_to_complex(self.get_pen_tip() - center)))
        return self

    def set_compass_to_draw_arc(self, arc):
        return self.set_compass(arc.arc_center, arc.get_start())

    def reverse_tip(self):
        return self.flip(axis=self.head[0].get_end() - self.head[0].get_start(), about_point=self.c.get_center())

class DrawingScene(Scene):

    CONFIG = {
        'compass_config':{
            'stroke_color': GREY_E,
            'fill_color': WHITE,
            'stroke_width': 2,
            'leg_length': 3,
            'leg_width': 0.12,
            'r': 0.2,
            'depth_test': True,
        },
        'ruler_config':{
            'width': 10,
            'height': 0.8,
            'stroke_width': 8,
            'stroke_color': GREY_E,
            'stroke_opacity': 0.4,
            'fill_color': WHITE,
            'fill_opacity': 0.5,
        },
        'dot_config':{
            'radius': 0.06,
            'color': GREY_E,
        },
        'line_config':{
            'stroke_color': GREY_E,
            'stroke_width': 2.5,
        },
        'brace_config':{
            'fill_color': GREY_E,
            'buff':0.025,
        },
        'text_config':{
            'size': 0.6 * 5, # 5 times than the actual size and the sacle down
            'font': 'Cambria Math',
            'color': GREY_E,
        },
        'add_ruler': False,
    }

    def setup(self):
        self.cp = Compass(**self.compass_config)
        self.ruler = VGroup(Rectangle(**self.ruler_config).set_height(self.ruler_config['height'] - self.ruler_config['stroke_width']/2/100, stretch=True)\
                            .round_corners(self.ruler_config['height']/8),
                            Rectangle(**self.ruler_config).set_opacity(0))
        self.dot = Dot(**self.dot_config)

        self.cp.move_to(UP * 10)
        if self.add_ruler:
            self.ruler.move_to(DOWN * 10)
            self.add(self.ruler)
        self.add(self.cp)

        self.temp_points = []

    def construct(self):

        self.add(self.cp)
        self.play(self.cp.move_niddle_tip_to, ORIGIN, run_time=1)
        self.wait(0.3)
        self.set_span(3.6, run_time=1, rate_func=smooth)
        self.wait(0.5)
        self.set_compass(DL * 0.5, UR * 0.5, run_time=1, rate_func=there_and_back)
        arc = Arc(color=GREY_E)
        self.set_compass_to_draw_arc(arc)
        self.draw_arc_by_compass(arc)

        self.wait()

    def set_span(self, s, run_time=1, rate_func=smooth):

        s_old = self.cp.get_span()
        n = int(run_time * self.camera.frame_rate)
        dt = 1/self.camera.frame_rate
        t_series = np.linspace(1, n, n)/n
        # s_series = s_old + rate_func(t_series) * (s - s_old)
        s_series = [s_old + rate_func(t_series[i]) * (s - s_old) for i in range(n)]
        for i in range(n):
            self.cp.set_span(s_series[i])
            self.wait(dt)

    def set_compass_direction(self, start, end, run_time=1, rate_func=smooth):
        vect = end - start
        a = np.angle(R3_to_complex(vect))
        c_old, p_old = self.cp.get_niddle_tip(), self.cp.get_pen_tip()
        a_old = np.angle(R3_to_complex(p_old - c_old))
        n = int(run_time * self.camera.frame_rate)
        dt = 1/self.camera.frame_rate
        t_series = np.linspace(1, n, n)/n
        c_series = [c_old + rate_func(t_series[i]) * (start - c_old) for i in range(n)]
        delta_a = (a - a_old)/n
        for i in range(n):
            self.bring_to_front(self.cp)
            self.cp.move_niddle_tip_to(c_series[i])
            self.cp.rotate_about_niddle_tip(delta_a)
            self.wait(dt)

    def set_compass(self, center, pen_tip, run_time=1, rate_func=smooth, emphasize_dot=False):
        if emphasize_dot:
            run_time -= 0.15
        c_old, p_old = self.cp.get_niddle_tip(), self.cp.get_pen_tip()
        n = int(run_time * self.camera.frame_rate)
        dt = 1/self.camera.frame_rate
        t_series = np.linspace(1, n, n)/n
        # s_series = s_old + rate_func(t_series) * (s - s_old)
        c_series = [c_old + rate_func(t_series[i]) * (center - c_old) for i in range(n)]
        p_series = [p_old + rate_func(t_series[i]) * (pen_tip - p_old) for i in range(n)]

        for i in range(n):
            self.bring_to_front(self.cp)
            self.cp.set_compass(c_series[i], p_series[i])
            self.wait(dt)
        if emphasize_dot:
            self.emphasize_dot([center, pen_tip], run_time=0.15)

    def set_compass_(self, center, pen_tip, adjust_angle=0, run_time=1, rate_func=smooth, emphasize_dot=False):

        vect = center - pen_tip
        a = np.angle(R3_to_complex(vect)) + adjust_angle
        s = get_norm(vect)
        c_old, p_old, s_old = self.cp.get_niddle_tip(), self.cp.get_pen_tip(), self.cp.get_span()
        a_old = np.angle(R3_to_complex(p_old - c_old))
        if emphasize_dot:
            run_time -= 0.15
        n = int(run_time * self.camera.frame_rate)
        dt = 1/self.camera.frame_rate
        t_series = np.linspace(1, n, n)/n
        c_series = [c_old + rate_func(t_series[i]) * (center - c_old) for i in range(n)]
        delta_a = (a - a_old)/n
        s_series = [s_old + rate_func(t_series[i]) * (s - s_old) for i in range(n)]

        for i in range(n):
            self.bring_to_front(self.cp)
            self.cp.move_niddle_tip_to(c_series[i])
            self.cp.rotate_about_niddle_tip(delta_a)
            self.cp.set_span(s_series[i])
            self.wait(dt)
        if emphasize_dot:
            self.emphasize_dot([center, pen_tip], run_time=0.15)

    def set_compass_to_draw_arc(self, arc, **kwargs):
        self.set_compass(arc.arc_center, arc.get_start(), **kwargs)

    def set_compass_to_draw_arc_(self, arc, **kwargs):
        self.set_compass_(arc.arc_center, arc.get_start(), **kwargs)

    def draw_arc_by_compass(self, arc, is_prepared=True, run_time=1, rate_func=smooth, reverse=False, add_center=False, **kwargs):
        self.bring_to_front(self.cp)
        if not is_prepared: self.set_compass_to_draw_arc(arc, run_time=0.5)
        theta = arc.angle if not reverse else -1 * arc.angle
        self.play(Rotating(self.cp, angle=theta, about_point=self.cp.get_niddle_tip()), ShowCreation(arc), rate_func=rate_func, run_time=run_time)
        if add_center:
            d = Dot(self.cp.get_niddle_tip(), **self.dot_config).scale(0.5)
            self.temp_points.append(d)
            self.add(d)

    def emphasize_dot(self, pos, add_dot=False, size=1.2, run_time=0.2, **kwargs):
        if type(pos) == list:
            d = VGroup(*[Dot(pos[i], radius=size/2, color=GREY_C, fill_opacity=0.25).scale(0.25) for i in range(len(pos))])
        else:
            d = Dot(pos, radius=size/2, color=GREY_C, fill_opacity=0.25).scale(0.25)
        self.add(d)
        if type(pos) == list:
            self.play(d[0].scale, 4, d[1].scale, 4, rate_func=linear, run_time=run_time)
            
        else:
            self.play(d.scale, 4, rate_func=linear, run_time=run_time)

        self.remove(d)
        if add_dot:
            if type(pos) == list:
                dot = VGroup(*[Dot(pos[i],**kwargs) for i in range(len(pos))])
            else:
                dot = Dot(pos, **kwargs)
            self.add(dot)
            return dot

    def set_ruler(self, pos1, pos2, run_time=1, rate_func=smooth):
        p1, p2 = self.ruler[-1].get_vertices()[1], self.ruler[-1].get_vertices()[0]
        c12 = (p1 + p2) / 2
        center = (pos1 + pos2)/2
        self.bring_to_front(self.ruler)
        self.play(self.ruler.shift, center - c12, run_time=run_time/2, rate_func=rate_func)
        self.play(Rotating(self.ruler, angle=np.angle(R3_to_complex(pos2 - pos1)) - np.angle(R3_to_complex(p2 - p1)), about_point=center), run_time=run_time/2, rate_func=rate_func)

    def draw_line(self, pos1, pos2, is_prepared=True, run_time=1.2, rate_func=smooth, pre_time=0.8):
        if not is_prepared: self.set_ruler(pos1, pos2, run_time=pre_time)
        self.dot.move_to(pos1)
        self.emphasize_dot(pos1, run_time=0.15)
        self.add(self.dot)
        l = Line(pos1, pos2, **self.line_config)
        self.play(ShowCreation(l), self.dot.move_to, pos2, run_time=run_time-0.3, rate_func=rate_func)
        self.emphasize_dot(pos2, run_time=0.15)
        self.remove(self.dot)
        return l

    def draw_line_(self, l, is_prepared=True, run_time=1.2, rate_func=smooth):
        pos1, pos2 = l.get_start(), l.get_end()
        if not is_prepared: self.set_ruler(pos1, pos2, run_time=0.5)
        self.dot.move_to(pos1)
        self.emphasize_dot(pos1, run_time=0.15)
        self.add(self.dot)
        # l = Line(pos1, pos2, **self.line_config)
        self.play(ShowCreation(l), self.dot.move_to, pos2, run_time=run_time-0.3, rate_func=rate_func)
        self.emphasize_dot(pos2, run_time=0.15)
        self.remove(self.dot)
        return l

    def put_aside_ruler(self, direction=DOWN, run_time=0.5):
        self.bring_to_front(self.ruler)
        self.play(self.ruler.move_to, direction * 15, run_time=run_time)

    def put_aside_compass(self, direction=DOWN, run_time=0.5):
        self.bring_to_front(self.cp)
        self.play(self.cp.move_to, direction * 15, run_time=run_time)

    def get_length_label(self, p1, p2, text='', reverse_label=False, add_bg=False, bg_color=WHITE):
        l = Line(p1, p2)
        b = Brace(l, direction=complex_to_R3(np.exp(1j * (l.get_angle()+PI/2 * (1 -2 * float(reverse_label))))), **self.brace_config)
        t = Text(text, **self.text_config).scale(0.2)
        if add_bg:
            bg = SurroundingRectangle(t, fill_color=bg_color, fill_opacity=0.6, stroke_opacity=0).set_height(t.get_height() + 0.05, stretch=True).set_width(t.get_width() + 0.05, stretch=True)
            b.put_at_tip(bg, buff=0.0)
            b.put_at_tip(t, buff=0.05)
            return b, bg, t
        else:
            b.put_at_tip(t, buff=0.05)
            return b, t

    def set_compass_and_show_span(self, p1, p2, run_time=1, show_span_time=[0.4, 0.3, 0.9, 0.4], text='', reverse_label=False, add_bg=True, **kwargs):
        self.set_compass(p1, p2, run_time=run_time, **kwargs)
        bt = self.get_length_label(p1, p2, text=text, reverse_label=reverse_label, add_bg=add_bg)
        b, t = bt[0], bt[-1]
        st = show_span_time
        self.play(ShowCreation(b), run_time=st[0])
        if add_bg:
            self.add(bt[1])
            self.play(FadeIn(t), run_time=st[1])
        else:
            self.play(FadeIn(t), run_time=st[1])
        self.wait(st[2])
        self.play(FadeOut(VGroup(*bt)), run_time=st[3])
        return bt

    def set_compass_and_show_span_(self, p1, p2, run_time=1, show_span_time=[0.4, 0.3, 0.9, 0.4], text='', reverse_label=False, add_bg=True, **kwargs):
        self.set_compass_(p1, p2, run_time=run_time, **kwargs)
        bt = self.get_length_label(p1, p2, text=text, reverse_label=reverse_label)
        b, t = bt[0], bt[-1]
        st = show_span_time
        self.play(ShowCreation(b), run_time=st[0])
        if add_bg:
            self.add(bt[1])
            self.play(FadeIn(t), run_time=st[1])
        else:
            self.play(FadeIn(t), run_time=st[1])
        self.wait(st[2])
        self.play(FadeOut(VGroup(*bt)), run_time=st[3])
        return bt

    def highlight_on(self, *mobjects, to_front=True, stroke_config={'color': '#66CCFF', 'width': 4}, run_time=1, **kwargs):
        self.highlight = VGroup(*mobjects)
        self.play(self.highlight.set_stroke, stroke_config, run_time=run_time, **kwargs)
        if to_front:
            self.bring_to_front(self.highlight)
            self.bring_to_front(self.cp, self.ruler)

    def highlight_off(self, *mobjects):

        pass

    def show_arc_info(self, arc, time_list=[0.5, 0.2, 0.3]):

        c, r, s, a, ps, pe = arc.arc_center, arc.radius, arc.start_angle, arc.angle, arc.get_start(), arc.get_end()
        d_center = Dot(c, radius=0.08, color=PINK)
        r1, r2 = DashedLine(c, ps, stroke_width=3.5, stroke_color=PINK), DashedLine(c, pe , stroke_width=3.5, stroke_color=PINK)
        arc_new = Arc(arc_center=c, radius=r, start_angle=s, angle=a, stroke_width=8, stroke_color=RED)
        self.play(ShowCreation(arc_new), run_time=time_list[0])
        self.play(FadeIn(arc_new), run_time=time_list[1])
        self.play(ShowCreation(r1), ShowCreation(r2), run_time=time_list[2])

class Test_01(Scene):

    def construct(self):

        logo = Apple_logo()
        kl = logo.key_lines
        ol = logo.outline_by_arcs
        self.play(ShowCreation(kl), run_time=6)
        self.wait(0.25)
        # self.play(ShowCreation(ol), run_time=4)
        # self.wait(0.8)

        self.play(DrawBorderThenFill(logo.shape_1, stroke_width=logo.logo_stroke), run_time=3)
        self.play(DrawBorderThenFill(logo.shape_2, stroke_width=logo.logo_stroke), run_time=1.6)
        self.wait(0.2)
        self.play(Uncreate(kl), run_time=1.5)

        self.wait(2)

class Test_compass(Scene):

    def construct(self):
        coord = NumberPlane(axis_config={"stroke_color": GREY_D}, background_line_style={"stroke_color": BLUE_C},)
        self.add(coord)
        cp = Compass(stroke_color=PINK)
        c = Circle(radius=cp.get_span())
        self.add(cp)
        self.wait()
        self.play(cp.move_niddle_tip_to, ORIGIN, run_time=1)
        self.wait()

        self.bring_to_front(cp)
        self.play(Rotating(cp, about_point=cp.get_niddle_tip()), ShowCreation(c), rate_func=smooth, run_time=1.5)
        self.bring_to_front(cp)
        c1 = Circle(stroke_color=GREY_E)
        # self.play(cp.set_span, 1, run_time=1)
        # cp.set_span(1)
        # self.wait()
        # self.play(Rotating(cp, about_point=cp.get_niddle_tip()), ShowCreation(c1), rate_func=smooth, run_time=1.5)
        self.bring_to_front(cp)
        # self.play(cp.set_compass, DL * 2, UR * 2, run_time=1.5)
        cp.set_compass(DL * 2, UR * 2)

        self.wait(2)

class Test_1(DrawingScene):

    def construct(self):

        s = 0.5
        # axis = Axes(x_range=[-30, 30, 1], y_range=[-20, 20, 1], axis_config={"stroke_color": GREY_D, "stroke_width": 2.5, "stroke_opacity": 1},).scale(s)
        # logo = Apple_logo(create_shape=False, coord_center=ORIGIN, scale=s*2)
        # self.add(axis, logo.c1)
        c = Circle(color=BLACK)
        c1 = Circle(color=BLACK)
        c2 = Circle(color=BLACK)
        self.add(c, c1, c2)
        self.wait()
        self.play(ApplyMethod(c.shift, RIGHT * 4, run_time=1),
                  ApplyMethod(c1.shift, RIGHT * 4, run_time=2),
                  ApplyMethod(c2.shift, RIGHT * 4, run_time=4)
        )

class Step_0(DrawingScene):

    '''
    画出基本的直角坐标系作为辅助
    '''

    def construct(self):
        s = 0.5
        # coord = NumberPlane(x_range=[-15, 15, 1], y_range=[-15, 15, 1], axis_config={"stroke_color": GREY_D}, background_line_style={"stroke_color": BLUE_C},).scale(s)
        # logo = Apple_logo(create_shape=False, coord_center=ORIGIN, scale=s)
        self.cp.move_to(UP * 10)
        # self.add(coord)
        self.wait()
        self.play(FadeIn(self.ruler))

        l1 = self.draw_line(LEFT * 4.5, RIGHT * 4.5, is_prepared=False)
        self.put_aside_ruler()
        self.wait()

        arc_1 = Arc(arc_center=LEFT * 2, radius=3, start_angle=-PI/3, angle=2*PI/3, **self.line_config)
        arc_2 = Arc(arc_center=RIGHT * 2, radius=3, start_angle=2 * PI/3, angle=2*PI/3, **self.line_config)

        self.play(self.cp.move_to, ORIGIN)
        self.wait(0.2)
        self.set_compass_to_draw_arc(arc_1, emphasize_dot=True)
        self.draw_arc_by_compass(arc_1)
        self.wait(0.1)
        self.set_compass_to_draw_arc_(arc_2, adjust_angle=PI, emphasize_dot=True)
        self.draw_arc_by_compass(arc_2)
        self.wait(0.2)
        self.put_aside_compass()
        self.set_ruler(UP, DOWN)
        l2 = self.draw_line(UP * 3, DOWN * 3)
        self.put_aside_ruler(direction=LEFT)

        self.wait(0.6)
        self.play(FadeOut(arc_1), FadeOut(arc_2), l1.scale, 2, l2.scale, 2, run_time=1.2)
        self.wait(0.8)

        c1 = Circle(radius=1*s, **self.line_config)
        # c2_l = Circle(arc_center=6*s*LEFT, radius=5*s, **self.line_config)
        # c2_r = Arc(arc_center=6*s*RIGHT, radius=5*s, start_angle=PI, angle=-TAU, **self.line_config)
        self.set_compass_to_draw_arc(c1, run_time=1.2)
        self.wait(0.12)
        self.draw_arc_by_compass(c1)
        self.wait(0.2)
        arcs = VGroup(*[Arc(arc_center=i*s*RIGHT, radius=1*s, start_angle=-PI/6, angle=PI/3, **self.line_config) for i in range(1, 7)])
        for i in range(6):
            self.set_compass_to_draw_arc(arcs[i], run_time=0.32, emphasize_dot=False)
            self.draw_arc_by_compass(arcs[i], run_time=0.5)
        self.wait(0.6)
        axis = Axes(x_range=[-15, 15, 1], y_range=[-10, 10, 1], axis_config={"stroke_color": GREY_D, "stroke_width": 2.5}, ).scale(s)
        dot = Dot(color=GREY_E, radius=0.06)
        self.play(FadeIn(axis), FadeIn(dot), FadeOut(l1), FadeOut(l2), FadeOut(self.cp), FadeOut(arcs))
        self.wait(2)

class Step_1(DrawingScene):
    '''
    画出...
    '''
    def construct(self):

        s = 0.5
        axis = Axes(x_range=[-30, 30, 1], y_range=[-20, 20, 1], axis_config={"stroke_color": GREY_D, "stroke_width": 2.5, "stroke_opacity": 1},).scale(s)
        logo = Apple_logo(create_shape=False, coord_center=ORIGIN, scale=s*2)
        dot_config = {'color': GREY_E, 'radius': 0.06}
        d1 = Dot(**dot_config)
        self.add(axis, logo.c1, d1)
        self.wait()

        d5_l, d5_r = Dot(logo.c5_l.get_center(), **dot_config), Dot(logo.c5_r.get_center(), **dot_config)
        # self.set_compass_to_draw_arc(logo.c5_l, emphasize_dot=True)
        self.set_compass_and_show_span(logo.c5_l.get_center(), logo.c5_l.get_start(), reverse_label=True, text='r=5')
        self.wait(0.1)
        self.draw_arc_by_compass(logo.c5_l)
        self.cp.reverse_tip()
        logo.c5_r.flip()
        self.wait(0.15)

        self.add(d5_l)
        self.set_compass_to_draw_arc(logo.c5_r, emphasize_dot=True)
        # self.set_compass_to_draw_arc_(logo.c5_r, emphasize_dot=True)
        self.draw_arc_by_compass(logo.c5_r, reverse=True)

        self.wait(0.1)
        self.add(d5_r)
        self.put_aside_compass(direction=UP)
        self.wait(0.4)
        self.play(VGroup(*self.mobjects).scale, 0.6, {'about_point': ORIGIN}, run_time=1.2)
        self.play(VGroup(*self.mobjects).shift, UP * 2, run_time=1.2)

        # s_vg = VGroup(axis, logo.c5_l, logo.c5_r, logo.c1)
        # s_vg2 = logo.key_lines.remove(logo.c5_l, logo.c5_r, logo.c1)
        # self.play(s_vg.scale, 0.5, {'about_point': ORIGIN}, run_time=1.2)
        # s_vg2.scale(0.5, about_point=ORIGIN)
        # self.wait(0.4)
        # self.set_compass_(logo.c8_d.get_center(), logo.c8_d.get_start(), emphasize_dot=True)
        # # self.set_compass_to_draw_arc(logo.c8_d, emphasize_dot=True)
        # self.draw_arc_by_compass(logo.c8_d)

        self.wait(2)

class Step_11(DrawingScene):

    CONFIG = {
        'compass_config':{
            'stroke_color': GREY_E,
            'fill_color': WHITE,
            'stroke_width': 2,
            'leg_length': 4,
            'leg_width': 0.12,
            'r': 0.2,
            'depth_test': True,
        },
        'add_ruler': True,
    }

    def construct(self):

        s = 0.5 * 0.6
        axis = Axes(x_range=[-30, 30, 1], y_range=[-25, 25, 1], axis_config={"stroke_color": GREY_D, "stroke_width": 2.5, "stroke_opacity": 1},).scale(s).shift(UP * 2)
        logo = Apple_logo(create_shape=False, coord_center=UP * 2, scale=s*2)
        dot_config = {'color': GREY_E, 'radius': 0.03}
        d1 = Dot(logo.c1.get_center(), **dot_config)
        d5_l, d5_r = Dot(logo.c5_l.get_center(), **dot_config), Dot(logo.c5_r.get_center(), **dot_config)

        self.add(axis, logo.c1, logo.c5_l, logo.c5_r, d1, d5_l, d5_r)

        self.wait()
        self.cp.move_to(DOWN * 10)
        self.cp.rotate_about_niddle_tip(PI)

        arc_13_l = Arc(arc_center=logo.c5_l.get_center(), radius=13 * s, start_angle=3*PI/2, angle=PI/4, **self.line_config)
        arc_13_r = Arc(arc_center=logo.c5_r.get_center(), radius=13 * s, start_angle=3*PI/2-PI/4, angle=PI/4 + PI/2, **self.line_config)
        self.highlight_on(logo.c5_l, logo.c5_r)
        self.wait(0.15)
        self.set_compass_and_show_span(logo.c5_l.get_center(), logo.c5_l.get_center() + (5 + 8) * s * LEFT, reverse_label=True, text='r=5+8=13', run_time=1.4)
        self.wait(0.4)
        self.set_compass_to_draw_arc_(arc_13_l, adjust_angle=PI, rate_func=linear, run_time=0.6)
        self.draw_arc_by_compass(arc_13_l, rate_func=linear, run_time=0.3)
        self.wait(0.12)
        self.set_compass_(logo.c5_r.get_center(), logo.c5_r.get_center() + (5 + 8) * s * LEFT, adjust_angle=PI, emphasize_dot=True, run_time=1.4)
        self.wait(0.2)
        self.set_compass_to_draw_arc_(arc_13_r, adjust_angle=-PI, rate_func=linear, run_time=0.6)
        self.draw_arc_by_compass(arc_13_r, rate_func=linear, run_time=0.9)
        self.wait(0.6)

        self.set_compass_and_show_span(axis.c2p(11, 0), axis.c2p(19, 0), reverse_label=True, text='r=8', run_time=1.2)
        self.wait(0.15)
        self.set_compass_to_draw_arc_(logo.c8_d.scale(0.995), adjust_angle=-PI, run_time=1.)
        self.draw_arc_by_compass(logo.c8_d, run_time=1.2)
        d8_d = Dot(logo.c8_d.get_center(), **dot_config)
        self.add(d8_d)
        self.wait(0.2)
        self.put_aside_compass(UP * 0.5, run_time=1.)
        self.play(FadeOut(arc_13_l), FadeOut(arc_13_r))
        self.remove(self.cp)
        self.wait(0.4)
        self.play(logo.c5_r.set_stroke, {'color': GREY_E, 'width': 2.5}, logo.c5_l.set_stroke, {'color': GREY_E, 'width': 2.5}, run_time=0.6)
        self.wait(0.2)
        self.play(VGroup(*self.mobjects).shift, DOWN * 4, run_time=1.25)

        self.wait(2)

class Step_12(DrawingScene):

    def construct(self):

        s = 0.5 * 0.6
        axis = Axes(x_range=[-30, 30, 1], y_range=[-30, 30, 1], axis_config={"stroke_color": GREY_D, "stroke_width": 2.5, "stroke_opacity": 1},).scale(s).shift(DOWN * 2)
        logo = Apple_logo(create_shape=False, coord_center=DOWN * 2, scale=s*2)
        dot_config = {'color': GREY_E, 'radius': 0.03}
        d1 = Dot(logo.c1.get_center(), **dot_config)
        d5_l, d5_r = Dot(logo.c5_l.get_center(), **dot_config), Dot(logo.c5_r.get_center(), **dot_config)

        self.add(axis, logo.c1, logo.c5_l, logo.c5_r, logo.c8_d.scale(0.995), d1, d5_l, d5_r)
        self.set_compass_and_show_span(axis.c2p(0, 13), axis.c2p(0,0), emphasize_dot=True, reverse_label=True, text='r=13', run_time=2)
        self.wait(0.6)
        logo.c13.rotate(-PI/2)
        self.set_compass_to_draw_arc(logo.c13, emphasize_dot=True)
        self.wait(0.2)
        d13 = Dot(logo.c13.get_center(), **dot_config)
        a_13 = Arc(arc_center=logo.c8_d.get_center() + UP * 8 * s, start_angle=PI/2 + PI/20, radius=13 * s, angle=-PI/10, **self.line_config)

        self.cp.reverse_tip()
        self.set_compass_to_draw_arc(a_13, run_time=0.25)
        self.draw_arc_by_compass(a_13, run_time=0.5)
        self.add(d13)
        self.wait(0.25)
        self.put_aside_compass(RIGHT * 0.8, run_time=1.2)
        self.wait(0.6)
        self.play(VGroup(*self.mobjects).scale, 0.8, {'about_point': axis.c2p(0,0)}, run_time=1.2)

        self.wait(2)

class Step_2(DrawingScene):

    """
    画出辅助正方形
    """

    CONFIG = {
        'compass_config':{
            'stroke_color': GREY_E,
            'fill_color': WHITE,
            'stroke_width': 2,
            'leg_length': 4,
            'leg_width': 0.12,
            'r': 0.2,
            'depth_test': True,
        },
    }

    def construct(self):

        s = 0.5 * 0.6 * 0.8
        axis = Axes(x_range=[-40, 40, 1], y_range=[-36, 36, 1], axis_config={"stroke_color": GREY_D, "stroke_width": 2.5, "stroke_opacity": 1},).scale(s).shift(DOWN * 2)
        logo = Apple_logo(create_shape=False, coord_center=DOWN * 2, scale=s*2)
        dot_config = {'color': GREY_E, 'radius': 0.03}
        d1 = Dot(logo.c1.get_center(), **dot_config)
        d5_l, d5_r = Dot(logo.c5_l.get_center(), **dot_config), Dot(logo.c5_r.get_center(), **dot_config)
        a_13 = Arc(arc_center=logo.c8_d.get_center() + UP * 8 * s, start_angle=PI/2 + PI/30, radius=13 * s, angle=-PI/15, **self.line_config)
        d13 = Dot(logo.c13.get_center(), **dot_config)

        self.add(axis, logo.c1, logo.c5_l, logo.c5_r, logo.c8_d.scale(0.995), a_13, d1, d5_l, d5_r, d13)
        self.wait()

        self.play(FadeIn(self.ruler))
        self.wait(0.2)
        dl, dr = logo.c5_l.get_center() * 8/13 + logo.c8_d.get_center() * 5/13, logo.c5_r.get_center() * 8/13 + logo.c8_d.get_center() * 5/13
        self.set_ruler(dl, dr)
        self.emphasize_dot([dl, dr], run_time=0.2)
        # l = Line(dl + LEFT * 4.5, dr + RIGHT *4.5, **self.line_config)
        self.wait(0.5)
        l = self.draw_line(dl + LEFT * 3.6, dr + RIGHT * 3.6, run_time=1.25)
        self.put_aside_ruler(DOWN * 0.4)
        self.wait(0.1)
        dm = (dl+dr)/2
        self.set_compass(d13.get_center(), dm, emphasize_dot=True, run_time=1.5)
        self.wait(0.2)
        a_13_r = Arc(arc_center=dm, radius=self.cp.get_span(), start_angle=10 * DEGREES, angle=-20 * DEGREES, **self.line_config)
        a_13_l = Arc(arc_center=dm, radius=self.cp.get_span(), start_angle=190 * DEGREES, angle=-20 * DEGREES, **self.line_config)
        # a_13_u = Arc(arc_center=d13.get_center(), radius=self.cp.get_span(), start_angle=100 * DEGREES, angle=20 * DEGREES, **self.line_config)
        l_square = get_norm(d13.get_center()-dm)
        circle = Circle(arc_center=d13.get_center(), radius=l_square * np.sqrt(2), **self.line_config).rotate(-PI/4)

        self.cp.reverse_tip()
        self.set_compass_to_draw_arc_(a_13_l, adjust_angle=PI, run_time=0.64)
        self.draw_arc_by_compass(a_13_l, run_time=0.12, rate_func=linear)
        self.set_compass_to_draw_arc_(a_13_r, adjust_angle=PI, run_time=0.96, rate_func=linear)
        self.draw_arc_by_compass(a_13_r, run_time=0.12, rate_func=linear)
        self.wait(0.25)
        self.cp.reverse_tip()
        self.set_compass_to_draw_arc(circle, run_time=1.2, emphasize_dot=True)
        self.wait(0.15)
        self.draw_arc_by_compass(circle, run_time=1.6)
        self.wait(0.5)
        self.set_compass(dm + l_square * LEFT, dm + l_square * RIGHT, emphasize_dot=True)
        self.wait(0.2)
        self.cp.reverse_tip()
        arc_r = Arc(arc_center=dm + l_square * RIGHT, radius=l_square * 2, start_angle=100 * DEGREES, angle=-20 * DEGREES, **self.line_config)
        arc_l = Arc(arc_center=dm + l_square * LEFT, radius=l_square * 2, start_angle=80 * DEGREES, angle=20 * DEGREES, **self.line_config)

        # self.set_compass_to_draw_arc_(arc_r, adjust_angle=PI, run_time=0.6, rate_func=linear)
        self.play(Rotating(self.cp, angle=-80 * DEGREES, about_point=self.cp.get_niddle_tip(), rate_func=linear), run_time=0.6)
        self.draw_arc_by_compass(arc_r, run_time=0.15, rate_func=linear)
        self.wait(0.2)
        # self.set_compass_(dm + l_square * RIGHT, dm + l_square * LEFT, emphasize_dot=True)
        self.play(Rotating(self.cp, angle=100 * DEGREES, about_point=self.cp.get_niddle_tip()), run_time=0.8)
        self.emphasize_dot([self.cp.get_niddle_tip(), self.cp.get_pen_tip()], run_time=0.15)
        self.wait(0.2)
        self.cp.reverse_tip()
        self.set_compass_to_draw_arc_(arc_l, adjust_angle=PI, run_time=0.6, rate_func=linear)
        self.draw_arc_by_compass(arc_l, run_time=0.15, rate_func=linear)
        self.wait(0.2)
        self.put_aside_compass(LEFT)
        self.wait(0.6)

        dots = [dm + l_square * RIGHT, dm + l_square * (RIGHT + 2 * UP), dm + l_square * (LEFT + 2 * UP), dm + l_square * LEFT]
        # self.set_ruler(dots[0], dots[1])
        l_r = self.draw_line(dots[0], dots[1], is_prepared=False, pre_time=0.75)
        self.wait(0.2)
        l_u = self.draw_line(dots[1], dots[2], is_prepared=False, pre_time=0.75)
        self.wait(0.2)
        l_l = self.draw_line(dots[3], dots[2], is_prepared=False, pre_time=0.75)
        l_d = Line(dots[3], dots[0],**self.line_config)
        self.wait(0.18)
        self.put_aside_ruler(LEFT * 0.7)
        self.wait(0.9)
        self.play(Transform(l, l_d, run_time=0.9),
                  FadeOut(a_13_r, run_time=0.6),
                  # FadeOut(a_13, run_time=0.8),
                  FadeOut(a_13_l, run_time=0.8),
                  FadeOut(arc_r, run_time=1.),
                  FadeOut(arc_l, run_time=1.2),
                  FadeOut(circle, run_time=1.4)
                  )
        self.wait(0.75)
        self.play(VGroup(*self.mobjects).scale, 0.8, {'about_point': axis.c2p(0,0)})
        self.wait(2)

class Step_3(DrawingScene):

    CONFIG = {
        'add_ruler': True,
    }

    def construct(self):

        s = 0.5 * 0.6 * 0.8 * 0.8
        axis = Axes(x_range=[-40, 40, 1], y_range=[-36, 36, 1], axis_config={"stroke_color": GREY_D, "stroke_width": 2.5, "stroke_opacity": 1},).scale(s).shift(DOWN * 2)
        logo = Apple_logo(create_shape=False, coord_center=DOWN * 2, scale=s*2)
        dot_config = {'color': GREY_E, 'radius': 0.03}
        d1 = Dot(logo.c1.get_center(), **dot_config)
        d5_l, d5_r = Dot(logo.c5_l.get_center(), **dot_config), Dot(logo.c5_r.get_center(), **dot_config)
        a_13 = Arc(arc_center=logo.c8_d.get_center() + UP * 8 * s, start_angle=PI/2 + PI/30, radius=13 * s, angle=-PI/15, **self.line_config)
        d13 = Dot(logo.c13.get_center(), **dot_config)

        dl, dr = logo.c5_l.get_center() * 8/13 + logo.c8_d.get_center() * 5/13, logo.c5_r.get_center() * 8/13 + logo.c8_d.get_center() * 5/13
        dm = (dl+dr)/2
        l_square = get_norm(d13.get_center()-dm)
        dots = [dm + l_square * RIGHT, dm + l_square * (RIGHT + 2 * UP), dm + l_square * (LEFT + 2 * UP), dm + l_square * LEFT]
        square = Polygon(*dots, **self.line_config)
        before = VGroup(axis, logo.c1, logo.c5_l, logo.c5_r, logo.c8_d.scale(0.995), a_13, d1, d5_l, d5_r, d13, square)
        self.add(before)
        self.wait()

        dots = square.get_vertices()
        r1 = l_square * 0.7

        ### left part ###
        a_1 = Arc(arc_center=dots[2], radius=r1, start_angle=PI/3,  angle=-2 * PI/3, **self.line_config)
        a_2 = Arc(arc_center=(dots[1] +dots[2])/2, radius=r1, start_angle=2 * PI/3, angle=2 * PI/3, **self.line_config)
        self.cp.flip(axis=RIGHT)
        self.set_compass_to_draw_arc(a_1)
        self.draw_arc_by_compass(a_1)
        self.wait(0.15)
        self.cp.reverse_tip()
        self.set_compass_to_draw_arc_(a_2, adjust_angle=PI)
        self.draw_arc_by_compass(a_2)
        self.put_aside_compass(RIGHT * 0.8, run_time=0.64)

        pm = (dots[2] + (dots[1] +dots[2])/2)/2
        pu, pd = pm + 10 * s * UP, pm + 10 * s * DOWN

        l = self.draw_line(pu, pd, is_prepared=False, pre_time=0.72)
        self.wait(0.18)
        self.put_aside_ruler(LEFT * 0.65)
        logo.c8_l.rotate(PI/2)
        self.set_compass_and_show_span_(axis.c2p(0,0), axis.c2p(0,8), run_time=1.4, emphasize_dot=True, adjust_angle=PI, text='r=8', reverse_label=True, add_bg=True)
        self.wait(0.5)

        self.set_compass_to_draw_arc_(logo.c8_l, adjust_angle=PI, emphasize_dot=True)
        self.wait(0.2)
        self.draw_arc_by_compass(logo.c8_l, run_time=1.25, add_center=True)
        self.wait(0.2)
        self.put_aside_compass(LEFT * 0.64)
        self.wait(0.6)

        ### right part ### 同理直接copy吧
        a_3 = Arc(arc_center=(dots[1] + dots[2])/2, radius=r1, start_angle=PI/3,  angle=-2 * PI/3, **self.line_config)
        a_4 = Arc(arc_center=dots[1], radius=r1, start_angle=2 * PI/3, angle=2 * PI/3, **self.line_config)
        d8_r = Dot(logo.c8_r.get_center(), **dot_config)
        pm_r = (dots[1] + (dots[1] +dots[2])/2)/2
        pu_r, pd_r = pm_r + 10 * s * UP, pm_r + 10 * s * DOWN
        logo.c8_r.rotate(PI/2)
        l02 = Line(pu_r, pd_r, **self.line_config)
        right_part = VGroup(a_3, a_4, l02, logo.c8_r)
        right_part_ = right_part.copy().set_stroke(opacity=0.32).shift(l_square * LEFT)
        self.add(right_part_)
        self.play(right_part_.shift, l_square * RIGHT)
        self.wait(0.2)
        self.play(ShowCreation(a_3), run_time=0.8)
        self.play(ShowCreation(a_4), run_time=0.8)
        self.play(ShowCreation(l02), run_time=0.8)
        self.play(ShowCreation(logo.c8_r), FadeIn(d8_r))
        self.remove(right_part_)
        self.wait()

        self.play(FadeOut(a_4, run_time=0.6), FadeOut(l02, run_time=0.7), FadeOut(a_3, run_time=0.8),
                  FadeOut(a_2, run_time=0.9), FadeOut(l, run_time=1.), FadeOut(a_1, run_time=1.1),
                  )
        self.wait(0.8)
        self.play(VGroup(*self.mobjects).scale, 1.25, {'about_point': axis.c2p(0,0)})

        self.wait(2)

class Step_4(DrawingScene):

    CONFIG = {
            'add_ruler': True,
        }

    def construct(self):

        s = 0.5 * 0.6 * 0.8
        axis = Axes(x_range=[-45, 45, 1], y_range=[-36, 36, 1], axis_config={"stroke_color": GREY_D, "stroke_width": 2.5, "stroke_opacity": 1},).scale(s).shift(DOWN * 2)
        logo = Apple_logo(create_shape=False, coord_center=DOWN * 2, scale=s*2)
        dot_config = {'color': GREY_E, 'radius': 0.03}
        d1 = Dot(logo.c1.get_center(), **dot_config)
        d5_l, d5_r = Dot(logo.c5_l.get_center(), **dot_config), Dot(logo.c5_r.get_center(), **dot_config)
        a_13 = Arc(arc_center=logo.c8_d.get_center() + UP * 8 * s, start_angle=PI/2 + PI/30, radius=13 * s, angle=-PI/15, **self.line_config)
        d13 = Dot(logo.c13.get_center(), **dot_config)

        dl, dr = logo.c5_l.get_center() * 8/13 + logo.c8_d.get_center() * 5/13, logo.c5_r.get_center() * 8/13 + logo.c8_d.get_center() * 5/13
        dm = (dl+dr)/2
        l_square = get_norm(d13.get_center()-dm)
        dots = [dm + l_square * RIGHT, dm + l_square * (RIGHT + 2 * UP), dm + l_square * (LEFT + 2 * UP), dm + l_square * LEFT]
        square = Polygon(*dots, **self.line_config)

        d8_l, d8_r = Dot(logo.c8_l.get_center(), **dot_config), Dot(logo.c8_r.get_center(), **dot_config)
        before = VGroup(axis, logo.c1, logo.c5_l, logo.c5_r, logo.c8_l, logo.c8_r, logo.c8_d.scale(0.995), a_13, d1, d5_l, d5_r, d13, d8_l, d8_r, square)
        self.add(before)
        self.wait()

        # circle R=3
        self.highlight_on(logo.c8_l, logo.c5_l)
        self.wait(0.5)
        brace_r8 = self.set_compass_and_show_span(axis.c2p(-8, 0), axis.c2p(0, 0), emphasize_dot=True, run_time=1., reverse_label=True, text='r=5+3=8')
        self.set_compass(axis.c2p(-6-8, 0), axis.c2p(-6, 0))
        self.wait(0.1)
        self.cp.reverse_tip()
        arc_r8 = Arc(arc_center=logo.c5_l.get_center(), start_angle=PI, angle=-PI/2, radius=8 * s, **self.line_config)
        self.draw_arc_by_compass(arc_r8)
        self.wait(0.2)

        self.cp.reverse_tip()
        brace_r11 = self.set_compass_and_show_span(axis.c2p(-11, 0), axis.c2p(0, 0), emphasize_dot=True, run_time=1., reverse_label=True, text='r=8+3=11')
        # self.cp.reverse_tip()
        arc_r11 = Arc(arc_center=logo.c8_l.get_center(), start_angle=-PI/2-PI/3, angle=PI/3, radius=11 * s, **self.line_config)
        self.set_compass_to_draw_arc_(arc_r11, adjust_angle=-PI)
        self.wait(0.1)
        self.draw_arc_by_compass(arc_r11)
        self.wait(0.5)

        brace_r11 = self.set_compass_and_show_span(axis.c2p(-3, 0), axis.c2p(0, 0), emphasize_dot=True, run_time=1., reverse_label=True, text='r=3')
        self.set_compass_to_draw_arc(logo.c3_l)
        self.wait(0.1)
        self.draw_arc_by_compass(logo.c3_l, add_center=True, run_time=1.2)
        self.wait(0.4)
        self.put_aside_compass(direction=UP * 0.6)
        self.wait(0.1)
        self.play(FadeOut(arc_r8), FadeOut(arc_r11), run_time=1.2)
        self.play(logo.c5_l.set_stroke, {'color': GREY_E, 'width': 2.5}, logo.c8_l.set_stroke, {'color': GREY_E, 'width': 2.5}, run_time=0.6)
        self.wait(0.5)
        self.play(VGroup(*self.mobjects).scale, 0.7, {'about_point': axis.c2p(0,0)})

        self.wait(2)

class Step_41(DrawingScene):

    CONFIG = {
            'compass_config':{
                'stroke_color': GREY_E,
                'fill_color': WHITE,
                'stroke_width': 2,
                'leg_length': 4,
                'leg_width': 0.12,
                'r': 0.2,
                'depth_test': True,
            },
            'add_ruler': True,
        }

    def construct(self):

        s = 0.5 * 0.6 * 0.8 * 0.7
        axis = Axes(x_range=[-45, 45, 1], y_range=[-36, 36, 1], axis_config={"stroke_color": GREY_D, "stroke_width": 2.5, "stroke_opacity": 1},).scale(s).shift(DOWN * 2)
        logo = Apple_logo(create_shape=False, coord_center=DOWN * 2, scale=s*2)
        dot_config = {'color': GREY_E, 'radius': 0.03}
        d1 = Dot(logo.c1.get_center(), **dot_config)
        d5_l, d5_r = Dot(logo.c5_l.get_center(), **dot_config), Dot(logo.c5_r.get_center(), **dot_config)
        a_13 = Arc(arc_center=logo.c8_d.get_center() + UP * 8 * s, start_angle=PI/2 + PI/30, radius=13 * s, angle=-PI/15, **self.line_config)
        d13 = Dot(logo.c13.get_center(), **dot_config)

        dl, dr = logo.c5_l.get_center() * 8/13 + logo.c8_d.get_center() * 5/13, logo.c5_r.get_center() * 8/13 + logo.c8_d.get_center() * 5/13
        dm = (dl+dr)/2
        l_square = get_norm(d13.get_center()-dm)
        dots = [dm + l_square * RIGHT, dm + l_square * (RIGHT + 2 * UP), dm + l_square * (LEFT + 2 * UP), dm + l_square * LEFT]
        square = Polygon(*dots, **self.line_config)

        d8_l, d8_r = Dot(logo.c8_l.get_center(), **dot_config), Dot(logo.c8_r.get_center(), **dot_config)
        d3_l = Dot(logo.c3_l.get_center(), **dot_config)
        before = VGroup(axis, logo.c1, logo.c5_l, logo.c5_r, logo.c8_l, logo.c8_r, logo.c8_d.scale(0.995), logo.c3_l, a_13, d1, d5_l, d5_r, d13, d3_l, d8_l, d8_r, square)
        self.add(before)
        self.wait()

        ### circle R=24
        self.highlight_on(logo.c3_l, logo.c5_l)
        self.wait(0.5)
        brace_r11 = self.set_compass_and_show_span(axis.c2p(-21, 0), axis.c2p(0, 0), emphasize_dot=True, run_time=1., reverse_label=True, text='r=24-3=21')
        arc_r21 = Arc(arc_center=logo.c3_l.get_center(), angle=PI/6, radius=21 * s, **self.line_config)
        self.set_compass_to_draw_arc(arc_r21)
        self.wait(0.1)
        self.draw_arc_by_compass(arc_r21, run_time=0.6)
        self.wait(0.4)

        brace_r19 = self.set_compass_and_show_span(axis.c2p(-19, 0), axis.c2p(0, 0), emphasize_dot=True, run_time=1., reverse_label=True, text='r=24-5=19')
        arc_r19 = Arc(arc_center=logo.c5_l.get_center(), angle=75 * DEGREES, radius=19 * s, **self.line_config)
        self.set_compass_to_draw_arc(arc_r19)
        self.wait(0.1)
        self.draw_arc_by_compass(arc_r19, run_time=0.9)
        self.wait(0.4)

        brace_r24 = self.set_compass_and_show_span_(axis.c2p(-24, 0), axis.c2p(0, 0), adjust_angle=-PI, emphasize_dot=True, run_time=1., reverse_label=True, text='r=24')

        self.set_compass_to_draw_arc(logo.c24_r)
        self.wait(0.1)
        self.draw_arc_by_compass(logo.c24_r, add_center=True, run_time=1.2)

        self.wait(0.4)
        self.put_aside_compass(direction=UP * 0.6)
        self.wait(0.1)
        self.play(FadeOut(arc_r19), FadeOut(arc_r21), logo.c5_l.set_stroke, {'color': GREY_E, 'width': 2.5}, logo.c3_l.set_stroke, {'color': GREY_E, 'width': 2.5})
        self.wait(0.6)

        self.play(VGroup(*self.mobjects).scale, 1/0.7, {'about_point': axis.c2p(0,0)})

        self.wait(2)

class Step_42(DrawingScene):

    CONFIG = {
        'add_ruler': True,
    }

    def construct(self):

        s = 0.5 * 0.6 * 0.8
        axis = Axes(x_range=[-45, 45, 1], y_range=[-36, 36, 1], axis_config={"stroke_color": GREY_D, "stroke_width": 2.5, "stroke_opacity": 1},).scale(s).shift(DOWN * 2)
        logo = Apple_logo(create_shape=False, coord_center=DOWN * 2, scale=s*2)
        dot_config = {'color': GREY_E, 'radius': 0.03}
        d1 = Dot(logo.c1.get_center(), **dot_config)
        d5_l, d5_r = Dot(logo.c5_l.get_center(), **dot_config), Dot(logo.c5_r.get_center(), **dot_config)
        a_13 = Arc(arc_center=logo.c8_d.get_center() + UP * 8 * s, start_angle=PI/2 + PI/30, radius=13 * s, angle=-PI/15, **self.line_config)
        d13 = Dot(logo.c13.get_center(), **dot_config)

        dl, dr = logo.c5_l.get_center() * 8/13 + logo.c8_d.get_center() * 5/13, logo.c5_r.get_center() * 8/13 + logo.c8_d.get_center() * 5/13
        dm = (dl+dr)/2
        l_square = get_norm(d13.get_center()-dm)
        dots = [dm + l_square * RIGHT, dm + l_square * (RIGHT + 2 * UP), dm + l_square * (LEFT + 2 * UP), dm + l_square * LEFT]
        square = Polygon(*dots, **self.line_config)

        d8_l, d8_r = Dot(logo.c8_l.get_center(), **dot_config), Dot(logo.c8_r.get_center(), **dot_config)
        d3_l = Dot(logo.c3_l.get_center(), **dot_config)
        d24_r = Dot(logo.c24_r.get_center(), **dot_config)
        before = VGroup(axis, logo.c1, logo.c5_l, logo.c5_r, logo.c8_l, logo.c8_r, logo.c8_d.scale(0.995), logo.c3_l, logo.c24_r,
                        a_13, d1, d5_l, d5_r, d13, d3_l, d8_l, d8_r, d24_r, square)
        self.add(before)
        self.wait()

        ### circle R=12
        self.highlight_on(logo.c8_l, logo.c24_r)
        self.wait(0.5)
        brace_r12 = self.set_compass_and_show_span(axis.c2p(-12, 0), axis.c2p(0, 0), emphasize_dot=True, run_time=1., reverse_label=True, text='r=24-12=12')
        arc_r12 = Arc(arc_center=logo.c24_r.get_center(), start_angle=PI + PI/6, angle=-PI/3, radius=12 * s, **self.line_config)
        self.cp.reverse_tip()
        self.set_compass_to_draw_arc(arc_r12)
        self.wait(0.1)
        self.draw_arc_by_compass(arc_r12, run_time=0.75)
        self.wait(0.5)

        self.cp.reverse_tip()
        brace_r4 = self.set_compass_and_show_span(axis.c2p(-4, 0), axis.c2p(0, 0), emphasize_dot=True, run_time=1., reverse_label=True, text='r=12-8=4')
        arc_r4 = Arc(arc_center=logo.c8_l.get_center(), start_angle=-PI/2, angle=75 * DEGREES, radius=4 * s, **self.line_config)
        self.set_compass_to_draw_arc_(arc_r4, adjust_angle=-PI)
        self.wait(0.1)
        self.draw_arc_by_compass(arc_r4)
        self.wait(0.5)

        brace_r12 = self.set_compass_and_show_span_(axis.c2p(-12, 0), axis.c2p(0, 0), adjust_angle=-PI, emphasize_dot=True, run_time=1., reverse_label=True, text='r=12')

        self.set_compass_to_draw_arc(logo.c12_l)
        self.wait(0.1)
        self.draw_arc_by_compass(logo.c12_l, add_center=True)
        self.wait(0.4)
        self.put_aside_compass(direction=UP * 0.6)
        self.wait(0.1)
        self.play(FadeOut(arc_r12), FadeOut(arc_r4), run_time=1.4)
        self.play(logo.c8_l.set_stroke, {'color': GREY_E, 'width': 2.5}, logo.c24_r.set_stroke, {'color': GREY_E, 'width': 2.5}, run_time=0.6)
        self.wait(1)

        # 右侧同理
        self.highlight_on(logo.c8_r, logo.c5_r, run_time=0.8)
        self.wait(0.2)
        d3_r = Dot(logo.c3_r.get_center(), **dot_config)
        self.play(ShowCreation(logo.c3_r), FadeIn(d3_r), run_time=0.8)
        self.wait(0.2)
        self.play(logo.c8_r.set_stroke, {'color': GREY_E, 'width': 2.5}, logo.c5_r.set_stroke, {'color': GREY_E, 'width': 2.5}, run_time=0.4)
        self.wait(0.4)

        self.highlight_on(logo.c3_r, logo.c5_r, run_time=0.8)
        self.wait(0.2)
        self.play(ShowCreation(logo.c24_l), run_time=1.2)
        self.wait(0.2)
        self.play(logo.c3_r.set_stroke, {'color': GREY_E, 'width': 2.5}, logo.c5_r.set_stroke, {'color': GREY_E, 'width': 2.5}, run_time=0.4)
        self.wait(0.4)

        self.highlight_on(logo.c8_r, logo.c24_l, run_time=0.8)
        self.wait(0.2)
        d12_r = Dot(logo.c12_r.get_center(), **dot_config)
        self.play(ShowCreation(logo.c12_r), FadeIn(d12_r), run_time=1)
        self.wait(0.2)
        self.play(logo.c8_r.set_stroke, {'color': GREY_E, 'width': 2.5}, logo.c24_l.set_stroke, {'color': GREY_E, 'width': 2.5}, run_time=0.5)

        self.wait(2)

class Step_5(DrawingScene):

    # 画苹果的最后两个圆弧（不含叶子）

    def construct(self):

        s = 0.5 * 0.6 * 0.8
        axis = Axes(x_range=[-45, 45, 1], y_range=[-45, 45, 1], axis_config={"stroke_color": GREY_D, "stroke_width": 2.5, "stroke_opacity": 1},).scale(s).shift(DOWN * 2)
        logo = Apple_logo(create_shape=False, coord_center=DOWN * 2, scale=s*2)
        dot_config = {'color': GREY_E, 'radius': 0.03}
        d1 = Dot(logo.c1.get_center(), **dot_config)
        d5_l, d5_r = Dot(logo.c5_l.get_center(), **dot_config), Dot(logo.c5_r.get_center(), **dot_config)
        a_13 = Arc(arc_center=logo.c8_d.get_center() + UP * 8 * s, start_angle=PI/2 + PI/30, radius=13 * s, angle=-PI/15, **self.line_config)
        d13 = Dot(logo.c13.get_center(), **dot_config)

        dl, dr = logo.c5_l.get_center() * 8/13 + logo.c8_d.get_center() * 5/13, logo.c5_r.get_center() * 8/13 + logo.c8_d.get_center() * 5/13
        dm = (dl+dr)/2
        l_square = get_norm(d13.get_center()-dm)
        dots = [dm + l_square * RIGHT, dm + l_square * (RIGHT + 2 * UP), dm + l_square * (LEFT + 2 * UP), dm + l_square * LEFT]
        square = Polygon(*dots, **self.line_config)

        d8_l, d8_r = Dot(logo.c8_l.get_center(), **dot_config), Dot(logo.c8_r.get_center(), **dot_config)
        d3_l, d3_r = Dot(logo.c3_l.get_center(), **dot_config), Dot(logo.c3_r.get_center(), **dot_config)
        d12_l, d12_r = Dot(logo.c12_l.get_center(), **dot_config), Dot(logo.c12_r.get_center(), **dot_config)
        d24_r, d24_l = Dot(logo.c24_r.get_center(), **dot_config), Dot(logo.c24_l.get_center(), **dot_config)
        before = VGroup(axis, logo.c1, logo.c5_l, logo.c5_r, logo.c8_l, logo.c8_r, logo.c8_d.scale(0.995), logo.c3_l,
                        logo.c24_r, logo.c24_l, logo.c3_r, logo.c12_r, logo.c12_l,
                        a_13, d1, d5_l, d5_r, d13, d3_l, d3_r, d8_l, d8_r, d24_r, d24_l, d12_r, d12_l, square)
        self.add(before)
        self.wait()
        brace_r8 = self.set_compass_and_show_span_(axis.c2p(0, 0), axis.c2p(8, 0), adjust_angle=-PI, emphasize_dot=True, run_time=1.2, reverse_label=True, text='r=8')

        x1 = l_square - logo.c12_r.get_center()[0]
        y1 = np.sqrt((12*s) ** 2 - x1 ** 2)
        p1, p2 = logo.c12_r.get_center() + x1 * RIGHT - y1 * UP, logo.c12_r.get_center() + x1 * RIGHT + y1 * UP
        a8_d = Arc(arc_center=p1, angle=PI/2, radius=8*s, **self.line_config)
        a8_u = Arc(arc_center=p2, start_angle=-PI/2, angle=PI/2, radius=8*s, **self.line_config)

        self.set_compass_to_draw_arc(a8_d, run_time=0.8)
        self.wait(0.1)
        self.draw_arc_by_compass(a8_d, run_time=0.8)
        self.wait(0.5)

        self.set_compass_to_draw_arc_(a8_u, adjust_angle=PI, run_time=0.8)
        self.wait(0.1)
        self.draw_arc_by_compass(a8_u, run_time=0.8)
        self.wait(0.5)

        self.set_compass_to_draw_arc(logo.c8_01)
        self.wait(0.1)
        self.draw_arc_by_compass(logo.c8_01, run_time=1.2, add_center=True)
        self.wait(0.4)
        self.put_aside_compass(direction=UR * 0.6)
        self.wait(0.1)
        self.play(FadeOut(a8_u), FadeOut(a8_d), run_time=1.)
        self.wait()
        self.play(VGroup(*self.mobjects).shift, 3.5 * DOWN, run_time=1.25)

        self.wait(2)

class Step_51(DrawingScene):

    CONFIG = {
        'add_ruler': True,
    }

    def construct(self):

        s = 0.5 * 0.6 * 0.8
        axis = Axes(x_range=[-45, 45, 1], y_range=[-45, 45, 1], axis_config={"stroke_color": GREY_D, "stroke_width": 2.5, "stroke_opacity": 1},).scale(s).shift(DOWN * 5.5)
        logo = Apple_logo(create_shape=False, coord_center=DOWN * 5.5, scale=s*2)
        dot_config = {'color': GREY_E, 'radius': 0.03}
        d1 = Dot(logo.c1.get_center(), **dot_config)
        d5_l, d5_r = Dot(logo.c5_l.get_center(), **dot_config), Dot(logo.c5_r.get_center(), **dot_config)
        a_13 = Arc(arc_center=logo.c8_d.get_center() + UP * 8 * s, start_angle=PI/2 + PI/30, radius=13 * s, angle=-PI/15, **self.line_config)
        d13 = Dot(logo.c13.get_center(), **dot_config)

        dl, dr = logo.c5_l.get_center() * 8/13 + logo.c8_d.get_center() * 5/13, logo.c5_r.get_center() * 8/13 + logo.c8_d.get_center() * 5/13
        dm = (dl+dr)/2
        l_square = get_norm(d13.get_center()-dm)
        dots = [dm + l_square * RIGHT, dm + l_square * (RIGHT + 2 * UP), dm + l_square * (LEFT + 2 * UP), dm + l_square * LEFT]
        square = Polygon(*dots, **self.line_config)

        d8_l, d8_r = Dot(logo.c8_l.get_center(), **dot_config), Dot(logo.c8_r.get_center(), **dot_config)
        d3_l, d3_r = Dot(logo.c3_l.get_center(), **dot_config), Dot(logo.c3_r.get_center(), **dot_config)
        d12_l, d12_r = Dot(logo.c12_l.get_center(), **dot_config), Dot(logo.c12_r.get_center(), **dot_config)
        d24_r, d24_l = Dot(logo.c24_r.get_center(), **dot_config), Dot(logo.c24_l.get_center(), **dot_config)
        d8_01 = Dot(logo.c8_01.get_center(), **dot_config)
        before = VGroup(axis, logo.c1, logo.c5_l, logo.c5_r, logo.c8_l, logo.c8_r, logo.c8_d.scale(0.995), logo.c3_l,
                        logo.c24_r, logo.c24_l, logo.c3_r, logo.c12_r, logo.c12_l, logo.c8_01,
                        a_13, d1, d5_l, d5_r, d13, d3_l, d3_r, d8_l, d8_r, d24_r, d24_l, d12_r, d12_l, d8_01, square)
        self.add(before)
        self.wait()

        a16_l = Arc(arc_center=logo.c8_l.get_center(), start_angle=0, angle=PI/2, radius=16*s, **self.line_config)
        a16_r = Arc(arc_center=logo.c8_r.get_center(), start_angle=PI, angle=-PI/2, radius=16*s, **self.line_config)
        self.highlight_on(logo.c8_r, logo.c8_l)
        self.wait(0.2)
        brace_r16 = self.set_compass_and_show_span(logo.c8_l.get_center(), logo.c8_l.get_center()+16*RIGHT*s, emphasize_dot=True, run_time=1.2, reverse_label=True, text='r=8+8=16')
        self.wait(0.1)
        self.draw_arc_by_compass(a16_l)
        self.wait(0.25)
        self.set_compass_(logo.c8_r.get_center()+16*LEFT*s, logo.c8_r.get_center(), adjust_angle=-PI)
        self.cp.reverse_tip()
        self.wait(0.2)
        self.draw_arc_by_compass(a16_r)
        self.wait(0.4)
        self.set_compass_and_show_span(logo.c8_u.get_center(), logo.c8_u.get_center()+8*s*RIGHT, emphasize_dot=True, run_time=1.2, reverse_label=False, text='r=8')
        logo.c8_u.flip(axis=RIGHT)
        logo.c8_u.angle=-TAU
        self.draw_arc_by_compass(logo.c8_u.scale(0.995), run_time=1.2, add_center=True)
        self.wait(0.6)
        self.put_aside_compass(DOWN * 0.8)
        self.play(FadeOut(a16_r), FadeOut(a16_l), run_time=0.8)
        self.wait(0.2)
        self.play(logo.c8_r.set_stroke, {'color': GREY_E, 'width': 2.5}, logo.c8_l.set_stroke, {'color': GREY_E, 'width': 2.5}, run_time=0.5)
        self.wait(2)

class Step_6(DrawingScene):

    CONFIG = {
        'compass_config':{
            'stroke_color': GREY_E,
            'fill_color': WHITE,
            'stroke_width': 2,
            'leg_length': 3.2,
            'leg_width': 0.12,
            'r': 0.2,
            'depth_test': True,
        },
        'add_ruler': True,
    }

    def construct(self):

        s = 0.5 * 0.6 * 0.8
        axis = Axes(x_range=[-45, 45, 1], y_range=[-45, 45, 1], axis_config={"stroke_color": GREY_D, "stroke_width": 2.5, "stroke_opacity": 1},).scale(s).shift(DOWN * 5.5)
        logo = Apple_logo(create_shape=False, coord_center=DOWN * 5.5, scale=s*2)
        dot_config = {'color': GREY_E, 'radius': 0.03}
        d1 = Dot(logo.c1.get_center(), **dot_config)
        d5_l, d5_r = Dot(logo.c5_l.get_center(), **dot_config), Dot(logo.c5_r.get_center(), **dot_config)
        a_13 = Arc(arc_center=logo.c8_d.get_center() + UP * 8 * s, start_angle=PI/2 + PI/30, radius=13 * s, angle=-PI/15, **self.line_config)
        d13 = Dot(logo.c13.get_center(), **dot_config)

        dl, dr = logo.c5_l.get_center() * 8/13 + logo.c8_d.get_center() * 5/13, logo.c5_r.get_center() * 8/13 + logo.c8_d.get_center() * 5/13
        dm = (dl+dr)/2
        l_square = get_norm(d13.get_center()-dm)
        dots = [dm + l_square * RIGHT, dm + l_square * (RIGHT + 2 * UP), dm + l_square * (LEFT + 2 * UP), dm + l_square * LEFT]
        square = Polygon(*dots, **self.line_config)

        d8_l, d8_r = Dot(logo.c8_l.get_center(), **dot_config), Dot(logo.c8_r.get_center(), **dot_config)
        d3_l, d3_r = Dot(logo.c3_l.get_center(), **dot_config), Dot(logo.c3_r.get_center(), **dot_config)
        d12_l, d12_r = Dot(logo.c12_l.get_center(), **dot_config), Dot(logo.c12_r.get_center(), **dot_config)
        d24_r, d24_l = Dot(logo.c24_r.get_center(), **dot_config), Dot(logo.c24_l.get_center(), **dot_config)
        d8_01 = Dot(logo.c8_01.get_center(), **dot_config)
        d8_u = Dot(logo.c8_u.get_center(), **dot_config)
        before = VGroup(axis, logo.c1, logo.c5_l, logo.c5_r, logo.c8_l, logo.c8_r, logo.c8_d.scale(0.995), logo.c3_l,
                        logo.c24_r, logo.c24_l, logo.c3_r, logo.c12_r, logo.c12_l, logo.c8_01, logo.c8_u.scale(0.995),
                        a_13, d1, d5_l, d5_r, d13, d3_l, d3_r, d8_l, d8_r, d24_r, d24_l, d12_r, d12_l, d8_01, d8_u, square)
        self.add(before)
        self.wait()
        self.highlight_on(logo.c12_l, logo.c12_r)
        self.wait(0.15)
        l = Line(logo.c12_l.get_center(), logo.c12_r.get_center(), **self.line_config).scale(4.5)
        self.set_ruler(logo.c12_l.get_center(), logo.c12_r.get_center())
        self.wait(0.15)
        self.draw_line_(l)
        self.wait(0.15)
        self.put_aside_ruler(DOWN * 0.3, run_time=0.4)
        self.wait(0.2)
        self.set_compass_and_show_span(logo.c12_r.get_center(), logo.c12_r.get_start(), reverse_label=True, text='r=12')
        a12_l = Arc(arc_center=dots[2], start_angle=-PI/2, angle=PI/2, radius=12 * s, **self.line_config)
        self.set_compass_to_draw_arc_(a12_l, adjust_angle=-PI)
        self.wait(0.2)
        self.draw_arc_by_compass(a12_l)
        self.wait(0.2)
        self.set_compass_and_show_span(a12_l.get_start(), a12_l.get_end(), reverse_label=True, text='r=12*sqrt(2)')
        a12s2_l = Arc(arc_center=logo.c12_l.get_center()+LEFT * 12 * s, start_angle=PI/4-10 * DEGREES, angle=20*DEGREES, radius=12*np.sqrt(2)*s, **self.line_config)
        self.set_compass_to_draw_arc_(a12s2_l, adjust_angle=PI)
        self.wait(0.1)
        self.draw_arc_by_compass(a12s2_l, run_time=0.6)
        self.wait(0.2)
        a12s2_r = Arc(arc_center=logo.c12_r.get_center()+RIGHT * 12 * s, start_angle=PI*3/4-10 * DEGREES, angle=20*DEGREES, radius=12*np.sqrt(2)*s, **self.line_config)
        self.set_compass_to_draw_arc_(a12s2_r, adjust_angle=PI)
        self.wait(0.1)
        self.draw_arc_by_compass(a12s2_r, run_time=0.6)
        self.wait(0.2)
        self.put_aside_compass(DOWN * 0.5)
        p1, p2 = logo.c12_l.get_center() + UP * 12 * s, logo.c12_r.get_center() + UP * 12 * s
        l2 = Line(p1, p2, **self.line_config).scale(3)
        self.wait(0.25)
        self.set_ruler(p1, p2)
        self.wait(0.1)
        self.draw_line_(l2)
        self.wait(0.1)
        self.put_aside_ruler(DOWN * 0.5)
        self.wait(0.1)
        self.play(FadeOut(a12_l), FadeOut(a12s2_r), FadeOut(a12s2_l), run_time=0.9)
        self.wait(0.3)
        self.play(logo.c12_r.set_stroke, {'color': GREY_E, 'width': 2.5}, logo.c12_l.set_stroke, {'color': GREY_E, 'width': 2.5}, run_time=0.5)

        self.wait(2)

class Step_61(DrawingScene):

    CONFIG = {
        'add_ruler': True,
    }

    def construct(self):

        s = 0.5 * 0.6 * 0.8 # 0.24
        axis = Axes(x_range=[-45, 45, 1], y_range=[-45, 45, 1], axis_config={"stroke_color": GREY_D, "stroke_width": 2.5, "stroke_opacity": 1},).scale(s).shift(DOWN * 5.5)
        logo = Apple_logo(create_shape=False, coord_center=DOWN * 5.5, scale=s*2)
        dot_config = {'color': GREY_E, 'radius': 0.03}
        d1 = Dot(logo.c1.get_center(), **dot_config)
        d5_l, d5_r = Dot(logo.c5_l.get_center(), **dot_config), Dot(logo.c5_r.get_center(), **dot_config)
        a_13 = Arc(arc_center=logo.c8_d.get_center() + UP * 8 * s, start_angle=PI/2 + PI/30, radius=13 * s, angle=-PI/15, **self.line_config)
        d13 = Dot(logo.c13.get_center(), **dot_config)

        dl, dr = logo.c5_l.get_center() * 8/13 + logo.c8_d.get_center() * 5/13, logo.c5_r.get_center() * 8/13 + logo.c8_d.get_center() * 5/13
        dm = (dl+dr)/2
        l_square = get_norm(d13.get_center()-dm)
        dots = [dm + l_square * RIGHT, dm + l_square * (RIGHT + 2 * UP), dm + l_square * (LEFT + 2 * UP), dm + l_square * LEFT]
        square = Polygon(*dots, **self.line_config)

        d8_l, d8_r = Dot(logo.c8_l.get_center(), **dot_config), Dot(logo.c8_r.get_center(), **dot_config)
        d3_l, d3_r = Dot(logo.c3_l.get_center(), **dot_config), Dot(logo.c3_r.get_center(), **dot_config)
        d12_l, d12_r = Dot(logo.c12_l.get_center(), **dot_config), Dot(logo.c12_r.get_center(), **dot_config)
        d24_r, d24_l = Dot(logo.c24_r.get_center(), **dot_config), Dot(logo.c24_l.get_center(), **dot_config)
        d8_01 = Dot(logo.c8_01.get_center(), **dot_config)
        d8_u = Dot(logo.c8_u.get_center(), **dot_config)

        p1, p2 = logo.c12_l.get_center() + UP * 12 * s, logo.c12_r.get_center() + UP * 12 * s
        l = Line(p1, p2, **self.line_config).scale(3)

        before = VGroup(axis, logo.c1, logo.c5_l, logo.c5_r, logo.c8_l, logo.c8_r, logo.c8_d.scale(0.995), logo.c3_l,
                        logo.c24_r, logo.c24_l, logo.c3_r, logo.c12_r, logo.c12_l, logo.c8_01, logo.c8_u.scale(0.995),
                        a_13, d1, d5_l, d5_r, d13, d3_l, d3_r, d8_l, d8_r, d24_r, d24_l, d12_r, d12_l, l, d8_01, d8_u, square)
        self.add(before)
        self.wait()
        p3 = logo.c12_r.get_center()
        p4 = dots[1] * 0.75 + dots[2] * 0.25
        p5 = p3 + (p4-p3) * 12 * s / (p4-p3)[1]
        p6 = p3 + (p4-p3) * 15 * s / (p4-p3)[1]
        self.set_ruler(p3, p6)
        self.wait(0.15)
        self.draw_line(p3, p6)
        self.wait(0.15)
        self.put_aside_ruler(DR * 0.6)
        self.wait(0.2)
        self.set_compass_and_show_span(logo.c8_r.get_center(), logo.c8_r.get_start(), reverse_label=True, text='r=8')
        self.set_compass_to_draw_arc(logo.c8_02)
        self.wait(0.2)
        self.draw_arc_by_compass(logo.c8_02, add_center=True)
        self.wait(0.25)
        a8 = Arc(arc_center=p5+LEFT * 8 * s, angle=PI/2 * 0.75, radius=8 * s, **self.line_config)
        self.set_compass_to_draw_arc(a8)
        self.wait(0.2)
        self.draw_arc_by_compass(a8)
        self.wait(0.1)
        self.put_aside_compass(LEFT * 0.6)
        l_120 = Line(p5, p5 + 4 * complex_to_R3(np.exp(1j * PI * 2/3)), **self.line_config)
        self.wait(0.1)
        self.set_ruler(p5, p5 + 4 * complex_to_R3(np.exp(1j * PI * 2/3)))
        self.wait(0.15)
        self.draw_line_(l_120)
        self.wait(0.1)
        self.put_aside_ruler(UR * 0.6)
        self.wait(0.15)
        a_u = Arc(arc_center=p5+LEFT*p5[0]+np.sqrt(3)*UP*p5[0], start_angle=-PI/2-10*DEGREES, angle=50*DEGREES, **self.line_config)
        a_d = Arc(arc_center=logo.c8_u.get_center(), start_angle=-PI/2-10*DEGREES, angle=50*DEGREES, **self.line_config)
        self.cp.rotate(PI*2/3)
        self.set_compass_to_draw_arc(a_u)
        self.wait(0.1)
        self.draw_arc_by_compass(a_u, run_time=0.75)
        self.wait(0.2)
        self.set_compass_to_draw_arc(a_d, run_time=0.6)
        self.wait(0.1)
        self.draw_arc_by_compass(a_d, run_time=0.75)
        self.wait(0.25)
        d01, d02 = a_u.arc_center + 1 * DOWN, a_u.arc_center + 1 * complex_to_R3(np.exp(-1j*PI/3))
        self.set_compass(d02, d01)
        self.wait(0.3)
        d11, d12 = a_d.arc_center + 1 * DOWN, a_d.arc_center + 1 * complex_to_R3(np.exp(-1j*PI/3))
        arc = Arc(arc_center=d11, start_angle=PI/6, angle=-PI/6, radius=get_norm(d12-d11), **self.line_config)
        self.cp.reverse_tip()
        self.set_compass_to_draw_arc_(arc, adjust_angle=PI)
        self.wait(0.1)
        self.draw_arc_by_compass(arc, run_time=0.4)
        self.wait(0.2)
        self.put_aside_compass(DOWN * 0.6)
        self.wait(0.2)

        vect = complex_to_R3(np.exp(1j * PI * 2/3))
        p01, p02 = logo.c8_u.get_center() + vect * 1.2, logo.c8_u.get_center() - vect * 2
        l_120_ = Line(p01, p02, **self.line_config)

        self.set_ruler(p02, p01)
        self.wait(0.15)
        self.draw_line_(l_120_)
        self.wait(0.15)
        self.put_aside_ruler(UR * 0.5)
        self.wait(0.4)

        circle = Arc(arc_center=logo.c8_03.get_center(), radius=8*s, start_angle=-PI/3, angle=-TAU, **self.line_config)
        self.set_compass_to_draw_arc(circle, emphasize_dot=True)
        self.wait(0.25)
        self.draw_arc_by_compass(circle, add_center=True)
        self.wait(0.2)
        self.put_aside_compass(DL * 0.7)
        self.wait(0.2)
        self.play(FadeOut(l_120), FadeOut(a_u), FadeOut(a_d), FadeOut(arc), FadeOut(a8), run_time=1)
        self.wait(0.8)
        self.play(VGroup(*self.mobjects).shift, UP * 3.25, run_time=0.8)
        self.play(VGroup(*self.mobjects).scale, 0.18/0.24, {'about_point': axis.c2p(0,0)}, run_time=1)

        self.wait(2)

class Step_7(DrawingScene):

    CONFIG = {
        'add_ruler': True,
    }

    def construct(self):

        s = 0.18
        axis = Axes(x_range=[-45, 45, 1], y_range=[-45, 45, 1], axis_config={"stroke_color": GREY_D, "stroke_width": 2.5, "stroke_opacity": 1},).scale(s).shift(DOWN * 2.25)
        logo = Apple_logo(create_shape=False, coord_center=DOWN * 2.25, scale=s*2)
        dot_config = {'color': GREY_E, 'radius': 0.024}
        d1 = Dot(logo.c1.get_center(), **dot_config)
        d5_l, d5_r = Dot(logo.c5_l.get_center(), **dot_config), Dot(logo.c5_r.get_center(), **dot_config)
        a_13 = Arc(arc_center=logo.c8_d.get_center() + UP * 8 * s, start_angle=PI/2 + PI/30, radius=13 * s, angle=-PI/15, **self.line_config)
        d13 = Dot(logo.c13.get_center(), **dot_config)

        dl, dr = logo.c5_l.get_center() * 8/13 + logo.c8_d.get_center() * 5/13, logo.c5_r.get_center() * 8/13 + logo.c8_d.get_center() * 5/13
        dm = (dl+dr)/2
        l_square = get_norm(d13.get_center()-dm)
        dots = [dm + l_square * RIGHT, dm + l_square * (RIGHT + 2 * UP), dm + l_square * (LEFT + 2 * UP), dm + l_square * LEFT]
        square = Polygon(*dots, **self.line_config)

        d8_l, d8_r = Dot(logo.c8_l.get_center(), **dot_config), Dot(logo.c8_r.get_center(), **dot_config)
        d3_l, d3_r = Dot(logo.c3_l.get_center(), **dot_config), Dot(logo.c3_r.get_center(), **dot_config)
        d12_l, d12_r = Dot(logo.c12_l.get_center(), **dot_config), Dot(logo.c12_r.get_center(), **dot_config)
        d24_r, d24_l = Dot(logo.c24_r.get_center(), **dot_config), Dot(logo.c24_l.get_center(), **dot_config)
        d8_01, d8_02, d8_03 = Dot(logo.c8_01.get_center(), **dot_config), Dot(logo.c8_02.get_center(), **dot_config), Dot(logo.c8_03.get_center(), **dot_config)
        d8_u = Dot(logo.c8_u.get_center(), **dot_config)

        p1, p2 = logo.c12_l.get_center() + UP * 12 * s, logo.c12_r.get_center() + UP * 12 * s
        p3 = logo.c12_r.get_center()
        p4 = dots[1] * 0.75 + dots[2] * 0.25
        p5 = p3 + (p4-p3) * 12 * s / (p4-p3)[1]
        p6 = p3 + (p4-p3) * 15 * s / (p4-p3)[1]
        l1 = Line(p1, p2, **self.line_config).scale(3)
        l2 = Line(p3, p6, **self.line_config)
        vect = complex_to_R3(np.exp(1j * PI * 2/3))
        p01, p02 = logo.c8_u.get_center() + vect * 1.2 * 18/24, logo.c8_u.get_center() - vect * 2 * 18/24
        l3 = Line(p01, p02, **self.line_config)
        logo.c8_d.scale(0.995), logo.c8_u.scale(0.995)
        logo.key_lines.remove(logo.c13)
        before = VGroup(axis, logo.key_lines, a_13, d1, d5_l, d5_r, d13, d3_l, d3_r, d8_l, d8_r, d24_r, d24_l, d12_r, d12_l,
                        l1, l2, l3, d8_01, d8_02, d8_03, d8_u, square)
        self.add(before)
        self.wait()

        # for i in range(4):
        #     self.show_arc_info(logo.outline_by_arcs[i])

        self.play(ShowCreation(logo.outline_by_arcs), rate_func=smooth, run_time=12)
        self.wait(0.8)
        logo.set_logo_shape()

        self.play(FadeIn(logo[-2]), FadeIn(logo[-1]), run_time=1.6)
        self.wait(0.8)
        self.play(FadeOut(before))

        self.wait(2)


# class Intro_01(DrawingScene):
#
#     def construct(self):
#
#         pass

class Perpendicular_bisector(DrawingScene):

    CONFIG = {
        'compass_config':{
            'stroke_color': GREY_E,
            'fill_color': WHITE,
            'stroke_width': 2,
            'leg_length': 3.6,
            'leg_width': 0.12,
            'r': 0.2,
            'depth_test': True,
        },
        'add_ruler': True,
    }

    def construct(self):

        l = Line(LEFT * 3, RIGHT * 3, stroke_width=8, stroke_color='#66CCFF')
        d1, d2 = Dot(l.get_start(), color=GREY_C).set_height(0.2), Dot(l.get_end(), color=GREY_C).set_height(0.2)
        self.add(l, d1, d2)
        self.wait()
        self.set_compass(l.get_start(), l.get_start()+RIGHT*2)
        self.wait(0.1)
        self.set_compass(l.get_start(), l.get_start()+RIGHT*4, run_time=0.75)
        self.wait(0.1)
        arc_l = Arc(arc_center=l.get_start(), start_angle=-60*DEGREES, angle=120*DEGREES, radius=4, **self.line_config)
        arc_r = Arc(arc_center=l.get_end(),   start_angle=120*DEGREES, angle=120*DEGREES, radius=4, **self.line_config)
        self.set_compass_to_draw_arc_(arc_l, adjust_angle=-PI, run_time=0.6)
        self.wait(0.1)
        self.draw_arc_by_compass(arc_l)
        self.wait(0.3)
        self.set_compass_to_draw_arc_(arc_r, adjust_angle=PI, run_time=0.6)
        self.wait(0.1)
        self.draw_arc_by_compass(arc_r)
        self.wait(0.1)
        self.put_aside_compass(DR * 0.6)
        self.wait(0.6)
        p1, p2 = np.sqrt(7) * UP, np.sqrt(7) * DOWN
        self.set_ruler(p1, p2)
        self.emphasize_dot([p1,p2], run_time=0.25)
        self.wait(0.2)
        l = Line(p1, p2, **self.line_config).scale(1.25).set_color(PINK)
        self.draw_line_(l)
        self.wait(0.1)
        self.put_aside_ruler(LEFT * 0.7)
        center = Dot((p1+p2)/2, color=RED).set_height(0.15)
        angle_90 = Square(0.32, stroke_width=2.5, stroke_color=GREY_C).shift(UR * 0.16)
        self.bring_to_back(angle_90)
        self.add(center)
        self.play(WiggleOutThenIn(center), FadeIn(angle_90), run_time=0.64)

        self.wait(2)


class Tangent_circle(DrawingScene):

    CONFIG = {
        'compass_config':{
            'stroke_color': GREY_E,
            'fill_color': WHITE,
            'stroke_width': 2,
            'leg_length': 4.05,
            'leg_width': 0.12,
            'r': 0.2,
            'depth_test': True,
        },
        'add_ruler': True,
    }

    def construct(self):
        s = 0.7
        p0 = DOWN * 1.5
        c1 = Circle(arc_center=3*LEFT*s+p0, radius=1*s, stroke_width=5, stroke_color='#66CCFF')
        c2 = Circle(arc_center=3*RIGHT*s+p0, radius=(3*np.sqrt(3)-2)*s, stroke_width=5, stroke_color='#66CCFF')
        l = Line(LEFT * 3*s+p0, RIGHT * 3*s+p0, stroke_width=4, stroke_color=GREY_E)
        d1, d2 = Dot(3*LEFT*s+p0, color=GREY_C).set_height(0.2), Dot(3*RIGHT*s+p0, color=GREY_C).set_height(0.2)


        self.add(c1, c2, l, d1, d2)
        self.wait()
        self.set_compass_and_show_span(c1.get_start(), c1.get_start() + 2*RIGHT*s, show_span_time=[0.4, 0.25, 0.6, 0.3], text='r', reverse_label=True)
        self.set_compass(c1.get_center(), c1.get_start() + 2*RIGHT*s, run_time=0.4)
        arc_l = Arc(arc_center=c1.get_center(), radius=3*s, angle=75 * DEGREES, **self.line_config)
        self.wait(0.14)
        self.draw_arc_by_compass(arc_l, run_time=0.6)
        self.wait(0.25)
        self.set_compass_and_show_span(c2.get_center()+3*np.sqrt(3)*s*LEFT, c2.get_center()+(3*np.sqrt(3)-2)*s*LEFT, show_span_time=[0.3, 0.25, 0.6, 0.3], text='r', reverse_label=True)
        self.set_compass(c2.get_center()+3*np.sqrt(3)*s*LEFT, c2.get_center(), run_time=0.4)
        arc_r = Arc(arc_center=c2.get_center(), radius=3*np.sqrt(3)*s, start_angle=PI, angle=-36 * DEGREES, **self.line_config)
        self.cp.reverse_tip()
        self.wait(0.1)
        self.draw_arc_by_compass(arc_r, run_time=0.6)
        self.wait(0.2)
        self.cp.reverse_tip()
        self.set_compass(c2.get_center()+3*np.sqrt(3)*s*LEFT, c2.get_center()+(3*np.sqrt(3)-2)*s*LEFT)
        self.wait(0.3)
        circle = Circle(arc_center=LEFT * 1.5 * s + UP * 1.5 * np.sqrt(3) * s + p0, radius=2*s, stroke_color=RED, stroke_width=4)
        self.set_compass_to_draw_arc(circle, run_time=0.4)
        self.wait(0.1)
        self.draw_arc_by_compass(circle, run_time=0.8, add_center=True)
        self.wait(0.08)
        self.put_aside_compass(UP * 0.6)

        self.wait(2)

class Equal_angle(DrawingScene):

    CONFIG = {
        'add_ruler': True,
    }

    def construct(self):

        p0 = LEFT * 4.5 + DOWN * 1.5
        p1, p2 = p0 + UR * 4/np.sqrt(2), p0 + 4 * complex_to_R3(np.exp(1j * 15 * DEGREES))
        p_0 = RIGHT* 0.5 + DOWN * 1.5
        p_1, p_2 = p_0 + 4 * complex_to_R3(np.exp(1j * 30 * DEGREES)), p_0 + 4 * RIGHT
        l1 = Line(p0, p1, stroke_width=5, stroke_color='#66CCFF')
        l2 = Line(p0, p2, stroke_width=5, stroke_color='#66CCFF')
        d0 = Dot(p0, color=GREY_C).set_height(0.18)

        l_1 = Line(p_0, p_1, stroke_width=4, stroke_color=RED)
        l_2 = Line(p_0, p_2, stroke_width=5, stroke_color=GREY_E)
        d_0 = Dot(p_0, color=GREY_E).set_height(0.1)

        self.add(l1, l2, d0, d_0,l_2)
        self.wait()
        arc_l = Arc(arc_center=p0, radius=2.5, angle=PI/3, **self.line_config)
        arc_r = Arc(arc_center=p_0, radius=2.5, angle=PI/3, start_angle=-PI/12, **self.line_config)
        self.set_compass_to_draw_arc(arc_l, run_time=0.6)
        self.wait(0.2)
        self.draw_arc_by_compass(arc_l, run_time=0.64)
        self.wait(0.3)
        self.set_compass_to_draw_arc(arc_r, run_time=0.5)
        self.wait(0.2)
        self.draw_arc_by_compass(arc_r, run_time=0.64)
        self.wait(0.3)
        p3, p4 = p0+2.5*complex_to_R3(np.exp(1j*15*DEGREES)), p0+2.5*complex_to_R3(np.exp(1j*45*DEGREES))
        p_3, p_4 = p_0+2.5*complex_to_R3(np.exp(1j*30*DEGREES)), p_0+2.5*RIGHT
        self.set_compass(p4, p3, run_time=0.8, emphasize_dot=True)
        self.wait(0.2)
        self.set_compass_(p_4, p_3, run_time=0.5, adjust_angle=PI)
        self.wait(0.2)
        arc = Arc(arc_center=p_4, start_angle=85 * DEGREES, angle=40*DEGREES, radius=get_norm(p_3 - p_4), **self.line_config)
        self.set_compass_to_draw_arc_(arc, run_time=0.25, adjust_angle=PI)
        self.draw_arc_by_compass(arc, run_time=0.45)
        self.wait(0.15)
        self.put_aside_compass(DOWN * 0.6)
        self.wait(0.2)
        self.set_ruler(p_0, p_3, run_time=0.6)
        self.wait(0.12)
        self.draw_line_(l_1, run_time=0.6)
        self.bring_to_front(d_0)
        self.wait(0.12)
        self.put_aside_ruler(DR * 0.6)
        self.wait(0.2)

        a1 = Arc(arc_center=p0, radius=0.5, start_angle=PI/12, angle=PI/6, stroke_color=PINK, stroke_width=8, stroke_opacity=0.8)
        a2 = Arc(arc_center=p_0, radius=0.5, start_angle=0, angle=PI/6, stroke_color=PINK, stroke_width=8, stroke_opacity=0.8)
        self.play(ShowCreation(a1), ShowCreation(a2), run_time=0.75)

        self.wait(2)



