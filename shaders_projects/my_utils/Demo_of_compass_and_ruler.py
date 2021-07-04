from manimlib.imports import *
from my_projects.active_projects.compass_and_ruler_scene import *

class Perpendicular_bisector(CompassAndRulerScene):

    CONFIG = {
        'compass_config':{
            'leg_length': 3.6,
        },
        'add_ruler': True, # add ruler when the scene starts
    }

    def construct(self):

        # built a line and we'll draw its perpendicular bisector
        l = Line(LEFT * 3, RIGHT * 3, stroke_width=8, stroke_color='#66CCFF')
        # start and end dots of the line
        d1, d2 = Dot(l.get_start(), color=GREY_C).set_height(0.2), Dot(l.get_end(), color=GREY_C).set_height(0.2)
        # add line and dots into the scene
        self.add(l, d1, d2)
        self.wait()
        # move compass to the right place: the niddle tip in 'l.get_start()' and the pen tip in 'l.get_start()'
        self.set_compass(l.get_start(), l.get_start()+RIGHT*2)
        self.wait(0.1)
        # change the position of the tip
        self.set_compass(l.get_start(), l.get_start()+RIGHT*4, run_time=0.75)
        self.wait(0.1)
        # create the two arcs
        arc_l = Arc(arc_center=l.get_start(), start_angle=-60*DEGREES, angle=120*DEGREES, radius=4, **self.line_config)
        arc_r = Arc(arc_center=l.get_end(),   start_angle=120*DEGREES, angle=120*DEGREES, radius=4, **self.line_config)
        # adjust the compass state to prepare for drawing of the left arc
        self.set_compass_to_draw_arc_(arc_l, adjust_angle=-PI, run_time=0.6)
        self.wait(0.1)
        # rotate the compass and draw the left arc
        self.draw_arc_by_compass(arc_l)
        self.wait(0.3)
        # adjust the compass state to prepare for the drawing of the right arc
        self.set_compass_to_draw_arc_(arc_r, adjust_angle=PI, run_time=0.6)
        self.wait(0.1)
        # rotate the compass and draw the right arc
        self.draw_arc_by_compass(arc_r)
        self.wait(0.1)
        # put the compass aside
        self.put_aside_compass(DR * 0.6)
        self.wait(0.6)
        # set p1, p2 and use these two points to set the ruler's position
        p1, p2 = np.sqrt(7) * UP, np.sqrt(7) * DOWN
        self.set_ruler(p1, p2)
        # emphasize the two dots
        self.emphasize_dot([p1,p2], run_time=0.25)
        self.wait(0.2)
        # create the line (perpendicular bisector) to be drawn by ruler
        l_pb = Line(p1, p2, **self.line_config).scale(1.25).set_color(PINK)
        # draw the perpendicular bisector
        self.draw_line_(l_pb)
        self.wait(0.1)
        # put the ruler aside
        self.put_aside_ruler(LEFT * 0.7)
        # create the foot point by Dot and vertical symbol by Square
        center = Dot((p1+p2)/2, color=RED).set_height(0.15)
        angle_90 = Square(0.32, stroke_width=2.5, stroke_color=GREY_C).shift(UR * 0.16)
        self.bring_to_back(angle_90)
        # add foot point and vertical symbol
        self.add(center)
        self.play(WiggleOutThenIn(center), FadeIn(angle_90), run_time=0.64)
        self.wait(2)

class Tangent_circle(CompassAndRulerScene):

    CONFIG = {
        'compass_config':{
            'leg_length': 4.05,
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

class Equal_angle(CompassAndRulerScene):

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
