from manimlib.imports import *
from my_manim_projects.my_imports import *

class Intro_old(Text4animScene):

    def construct(self):
        t2c = {'任意四边形': BLUE, '切两刀': ORANGE, '平行四边形': PINK}
        text_01 = Text('对任意四边形', font='思源黑体 Bold', size=1).to_corner(LEFT * 2 + UP * 3.5)
        text_02 = Text('如何能在切两刀之后', font='思源黑体 Bold', size=1).next_to(text_01, DOWN * 1.8, aligned_edge=LEFT)
        text_03 = Text('将碎片重新拼成平行四边形', font='思源黑体 Bold', size=1).next_to(text_02, DOWN * 1.8, aligned_edge=LEFT)
        text_01.set_color_by_t2c(t2c), text_02.set_color_by_t2c(t2c), text_03.set_color_by_t2c(t2c)
        t4a_1 = self.ShiftInOneByOne_new(text_01, run_speed=0.22, wait_time=0.0)
        t4a_2 = self.ShiftInOneByOne_new(text_02, run_speed=0.2, wait_time=0.0)
        t4a_3 = self.ShiftInOneByOne_new(text_03, run_speed=0.18, wait_time=1.)
        title = VGroup(t4a_1, t4a_2, t4a_3)
        title_02 = title.copy().scale(0.6).to_corner(LEFT * 1.5 + UP * 1.5)

        self.play(ReplacementTransform(title, title_02), run_time=1.)
        self.wait(0.4)

        A, B, C, D = Dot(UP * 1.6 + RIGHT * 0.8), Dot(UP * 1. + RIGHT * 2.), Dot(RIGHT * 2.7), Dot(DOWN * 0.8)
        ABCD = VGroup(A, B, C, D).to_corner(DOWN * 2.4 + LEFT * 1.8).set_fill(opacity=0)
        quadrilateral = Polygon(A.get_center(), B.get_center(), C.get_center(), D.get_center())\
            .add_updater(lambda p: p.become(Polygon(A.get_center(), B.get_center(), C.get_center(), D.get_center(),
                                       color=BLUE, fill_color=BLUE, fill_opacity=1.0)))
        self.play(TransformFromCopy(t4a_1[1:], quadrilateral), FadeIn(ABCD), run_time=1)
        self.wait(0.2)
        self.play(A.shift, UP * 0.5, B.shift, UR * 0.3, rate_func=there_and_back, run_time=0.7)
        self.wait(0.1)
        circle = Circle().move_to(D).rotate(PI).shift(RIGHT)
        self.play(MoveAlongPath(D, circle), run_time=0.75)

        arrow = Arrow(ORIGIN, RIGHT * 5, color=ORANGE, buff=0).next_to(quadrilateral, RIGHT * 1.6)
        parallelogram = Polygon(RIGHT + UP * 2, RIGHT * 3.5 + UP * 2, RIGHT * 2.5, ORIGIN,
                                color=BLUE, fill_color=BLUE, fill_opacity=1.0).next_to(arrow, RIGHT * 1.2)

        arrow.shift(DOWN * 0.8)
        text = Text('切两刀，重新拼接', font='思源黑体 Bold', size=0.36).move_to(arrow).shift(UP * 0.4)

        E = self.get_point_on_line(A, B, 0.3)
        F = self.get_point_on_line(B, C, 0.35)
        G = self.get_point_on_line(C, D, 0.3)
        H = self.get_point_on_line(D, A, 0.6)
        I = self.intersection(E, G, F, H)
        cut_line_01 = Line(E, G, color=YELLOW).scale(2)
        cut_line_02 = Line(H, F, color=YELLOW).scale(2)

        poly_1 = Polygon(A.get_center(), E.get_center(), I.get_center(), H.get_center(), color=BLUE, fill_color=BLUE, fill_opacity=1.0)
        poly_2 = Polygon(E.get_center(), B.get_center(), F.get_center(), I.get_center(), color=BLUE, fill_color=BLUE, fill_opacity=1.0)
        poly_3 = Polygon(H.get_center(), I.get_center(), G.get_center(), D.get_center(), color=BLUE, fill_color=BLUE, fill_opacity=1.0)
        poly_4 = Polygon(I.get_center(), F.get_center(), C.get_center(), G.get_center(), color=BLUE, fill_color=BLUE, fill_opacity=1.0)
        fragments = VGroup(poly_1, poly_2, poly_3, poly_4)
        fragments_02 = fragments.copy().arrange(RIGHT * 0.35).scale(0.95).next_to(text, UP)

        self.play(ShowCreation(arrow), run_time=1)
        t4a = self.ShiftInOneByOne_new(text, shift_vect=DOWN * 0.8, run_speed=0.2)
        self.play(ShowCreationThenDestruction(cut_line_01), ShowCreationThenDestruction(cut_line_02), run_time=0.72)
        # self.add(cut_line_01, cut_line_02)

        self.play(TransformFromCopy(fragments, fragments_02), run_time=1)
        self.wait(0.2)
        self.play(TransformFromCopy(fragments_02, parallelogram), run_time=1)

        self.play(FadeOutRandom(title_02[0]), FadeOutRandom(title_02[1]), FadeOutRandom(title_02[2]), run_time=1.2)
        text_how = Text('如何切，如何拼？', font='思源黑体 Bold', size=1.2).to_corner(UP * 2.4 + LEFT * 2)
        self.ShiftInOneByOne_new(text_how, run_speed=0.3, wait_time=0.1)
        # self.play(WiggleOutThenIn(t4a_how), run_time=0.9)
        self.Countdown_anim()
        self.wait(2)

    def get_point_on_line(self, P1, P2, t=0.5, **kwargs):
        try:
            return Dot(P1.get_center() + t * (P2.get_center() - P1.get_center()), **kwargs)
        except:
            return Dot(P1 + t * (P2 - P1), **kwargs)

    def intersection(self, P1, P2, P3, P4, **kwargs):
        try:
            return Dot(line_intersection([P1.get_center(), P2.get_center()], [P3.get_center(), P4.get_center()]), **kwargs)
        except:
            return Dot(line_intersection([P1, P2], [P3, P4]), **kwargs)

    def Countdown_anim(self, time=5):

        num = VGroup(*[Text(str(i), font='思源黑体 Bold', color=GREEN).set_height(1.2) for i in range(time, 0, -1)]).to_corner(RIGHT * 1.25 + UP * 1.25, buff=1)
        circle = Circle(radius=1).move_to(num).set_stroke(GREEN, 16)
        for i in range(time):
            self.add(num[i])
            self.play(WiggleOutThenIn(num[i]), ShowCreationThenDestruction(circle), run_time=1)
            self.remove(num[i])

