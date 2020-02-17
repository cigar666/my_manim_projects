from manimlib.imports import *

class Sum_12_by_cube(Scene):

    def construct(self):

        l = 4.8
        loc = LEFT * l * 1.25 + UP * l * 0.6

        A = loc + RIGHT * l
        B = loc
        C = loc + DOWN * l
        D = loc + RIGHT * l + DOWN * l

        AD_list = [A, D + l * UP * 0.5, D + l * UP * 0.5 ** 2, D + l * UP * 0.5 ** 3, D + l * UP * 0.5 ** 4]
        BD_list = [B, D + l * (UP + LEFT) * 0.5, D + l * (UP + LEFT) * 0.5 ** 2, D + l * (UP + LEFT) * 0.5 ** 3, D + l * (UP + LEFT) * 0.5 ** 4]

        cube = Polygon(A, B, C, D, color=WHITE)

        c_list = color_gradient([GREEN_C, YELLOW], 24)
        colors = [c_list[0], c_list[5], c_list[9], c_list[12], c_list[15], c_list[18], c_list[21], c_list[-1]]

        BCD = Polygon(B, C, D, color=WHITE, fill_color=colors[0], fill_opacity=0.8, stroke_width=2)

        brace = Brace(cube, DOWN)
        text_1 = TexMobject('1').next_to(brace, DOWN * 0.5)

        tri_4 = Polygon(AD_list[0], BD_list[0], BD_list[1], color=WHITE, fill_color=colors[1], fill_opacity=0.8, stroke_width=2)
        tri_8 = Polygon(AD_list[0], BD_list[1], AD_list[1], color=WHITE, fill_color=colors[2], fill_opacity=0.8, stroke_width=2)
        tri_16 = Polygon(AD_list[1], BD_list[1], BD_list[2], color=WHITE, fill_color=colors[3], fill_opacity=0.8, stroke_width=2)
        tri_32 = Polygon(AD_list[1], BD_list[2], AD_list[2], color=WHITE, fill_color=colors[4], fill_opacity=0.8, stroke_width=2)
        tri_64 = Polygon(AD_list[2], BD_list[2], BD_list[3], color=WHITE, fill_color=colors[5], fill_opacity=0.8, stroke_width=2)
        tri_128 = Polygon(AD_list[2], BD_list[3], AD_list[3], color=WHITE, fill_color=colors[6], fill_opacity=0.8, stroke_width=2)
        tri_rest = Polygon(BD_list[3], AD_list[3], D, color=WHITE, fill_color=colors[7], fill_opacity=0.8, stroke_width=2)
        tri_group = VGroup(BCD, tri_4, tri_8, tri_16, tri_32, tri_64, tri_128, tri_rest)

        text_2 = TexMobject('\\frac{1}{2}', background_stroke_color=WHITE).scale(1.6).move_to(BCD).shift(DOWN * 0.9 + LEFT * 0.75)
        text_4 = TexMobject('\\frac{1}{4}', background_stroke_color=WHITE).scale(1.1).move_to(tri_4).shift(UP * 0.15)
        text_8 = TexMobject('\\frac{1}{8}', background_stroke_color=WHITE).scale(0.9).move_to(tri_8).shift(RIGHT * 0.35 + DOWN * 0.45)
        text_16 = TexMobject('\\frac{1}{16}', background_stroke_color=WHITE).scale(0.64).move_to(tri_16).shift(UP * 0.1)
        text_32 = TexMobject('\\frac{1}{32}', background_stroke_color=WHITE).scale(0.4).move_to(tri_32).shift(RIGHT * 0.25 + DOWN * 0.24)
        text_64 = TexMobject('\\frac{1}{64}', background_stroke_color=WHITE).scale(0.3).move_to(tri_64).shift(UP * 0.05)
        text_128 = TexMobject('\\frac{1}{128}', background_stroke_color=WHITE).scale(0.24).move_to(tri_128).shift(RIGHT * 0.1 + DOWN * 0.12)

        text_rest = TexMobject('\\ddots', background_stroke_color=WHITE).scale(0.4).move_to(tri_rest).shift(RIGHT * 0.1 + UP * 0.11)

        formula = TexMobject(*['\\frac{1}{2}', '+', '\\frac{1}{4}', '+', '\\frac{1}{8}', '+', '\\frac{1}{16}', '+\\\\',
                               '\\frac{1}{32}', '+',  '\\frac{1}{64}', '+',  '\\frac{1}{128}', '+', '\\cdots', '\\\\=','1']).scale(1.25).align_to(cube, UP).shift(RIGHT * 3)
        formula[0:8].align_to(formula[8], LEFT)
        formula[15:17].scale(1.25).align_to(formula[8], LEFT).shift(DOWN * 0.65)
        formula[-1].scale(1.8).shift(RIGHT * 0.25)

        self.play(ShowCreation(cube), run_time=1.)
        self.wait(0.2)
        self.play(ShowCreation(brace), Write(text_1), run_time=1.2)
        self.wait(0.6)

        self.play(FadeIn(BCD), run_time=1.25)
        self.wait(0.6)
        self.play(Write(text_2), run_time=0.75)
        self.wait(0.6)

        self.play(TransformFromCopy(BCD, tri_4), run_time=1.2)
        self.wait(0.5)
        self.play(Write(text_4), run_time=1)
        self.wait(0.5)
        self.play(TransformFromCopy(tri_4, tri_8), run_time=0.9)
        self.wait(0.4)
        self.play(Write(text_8), run_time=0.75)
        self.wait(0.3)
        self.play(TransformFromCopy(tri_8, tri_16), run_time=0.72)
        self.wait(0.2)
        self.play(Write(text_16), run_time=0.56)
        self.wait(0.15)
        self.play(TransformFromCopy(tri_16, tri_32), run_time=0.6)
        self.wait(0.1)
        self.play(Write(text_32), run_time=0.45)
        self.wait(0.1)
        self.play(TransformFromCopy(tri_32, tri_64), run_time=0.5)
        self.wait(0.1)
        self.play(Write(text_64), run_time=0.4)
        self.wait(0.1)
        self.play(TransformFromCopy(tri_64, tri_128), run_time=0.4)
        self.wait(0.1)
        self.play(Write(text_128), run_time=0.36)
        self.wait(0.2)
        # self.play(TransformFromCopy(tri_128, tri_rest))
        # self.wait(0.5)
        self.play(Write(text_rest), run_time=0.32)
        self.wait(0.25)
        self.play(FadeIn(tri_rest), run_time=0.25)

        self.wait()

        for i in range(8):
            self.play(TransformFromCopy(tri_group[i], formula[i*2].set_color(colors[i])), run_time=(1-np.sqrt(i) * 0.12))
            self.play(Write(formula[2*i + 1]), run_time=0.45)
            self.wait(0.24)
        self.wait(0.2)
        self.play(TransformFromCopy(cube, formula[-1].set_color(GREEN)), run_time=1.4)
        self.wait(4)

