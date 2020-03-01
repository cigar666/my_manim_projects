"""

  > Author             : cigar666
  > Created Time       : 2020/02/26
  > Animation used in  : https://www.bilibili.com/video/av92747585

"""

from manimlib.imports import *
from my_manim_projects.my_utils.my_geometry import *

class Cycloid_generation(Scene):

    def construct(self):

        r = 1.5
        circle = Circle(radius=r, color=WHITE, stroke_width=2.5, fill_color=RED, fill_opacity=0)

        init_O = DOWN * 0. + LEFT * PI * r + r * UP

        ground_line = Line(DOWN * 0. + LEFT * 6, DOWN * 0. + RIGHT * 6, color=WHITE, stroke_width=2.5)
        dot_O = Dot(init_O, color=YELLOW, plot_depth=1)

        dot_P = Dot(init_O + r * DOWN, color=BLUE, plot_depth=1)
        line_r = Line(dot_O.get_center(), dot_P.get_center(), stroke_width=2.5)

        get_t = lambda : (dot_O.get_center()[0] - init_O[0]) / r
        get_P = lambda t: np.array([t - np.sin(t), 1 - np.cos(t), 0]) * r

        dot_P.add_updater(lambda d: d.move_to(init_O + r * DOWN + get_P(get_t())))
        line_r.add_updater(lambda l: l.become(Line(init_O + r * get_t() * RIGHT, init_O + r * DOWN + get_P(get_t()), stroke_width=2.5)))
        circle.add_updater(lambda c: c.move_to(dot_O))

        area = Polygon(*[init_O + r * DOWN + get_P(t) for t in np.linspace(0, TAU, 100)], fill_color=BLUE, fill_opacity=0.6)
        curve = ParametricFunction(lambda t: init_O + r * DOWN + get_P(t), t_min=0, t_max=TAU, stroke_width=2)
        curve.add_updater(lambda c: c.become(ParametricFunction(lambda t: init_O + r * DOWN + get_P(t),
                                                                t_min=-0.01, t_max=get_t(), stroke_width=2)))

        text = Text('S = ？', font='思源黑体 Bold').scale([1.8, 1.5, 1])
        text.set_color_by_t2c({'S': BLUE, '？': PINK})
        text.shift(DOWN * 1.5)

        self.play(ShowCreation(ground_line))
        self.wait(0.5)
        self.play(FadeIn(dot_O), run_time=0.7)
        self.play(FadeIn(circle), run_time=0.8)
        self.wait(0.2)

        self.play(ShowCreation(line_r))
        self.play(FadeIn(dot_P), run_time=0.7)
        self.wait(0.6)
        self.add(curve)
        self.play(dot_O.shift, 2 * PI * r * RIGHT, rate_func=linear, run_time=4)

        self.wait()
        self.play(FadeIn(area), run_time=1.2)
        self.wait(0.4)
        self.play(TransformFromCopy(area, text), run_time=1.5)
        self.wait(0.5)
        # self.play(ShowCreationThenFadeAround(SurroundingRectangle(text)), run_time=1.25)
        self.play(WiggleOutThenIn(text), run_time=1.2)
        self.wait(5)

