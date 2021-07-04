from manimlib.imports import *

# utils
get_angle = lambda c: np.angle(-c) + PI if not c/abs(c) == 1 else 0
convert_angle = lambda a: a if a>=0 else a + TAU

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
        }, # to define size and style of the compass
        'ruler_config':{
            'width': 10,
            'height': 0.8,
            'stroke_width': 8,
            'stroke_color': GREY_E,
            'stroke_opacity': 0.4,
            'fill_color': WHITE,
            'fill_opacity': 0.5,
        }, # to define size and style of the ruler
        'dot_config':{
            'radius': 0.06,
            'color': GREY_E,
        }, # to define size and color of the dot (e.g., dot in arc/circle's center)
        'line_config':{
            'stroke_color': GREY_E,
            'stroke_width': 2.5,
        }, # the default line style drawing by ruler (not the defualt arc style drawing by compass)
        'brace_config':{
            'fill_color': GREY_E,
            'buff':0.025,
        },
        'text_config':{
            'size': 0.6 * 5, # 5 times than the actual size here and
                             # will be sacle down to the actual size later
                             # in 'get_length_label' methods.
            'font': 'Cambria Math',
            'color': GREY_E,
        },
        'add_ruler': False, # whether to add ruler into the scene at very begining
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

class CompassAndRulerScene(DrawingScene):

    # just rename `DrawingScene`
    pass