class Sum_13_by_cube(Scene):

    def construct(self):

        loc = LEFT * 3.6 + UP * 0.7
        l = 5

        # cube & rect #
        cube = Cube(color=WHITE, fill_color=YELLOW, fill_opacity=0, stroke_width=2.4).scale(l/2).move_to(loc)

        brace = Brace(cube, DOWN)
        text_1 = TexMobject('1').next_to(brace, DOWN * 0.5)

        rect_3 = Polygon(l/2 * LEFT, l/2 * RIGHT, l/2 * RIGHT + l/3 * UP, l/2 * LEFT + l/3 * UP, stroke_width=1.2,
                         color=WHITE, fill_color=GREEN, fill_opacity=0).move_to(loc).shift(DOWN * l/3)
        rect_2 = rect_3.copy().shift(UP * l/3)
        rect_1 = rect_3.copy().shift(UP * 2 * l/3).set_fill(YELLOW_D, 0)
        rect_group = VGroup(rect_1, rect_2, rect_3)
        rect_group_2 = rect_group.copy().scale(1/3).set_stroke(width=1)
        rect_group_3 = rect_group.copy().scale(1/9).set_stroke(width=0.6)
        rect_group_4 = rect_group.copy().scale(1/27).set_stroke(width=0.25)

        cube_2 = Cube(color=WHITE, fill_color=GREEN, fill_opacity=0, stroke_width=1.2).scale(l/2/3).move_to(loc)
        cube_1 = Cube(color=WHITE, fill_color=YELLOW_D, fill_opacity=0, stroke_width=1.2).scale(l/2/3).move_to(loc).shift(RIGHT * l/3)
        cube_3 = Cube(color=WHITE, fill_color=GREEN, fill_opacity=0, stroke_width=1.2).scale(l/2/3).move_to(loc).shift(LEFT * l/3)
        cube_group = VGroup(cube_1, cube_2, cube_3)
        cube_group_2 = cube_group.copy().scale(1/3).set_stroke(width=1)
        cube_group_3 = cube_group.copy().scale(1/9).set_stroke(width=0.6)
        cube_group_4 = cube_group.copy().scale(1/27).set_stroke(width=0.25)

        small_rect_up = Polygon(l/2 * LEFT, l/2 * RIGHT, l/2 * RIGHT + l/2 * UP, l/2 * LEFT + l/2 * UP, stroke_width=0.1,
                         color=WHITE, fill_color=YELLOW, fill_opacity=11).move_to(loc).shift(UP * l/4)
        small_rect_down = Polygon(l/2 * LEFT, l/2 * RIGHT, l/2 * RIGHT + l/2 * UP, l/2 * LEFT + l/2 * UP, stroke_width=0.1,
                         color=WHITE, fill_color=GREEN, fill_opacity=1).move_to(loc).shift(DOWN * l/4)
        s_group = VGroup(small_rect_up, small_rect_down).scale(1/81)

        group_g = VGroup(rect_group[2], rect_group_2[2], rect_group_3[2], rect_group_4[2],
                         cube_group[2], cube_group_2[2], cube_group_3[2], cube_group_4[2], s_group[1])
        group_y = VGroup(rect_group[0], rect_group_2[0], rect_group_3[0], rect_group_4[0],
                         cube_group[0], cube_group_2[0], cube_group_3[0], cube_group_4[0], s_group[0])

        # text #
        text_3 = TexMobject('\\frac{1}{3}', background_stroke_color=WHITE).scale(1.15).move_to(rect_group[2])
        text_9 = TexMobject('\\frac{1}{9}', background_stroke_color=WHITE).scale(1.05).move_to(cube_group[2])
        text_27 = TexMobject('\\frac{1}{27}', background_stroke_color=WHITE).scale(0.4).move_to(rect_group_2[2])
        text_81 = TexMobject('\\frac{1}{81}', background_stroke_color=WHITE).scale(0.36).move_to(cube_group_2[2])
        text_243 = TexMobject('\\frac{1}{243}', background_stroke_color=WHITE).scale(0.15).move_to(rect_group_3[2])
        text_729 = TexMobject('\\frac{1}{729}', background_stroke_color=WHITE).scale(0.14).move_to(cube_group_3[2])

        equation_01 = TexMobject(*['S_{green}', '=', 'S_{yellow}', '=', '\\frac{1}{2}']).scale(1.4).next_to(cube, RIGHT * 3).align_to(cube, UP)
        equation_01.set_color_by_tex_to_color_map({
            'S_{green}': GREEN, 'S_{yellow}': YELLOW,
        })

        equation_02 = TexMobject(*['\\frac{1}{3}', '+', '\\frac{1}{9}', '+', '\\frac{1}{27}', '+', '\\cdots', '+', '\\frac{1}{3^{i}}', '+', '\\cdots', '\\\\=', '0.5']).scale(1.05)
        equation_02.set_color_by_tex_to_color_map({
            '\\frac{1}{3}': GREEN, '\\frac{1}{9}': GREEN, '\\frac{1}{27}': GREEN, '\\cdots': GREEN, '\\frac{1}{3^{i}}': GREEN, '0.5': GREEN,
        })
        equation_02[0:11].next_to(equation_01, DOWN * 1.5).align_to(equation_01, LEFT)
        equation_02[11:13].scale(1.5).next_to(equation_02[0], DOWN * 3.2).align_to(equation_01, LEFT)
        equation_02[12].scale(1.5).shift(RIGHT * 0.36)
        # animation #

        self.play(ShowCreation(cube), run_time=1.)
        self.wait(0.1)
        self.play(ShowCreation(brace), run_time=0.8)
        self.play(Write(text_1), run_time=0.8)
        self.wait(0.4)

        self.play(FadeIn(rect_group), run_time=0.8)
        self.play(ApplyMethod(rect_group[2].set_opacity, 1.), ApplyMethod(rect_group[0].set_opacity, 1.), run_time=1)
        self.wait(0.4)

        self.play(FadeIn(cube_group), run_time=0.75)
        self.play(ApplyMethod(cube_group[2].set_opacity, 1.), ApplyMethod(cube_group[0].set_opacity, 1.), run_time=0.8)
        self.wait(0.32)

        self.play(FadeIn(rect_group_2), run_time=0.6)
        self.play(ApplyMethod(rect_group_2[2].set_opacity, 1.), ApplyMethod(rect_group_2[0].set_opacity, 1.), run_time=0.6)
        self.wait(0.25)

        self.play(FadeIn(cube_group_2), run_time=0.6)
        self.play(ApplyMethod(cube_group_2[2].set_opacity, 1.), ApplyMethod(cube_group_2[0].set_opacity, 1.), run_time=0.6)
        self.wait(0.2)

        self.play(FadeIn(rect_group_3), run_time=0.5)
        self.play(ApplyMethod(rect_group_3[2].set_opacity, 1.), ApplyMethod(rect_group_3[0].set_opacity, 1.), run_time=0.5)
        self.wait(0.15)

        self.play(FadeIn(cube_group_3), run_time=0.5)
        self.play(ApplyMethod(cube_group_3[2].set_opacity, 1.), ApplyMethod(cube_group_3[0].set_opacity, 1.), run_time=0.5)
        self.wait(0.12)

        self.play(FadeIn(rect_group_4), run_time=0.4)
        self.play(ApplyMethod(rect_group_4[2].set_opacity, 1.), ApplyMethod(rect_group_4[0].set_opacity, 1.), run_time=0.4)
        self.wait(0.1)

        self.play(FadeIn(cube_group_4), run_time=0.3)
        self.play(ApplyMethod(cube_group_4[2].set_opacity, 1.), ApplyMethod(cube_group_4[0].set_opacity, 1.), run_time=0.3)
        self.play(FadeIn(s_group), run_time=0.5)
        self.wait(0.9)

        self.play(TransformFromCopy(group_g, equation_01[0]), run_time=1.5)
        self.wait(0.5)
        self.play(TransformFromCopy(group_y, equation_01[2]), run_time=1.5)
        self.wait(0.2)
        self.play(Write(equation_01[1]), run_time=1)
        self.wait(0.8)
        self.play(Write(equation_01[3:5]), run_time=1.5)
        self.wait()

        self.play(FadeInFromLarge(text_3), run_time=0.4)
        self.wait(0.1)
        self.play(FadeInFromLarge(text_9), run_time=0.4)
        self.wait(0.1)
        self.play(FadeInFromLarge(text_27), run_time=0.4)
        self.wait(0.1)
        self.play(FadeInFromLarge(text_81), run_time=0.4)
        self.wait(0.1)
        self.play(FadeInFromLarge(text_243), run_time=0.4)
        self.wait(0.1)
        self.play(FadeInFromLarge(text_729), run_time=0.4)
        self.wait(0.8)

        self.play(TransformFromCopy(equation_01[0], equation_02[0:11]), run_time=2)
        self.wait(0.5)
        self.play(ShowCreation(SurroundingRectangle(equation_02[0:11], color=GREEN)), run_time=1)
        self.play(Write(equation_02[11]), run_time=0.6)
        self.play(Write(equation_02[-1]), run_time=1)


        self.wait(4)