class Area_divide_into_tri(Scene):

    def construct(self):

        r = 1.5
        n = 6
        points_6 = [complex_to_R3(r * np.exp(1j * TAU/n * i)) for i in range(n)]
        poly_6 = Polygon(*points_6, stroke_width=3)
        poly_6.shift(r * 3 * LEFT + UP * 2)

        ground_line = Line(DOWN * r * np.sqrt(3)/2 + UP * 2 + LEFT * 6, DOWN * r * np.sqrt(3)/2 + UP * 2 + RIGHT * 6, color=WHITE, stroke_width=2.5)
        dot_pink = Dot(poly_6.get_center() + complex_to_R3(r * np.exp(1j * (-2) * TAU/n)), color=PINK, plot_depth=1)
        start_point = dot_pink.get_center()
        poly = VGroup(poly_6, dot_pink)

        self.add(ground_line)
        self.play(ShowCreation(poly_6))
        self.play(FadeInFromLarge(dot_pink))
        self.wait()
        line_points = []
        p_old = dot_pink.get_center()
        line_group = VGroup()
        for i in range(n):
            self.add(poly.copy().set_stroke(opacity=0.4))
            self.play(Rotating(poly, radians=-TAU/n, about_point=poly_6.get_center() + complex_to_R3(r * np.exp(1j * (-1) * TAU/n)), run_time=1.2)) #
            line_group.add(Line(p_old, dot_pink.get_center(), stroke_width=2.5))
            self.play(ShowCreation(line_group[-1]), run_time=0.5)
            p_old = dot_pink.get_center()
        self.play(FadeIn(poly.copy().set_stroke(opacity=0.25)), run_time=0.25)
        self.wait(0.5)

        c1, c2, c3, c4 = RED, BLUE, YELLOW, GREEN
        # r0 = 0.01
        tri_1_01 = Polygon(start_point + r * RIGHT, start_point + 2 * r * RIGHT,
                           start_point + r/2 * RIGHT + r * np.sqrt(3)/2 * UP,
                           color=WHITE, stroke_width=2., fill_color=c1, fill_opacity=0.8)#.round_corners(r0)
        tri_1_02 = Polygon(start_point + 2 * r * RIGHT, start_point + 3 * r * RIGHT,
                           start_point + 2 * r * RIGHT + r * np.sqrt(3) * UP,
                           color=WHITE, stroke_width=2., fill_color=c1, fill_opacity=0.8)#.round_corners(r0)
        tri_1_03 = Polygon(start_point + 3 * r * RIGHT, start_point + 4 * r * RIGHT,
                           start_point + 4 * r * RIGHT + r * np.sqrt(3) * UP,
                           color=WHITE, stroke_width=2., fill_color=c1, fill_opacity=0.8)#.round_corners(r0)
        tri_1_04 = Polygon(start_point + 4 * r * RIGHT, start_point + 5 * r * RIGHT,
                           start_point + 5.5 * r * RIGHT + r * np.sqrt(3)/2 * UP,
                           color=WHITE, stroke_width=2., fill_color=c1, fill_opacity=0.8)#.round_corners(r0)

        tri_2_01 = Polygon(start_point + 0 * RIGHT, start_point + 1 * r * RIGHT,
                           start_point - r/2 * RIGHT + r * np.sqrt(3)/2 * UP,
                           color=WHITE, stroke_width=2., fill_color=c2, fill_opacity=0.8)#.round_corners(r0)
        tri_2_02 = Polygon(start_point + 0.5 * r * RIGHT + np.sqrt(3)/2 * r * UP,
                           start_point + 2 * r * RIGHT, start_point + r * RIGHT + r * np.sqrt(3) * UP,
                           color=WHITE, stroke_width=2., fill_color=c2, fill_opacity=0.8)#.round_corners(r0)
        tri_2_03 = tri_2_02.copy().flip(about_point=0.5 * r * LEFT)
        tri_2_04 = tri_2_01.copy().flip(about_point=0.5 * r * LEFT)

        tri_3_01 = Polygon(start_point + 2 * r * RIGHT, start_point + 1.5 * r * RIGHT + np.sqrt(3)/2 * r * UP,
                           start_point + r * 2 * RIGHT + r * np.sqrt(3) * UP,
                           color=WHITE, stroke_width=2., fill_color=c3, fill_opacity=0.8)#.round_corners(r0)
        tri_3_02 = Polygon(start_point + 2 * r * RIGHT + np.sqrt(3) * r * UP,
                           start_point + 3 * r * RIGHT + np.sqrt(3) * r * UP, start_point + 3 * r * RIGHT,
                           color=WHITE, stroke_width=2., fill_color=c3, fill_opacity=0.8)#.round_corners(r0)
        tri_3_03 = tri_3_02.copy().flip(about_point=0.5 * r * LEFT)
        tri_3_04 = tri_3_01.copy().flip(about_point=0.5 * r * LEFT)

        tri_4_01 = Polygon(start_point, start_point + 1 * r * RIGHT,
                           start_point + r * 0.5 * RIGHT + r * np.sqrt(3)/2 * UP,
                           color=WHITE, stroke_width=2., fill_color=c4, fill_opacity=0.8)#.round_corners(r0)
        tri_4_02 = Polygon(start_point + r * 0.5 * RIGHT + r * np.sqrt(3)/2 * UP,
                           start_point + 2 * r * RIGHT + np.sqrt(3) * r * UP, start_point + 2 * r * RIGHT,
                           color=WHITE, stroke_width=2., fill_color=c4, fill_opacity=0.8)#.round_corners(r0)
        tri_4_03 = tri_4_02.copy().flip(about_point=0.5 * r * LEFT)
        tri_4_04 = tri_4_01.copy().flip(about_point=0.5 * r * LEFT)

        tri_group_01, tri_group_02, tri_group_03, tri_group_04 = VGroup(tri_1_01, tri_1_02, tri_1_03, tri_1_04),\
                                                   VGroup(tri_2_01, tri_2_02, tri_2_03, tri_2_04),\
                                                   VGroup(tri_3_01, tri_3_02, tri_3_03, tri_3_04),\
                                                   VGroup(tri_4_01, tri_4_02, tri_4_03, tri_4_04)

        self.play(FadeIn(tri_group_01), FadeIn(tri_group_04), FadeIn(tri_group_03[1:3]))
        self.wait()

        self.play(ReplacementTransform(tri_group_04[0], tri_group_02[0]), run_time=1.25)
        self.wait(0.25)
        self.play(ReplacementTransform(tri_group_04[1], VGroup(tri_group_02[1], tri_group_03[0])), run_time=1.25)
        self.wait(0.25)
        self.play(ReplacementTransform(tri_group_04[2], VGroup(tri_group_02[2], tri_group_03[-1])), run_time=1.25)
        self.wait(0.25)
        self.play(ReplacementTransform(tri_group_04[3], tri_group_02[3]), run_time=1.25)
        self.wait(1.25)

        ## rearrange triangles ##
        p_6 = [complex_to_R3(r * np.exp(1j * (TAU/n * i + PI/2))) for i in range(n)]
        t_01 = Polygon(p_6[0], p_6[1], p_6[2],color=WHITE, stroke_width=2., fill_color=c1, fill_opacity=0.8)#.round_corners(r0)
        t_02 = Polygon(p_6[0], p_6[2], p_6[3],color=WHITE, stroke_width=2., fill_color=c1, fill_opacity=0.8)#.round_corners(r0)
        t_03 = Polygon(p_6[0], p_6[3], p_6[4],color=WHITE, stroke_width=2., fill_color=c1, fill_opacity=0.8)#.round_corners(r0)
        t_04 = Polygon(p_6[0], p_6[4], p_6[5],color=WHITE, stroke_width=2., fill_color=c1, fill_opacity=0.8)#.round_corners(r0)
        poly_by_tri_01 = VGroup(t_01, t_02, t_03, t_04)
        poly_by_tri_02 = poly_by_tri_01.copy().set_fill(color=c2).shift(DOWN * r)
        poly_by_tri_03 = poly_by_tri_01.copy().set_fill(color=c3).shift(DOWN * r + RIGHT * r * 2.5)
        poly_by_tri_01.shift(DOWN * r + LEFT * r * 2.5)

        self.play(TransformFromCopy(tri_group_01, poly_by_tri_01), run_time=2.25)
        self.wait(0.75)
        self.play(TransformFromCopy(tri_group_02, poly_by_tri_02), run_time=2.25)
        self.wait(0.75)
        self.play(TransformFromCopy(tri_group_03, poly_by_tri_03), run_time=2.25)

        self.wait(4)