class Intro(Text4animScene):

    def construct(self):
        t2c = {'任意四边形': BLUE, '切两刀': ORANGE, '平行四边形': PINK}
        text_01 = Text('对任意四边形', font='思源黑体 Bold', size=1).to_corner(LEFT * 2 + UP * 3.5)
        text_02 = Text('如何能在切两刀之后', font='思源黑体 Bold', size=1).next_to(text_01, DOWN * 1.8, aligned_edge=LEFT)
        text_03 = Text('将碎片重新拼成平行四边形', font='思源黑体 Bold', size=1).next_to(text_02, DOWN * 1.8, aligned_edge=LEFT)
        text_01.set_color_by_t2c(t2c), text_02.set_color_by_t2c(t2c), text_03.set_color_by_t2c(t2c)
        t4a_1 = self.ShiftInOneByOne_new(text_01, run_speed=0.3, wait_time=0.0)
        t4a_2 = self.ShiftInOneByOne_new(text_02, run_speed=0.26, wait_time=0.0)
        t4a_3 = self.ShiftInOneByOne_new(text_03, run_speed=0.23, wait_time=0.9)
        title = VGroup(t4a_1, t4a_2, t4a_3)
        title_02 = title.copy().scale(0.6).to_corner(LEFT * 1.5 + UP * 1.5)

        self.play(ReplacementTransform(title, title_02), run_time=0.8)
        self.wait(0.4)

        A, B, C, D = Dot(UP * 1.6 + RIGHT * 0.8), Dot(UP * 1. + RIGHT * 2.), Dot(RIGHT * 2.7), Dot(DOWN * 0.8)
        ABCD = VGroup(A, B, C, D).to_corner(DOWN * 3.2 + LEFT * 1.8).set_fill(opacity=0)
        quadrilateral = Polygon(A.get_center(), B.get_center(), C.get_center(), D.get_center())\
            .add_updater(lambda p: p.become(Polygon(A.get_center(), B.get_center(), C.get_center(), D.get_center(),
                                       stroke_color=WHITE, stroke_width=4, fill_color=BLUE, fill_opacity=1.0)))
        self.play(TransformFromCopy(t4a_1[1:], quadrilateral), FadeIn(ABCD), run_time=0.8)
        self.wait(0.1)
        # self.play(A.shift, UP * 0.5, B.shift, UR * 0.3, rate_func=there_and_back, run_time=0.7)
        # self.wait(0.1)
        # circle = Circle().move_to(D).rotate(PI).shift(RIGHT)
        # self.play(MoveAlongPath(D, circle), run_time=0.75)

        arrow = Arrow(ORIGIN, RIGHT * 5, color=ORANGE, buff=0).next_to(quadrilateral, RIGHT * 1.6)
        parallelogram = Polygon(RIGHT + UP * 2, RIGHT * 3.5 + UP * 2, RIGHT * 2.5, ORIGIN,
                                stroke_color=WHITE, stroke_width=4, fill_color=BLUE, fill_opacity=1.0).next_to(arrow, RIGHT * 1.25)

        arrow.shift(DOWN * 0.8)
        text = Text('切两刀，重新拼接', font='思源黑体 Bold', size=0.36).move_to(arrow).shift(UP * 0.4)

        E = self.get_point_on_line(A, B, 0.3)
        F = self.get_point_on_line(B, C, 0.35)
        G = self.get_point_on_line(C, D, 0.3)
        H = self.get_point_on_line(D, A, 0.6)
        I = self.intersection(E, G, F, H)
        cut_line_01 = Line(E, G, color=YELLOW).scale(2)
        cut_line_02 = Line(H, F, color=YELLOW).scale(2)

        poly_1 = Polygon(A.get_center(), E.get_center(), I.get_center(), H.get_center(), stroke_color=WHITE, stroke_width=4, fill_color=BLUE, fill_opacity=1.0)
        poly_2 = Polygon(E.get_center(), B.get_center(), F.get_center(), I.get_center(), stroke_color=WHITE, stroke_width=4, fill_color=BLUE, fill_opacity=1.0)
        poly_3 = Polygon(H.get_center(), I.get_center(), G.get_center(), D.get_center(), stroke_color=WHITE, stroke_width=4, fill_color=BLUE, fill_opacity=1.0)
        poly_4 = Polygon(I.get_center(), F.get_center(), C.get_center(), G.get_center(), stroke_color=WHITE, stroke_width=4, fill_color=BLUE, fill_opacity=1.0)
        fragments = VGroup(poly_1, poly_2, poly_3, poly_4)
        fragments_02 = fragments.copy().arrange(RIGHT * 0.35).scale(0.95).next_to(text, UP)

        self.play(ShowCreation(arrow), run_time=1)
        self.wait(0.1)
        self.play(FadeInFrom(text, direction=UP), run_time=0.8)
        self.wait(0.1)
        self.play(ShowCreationThenDestruction(cut_line_01), ShowCreationThenDestruction(cut_line_02), run_time=0.8)
        # self.add(cut_line_01, cut_line_02)

        self.play(TransformFromCopy(fragments, fragments_02), run_time=0.95)
        self.wait(0.1)
        self.play(TransformFromCopy(fragments_02, parallelogram), run_time=0.95)

        self.play(FadeOutRandom(title_02[0]), FadeOutRandom(title_02[1]), FadeOutRandom(title_02[2]), run_time=1.)
        self.wait(0.1)
        text_how = Text('如何切，如何拼？', font='思源黑体 Bold', size=1.2).to_corner(UP * 2.4 + LEFT * 2)
        self.ShiftInOneByOne_new(text_how, run_speed=0.325, wait_time=0.05)
        # self.play(WiggleOutThenIn(t4a_how), run_time=0.9)
        self.Countdown_anim()
        self.wait(2)

    def get_point_on_line(self, P1, P2, t=0.5, **kwargs):
        try:
            return Dot(P1.get_center() + t * (P2.get_center() - P1.get_center()), **kwargs)
        except:
            return Dot(P1 + t * (P2 - P1), **kwargs)

    def intersection(self, P1, P2, P3, P4, **kwargs):
        try:
            return Dot(line_intersection([P1.get_center(), P2.get_center()], [P3.get_center(), P4.get_center()]), **kwargs)
        except:
            return Dot(line_intersection([P1, P2], [P3, P4]), **kwargs)

    def Countdown_anim(self, time=5):

        num = VGroup(*[Text(str(i), font='思源黑体 Bold', color=GREEN).set_height(1.2) for i in range(time, 0, -1)]).to_corner(RIGHT * 1.25 + UP * 1.25, buff=1)
        circle = Circle(radius=1).move_to(num).set_stroke(GREEN, 16)
        for i in range(time):
            self.add(num[i])
            self.play(WiggleOutThenIn(num[i]), ShowCreationThenDestruction(circle), run_time=1)
            self.remove(num[i])