class Sum_by_poly_3(Scene):

    def construct(self):

        loc = LEFT * 3.2 + DOWN * 2.25
        l = 5.2

        A = UP * l/2 * np.sqrt(3) + loc
        B = LEFT * l/2 + loc
        C = RIGHT * l/2 + loc
        t_a = TextMobject('A', color=RED).move_to(A).shift(UP * 0.3 + RIGHT * 0.15)
        t_b = TextMobject('B', color=RED).move_to(B).shift(DOWN * 0.3 + LEFT * 0.15)
        t_c = TextMobject('C', color=RED).move_to(C).shift(DOWN * 0.3 + RIGHT * 0.15)

        tri_y = Polygon(A, B, C, color=WHITE, fill_opacity=0.0,
                        stroke_width=3.2)
        tri_abc = VGroup(tri_y, t_a, t_b, t_c)

        tri_b_1 = tri_y.copy().set_fill(GREEN, 0.95).set_stroke(width=1.8).scale(0.5).move_to(tri_y).rotate(PI).align_to(tri_y, DOWN)
        blue_tri = VGroup(tri_b_1)
        for i in range(6):
            tri_b = blue_tri[-1].copy().set_stroke(width=1.8 - np.sqrt(i+1) * 0.25).scale(0.5).next_to(blue_tri[-1], UP * 0.00001) #.shift(UP * l/4*2/np.sqrt(3) * 0.5 ** i)
            blue_tri.add(tri_b)

        eq_01 = TexMobject(*['S_{ABC}', '=', '1', '=', 'S_{green}', '+', 'S_{yellow}']).align_to(tri_y, UP).shift(RIGHT * 2.5)
        eq_01.set_color_by_tex_to_color_map({
            'S_{ABC}': RED, 'S_{green}': GREEN, 'S_{yellow}':YELLOW
        })
        eq_02 = TexMobject(*['S_{yellow}', '=', '2', 'S_{green}']).next_to(eq_01, DOWN * 1.5).align_to(eq_01, LEFT)
        eq_02.set_color_by_tex_to_color_map({
            'S_{green}': GREEN, 'S_{yellow}':YELLOW
        })
        eq_02[-1].shift(RIGHT * 0.12)

        eq_03 = TexMobject(*['\\Rightarrow', 'S_{green}', '=', '\\frac{1}{3}']).next_to(eq_02, RIGHT * 1)
        eq_03.set_color_by_tex_to_color_map({'S_{green}': GREEN})

        sum_text = TexMobject('\\therefore', '\\frac{1}{4}', '+', '\\frac{1}{4^2}', '+', '\\frac{1}{4^3}', '+', '\\cdots',
                              '=', '\\frac{1}{3}').next_to(eq_02, DOWN * 1.5).align_to(eq_01, LEFT)
        sum_text.set_color_by_tex_to_color_map({
            '\\frac{1}{4}': GREEN, '\\frac{1}{4^2}': GREEN, '\\frac{1}{4^3}': GREEN, '\\cdots':GREEN, '\\frac{1}{3}': GREEN,
        })

        sum_text[-1].scale(1.1).next_to(sum_text[-2], RIGHT * 0.8)

        self.play(FadeIn(tri_y), run_time=1.)
        self.wait(0.1)
        self.play(Write(t_a), Write(t_b), Write(t_c), time=0.8)
        self.wait(0.5)

        self.play(FadeIn(tri_b_1), run_time=1)
        self.wait(0.5)
        for i in range(6):
            self.play(TransformFromCopy(blue_tri[i], blue_tri[i+1]), run_time=0.6-np.sqrt(i)*0.12)
            self.wait(0.3 - np.sqrt(i) * 0.08)
        self.wait(0.8)


        self.play(TransformFromCopy(tri_abc, eq_01[0]), run_time=1)
        self.wait(0.1)
        self.play(Write(eq_01[1:3]), run_time=0.75)
        self.wait(0.45)
        self.play(ApplyMethod(tri_y.set_fill, YELLOW, 0.8), run_time=1)
        self.wait(1.2)
        self.play(Write(eq_01[3:7]), run_time=1.6)
        self.wait(1.2)
        self.play(Write(eq_02), run_time=1.4)
        self.wait(1.2)
        self.play(Write(eq_03), run_time=1.4)
        self.wait(1.2)
        self.play(Write(sum_text[0].shift(LEFT * 0.1).scale(1.25)), run_time=0.8)
        self.wait(0.5)
        self.play(TransformFromCopy(blue_tri[0], sum_text[1]), run_time=1)
        self.play(Write(sum_text[2]), run_time=0.75)
        self.wait(0.4)
        self.play(TransformFromCopy(blue_tri[1], sum_text[3]), run_time=0.9)
        self.play(Write(sum_text[4]), run_time=0.65)
        self.wait(0.3)
        self.play(TransformFromCopy(blue_tri[2], sum_text[5]), run_time=0.9)
        self.play(Write(sum_text[6]), run_time=0.6)
        self.wait(0.25)
        self.play(TransformFromCopy(blue_tri[3:6], sum_text[7]), run_time=0.9)
        self.wait(0.8)
        self.play(Write(sum_text[-2]), run_time=1)
        self.play(Write(sum_text[-1]), rum_time=1.2)

        self.wait(4)

        self.play(FadeOut(eq_01), FadeOut(eq_02), FadeOut(eq_03), FadeOut(sum_text))
        self.play(ApplyMethod(tri_y.set_fill, YELLOW, 0), FadeOut(blue_tri))
        self.wait(2)