class Area_divide_into_tri_02(Scene):

    def construct(self):

        r = 1.5
        n = 8
        points_8 = [complex_to_R3(r * np.exp(1j * (TAU/n * i + PI/n))) for i in range(n)]
        poly_8 = Polygon(*points_8, stroke_width=3)
        poly_8.shift(r * 3 * LEFT + UP * 2)

        ground_line = Line(DOWN * r * np.cos(PI/n) + UP * 2 + LEFT * 6, DOWN * r * np.cos(PI/n) + UP * 2 + RIGHT * 6, color=WHITE, stroke_width=2.5)
        dot_pink = Dot(poly_8.get_center() + complex_to_R3(r * np.exp(1j * ((-3) * TAU/n + PI/n))), color=PINK, plot_depth=1)
        start_point = dot_pink.get_center()
        poly = VGroup(poly_8, dot_pink)

        self.add(ground_line)
        self.wait()
        self.play(ShowCreation(poly_8))
        self.play(FadeInFromLarge(dot_pink), run_time=0.75)
        self.wait()
        line_points = []
        p_old = dot_pink.get_center()
        line_group = VGroup()
        for i in range(n):
            self.add(poly.copy().set_stroke(opacity=0.4))
            self.play(Rotating(poly, radians=-TAU/n, about_point=poly_8.get_center() + complex_to_R3(r * np.exp(1j * ((-2) * TAU/n + PI/n))), run_time=0.8)) #
            line_group.add(Line(p_old, dot_pink.get_center(), stroke_width=2.5))
            self.play(ShowCreation(line_group[-1]), run_time=0.4)
            p_old = dot_pink.get_center()
        # self.play(FadeIn(poly.copy().set_stroke(opacity=0.25)), run_time=0.25)
        self.wait(2.)

        r = 1.5
        n = 10
        points_10 = [complex_to_R3(r * np.exp(1j * TAU/n * i)) for i in range(n)]
        poly_10 = Polygon(*points_10, stroke_width=3)
        poly_10.shift(r * 3 * LEFT + DOWN * 2)

        ground_line = Line(DOWN * r * np.cos(PI/n) + DOWN * 2 + LEFT * 6, DOWN * r * np.cos(PI/n) + DOWN * 2 + RIGHT * 6, color=WHITE, stroke_width=2.5)
        dot_pink = Dot(poly_10.get_center() + complex_to_R3(r * np.exp(1j * (-3) * TAU/n)), color=PINK, plot_depth=1)
        start_point = dot_pink.get_center()
        poly = VGroup(poly_10, dot_pink)

        self.play(ShowCreation(ground_line))
        self.wait()
        self.play(ShowCreation(poly_10))
        self.play(FadeInFromLarge(dot_pink))
        self.wait()
        line_points = []
        p_old = dot_pink.get_center()
        line_group = VGroup()
        for i in range(n):
            self.add(poly.copy().set_stroke(opacity=0.4))
            self.play(Rotating(poly, radians=-TAU/n, about_point=poly_10.get_center() + complex_to_R3(r * np.exp(1j * (-2) * TAU/n)), run_time=0.72)) #
            line_group.add(Line(p_old, dot_pink.get_center(), stroke_width=2.5))
            self.play(ShowCreation(line_group[-1]), run_time=0.36)
            p_old = dot_pink.get_center()
        self.wait(2)

        self.play(VGroup(*self.mobjects).shift, UP * 4, run_time=1.8)
        self.wait()

        start_point += 4 * UP
        c1, c2, c3, c4 = RED, BLUE, YELLOW, GREEN
        # r0 = 0.0001
        tri_group_01 = VGroup()
        l = r * np.sin(PI/n) * 2
        for i in range(1, 5):
            tri_group_01.add(Polygon(start_point + l * i * RIGHT, start_point + l * (i+1) * RIGHT, line_group[i-1].get_end(),
                                     color=WHITE, stroke_width=2.5, fill_color=c1, fill_opacity=0.8))
        for i in range(5, 9):
            tri_group_01.add(Polygon(start_point + l * i * RIGHT, start_point + l * (i+1) * RIGHT, line_group[i-1].get_end(),
                                     color=WHITE, stroke_width=2.5, fill_color=c1, fill_opacity=0.8))

        tri_group_02 = VGroup()
        for i in range(0, 4):
            tri_group_02.add(Polygon(line_group[i].get_start(), start_point + l * (i+1) * RIGHT,
                                     line_group[i].get_end() + l * LEFT,
                                     color=WHITE, stroke_width=2., fill_color=c2, fill_opacity=0.8))
        for i in range(0, 4):
            tri_group_02.add(Polygon(line_group[3-i].get_start(), start_point + l * (3-i+1) * RIGHT,
                                     line_group[3-i].get_end() + l * LEFT,
                                     color=WHITE, stroke_width=2., fill_color=c2, fill_opacity=0.8).flip(about_point=start_point + l * 5))

        tri_group_03 = VGroup()
        for i in range(1, 4):
            tri_group_03.add(Polygon(line_group[i].get_end(), start_point + l * (i+1) * RIGHT,
                                     line_group[i-1].get_end() + l * RIGHT,
                                     color=WHITE, stroke_width=2., fill_color=c3, fill_opacity=0.8))
        tri_group_03.add(Polygon(line_group[3].get_end(), start_point + l * 5 * RIGHT,
                                 line_group[3].get_end() + l * RIGHT,
                                 color=WHITE, stroke_width=2., fill_color=c3, fill_opacity=0.8))
        tri_group_03.add(Polygon(line_group[3].get_end(), start_point + l * 5 * RIGHT,
                                 line_group[3].get_end() + l * RIGHT,
                                 color=WHITE, stroke_width=2., fill_color=c3, fill_opacity=0.8).flip(about_point=start_point + l * 5))

        for i in range(1, 4):
            tri_group_03.add(Polygon(line_group[4-i].get_end(), start_point + l * (4-i+1) * RIGHT,
                                     line_group[4-i-1].get_end() + l * RIGHT,
                                     color=WHITE, stroke_width=2., fill_color=c3, fill_opacity=0.8).flip(about_point=start_point + l * 5))
        tri_group_04 = VGroup()
        for i in range(9):
            tri_group_04.add(Polygon(line_group[i].get_start(), start_point + l * (i+1) * RIGHT, line_group[i].get_end(),
                                     color=WHITE, stroke_width=2., fill_color=c4, fill_opacity=0.8))

        self.play(FadeIn(tri_group_01))
        self.wait()
        self.play(FadeIn(tri_group_04))
        self.wait()
        self.play(ReplacementTransform(tri_group_04[0], tri_group_02[0]), run_time=0.8)
        self.wait(0.2)
        self.play(ReplacementTransform(tri_group_04[1], VGroup(tri_group_02[1], tri_group_03[0])), run_time=0.8)
        self.wait(0.2)
        self.play(ReplacementTransform(tri_group_04[2], VGroup(tri_group_02[2], tri_group_03[1])), run_time=0.8)
        self.wait(0.2)
        self.play(ReplacementTransform(tri_group_04[3], VGroup(tri_group_02[3], tri_group_03[2])), run_time=0.8)

        self.wait(0.2)
        self.play(ReplacementTransform(tri_group_04[4], tri_group_03[3:5]), run_time=1.2)
        self.wait(0.2)
        self.play(ReplacementTransform(tri_group_04[5], VGroup(tri_group_02[4], tri_group_03[5])), run_time=0.8)
        self.wait(0.2)
        self.play(ReplacementTransform(tri_group_04[6], VGroup(tri_group_02[5], tri_group_03[6])), run_time=0.8)
        self.wait(0.2)
        self.play(ReplacementTransform(tri_group_04[7], VGroup(tri_group_02[6], tri_group_03[7])), run_time=0.8)
        self.wait(0.24)
        self.play(ReplacementTransform(tri_group_04[8], tri_group_02[-1]), run_time=0.8)
        self.wait()

        ## rearrange triangles ##
        p_10 = [complex_to_R3(r * np.exp(1j * (TAU/n * i + PI/2))) for i in range(n)]
        poly_by_tri_01 = VGroup()
        for i in range(n-2):
            tri_i = Polygon(p_10[0], p_10[i+1], p_10[i+2],color=WHITE, stroke_width=2., fill_color=c1, fill_opacity=0.8)
            poly_by_tri_01.add(tri_i)
        poly_by_tri_02 = poly_by_tri_01.copy().set_fill(color=c2).shift(DOWN * r)
        poly_by_tri_03 = poly_by_tri_01.copy().set_fill(color=c3).shift(DOWN * r + RIGHT * r * 2.5)
        poly_by_tri_01.shift(DOWN * r + LEFT * r * 2.5)

        self.play(TransformFromCopy(tri_group_01, poly_by_tri_01), run_time=2.25)
        self.wait(0.75)
        self.play(TransformFromCopy(tri_group_02, poly_by_tri_02), run_time=2.25)
        self.wait(0.75)
        self.play(TransformFromCopy(tri_group_03, poly_by_tri_03), run_time=2.25)
        self.wait(4)