class How_to(Text4animScene):

    def construct(self):

        """
        1.沿两组对边的中点连成的直线切两刀
        2.形成了四个碎片
        3.易得：颜色相同的边长度相等
                红色角和黄色角互补
                所有紫色角之和为360°
        4.因此，不难证明：按照动画里面的拼法，得到的图形为平行四边形
        """

        A, B, C, D = Dot(UP * 1.6 + RIGHT * 0.9), Dot(UP * 0.9 + RIGHT * 2.2), Dot(RIGHT * 2.7 + DOWN * 0.1), Dot(DOWN * 0.8)
        ABCD = VGroup(A, B, C, D).move_to(DOWN * 0.6 + RIGHT * 0.4).scale(2.25)
        # quadrilateral = self.get_poly_d(A, B, C, D) .add_updater(lambda p: p.become(self.get_poly_d(A, B, C, D, stroke_color=WHITE, stroke_width=8, fill_color=BLUE, fill_opacity=1.0)))
        quadrilateral = self.get_poly_d(A, B, C, D, stroke_color=WHITE, stroke_width=4.5, fill_color=BLUE, fill_opacity=0.9)
        E = self.get_point_on_line(A, B, 0.5)
        F = self.get_point_on_line(B, C, 0.5)
        G = self.get_point_on_line(C, D, 0.5)
        H = self.get_point_on_line(D, A, 0.5)
        I = self.intersection(E, G, F, H)
        cut_line_01 = Line(E, G, color=YELLOW).scale(2)
        cut_line_02 = Line(H, F, color=YELLOW).scale(2)

        poly_1 = self.get_poly_d(A, E, I, H, stroke_color=WHITE, stroke_width=4.5, fill_color=BLUE, fill_opacity=0.9)
        poly_2 = self.get_poly_d(E, B, F, I, stroke_color=WHITE, stroke_width=4.5, fill_color=BLUE, fill_opacity=0.9)
        poly_3 = self.get_poly_d(H, I, G, D, stroke_color=WHITE, stroke_width=4.5, fill_color=BLUE, fill_opacity=0.9)
        poly_4 = self.get_poly_d(I, F, C, G, stroke_color=WHITE, stroke_width=4.5, fill_color=BLUE, fill_opacity=0.9)
        fragments = VGroup(poly_1, poly_2, poly_3, poly_4).set_plot_depth(-1)
        # fragments_02 = fragments.copy().arrange(RIGHT * 0.35)

        text = Text('沿两组对边的中点构成的直线切两刀', font='思源黑体 Bold', size=0.56, color=BLUE).to_corner(LEFT * 1.25 + UP * 1.25)
        self.play(FadeInFromLarge(quadrilateral), run_time=1.2)
        self.wait(0.2)
        t4a = self.ShiftInOneByOne_new(text, run_speed=0.25, wait_time=0.15)

        self.play(ShowCreationThenDestruction(cut_line_01), ShowCreationThenDestruction(cut_line_02), FadeIn(fragments), run_time=0.8)
        self.remove(quadrilateral)
        self.play(fragments[0].shift, UL * 0.25, fragments[1].shift, UR * 0.25,
                  fragments[2].shift, DL * 0.25, fragments[3].shift, DR * 0.25, run_time=1.6)
        self.wait(0.5)

        text_0 = Text('易得：', font='思源黑体 Bold', size=0.4).next_to(text, DOWN * 2, aligned_edge=LEFT)
        text_1 = Text('1.同色线段等长', font='思源黑体 Bold', size=0.4).next_to(text_0, DOWN * 1.6, aligned_edge=LEFT)
        text_1.set_color_by_t2c({'同色线段': GREEN})
        text_2 = Text('2.红角黄角互补', font='思源黑体 Bold', size=0.4).next_to(text_1, DOWN * 1.6, aligned_edge=LEFT)
        text_2.set_color_by_t2c({'红角': RED, '黄角': YELLOW})
        text_3 = Text('3.紫色角之和为360度', font='思源黑体 Bold', size=0.4).next_to(text_2, DOWN * 1.6, aligned_edge=LEFT)
        text_3.set_color_by_t2c({'紫色角': PINK})
        text_4 = Text('一通操作猛如虎', font='思源黑体 Bold', size=0.4).next_to(text_3, DOWN * 1.6, aligned_edge=LEFT)
        text_5 = Text('结果真的是非常的amazing啊！', font='思源黑体 Bold', size=0.4).next_to(text_4, DOWN * 1.6, aligned_edge=LEFT)
        text_6 = Text('(由上面3个结论不难证明结果恰好为平行四边形)', font='思源黑体 Bold', size=0.4).next_to(text_5, DOWN * 1.6, aligned_edge=LEFT).set_color(GREEN)

        texts = VGroup(text_0, text_1, text_2, text_3, text_4, text_5, text_6).shift(RIGHT * 0.25)

        lines = VGroup(*[
            Line(A.get_center(), E.get_center(), color=RED,    stroke_width=5.4).scale(1.012).shift(UL * 0.25),
            Line(E.get_center(), B.get_center(), color=RED,    stroke_width=5.4).scale(1.012).shift(UR * 0.25),
            Line(B.get_center(), F.get_center(), color=YELLOW, stroke_width=5.4).scale(1.012).shift(UR * 0.25),
            Line(F.get_center(), C.get_center(), color=YELLOW, stroke_width=5.4).scale(1.012).shift(DR * 0.25),
            Line(C.get_center(), G.get_center(), color=GREEN,  stroke_width=5.4).scale(1.012).shift(DR * 0.25),
            Line(G.get_center(), D.get_center(), color=GREEN,  stroke_width=5.4).scale(1.012).shift(DL * 0.25),
            Line(D.get_center(), H.get_center(), color=PINK,   stroke_width=5.4).scale(1.012).shift(DL * 0.25),
            Line(H.get_center(), A.get_center(), color=PINK,   stroke_width=5.4).scale(1.012).shift(UL * 0.25),
        ]).set_plot_depth(2)
        angles = VGroup(*[
            Angle(H.get_center(), I.get_center(), E.get_center(), color=RED, radius=0.5).shift(UL * 0.25),
            Angle(E.get_center(), I.get_center(), F.get_center(), color=YELLOW, radius=0.5).shift(UR * 0.25),
            Angle(F.get_center(), I.get_center(), G.get_center(), color=RED, radius=0.5).shift(DR * 0.25),
            Angle(G.get_center(), I.get_center(), H.get_center(), color=YELLOW, radius=0.5).shift(DL * 0.25),
        ]).set_plot_depth(4)

        angles_02 = VGroup(*[
            Angle(H.get_center(), A.get_center(), E.get_center(), color=PINK,   radius=0.45).shift(UL * 0.25),
            Angle(E.get_center(), B.get_center(), F.get_center(), color=PINK,   radius=0.45).shift(UR * 0.25),
            Angle(F.get_center(), C.get_center(), G.get_center(), color=PINK,   radius=0.45).shift(DR * 0.25),
            Angle(G.get_center(), D.get_center(), H.get_center(), color=PINK,   radius=0.45).shift(DL * 0.25),
        ]).set_plot_depth(6)

        self.play(Write(text_0), run_time=0.9)
        self.wait(0.25)
        self.play(Write(text_1), ShowCreation(lines), run_time=2.1)
        self.wait(1.4)
        self.play(Write(text_2), ShowCreation(angles), run_time=2.2)
        self.wait(1.6)
        self.play(Write(text_3), ShowCreation(angles_02), run_time=2.5)
        self.wait(1.5)

        group_all = VGroup(fragments, lines, angles, angles_02)

        self.play(group_all.shift, RIGHT * 1.2)
        self.wait(0.4)
        self.remove(fragments, lines, angles, angles_02)
        ul = VGroup(fragments[0].set_plot_depth(-1), lines[0].set_plot_depth(1), lines[7].set_plot_depth(1), angles[0].set_plot_depth(2), angles_02[0].set_plot_depth(3))
        ur = VGroup(fragments[1].set_plot_depth(-1), lines[1].set_plot_depth(1), lines[2].set_plot_depth(1), angles[1].set_plot_depth(2), angles_02[1].set_plot_depth(3))
        dr = VGroup(fragments[3].set_plot_depth(-1), lines[3].set_plot_depth(1), lines[4].set_plot_depth(1), angles[2].set_plot_depth(2), angles_02[2].set_plot_depth(3))
        dl = VGroup(fragments[2].set_plot_depth(-1), lines[5].set_plot_depth(1), lines[6].set_plot_depth(1), angles[3].set_plot_depth(2), angles_02[3].set_plot_depth(3))
        self.add(*ul, *ur, *dr, *dl)
        t4a_2 = self.ShiftInOneByOne_new(text_4, run_speed=0.32, wait_time=0.15)
        self.play(Rotating(ul, radians=PI, about_point=(lines[-1].get_start() + lines[-2].get_end())/2, run_time=1.8, rate_func=smooth))
        self.wait(0.2)
        self.play(Rotating(dr, radians=PI, about_point=(lines[3].get_start() + lines[2].get_end())/2, run_time=1.8, rate_func=smooth))
        self.wait(0.4)

        self.play(ur.shift, DOWN * 3, dr.shift, DOWN * 3, ul.shift, UP * 3, dl.shift, UP * 3, run_time=1.5)
        self.wait(0.25)
        p1 = DOWN * 0.65 + RIGHT * 2

        self.play(ur.shift, (p1[0] - lines[2].get_start()[0] - 0.01) * RIGHT,
                  dr.shift, (p1[0] - lines[2].get_start()[0] - 0.01) * RIGHT,
                  ul.shift, (p1[0] - lines[0].get_start()[0]) * RIGHT,
                  dl.shift, (p1[0] - lines[0].get_start()[0]) * RIGHT, run_time=1.5)
        self.wait(0.2)
        self.play(ur.shift, (p1[1] - lines[2].get_start()[1]) * UP,
                  dr.shift, (p1[1] - lines[2].get_start()[1]) * UP,
                  ul.shift, (p1[1] - lines[0].get_start()[1]) * UP,
                  dl.shift, (p1[1] - lines[0].get_start()[1]) * UP, run_time=1.5)
        self.wait(0.1)
        t4a_3 = self.ShiftInOneByOne_new(text_5, run_speed=0.18, wait_time=0.1)
        self.play(WiggleOutThenIn(group_all))
        self.wait(0.4)
        self.play(WriteRandom(text_6), run_time=1.6)
        self.wait(5)

    def get_poly_p(self, p1, p2, p3, p4, **kwargs):

        return New_Polygon(p1, p2, p3, p4, **kwargs)

    def get_poly_d(self, d1, d2, d3, d4, **kwargs):

        return New_Polygon(d1.get_center(), d2.get_center(), d3.get_center(), d4.get_center(), **kwargs)

    def get_point_on_line(self, P1, P2, t=0.5, **kwargs):

        try:
            return Dot(P1.get_center() + t * (P2.get_center() - P1.get_center()), **kwargs)
        except:
            return Dot(P1 + t * (P2 - P1), **kwargs)

    def intersection(self, P1, P2, P3, P4, **kwargs):

        try:
            return Dot(line_intersection([P1.get_center(), P2.get_center()], [P3.get_center(), P4.get_center()]), **kwargs)
        except:
            return Dot(line_intersection([P1, P2], [P3, P4]), **kwargs)