class Poly_3(Scene):

    def construct(self):

        loc = LEFT * 3.2 + DOWN * 2.25
        l = 5.2

        A = UP * l/2 * np.sqrt(3) + loc
        B = LEFT * l/2 + loc
        C = RIGHT * l/2 + loc
        t_a = TextMobject('A', color=RED).move_to(A).shift(UP * 0.3 + RIGHT * 0.15)
        t_b = TextMobject('B', color=RED).move_to(B).shift(DOWN * 0.3 + LEFT * 0.15)
        t_c = TextMobject('C', color=RED).move_to(C).shift(DOWN * 0.3 + RIGHT * 0.15)

        tri_0 = Polygon(A, B, C, color=WHITE, fill_opacity=0.0, stroke_width=3.2)
        tri_abc = VGroup(tri_0, t_a, t_b, t_c)

        tri_1 = tri_0.copy().set_stroke(width=1.8).scale(0.5).move_to(tri_0).rotate(PI).align_to(tri_0, DOWN)
        tri_group = VGroup(tri_1)
        for i in range(7):

            tri_new = tri_group[-1].copy().set_stroke(width=1.8 - np.sqrt(i+1) * 0.32).scale(0.5).rotate(PI).align_to(tri_group[-1], UP * (-1) ** i)
            tri_group.add(tri_new)

        tri_b_1 = tri_0.copy().set_fill(GREEN, 0.9).set_stroke(width=1.8).scale(0.5).move_to(tri_0).align_to(tri_0, UP)
        tri_blue = VGroup(tri_b_1)
        for i in range(7):
            tri_b = tri_blue[-1].copy().set_stroke(width=1.8 - np.sqrt(i+1) * 0.4).shift(-(loc + UP * l/2/np.sqrt(3))).rotate_about_origin(1 * PI / 3).scale_about_point(0.5, ORIGIN).shift(loc + UP * l/2/np.sqrt(3))
            tri_blue.add(tri_b)
        tri_red = tri_blue.copy().shift(-(loc + UP * l/2/np.sqrt(3))).rotate_about_origin(2 * PI /3).shift(loc + UP * l/2/np.sqrt(3)).set_fill(RED, 0.9)
        tri_yellow = tri_red.copy().shift(-(loc + UP * l/2/np.sqrt(3))).rotate_about_origin(2 * PI /3).shift(loc + UP * l/2/np.sqrt(3)).set_fill(YELLOW, 0.9)

        self.add(tri_abc)
        self.wait(0.8)

        for i in range(7):
            self.play(FadeInFromLarge(tri_group[i]), run_time=1.25 - np.sqrt(i) * 0.4)
            self.wait(0.2 - np.sqrt(i) * 0.04)

        self.wait(1.2)
        for i in range(7):
            self.play(FadeIn(tri_blue[i]), FadeIn(tri_red[i]), FadeIn(tri_yellow[i]), run_time=1.25 - np.sqrt(i) * 0.2)
            self.wait(0.25 - np.sqrt(i) * 0.025)
        self.wait(1.25)

        self.play(FadeOut(tri_abc), FadeOut(tri_group), run_time=1)
        self.wait(0.5)

        tb = tri_blue.copy().align_to(t_a, UP).to_edge(LEFT * 1.25)
        tr = tri_red.copy().align_to(t_a, UP).next_to(tb, RIGHT * 3.5)
        ty = tri_yellow.copy().align_to(t_a, UP).next_to(tr, RIGHT * 3.5)


        self.play(ReplacementTransform(tri_blue, tb), ReplacementTransform(tri_red, tr), ReplacementTransform(tri_yellow, ty), run_time=2)
        self.wait(0.2)
        self.play(Write(TexMobject('=').scale(1.5).next_to(tb, RIGHT * 1.4)), Write(TexMobject('=').scale(1.5).next_to(tr, RIGHT * 1.25)), run_time=0.9)
        self.wait(0.8)
        self.play(Write(TexMobject('=').scale(1.5).next_to(ty, RIGHT * 0.4)))
        self.play(Write(TexMobject('\\frac{1}{3}').scale(2.4).next_to(ty, RIGHT * 4.8)), run_time=1)

        sum_text = TexMobject('\\therefore', '\\frac{1}{4}', '+', '\\frac{1}{4^2}', '+', '\\frac{1}{4^3}', '+', '\\cdots',
                              '=', '\\frac{1}{3}').scale(1.75).next_to(tb, DOWN * 2.25).align_to(tb, LEFT)
        sum_text.set_color_by_tex_to_color_map({
            '\\frac{1}{4}': GREEN, '\\frac{1}{4^2}': GREEN, '\\frac{1}{4^3}': GREEN, '\\cdots':GREEN, '\\frac{1}{3}': GREEN,
        })

        self.wait(1.25)
        self.play(Write(sum_text[0]), run_time=0.8)
        self.wait(0.2)
        self.play(TransformFromCopy(tb, sum_text[1:8:2]), Write(sum_text[2:8:2]), run_time=1.75)
        self.wait(0.6)
        self.play(Write(sum_text[8:10]), run_time=1.25)

        self.wait(4)

class Poly_4(Scene):

    def construct(self):

        loc_4 = LEFT * 3.75 + UP * 0.45
        l_4 = 5.15

        cube_group = VGroup()
        for i in range(16):
            cube_i = Cube(color=WHITE, fill_opacity=0, stroke_width=2.-np.sqrt(i) * 0.4).rotate(i*PI/4).scale(l_4/2 * (1/np.sqrt(2)) ** i)
            cube_group.add(cube_i)

        tri_group = VGroup()
        for i in range(16):
            tri_i = Polygon(l_4/2 * (UP + LEFT), l_4/2 * UP, l_4/2 * LEFT, color=WHITE, fill_color=GREEN, fill_opacity=1, stroke_width=1.82-np.sqrt(i) * 0.4)\
                .rotate_about_origin(i*PI/4).scale_about_point((1/np.sqrt(2)) ** i, ORIGIN)
            tri_group.add(tri_i)

        tri_b = tri_group.copy().set_fill(BLUE, 0.0).shift(loc_4)
        tri_r = tri_group.copy().set_fill(RED, 0.0).shift(loc_4)
        tri_y = tri_group.copy().set_fill(YELLOW, 0.0).shift(loc_4)

        cube_group.shift(loc_4)
        tri_group.shift(loc_4)

        brace = Brace(cube_group, DOWN * 0.2)
        text_2 = TexMobject('2').next_to(brace, DOWN * 0.5)

        brace_l = Brace(tri_group[0], LEFT * 0.1)
        text_l = TexMobject('1').scale(0.8).next_to(brace_l, LEFT * 0.4)

        brace_up = Brace(tri_group[0], UP * 0.1)
        text_up = TexMobject('1').scale(0.8).next_to(brace_up, UP * 0.5)

        self.play(ShowCreation(cube_group[0]), run_time=1.)
        self.wait(0.5)
        self.play(ShowCreation(brace), Write(text_2), run_time=1)
        self.wait(0.8)
        for i in range(15):
            self.play(TransformFromCopy(cube_group[i], cube_group[i+1]), run_time=1.1-np.sqrt(i) * 0.3)
            self.wait(0.25-np.sqrt(i) * 0.06)

        self.play(FadeIn(tri_group[0]), run_time=1.)
        self.wait(0.4)
        self.play(ShowCreation(brace_l), Write(text_l), ShowCreation(brace_up), Write(text_up), run_time=1)
        self.wait(0.2)
        for i in range(15):
            self.play(TransformFromCopy(tri_group[i], tri_group[i+1]), run_time=1.1-np.sqrt(i) * 0.3)
            self.wait(0.25-np.sqrt(i) * 0.06)
        self.wait()

        t = 1.2
        dt = 1/30
        n = int(t/dt)

        self.add(tri_y)
        for i in range(n):
            tri_y.shift(-loc_4).rotate_about_origin(-PI/2/n).shift(loc_4).set_opacity(np.sqrt(i) * 0.09+0.15)
            self.wait(dt)
        self.wait(0.4)

        self.add(tri_b.shift(-loc_4).rotate_about_origin(-PI/2).shift(loc_4))
        for i in range(n):
            tri_b.shift(-loc_4).rotate_about_origin(-PI/2/n).shift(loc_4).set_opacity(np.sqrt(i) * 0.09+0.15)
            self.wait(dt)
        self.wait(0.4)

        self.add(tri_r.shift(-loc_4).rotate_about_origin(-PI).shift(loc_4))
        for i in range(n):
            tri_r.shift(-loc_4).rotate_about_origin(-PI/2/n).shift(loc_4).set_opacity(np.sqrt(i) * 0.09+0.15)
            self.wait(dt)
        self.wait(1.4)


        sum_text = TexMobject('S(', ')', '=', '\\frac{1}{4}', '\\times', '2^2', color=YELLOW).scale(2).next_to(cube_group, RIGHT * 2.8).align_to(cube_group, UP)
        sum_text[2].set_color(WHITE), sum_text[3].set_color(GREEN), sum_text[4:6].set_color(WHITE)
        sum_text[1:6].shift(RIGHT * 1.6)
        sum_2 = TexMobject('\\frac{1}{2}', '+', '\\frac{1}{2^2}', '+', '\\frac{1}{2^3}', '+', '\\cdots', color=GREEN)\
            .scale(1.25).next_to(sum_text, DOWN * 1.8).align_to(sum_text, LEFT)
        sum_2.set_color_by_tex_to_color_map({'+': WHITE})

        tri_green = tri_group.copy().scale(0.4).set_stroke(width=0.4).next_to(sum_text[0], RIGHT)
        self.play(TransformFromCopy(tri_group, tri_green), run_time=1.25)
        self.play(Write(sum_text[0:2]))
        self.wait()
        self.play(Write(sum_text[2:6]))
        self.wait()
        self.play(ReplacementTransform(sum_text[3:6], TexMobject('1', color=GREEN).scale(2.5).next_to(sum_text[2], RIGHT * 1.6)))
        self.wait(1.)
        self.play(TransformFromCopy(tri_green, sum_2), run_time=1.6)
        self.wait()
        self.play(Write(TexMobject('=', '1').set_color_by_tex_to_color_map({'1': GREEN}).scale(1.4).next_to(sum_2, RIGHT)), run_time=1.25)

        self.wait(2.5)