class Area_by_intergral(Scene):

    def construct(self):

        text_x = TexMobject('x=r(t-\\sin{t})', color=BLUE).to_corner(LEFT * 2 + UP * 1.5)
        text_y = TexMobject('y=r(1-\\cos{t})', color=BLUE).to_corner(LEFT * 2 + UP * 3)
        text_t = TexMobject('0\\leqslant t \\leqslant 2\\pi', color=BLUE).to_corner(LEFT * 1.5 + UP * 4.5).scale(0.75)

        text_01 = TexMobject('A=\\int^{t=2\\pi}_{t=0} y dx').to_corner(LEFT * 2 + UP * 7.5)
        text_02 = TexMobject('=\\int^{t=2\\pi}_{t=0} r^2(1-\\cos{t})^2 dt').next_to(text_01, RIGHT * 0.5)
        text_03 = TexMobject('=r^2({3\\over2}t-2\\sin{t}+{1\\over2}\\cos{t}\\sin{t})', '\\Big|', '^{t=2\\pi}', '_{t=0}').next_to(text_01, DOWN * 1.2).to_corner(LEFT * 2)
        # text_03[1].scale([1,2,1]), text_03[2].align_to(text_03[1], UP), text_03[3].align_to(text_03[1], DOWN)
        text_04 = TexMobject('=3\\pi r^2').scale(1.1).next_to(text_03, RIGHT * 0.5)
        self.play(Write(text_x), run_time=1.2)
        self.play(Write(text_y), run_time=1.2)
        self.play(Write(text_t), run_time=1.2)
        self.wait()
        self.play(Write(text_01), run_time=1.5)
        self.wait(0.5)
        self.play(Write(text_02), run_time=1.8)
        self.wait(0.5)
        self.play(Write(text_03), run_time=2)
        self.wait(0.5)
        self.play(Write(text_04), run_time=1.25)
        self.wait(5)

class Area_divide_into_rect(Scene):

    def construct(self):

        r = 1.5
        start_point = UP * 0.5 + PI * r * LEFT
        curve = ParametricFunction(lambda t: start_point + r * np.array([t-np.sin(t), 1-np.cos(t), 0]),
                                      t_min=0, t_max=PI * 2, stroke_width=2)

        ground_line = Line(UP * 0.5 + LEFT * 6, UP * 0.5 + RIGHT * 6, color=WHITE, stroke_width=2.5)
        circle = Circle(radius=r, color=WHITE, stroke_width=2., fill_color=RED, fill_opacity=0.0).move_to((r + 0.5) * UP)

        area_l = Polygon(*([start_point + r * np.array([t-np.sin(t), 1-np.cos(t), 0]) for t in np.linspace(0, PI, 50)] +
                           [start_point + r * UP + r * PI * RIGHT + r * np.array([np.cos(t), np.sin(t), 0]) for t in np.linspace(PI/2, 3*PI/2, 50)]),
                         stroke_width=2, fill_color=BLUE, fill_opacity=0.0)

        area_r = Polygon(*([start_point + r * np.array([t-np.sin(t), 1-np.cos(t), 0]) for t in np.linspace(2 * PI, PI, 50)] +
                           [start_point + r * UP + r * PI * RIGHT + r * np.array([np.cos(t), np.sin(t), 0]) for t in np.linspace(PI/2, -PI/2, 50)]),
                         stroke_width=2, fill_color=YELLOW, fill_opacity=0.0)

        s_l, s_m, s_r = area_l.copy().set_fill(opacity=0.8), circle.copy().set_fill(opacity=0.8), area_r.copy().set_fill(opacity=0.8)

        formula = TexMobject('S', '=', 'S_{\\text{蓝}}', '+', 'S_{\\text{红}}', '+', 'S_{\\text{黄}}').scale(1.6)
        formula[0].set_color(PINK), formula[2].set_color(BLUE), formula[4].set_color(RED), formula[6].set_color(YELLOW)
        formula.to_corner(LEFT * 2.5 + UP * 8.5)

        rects_7 = self.create_rects(num=7, start_point=start_point, r=1.5)
        rects_17 = self.create_rects(num=17, start_point=start_point, r=1.5, stroke_width=0.4)
        rects_37 = self.create_rects(num=37, start_point=start_point, r=1.5, stroke_width=0.1)
        rects_81 = self.create_rects(num=81, start_point=start_point, r=1.5, stroke_width=0.0).scale([1,1.001,1])

        rects_y_7 = rects_7.copy().set_fill(color=YELLOW).rotate(PI, about_point=start_point + r * UP + PI * r * RIGHT)
        rects_y_17 = rects_17.copy().set_fill(color=YELLOW).rotate(PI, about_point=start_point + r * UP + PI * r * RIGHT)
        rects_y_37 = rects_37.copy().set_fill(color=YELLOW).rotate(PI, about_point=start_point + r * UP + PI * r * RIGHT)
        rects_y_81 = rects_81.copy().set_fill(color=YELLOW).rotate(PI, about_point=start_point + r * UP + PI * r * RIGHT)

        self.add(curve, ground_line)
        self.wait(0.8)

        self.play(FadeIn(s_l))
        self.play(FadeIn(s_m))
        self.play(FadeIn(s_r))
        self.add(area_l, circle, area_r)
        self.wait(0.9)
        self.play(Write(formula[0:2]))
        self.wait(0.4)
        self.play(ReplacementTransform(s_l, formula[2]))
        self.play(Write(formula[3]), run_time=0.4)
        self.wait(0.25)
        self.play(ReplacementTransform(s_m, formula[4]))
        self.play(Write(formula[5]), run_time=0.4)
        self.wait(0.25)
        self.play(ReplacementTransform(s_r, formula[6]))
        self.wait(0.8)
        self.play(Rotating(area_r, radians=PI, axis=RIGHT, run_time=1.6))

        self.wait()
        for rect, rect_y in zip(rects_7, rects_y_7): self.play(FadeInFromUp(rect), FadeInFromDown(rect_y), run_time=0.8)
        self.wait(0.2)
        self.play(ReplacementTransform(rects_7, rects_17), ReplacementTransform(rects_y_7, rects_y_17), run_time=1.5)
        self.wait(0.2)
        self.play(ReplacementTransform(rects_17, rects_37), ReplacementTransform(rects_y_17, rects_y_37), run_time=1.25)
        self.wait(0.2)
        self.play(ReplacementTransform(rects_37, rects_81), ReplacementTransform(rects_y_37, rects_y_81), run_time=1.2)
        self.wait()

        rects_7_new = self.create_rects(num=7, start_point=start_point, r=1.5)
        rects_17_new = self.create_rects(num=17, start_point=start_point, r=1.5, stroke_width=0.4)
        rects_37_new = self.create_rects(num=37, start_point=start_point, r=1.5, stroke_width=0.1)
        rects_81_new = self.create_rects(num=81, start_point=start_point, r=1.5, stroke_width=0.0).scale([1, 1.001, 1])

        rects_y_7_new = rects_7_new.copy().set_fill(color=YELLOW).rotate(PI, about_point=start_point + r * UP + PI * r * RIGHT)
        rects_y_17_new = rects_17_new.copy().set_fill(color=YELLOW).rotate(PI, about_point=start_point + r * UP + PI * r * RIGHT)
        rects_y_37_new = rects_37_new.copy().set_fill(color=YELLOW).rotate(PI, about_point=start_point + r * UP + PI * r * RIGHT)
        rects_y_81_new = rects_81_new.copy().set_fill(color=YELLOW).rotate(PI, about_point=start_point + r * UP + PI * r * RIGHT)

        area_b = Polygon(*([(np.array([PI * r - r * t, r * (1 - np.cos(t)), 0]) + start_point) for t in np.linspace(0, PI, 100)] + [start_point]),
                         stroke_width=0.1, stroke_color=BLACK, fill_color=BLUE, fill_opacity=0.8)
        area_y = area_b.copy().set_fill(color=YELLOW).rotate(PI, about_point=start_point + r * UP + PI * r * RIGHT)
        self.play(FadeOut(formula))

        start_new = start_point + DOWN * 3.5
        ground_line_new = ground_line.copy().shift(DOWN * 3.5)
        curve_new = curve.copy().shift(DOWN * 3.5)

        init_O = start_new + r * UP
        circle_init = circle.copy().move_to(init_O)
        circle_new = circle.copy().move_to(init_O)
        circle_mid = circle.copy().move_to(init_O + r * PI * RIGHT)

        dot_O_init = Dot(init_O, color=YELLOW, plot_depth=1)
        dot_O = Dot(init_O, color=YELLOW, plot_depth=1)
        dot_O_2 = Dot(init_O + r * PI * RIGHT, color=YELLOW, plot_depth=1)

        dot_P_init = Dot(init_O + r * DOWN, color=BLUE, plot_depth=1)
        dot_P = Dot(init_O + r * DOWN, color=BLUE, plot_depth=1)
        dot_P_2 = Dot(init_O + r * DOWN + r * PI * RIGHT, color=BLUE, plot_depth=1)

        line_r_init = Line(dot_O.get_center(), dot_P.get_center(), stroke_width=2.5)
        line_r = Line(dot_O.get_center(), dot_P.get_center(), stroke_width=2.5)
        line_r_2 = Line(dot_O_2.get_center(), dot_P_2.get_center(), stroke_width=2.5)
        line_PP2 = Line(dot_P.get_center(), dot_P_2.get_center(), stroke_width=2.5, color=BLUE)
        line_PP_init = DashedLine(dot_P.get_center(), dot_P_init.get_center(), stroke_width=2.5, color=BLUE)

        get_t = lambda : (dot_O.get_center()[0] - init_O[0]) / r
        get_P = lambda t: np.array([t - np.sin(t), 1 - np.cos(t), 0]) * r
        get_P2 = lambda t: np.array([PI - np.sin(t), 1 - np.cos(t), 0]) * r
        get_P_init = lambda t: np.array([- np.sin(t), 1 - np.cos(t), 0]) * r

        dot_P_init.add_updater(lambda d: d.move_to(start_new + get_P_init(get_t())))
        dot_P.add_updater(lambda d: d.move_to(start_new + get_P(get_t())))
        dot_P_2.add_updater(lambda d: d.move_to(start_new + get_P2(get_t())))
        line_r_init.add_updater(lambda l: l.become(Line(init_O, start_new + get_P_init(get_t()), stroke_width=2.5)))
        line_r.add_updater(lambda l: l.become(Line(init_O + r * get_t() * RIGHT, start_new + get_P(get_t()), stroke_width=2.5)))
        line_r_2.add_updater(lambda l: l.become(Line(init_O + r * PI * RIGHT, start_new + get_P2(get_t()), stroke_width=2.5)))
        line_PP2.add_updater(lambda l: l.become(Line(start_new + get_P(get_t()), start_new + get_P2(get_t()), stroke_width=2.5, color=BLUE)))
        line_PP_init.add_updater(lambda l: l.become(DashedLine(start_new + get_P_init(get_t()), start_new + get_P(get_t()), stroke_width=2.5, color=BLUE)))
        circle_new.add_updater(lambda c: c.move_to(dot_O))

        g1 = VGroup(dot_P, dot_P_2, dot_O, line_r, line_r_2, line_PP2)

        self.play(ShowCreation(ground_line_new))
        self.play(ShowCreation(curve_new), FadeIn(circle_new))
        self.add(circle_init, dot_O_init)
        self.wait(0.2)
        self.play(FadeIn(dot_O))
        self.play(FadeIn(dot_P), FadeIn(line_r))
        self.wait(0.4)
        self.play(ShowCreation(dot_O_2), run_time=0.4)
        dash_line = DashedLine(init_O, dot_O_2.get_center(), color=YELLOW, stroke_width=2.5, plot_depth=0.5)
        self.play(ShowCreation(dash_line))
        self.wait(0.4)
        self.play(dot_O.shift, r * PI * RIGHT, run_time=2.5)

        self.play(FadeIn(dot_P_init), ShowCreation(line_r_init), ShowCreation(line_PP_init))
        self.add(dot_O_2, dot_P_2, line_r_2, line_PP2, circle_mid)
        self.wait(0.75)

        self.play(dot_O.shift, -0.36 * r * PI * RIGHT, rate_func=linear, run_time=3.6)

        g2 = g1.copy().suspend_updating()
        self.add(g2)

        self.play(dot_O.shift, -0.28 * r * PI * RIGHT, rate_func=linear, run_time=2.8)

        angle_1 = Angle(dot_O.get_center(), dot_O_2.get_center(), g2[1].get_center(), radius=0.5, color=YELLOW)
        angle_2 = Angle(dot_O.get_center(), dot_O_2.get_center(), g1[1].get_center(), radius=0.5, color=YELLOW)
        angle_3 = Angle(dot_O_init.get_center(), g2[2].get_center(), g2[0].get_center(), radius=0.5, color=YELLOW)
        angle_4 = Angle(dot_O_init.get_center(), dot_O.get_center(), g1[0].get_center(), radius=0.5, color=YELLOW)

        self.play(ShowCreation(angle_1), ShowCreation(angle_2))
        self.play(ShowCreation(angle_3), ShowCreation(angle_4))
        self.wait(0.8)
        line_down = Line(line_PP2.get_start(), line_PP2.get_end(), color=BLUE, stroke_opacity=0.5, stroke_width=16)
        line_up = Line(g2[5].get_start(), g2[5].get_end(), color=BLUE, stroke_opacity=0.5, stroke_width=16)
        # line_down.set_plot_depth(2), line_up.set_plot_depth(2)
        # line_down.suspend_updating(), line_up.suspend_updating()
        brace = Brace(dash_line, DOWN, color=RED)
        tex = brace.get_tex('\\pi r').set_color(RED)
        tex.scale(1.5) # .shift(UP * 0.05)
        self.play(ShowCreation(line_down))
        self.play(ShowCreation(line_up))
        self.wait(0.4)
        self.play(line_down.shift, dot_O.get_center() - dot_P.get_center(), rate_func=linear, run_time=1.2)
        self.wait(0.4)
        self.play(line_up.shift, init_O - g2[0].get_center(), rate_func=linear, run_time=1.2)
        self.wait(0.6)
        self.play(FadeInFromDown(brace))
        self.play(Write(tex))
        self.wait(0.8)

        explain_text = Text('距黄虚线相等的上下两\n'
                            '蓝色线的总和固定（πr）', font='思源黑体 Bold')
        t2c = {'黄虚线': YELLOW, '蓝色线': BLUE, 'πr':RED}
        explain_text.set_color_by_t2c(t2c)
        explain_text.scale(0.5).next_to(dot_O_2, RIGHT * 2.4)
        self.play(Write(explain_text), run_time=3)
        self.play(ShowCreation(SurroundingRectangle(explain_text)), run_time=1.2)
        self.wait()

        self.play(ReplacementTransform(rects_81, rects_7_new), ReplacementTransform(rects_y_81, rects_y_7_new))
        for rect, rect_y in zip(rects_7_new, rects_y_7_new): self.play(rect.align_to, rects_7, LEFT, rect_y.align_to, rects_y_7, RIGHT, run_time=0.4)
        self.wait(0.8)
        self.play(FadeOut(rects_7_new), FadeOut(rects_y_7_new), FadeIn(rects_17_new), FadeIn(rects_y_17_new), rate_func=linear, run_time=0.9)

        for rect, rect_y in zip(rects_17_new, rects_y_17_new): self.play(rect.align_to, rects_17, LEFT, rect_y.align_to, rects_y_17, RIGHT, run_time=0.32)
        self.wait(0.8)
        self.play(FadeOut(rects_17_new), FadeOut(rects_y_17_new), FadeIn(rects_37_new), FadeIn(rects_y_37_new), rate_func=linear, run_time=0.9)
        for rect, rect_y in zip(rects_37_new, rects_y_37_new): self.play(rect.align_to, rects_37, LEFT, rect_y.align_to, rects_y_37, RIGHT, run_time=0.2)
        self.wait(1.)

        for rect, rect_y in zip(rects_81_new, rects_y_81_new):
            rect.align_to(rects_81_new, LEFT)
            rect_y.align_to(rects_y_81_new, RIGHT)

        self.play(ReplacementTransform(rects_37_new, rects_81_new), ReplacementTransform(rects_y_37_new, rects_y_81_new), run_time=1.2)
        self.wait(0.4)
        self.play(FadeOut(rects_81_new), FadeIn(area_b), FadeOut(rects_y_81_new), FadeIn(area_y), rate_func=linear, run_time=1.25)
        self.wait(1.2)
        self.play(area_y.shift, PI * r * LEFT, run_time=1.2)
        self.wait(1)

        tex2color = {'S_{\\text{蓝}}': BLUE, 'S_{\\text{黄}}': YELLOW, 'S_{\\text{红}}': RED,
                     '2r': RED, '\\pi r': RED, '2\\pi r^2': RED, '3\\pi r^2': PINK, 'S': PINK}
        formula_02 = TexMobject('S_{\\text{蓝}}', '+ ', 'S_{\\text{黄}}', '=', '2r', '\\times', '\\pi r', plot_depth=5)
        # formula_02.set_color_by_tex_to_color_map(tex2color)
        formula_02[0].set_color(BLUE), formula_02[2].set_color(YELLOW), formula_02[4].set_color(RED), formula_02[6].set_color(RED),
        formula_02.scale(1.5).next_to(area_y, RIGHT * 2.5)
        formula_02_2 = TexMobject('S_{\\text{蓝}}', '+ ', 'S_{\\text{黄}}', '=', '2\\pi r^2', plot_depth=5)
        # formula_02_2.set_color_by_tex_to_color_map(tex2color)
        formula_02_2[0].set_color(BLUE), formula_02_2[2].set_color(YELLOW), formula_02_2[4].set_color(RED)
        formula_02_2.scale(1.5).next_to(area_y, RIGHT * 2.5)

        formula_03 = TexMobject('\\therefore', 'S', '=', 'S_{\\text{蓝}}', '+', 'S_{\\text{黄}}', '+', 'S_{\\text{红}}', '=', '3\\pi r^2', plot_depth=5)
        # formula_03.set_color_by_tex_to_color_map(tex2color)
        formula_03[1].set_color(PINK), formula_03[3].set_color(BLUE), formula_03[5].set_color(YELLOW), formula_03[7].set_color(RED), formula_03[9].set_color(PINK)
        formula_03.scale(1.6).to_corner(LEFT * 2.5 + UP * 8.75)
        self.play(Write(formula_02), run_time=1.5)
        self.wait(0.8)
        self.play(ReplacementTransform(formula_02, formula_02_2), run_time=1.5)
        self.wait(0.4)
        self.play(ShowCreation(SurroundingRectangle(formula_02, plot_depth=3)), run_time=1.2)
        self.wait(1.5)
        mask_rect = Rectangle(color=BLACK, fill_color=BLACK, fill_opacity=1, plot_depth=3).scale([10, 4, 1]).align_to(ORIGIN, UP)
        self.play(FadeIn(mask_rect), run_time=1.2)
        self.wait()
        self.play(Write(formula_03[0:8]), run_time=2.5)
        self.wait(0.2)
        self.play(Write(formula_03[8:10]))
        self.wait(4)

    def create_rects(self, num=7, r=1, start_point=ORIGIN, color=BLUE, stroke_width=0.5):
        x = lambda t: r * (t - np.sin(t))
        # y = lambda t: r * (1 - np.cos(t))
        x_c = lambda t: r * PI - r * np.sin(t) + 1e-3
        t = lambda y: np.arccos(1 - y/r)
        rects = VGroup()
        h = 2 * r / num
        s = start_point
        for i in range(num):
            h_i = h * i
            x_l, x_r = x(t(h_i)), x_c(t(h_i))
            rect_i = Polygon(s + x_l * RIGHT + h_i * UP, s + x_r * RIGHT + h_i * UP,
                             s + x_r * RIGHT + (h_i + h) * UP, s + x_l * RIGHT + (h_i + h) * UP,
                             fill_color=color, fill_opacity=0.8, stroke_width=stroke_width, stroke_color=BLACK)
            rects.add(rect_i)
        return rects