class Poly_56(Scene):

    def construct(self):

        loc_5 = LEFT * 3.7
        loc_6 = RIGHT * 3.7

        r_5 = 3
        r_6 = 3

        # poly_5
        p1 = Dot(UP * r_5)
        p2 = p1.copy().rotate_about_origin(TAU/5)
        p3 = p2.copy().rotate_about_origin(TAU/5)
        p4 = p3.copy().rotate_about_origin(TAU/5)
        p5 = p4.copy().rotate_about_origin(TAU/5)
        points = VGroup(p1, p2, p3, p4, p5)
        s5 = np.sqrt((3+np.sqrt(5))/8)
        points_2 = points.copy().rotate_about_origin(TAU/10).scale_about_point(s5, ORIGIN)

        poly_5 = Polygon(p1.get_center(), p2.get_center(), p3.get_center(), p4.get_center(), p5.get_center(), color=WHITE, fill_opactiy=0, stroke_width=2.4)
        poly5_group = VGroup(poly_5)
        for i in range(18):
            p_i = poly5_group[-1].copy().set_stroke(width=2.25 - np.sqrt(i) * 0.5).rotate_about_origin(TAU/10).scale_about_point(s5, ORIGIN)
            poly5_group.add(p_i)

        poly5_group.shift(loc_5)

        tri_1 = Polygon(p1.get_center(), points_2[0].get_center(), points_2[-1].get_center(), color=WHITE, stroke_width=2, fill_color=ORANGE, fill_opacity=.95)
        tri_group = VGroup(tri_1)
        for i in range(24):
            t_i = tri_group[-1].copy().set_stroke(width=2.2 - np.sqrt(i) * 0.5).rotate_about_origin(TAU/10).scale_about_point(s5, ORIGIN)
            tri_group.add(t_i)
        tri_group.shift(loc_5)


        self.wait(0.2)
        for i in range(19):
            self.add(poly5_group[i])
            self.wait(0.25 - np.sqrt(i) * 0.04)
        self.wait(1.2)
        for i in range(25):
            self.add(tri_group[i])
            self.wait(0.25 - np.sqrt(i) * 0.036)

        # poly_6
        p1 = Dot(UP * r_6)
        p2 = p1.copy().rotate_about_origin(TAU/6)
        p3 = p2.copy().rotate_about_origin(TAU/6)
        p4 = p3.copy().rotate_about_origin(TAU/6)
        p5 = p4.copy().rotate_about_origin(TAU/6)
        p6 = p5.copy().rotate_about_origin(TAU/6)
        points = VGroup(p1, p2, p3, p4, p5, p6)
        s6 = np.sqrt(3)/2
        points_2 = points.copy().rotate_about_origin(TAU/12).scale_about_point(s6, ORIGIN)

        poly_6 = Polygon(p1.get_center(), p2.get_center(), p3.get_center(), p4.get_center(), p5.get_center(), p6.get_center(), color=WHITE, fill_opactiy=0, stroke_width=2.4)
        poly6_group = VGroup(poly_6)
        for i in range(24):
            p_i = poly6_group[-1].copy().set_stroke(width=2.25 - np.sqrt(i) * 0.45).rotate_about_origin(TAU/12).scale_about_point(s6, ORIGIN)
            poly6_group.add(p_i)

        poly6_group.rotate_about_origin(-PI/6).shift(loc_6)

        tri_1_6 = Polygon(p2.get_center(), points_2[1].get_center(), points_2[0].get_center(), color=WHITE, stroke_width=2, fill_color=PINK, fill_opacity=.95)
        tri_group_6 = VGroup(tri_1_6)
        for i in range(27):
            t_i = tri_group_6[-1].copy().set_stroke(width=2.25 - np.sqrt(i) * 0.4).rotate_about_origin(TAU/12).scale_about_point(s6, ORIGIN)
            tri_group_6.add(t_i)
        tri_group_6.rotate_about_origin(-PI/6).shift(loc_6)


        self.wait(1.5)
        for i in range(25):
            self.add(poly6_group[i])
            self.wait(0.25 - np.sqrt(i) * 0.04)
        self.wait(1.2)
        for i in range(28):
            self.add(tri_group_6[i])
            self.wait(0.25 - np.sqrt(i) * 0.04)


        self.wait(4)

# class Poly_round_corner_test(Scene):
#
#     def construct(self):
#
#         triangle = Polygon(ORIGIN, RIGHT * 5, UP * 2.5, stroke_width=4).to_edge(LEFT * 2.5).shift(DOWN * 1)
#         triangle_round_corner = triangle.copy().round_corners(0.01).shift(RIGHT * 7.)
#
#         self.add(triangle)
#         self.play(TransformFromCopy(triangle, triangle_round_corner))
#         self.wait(4)

class Achilles_and_tortoise(Scene):

    def construct(self):

        svg_path = 'my_projects\\resource\\svg_files\\'
        number_line = NumberLine(x_min=0, x_max=10, color=WHITE).to_corner(LEFT * 4.5 + DOWN * 5)

        achilles = SVGMobject(svg_path + 'Achilles.svg', color=BLUE).scale(1.25).next_to(number_line, UP * 0.8).align_to(number_line, LEFT).shift(LEFT)
        tortoise = SVGMobject(svg_path + 'tortoise.svg', color=YELLOW).scale(0.3).next_to(number_line, UP * 0.8).shift(RIGHT * 1.1)
        p1, p2 = number_line.n2p(0), number_line.n2p(6)
        dot_1, dot_2 = Dot(p1, color=BLUE).scale(1.5), Dot(p2, color=YELLOW).scale(1.5)

        brace = Brace(Line(p1, p2), DOWN)
        t_a = brace.get_tex('distance=a').set_color(RED)

        arrow_a = Vector(RIGHT * 2.75).next_to(achilles, RIGHT * 1.6).shift(DOWN * 0.25)
        v_a = TexMobject('v=1', color=BLUE).scale(1.2).next_to(arrow_a, UP * 0.8).shift(LEFT * 0.2)

        arrow_t = Vector(RIGHT * 2).align_to(dot_2, LEFT).align_to(arrow_a, UP).shift(RIGHT * 0.2)
        v_t = TexMobject('\\upsilon =r', color=YELLOW).scale(1.2).next_to(arrow_t, UP*0.8)

        self.add(number_line)
        self.wait(0.4)

        self.play(ShowCreation(achilles))
        self.wait(0.2)
        self.play(ShowCreation(tortoise))
        self.wait(0.2)
        self.play(FadeInFromLarge(dot_1))
        self.play(FadeInFromLarge(dot_2))
        self.play(ShowCreation(brace), Write(t_a))
        self.wait()
        self.play(WiggleOutThenIn(achilles))
        self.play(ShowCreation(arrow_a), Write(v_a))
        self.wait()

        self.play(WiggleOutThenIn(tortoise))
        self.play(ShowCreation(arrow_t), Write(v_t))

        self.wait(4)