class Text(Scene):
    '''Area_divide_into_rect这个场景后面的动画有一点小问题，不想重新再渲染了，用这个场景在后期修补下'''
    def construct(self):


        formula_03 = TexMobject('\\therefore', 'S', '=', 'S_{\\text{蓝}}', '+', 'S_{\\text{黄}}', '+', 'S_{\\text{红}}', '=', '3\\pi r^2', plot_depth=5)
        # formula_03.set_color_by_tex_to_color_map(tex2color)
        formula_03[1].set_color(PINK), formula_03[3].set_color(BLUE), formula_03[5].set_color(YELLOW), formula_03[7].set_color(RED), formula_03[9].set_color(PINK)
        formula_03.scale(1.6).to_corner(LEFT * 2.5 + UP * 8.75)

        self.play(Write(formula_03[0:8]), run_time=2.5)
        self.wait(0.2)
        self.play(Write(formula_03[8:10]))
        self.wait(4)

class Ending(Scene):
    """用来骗三连的结尾"""
    def construct(self):

        r = 1.45
        start_point = DOWN * r + PI * r * LEFT
        init_O = start_point + r * UP
        curve = ParametricFunction(lambda t: start_point + r * np.array([t-np.sin(t), 1-np.cos(t), 0]),
                                      t_min=0, t_max=PI * 2, stroke_width=2)

        # get_t = lambda : (dot_O.get_center()[0] - init_O[0]) / r
        get_P = lambda t: np.array([t - np.sin(t), 1 - np.cos(t), 0]) * r
        area = Polygon(*[init_O + r * DOWN + get_P(t) for t in np.linspace(0, TAU, 100)],
                       fill_color=YELLOW, fill_opacity=0.95, stroke_width=0)

        circle_01 = Circle(radius=r-0.1, stroke_width=20, color=PINK, fill_color=PINK, fill_opacity=1).move_to(LEFT * 2.75 * r)
        circle_02 = Circle(radius=r-0.1, stroke_width=20, color=BLUE, fill_color=BLUE, fill_opacity=1).move_to(LEFT * 0)
        circle_03 = Circle(radius=r-0.1, stroke_width=20, color=ORANGE, fill_color=ORANGE, fill_opacity=1).move_to(RIGHT * 2.75 * r)
        circle_11, circle_12, cirlce_13 = circle_01.copy().set_fill(opacity=0), circle_02.copy().set_fill(opacity=0), circle_03.copy().set_fill(opacity=0)

        path = 'my_manim_projects\\my_projects\\resource\\svg_files\\'
        good = SVGMobject(path + 'good.svg', color=PINK).set_width(0.7 * 2 * r).move_to(circle_01).shift(UR * 0.06)
        coin = SVGMobject(path + 'coin.svg', color=BLUE).set_height(0.7 * 2 * r).move_to(circle_02)
        favo = SVGMobject(path + 'favo.svg', color=ORANGE).set_height(0.7 * 2 * r).move_to(circle_03).shift(UR * 0.05)

        self.play(FadeInFromLarge(area), run_time=0.8)
        # self.play(WiggleOutThenIn(area), run_time=0.8)
        self.wait(0.8)
        self.play(ReplacementTransform(area, VGroup(circle_01, circle_02, circle_03)), run_time=0.9)
        self.wait(2.5)

        self.add(circle_11, circle_12, cirlce_13)
        self.play(ReplacementTransform(circle_01, good), ReplacementTransform(circle_02, coin),
                  ReplacementTransform(circle_03, favo), run_time=2)
        self.wait()
        self.play(WiggleOutThenIn(good), WiggleOutThenIn(coin), WiggleOutThenIn(favo), run_time=2)

        self.wait(5)