class Plot_achiless_tortoise(GraphScene):

    CONFIG = {
        "x_min": 0,
        "x_max": 6,
        "y_min": 0,
        "y_max": 6,
        "x_axis_width": 5.6,
        "y_axis_height": 5.6,
        "y_axis_label": '',
        "x_axis_label": '',
        "axes_color": WHITE,
        "graph_origin": LEFT * 6.2 + DOWN * 3.,
        "exclude_zero_label": False,
    }


    def construct(self):

        self.setup_axes(animate=True)
        s = TexMobject('s', color=PINK).scale(1.4).move_to(self.coords_to_point(-0.5, 6.2))
        t = TexMobject('t', color=ORANGE).scale(1.4).move_to(self.coords_to_point(6.2, -0.5))
        self.play(Write(s), Write(t))
        self.wait()

        achilles = self.get_graph(lambda x: x, x_min=0, x_max=5.5, color=BLUE)
        k_t = (1-2.5/5.5)
        tortoise = self.get_graph(lambda x: 2.5 + x * k_t, x_min=0, x_max=5.5, color=YELLOW)

        svg_path = 'my_projects\\resource\\svg_files\\'

        achilles_svg = SVGMobject(svg_path + 'Achilles.svg', color=BLUE, stroke_width=0.15).scale(0.7).move_to(self.coords_to_point(3.25, 2.1))
        tortoise_svg = SVGMobject(svg_path + 'tortoise.svg', color=YELLOW).scale(0.25).move_to(self.coords_to_point(2.4, 4.5))
        func_a = TexMobject('s', '=', '1', '\\cdot', 't').scale(1.1).next_to(achilles_svg, DOWN * 0.9)
        func_a.set_color_by_tex_to_color_map({'1':BLUE, 's': PINK, 't': ORANGE})
        func_t = TexMobject('s', '=', 'r', '\\cdot', 't', '+', 'a').scale(1.).next_to(tortoise_svg, UP * 0.9)
        func_t.set_color_by_tex_to_color_map({'r':YELLOW, 'a':RED, 's': PINK, 't': ORANGE})


        tri_a = RegularPolygon(n=3, start_angle=0, color=RED, fill_color=RED, fill_opacity=1).scale(0.1).next_to(self.coords_to_point(0, 2.5), LEFT* 0.1)
        y_label_a = TexMobject('a', color=RED).next_to(tri_a, LEFT * 0.6)

        intersection_p = Dot(self.coords_to_point(5.5, 5.5), color=GREEN).scale(1.5)
        p_xy = TexMobject('(', '\\frac{a}{1-r}', ',', '\\frac{a}{1-r}',')').scale(0.8).next_to(intersection_p, UP * 0.6)
        p_xy[1].set_color(ORANGE), p_xy[3].set_color(PINK)

        text_1 = Text('每次让阿基里斯每次运动到乌龟的位置，', font='新蒂小丸子体').scale(0.36).align_to(self.coords_to_point(6.5, 5.6), LEFT).align_to(self.coords_to_point(6.5, 5.6), UP)
        text_2 = Text('乌龟则会在这段时间往前跑了一丢丢', font='新蒂小丸子体').scale(0.36).next_to(text_1, DOWN * 1).align_to(text_1, LEFT)

        p_a = Dot(self.coords_to_point(0, 0), color=BLUE).scale(1.2)
        p_t = Dot(self.coords_to_point(0, 2.5), color=YELLOW).scale(1.2)

        self.wait(0.5)
        self.play(ShowCreation(achilles))
        self.play(WiggleOutThenIn(achilles_svg))
        self.wait(0.2)
        self.play(Write(func_a))
        self.wait()
        self.play(ShowCreation(tortoise))
        self.play(WiggleOutThenIn(tortoise_svg))
        self.wait(0.2)
        self.play(Write(func_t))
        self.wait(0.2)
        self.play(FadeInFromLarge(VGroup(tri_a, y_label_a)))
        self.wait()
        self.play(FadeInFromLarge(intersection_p))
        self.play(Write(p_xy))
        self.wait(1.2)
        self.play(Write(text_1), run_time=2.4)
        self.wait(0.2)
        self.play(Write(text_2), run_time=2.4)
        self.wait(0.6)

        # chase process
        self.play(FadeInFromLarge(p_a), FadeInFromLarge(p_t))
        self.wait(0.2)
        self.play(ApplyMethod(p_a.move_to, self.coords_to_point(2.5, 2.5)))
        s_1 = Arrow(self.coords_to_point(0,0), self.coords_to_point(0, 2.5), max_tip_length_to_length_ratio=0.16, buff=0, color=PINK)
        t_1 = Arrow(self.coords_to_point(0,2.5), self.coords_to_point(2.5, 2.5), max_tip_length_to_length_ratio=0.16, buff=0, color=ORANGE)

        self.play(ShowCreation(s_1))
        self.play(ShowCreation(t_1))
        self.play(ApplyMethod(p_t.move_to, self.coords_to_point(2.5, 2.5 * k_t + 2.5)))
        self.wait(0.2)

        self.play(ApplyMethod(p_a.move_to, self.coords_to_point(2.5 * k_t + 2.5, 2.5 * k_t + 2.5)))
        s_2 = Arrow(self.coords_to_point(2.5, 2.5), self.coords_to_point(2.5, 2.5 * k_t + 2.5), max_tip_length_to_length_ratio=0.2, buff=0, color=PINK)
        t_2 = Arrow(self.coords_to_point(2.5, 2.5 * k_t + 2.5), self.coords_to_point(2.5 * k_t + 2.5, 2.5 * k_t + 2.5), max_tip_length_to_length_ratio=0.2, buff=0, color=ORANGE)
        self.play(ShowCreation(s_2))
        self.play(ShowCreation(t_2))
        self.play(ApplyMethod(p_t.move_to, self.coords_to_point(2.5 * k_t + 2.5, (2.5 * k_t + 2.5) * k_t + 2.5)))
        self.wait(0.2)
        pos_t = (2.5 * k_t + 2.5) * k_t + 2.5
        self.play(ApplyMethod(p_a.move_to, self.coords_to_point(pos_t, pos_t)))
        s_3 = Arrow(self.coords_to_point(2.5 * k_t + 2.5, 2.5 * k_t + 2.5), self.coords_to_point(2.5 * k_t + 2.5, pos_t), max_tip_length_to_length_ratio=0.24, buff=0, color=PINK)
        t_3 = Arrow(self.coords_to_point(2.5 * k_t + 2.5, pos_t), self.coords_to_point(pos_t, pos_t), max_tip_length_to_length_ratio=0.24, buff=0, color=ORANGE)
        self.play(ShowCreation(s_3))
        self.play(ShowCreation(t_3))
        self.play(ApplyMethod(p_t.move_to, self.coords_to_point(pos_t, pos_t * k_t + 2.5)))
        self.wait(0.2)

        pos_new = pos_t * k_t + 2.5
        self.play(ApplyMethod(p_a.move_to, self.coords_to_point(pos_new, pos_new)))
        s_4 = Arrow(self.coords_to_point(pos_t, pos_t), self.coords_to_point(pos_t, pos_new), max_tip_length_to_length_ratio=0.25, buff=0, color=PINK)
        t_4 = Arrow(self.coords_to_point(pos_t, pos_new), self.coords_to_point(pos_new, pos_new), max_tip_length_to_length_ratio=0.25, buff=0, color=ORANGE)
        self.play(ShowCreation(s_4))
        self.play(ShowCreation(t_4))
        self.play(ApplyMethod(p_t.move_to, self.coords_to_point(pos_new, pos_new * k_t + 2.5)))
        self.wait(0.4)
        pos_t = pos_new
        pos_new = pos_new * k_t + 2.5
        s_5 = Arrow(self.coords_to_point(pos_t, pos_t), self.coords_to_point(pos_t, pos_new), max_tip_length_to_length_ratio=0.25, buff=0, color=PINK)
        pos_t = pos_new
        pos_new = pos_new * k_t + 2.5
        s_6 = Arrow(self.coords_to_point(pos_t, pos_t), self.coords_to_point(pos_t, pos_new), max_tip_length_to_length_ratio=0.25, buff=0, color=PINK)


        text_s1 = TexMobject('a', color=PINK).scale(1.25).next_to(s_1, LEFT * 0.2)
        text_t1 = TexMobject('a', color=ORANGE).scale(1.25).next_to(t_1, DOWN * 0.1).shift(LEFT * 0.15)
        text_s2 = TexMobject('a', 'r', color=PINK).scale(0.75).next_to(s_2, LEFT * 0.2)
        text_t2 = TexMobject('a', 'r', color=ORANGE).scale(0.75).next_to(t_2, DOWN * 0.1).shift(LEFT*0.1)
        text_s3 = TexMobject('a', 'r^2', color=PINK).scale(0.4).next_to(s_3, LEFT * 0.15)
        text_t3 = TexMobject('a', 'r^2', color=ORANGE).scale(0.4).next_to(t_3, DOWN * 0.05).shift(UP * 0.05+LEFT*0.05)
        text_group = VGroup(VGroup(text_s1, text_t1), VGroup(text_s2, text_t2), VGroup(text_s3, text_t3))
        for i in range(3):
            self.play(FadeIn(text_group[i]))
            self.wait(0.5)
        self.wait(0.6)

        text_3 = Text('每个阶段对应时间为：', font='新蒂小丸子体').scale(0.36).next_to(text_2, DOWN * 1.6).align_to(text_2, LEFT)
        text_31 = TexMobject('a', ',', 'ar', ',', 'ar^2', ',', 'ar^3', ',','\\cdots', color=WHITE).set_color_by_tex_to_color_map({
            'a': ORANGE, 'ar': ORANGE, 'ar^2': ORANGE, 'ar^3': ORANGE,'\\cdots': ORANGE,
        })
        text_31.scale(1).next_to(text_3, DOWN * 0.6).align_to(text_3, LEFT)
        self.play(Write(text_3), run_time=1.8)
        self.play(Write(text_31), run_time=1.6)
        self.wait()

        text_4 = Text('每个阶段对应路程为：', font='新蒂小丸子体').scale(0.36).next_to(text_31, DOWN * 1.6).align_to(text_2, LEFT)
        text_41 = TexMobject('a', ',', 'ar', ',', 'ar^2', ',', 'ar^3', ',','\\cdots', color=WHITE).set_color_by_tex_to_color_map({
            'a': PINK, 'ar': PINK, 'ar^2': PINK, 'ar^3': PINK, '\\cdots': PINK,
        })
        text_41.scale(1).next_to(text_4, DOWN * 0.6).align_to(text_4, LEFT)
        self.play(Write(text_4), run_time=1.8)
        self.play(Write(text_41), run_time=1.6)
        self.wait(1.5)

        self.play(FadeOut(text_1), FadeOut(text_2))
        self.play(ApplyMethod(VGroup(text_3, text_31, text_4, text_41).align_to, text_1, UP))
        self.wait(0.5)

        text_5 = Text('则，追乌龟的总路程（或总时间）为：', font='新蒂小丸子体').scale(0.36).next_to(text_41, DOWN * 1.6).align_to(text_4, LEFT)
        text_51 = TexMobject('a', '+', 'ar', '+', 'ar^2', '+', 'ar^3', '+','\\cdots', color=WHITE).set_color_by_tex_to_color_map({
            'a': PINK, 'ar': PINK, 'ar^2': PINK, 'ar^3': PINK, '\\cdots': PINK,
        })
        text_51.scale(1).next_to(text_5, DOWN * 0.6).align_to(text_5, LEFT)
        self.play(Write(text_5), run_time=2.4)
        self.play(Write(text_51), run_time=1.8)
        self.wait(0.8)
        # self.play(FadeOut(achilles_svg), FadeOut(func_a))
        s01 = VGroup(s_1, text_s1).copy()
        s02 = VGroup(s_2, text_s2).copy()
        s03 = VGroup(s_3, text_s3).copy()

        self.play(ApplyMethod(s01.shift, (self.coords_to_point(5.5, 0)[0] - s01[0].get_center()[0]) * RIGHT), run_time=0.75)
        self.play(ApplyMethod(s02.shift, (self.coords_to_point(5.5, 0)[0] - s02[0].get_center()[0]) * RIGHT), run_time=0.6)
        self.play(ApplyMethod(s03.shift, (self.coords_to_point(5.5, 0)[0] - s03[0].get_center()[0]) * RIGHT), run_time=0.5)
        self.play(ApplyMethod(s_4.copy().shift, (self.coords_to_point(5.5, 0)[0] - s_4.get_center()[0]) * RIGHT), run_time=0.4)
        self.play(ApplyMethod(s_5.shift, (self.coords_to_point(5.5, 0)[0] - s_5.get_center()[0]) * RIGHT), run_time=0.35)
        self.play(ApplyMethod(s_6.shift, (self.coords_to_point(5.5, 0)[0] - s_6.get_center()[0]) * RIGHT), run_time=0.3)
        self.wait(0.2)

        line = DashedLine(self.coords_to_point(0, 5.5), self.coords_to_point(5.5, 5.5), color=PINK)
        line.get_
        self.play(ShowCreation(line))
        self.wait(0.8)

        text_6 = TexMobject('=', '\\frac{a}{1-r}').scale(1.05).set_color_by_tex_to_color_map({'\\frac{a}{1-r}':PINK})
        text_6.next_to(text_5, DOWN * 3.25).align_to(text_5, LEFT)

        self.play(Write(text_6[0]))
        self.play(TransformFromCopy(p_xy[3], text_6[1]), run_time=1.4)


        self.wait(4)

class Geometric_progression(Scene):

    def construct(self):

        text_1 = Text('等比数列', font='新蒂小丸子体').scale(0.75).to_corner(UP * 2.4 + LEFT * 2)
        text_2 = Text('几何级数', font='新蒂小丸子体').scale(0.75).to_corner(UP * 2.4 + LEFT * 2)

        text_3 = Text('（当r的绝对值小于1时收敛）', font='新蒂小丸子体', color=BLUE).scale(0.6).next_to(text_2, RIGHT)

        text_4 = Text('本视频将使用', font='新蒂小丸子体').scale(0.7).to_corner(UP * 8 + LEFT * 2)
        text_4_2 = Text('Manim', font='新蒂小丸子体', color=ORANGE).scale(0.85).next_to(text_4, RIGHT)
        text_4_3 = Text('数学动画给大家', font='新蒂小丸子体').scale(0.7).next_to(text_4_2, RIGHT)
        text_5 = Text('带来', font='新蒂小丸子体').scale(0.7).to_corner(UP * 11 + LEFT * 2)
        text_5_2 = Text('几何级数', font='新蒂小丸子体', color=BLUE).scale(0.7).next_to(text_5, RIGHT)
        text_5_3 = Text('结果的可视化展示', font='新蒂小丸子体').scale(0.7).next_to(text_5_2, RIGHT)

        a1 = Text('a', font='Comic Sans MS', color=BLUE).scale(0.8).to_corner(UP * 5.6 + LEFT * 3)
        a2 = Text('ar', font='Comic Sans MS', color=BLUE).scale(0.8).next_to(a1, RIGHT * 4.4).align_to(a1, DOWN)
        two = Text('2', font='Comic Sans MS', color=BLUE).scale(0.5).move_to(a2).shift(UP * 0.32 + RIGHT * 0.56)
        three = Text('3', font='Comic Sans MS', color=BLUE).scale(0.5).move_to(a2).shift(UP * 0.32 + RIGHT * 0.56)
        a3 = VGroup(a2.copy(), two).next_to(a2, RIGHT * 4.4).align_to(a1, DOWN)
        a4 = VGroup(a2.copy(), three).next_to(a3, RIGHT * 4.2).align_to(a1, DOWN)

        dots = Text('...', font='Comic Sans MS', color=BLUE).scale(0.8).next_to(a4, RIGHT * 4).shift(DOWN * 0.16)    #.align_to(a1, DOWN)

        self.play(Write(text_1))

        self.play(Write(a1), run_time=0.9)
        self.wait(0.2)
        self.play(Write(a2), run_time=0.8)
        self.wait(0.15)
        self.play(Write(a3), run_time=0.6)
        self.wait(0.1)
        self.play(Write(a4), run_time=0.5)
        self.wait(0.1)
        self.play(Write(dots), run_time=0.6)
        self.wait(1.2)

        self.play(ReplacementTransform(text_1, text_2), run_time=1.25)

        self.play(Write(Text('+', color=WHITE).scale(0.8).next_to(a1, RIGHT * 1.5).align_to(a1, DOWN)), run_time=0.4)
        self.play(Write(Text('+', color=WHITE).scale(0.8).next_to(a2, RIGHT * 1.4).align_to(a1, DOWN)), run_time=0.4)
        self.play(Write(Text('+', color=WHITE).scale(0.8).next_to(a3[0], RIGHT * 2).align_to(a1, DOWN)), run_time=0.4)
        self.play(Write(Text('+', color=WHITE).scale(0.8).next_to(a4[0], RIGHT * 2).align_to(a1, DOWN)), run_time=0.4)
        self.wait(0.5)

        self.play(Write(text_3), run_time=1.5)
        self.wait(0.25)
        self.play(Write(text_4), run_time=1)
        self.play(Write(text_4_2), run_time=0.5)

        self.play(Write(text_4_3), run_time=1.25)
        self.play(Write(text_5), run_time=0.25)
        self.play(Write(text_5_2), run_time=0.8)

        self.play(Write(text_5_3), run_time=1.25)

        self.play(WiggleOutThenIn(text_4_2), run_time=0.8)
        self.play(WiggleOutThenIn(text_5_2), run_time=0.8)

        self.wait(5)

class Intro_achilles(Scene):

    def construct(self):

        svg_path = 'my_projects\\resource\\svg_files\\'

        text_1 = Text('如何证明更一般的情况呢？', font='新蒂小丸子体', color=BLUE).scale(0.9).shift(UP * 1.8)
        text_2 = Text('让我们来回顾一个经典的问题', font='新蒂小丸子体', color=YELLOW).scale(0.7).shift(UP * 0.25)

        achilles_svg = SVGMobject(svg_path + 'Achilles.svg', color=BLUE, stroke_width=0.2).scale(1.25).to_corner(DOWN * 1.8 + LEFT * 6)
        tortoise_svg = SVGMobject(svg_path + 'tortoise.svg', color=YELLOW).scale(0.64).to_corner(DOWN * 1.8 + RIGHT * 6)

        self.wait(0.4)
        self.play(Write(text_1), run_time=1.8)
        self.wait(0.6)
        self.play(Write(text_2), run_time=2)
        self.wait(0.4)
        self.play(FadeInFromLarge(achilles_svg))
        self.play(FadeInFromLarge(tortoise_svg))
        self.play(WiggleOutThenIn(achilles_svg), WiggleOutThenIn(tortoise_svg))

        self.wait(2)

class Sum_of_n_terms(GraphScene):

    CONFIG = {
        "x_min": 0,
        "x_max": 9.25,
        "y_min": 0,
        "y_max": 1.05,
        "x_axis_width": 9.25,
        "y_axis_height": 5.25,
        "y_axis_label": 'y',
        "x_axis_label": 'x',
        "x_tick_frequency": 1,
        "y_tick_frequency": 0.2,
        "axes_color": WHITE,
        "graph_origin": LEFT * 6. + DOWN * 3.,
    }

    def construct(self):

        # text_01 = Text('', font='').to_corner(UP * 1.6 + LEFT * 1.8)

        self.setup_axes(animate=True)
        r = 0.8
        curve_r_n = self.get_graph(lambda n: r**n, color=RED, x_min=0, x_max=9)

        self.wait()
        self.play(ShowCreation(curve_r_n))

        self.wait(2)
