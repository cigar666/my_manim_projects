from manimlib.imports import *

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

class Right_angle(VGroup):
    CONFIG = {
        'size': 0.25,
        'stroke_color': WHITE,
        'stroke_width': 3.2,
        'fill_color': BLUE,
        'fill_opacity': 0.5,
        'on_the_right': True,
    }
    def __init__(self, corner=ORIGIN, angle=0, **kwargs):
        VGroup.__init__(self, **kwargs)
        self.corner = ORIGIN
        self.angle = 0
        r = UR if self.on_the_right else UL
        self.add(Polygon(ORIGIN, RIGHT * self.size * r, UR * self.size * r, UP * self.size * r, stroke_width=0,
                         fill_color=self.fill_color, fill_opacity=self.fill_opacity),
                 Line(RIGHT * self.size * r, UR * self.size * r + UP * self.stroke_width/100/2 * 0.8, stroke_width=self.stroke_width, stroke_color=self.stroke_color),
                 Line(UR * self.size * r + RIGHT * self.stroke_width/100/2 * r * 0.8, UP * self.size * r, stroke_width=self.stroke_width, stroke_color=self.stroke_color),
                 )
        self.move_corner_to(corner)
        self.change_angle_to(angle)

    def move_corner_to(self, new_corner):
        self.shift(new_corner - self.corner)
        self.corner = new_corner
        return self

    def change_angle_to(self, new_angle):
        self.rotate(new_angle - self.angle, about_point=self.corner)
        self.angle = new_angle
        return self

class Test(Scene):

    def construct(self):

        text_RM = TexMobject('\\mathbf{RM', '=', '\\sqrt{{a', '^2', '+', 'b', '^2}', '\\over', '{2}}', color=WHITE).shift(UP * 0.6)
        text_GM = TexMobject('\\sqrt{', '1', '2}', '\\,', color=WHITE).shift(DOWN * 0.6)
        text_RM[-1].set_color(RED)
        angle = Right_angle(size=2)
        dot_o = Dot(color=GREEN)
        #self.add(dot_o, angle)
        self.play(Write(text_RM))
        self.wait()
        self.play(Write(text_GM))
        self.wait(5)

class AM_GM(Scene):

    def construct(self):

        # dot position
        A = LEFT * 3 # + DOWN * 0.25
        r = 3.25
        B = r * LEFT + A
        C = r * RIGHT + A
        self.theta = PI/6 # init theta
        get_M = lambda theta: r * np.cos(theta * 2) * LEFT + r * np.sin(theta * 2) * UP + A
        get_G = lambda theta: r * np.cos(theta * 2) * LEFT + A
        get_H = lambda theta: r * np.cos(theta * 2) ** 2 * (np.cos(theta * 2) * LEFT + np.sin(theta * 2) * UP) + A
        get_R = lambda theta: r * np.cos(theta * 2) * (np.sin(theta * 2) * LEFT + np.cos(theta * 2) * DOWN) + A
        M = get_M(self.theta)
        G = get_G(self.theta)
        H = get_H(self.theta)
        R = get_R(self.theta)

        # dot, circle, line & angle ...
        circle = Circle(radius=r, color=BLUE).move_to(A)
        arc_config={'color': GRAY, 'stroke_width': 1.5}
        dash_circle = Dashed_Circle(radius=r * np.cos(self.theta * 2), center=A, arc_config=arc_config, arc_ratio=0.64, plot_depth=-0.5)
        line_color = WHITE
        BC = Line(B, C, color=line_color)
        BM = Line(B, M, color=line_color)
        CM = Line(C, M, color=line_color)
        GM = Line(G, M, color=line_color)
        AM = Line(A, M, color=line_color)
        HM = Line(H, M, color=line_color)
        RM = Line(R, M, color=line_color)
        GH = Line(G, H, color=line_color, plot_depth=0.5)
        AR = Line(A, R, color=line_color)

        angle_G = Right_angle(corner=G, plot_depth=0.5)
        angle_A = Right_angle(corner=A, angle=PI/2 - self.theta * 2, on_the_right=False, plot_depth=0.5)
        angle_H = Right_angle(corner=H, angle=PI/2 - self.theta * 2, on_the_right=False, plot_depth=0.5)

        bold_stroke = 10
        bold_color = color_gradient([RED, PINK, BLUE], 4)
        GM_bold = Line(G, M, color=bold_color[1], stroke_width=bold_stroke, plot_depth=0.6)
        AM_bold = Line(A, M, color=bold_color[2], stroke_width=bold_stroke, plot_depth=0.6)
        HM_bold = Line(H, M, color=bold_color[0], stroke_width=bold_stroke, plot_depth=0.6)
        RM_bold = Line(R, M, color=bold_color[3], stroke_width=bold_stroke, plot_depth=0.6)

        color_a = GREEN
        color_b = YELLOW
        GB = Line(A, B, color=color_a, stroke_width=8)
        GC = Line(A, C, color=color_b, stroke_width=8)

        dot_color = PINK
        dot_scale = 1.4
        dot_A = Dot(A, color=RED, plot_depth=1).scale(dot_scale)
        dot_G = Dot(G, color=dot_color, plot_depth=1).scale(dot_scale)
        dot_M = Dot(M, color=dot_color, plot_depth=1).scale(dot_scale)
        dot_H = Dot(H, color=dot_color, plot_depth=1).scale(dot_scale)
        dot_R = Dot(R, color=dot_color, plot_depth=1).scale(dot_scale)
        dot_B = Dot(B, color=GREEN, plot_depth=1)
        dot_C = Dot(C, color=YELLOW, plot_depth=1)

        brace_GB = Brace(GB, DOWN, color=color_a)
        brace_GC = Brace(GC, DOWN, color=color_b)

        # update obj
        dot_G.add_updater(lambda d: d.become(Dot(get_G(self.theta), color=dot_color, plot_depth=1).scale(dot_scale)))
        dot_M.add_updater(lambda d: d.become(Dot(get_M(self.theta), color=dot_color, plot_depth=1).scale(dot_scale)))
        dot_H.add_updater(lambda d: d.become(Dot(get_H(self.theta), color=dot_color, plot_depth=1).scale(dot_scale)))
        dot_R.add_updater(lambda d: d.become(Dot(get_R(self.theta), color=dot_color, plot_depth=1).scale(dot_scale)))

        BM.add_updater(lambda l: l.become(Line(B, get_M(self.theta), color=line_color)))
        CM.add_updater(lambda l: l.become(Line(C, get_M(self.theta), color=line_color)))
        AR.add_updater(lambda l: l.become(Line(A, get_R(self.theta), color=line_color)))
        GH.add_updater(lambda l: l.become(Line(get_G(self.theta), get_H(self.theta), color=line_color, plot_depth=0.5)))
        GB.add_updater(lambda l: l.become(Line(get_G(self.theta), B, color=color_a, stroke_width=8)))
        GC.add_updater(lambda l: l.become(Line(get_G(self.theta), C, color=color_b, stroke_width=8)))

        AM_bold.add_updater(lambda l: l.become(Line(A, get_M(self.theta), color=bold_color[2], stroke_width=bold_stroke, plot_depth=0.6)))
        GM_bold.add_updater(lambda l: l.become(Line(get_G(self.theta), get_M(self.theta), color=bold_color[1], stroke_width=bold_stroke, plot_depth=0.6)))
        HM_bold.add_updater(lambda l: l.become(Line(get_H(self.theta), get_M(self.theta), color=bold_color[0], stroke_width=bold_stroke, plot_depth=0.6)))
        RM_bold.add_updater(lambda l: l.become(Line(get_R(self.theta), get_M(self.theta), color=bold_color[3], stroke_width=bold_stroke, plot_depth=0.6)))

        dash_circle.add_updater(lambda c: c.become(Dashed_Circle(radius=r * np.cos(self.theta * 2), center=A, arc_config=arc_config, arc_ratio=-0.5)))
        angle_G.add_updater(lambda a: a.move_corner_to(get_G(self.theta)))
        angle_A.add_updater(lambda a: a.become(Right_angle(corner=A, angle=PI/2 - self.theta * 2, on_the_right=False or (self.theta>PI/4), plot_depth=0.5)))
        angle_H.add_updater(lambda a: a.become(Right_angle(corner=get_H(self.theta), angle=PI/2 - self.theta * 2, on_the_right=False or (self.theta>PI/4), plot_depth=0.5)))
        a = TexMobject('a', color=color_a).scale(0.9)
        b = TexMobject('b', color=color_b).scale(0.9)
        brace_GB.add_updater(lambda b: b.become(Brace(GB, DOWN, color=color_a).scale(np.array([1,1.8,1])).shift(DOWN*0.3).put_at_tip(TexMobject('.'))))
        brace_GC.add_updater(lambda b: b.become(Brace(GC, DOWN, color=color_b).scale(np.array([1,1.8,1])).shift(DOWN*0.3).put_at_tip(TexMobject('.'))))

        # text
        tex_color = PINK
        tex_A = TexMobject('A', color=tex_color, plot_depth=2).scale(0.8).next_to(dot_A, LEFT * 0.2 + DOWN * 0.2)
        tex_G = TexMobject('G', color=tex_color, plot_depth=2).scale(0.8).next_to(dot_G, LEFT * 0.2 + DOWN * 0.2)
        tex_M = TexMobject('M', color=tex_color, plot_depth=2).scale(0.8).move_to(dot_M).shift(0.36 * (np.cos(self.theta * 2) * LEFT + np.sin(self.theta * 2) * UP))
        tex_H = TexMobject('H', color=tex_color, plot_depth=2).scale(0.8).move_to(dot_H).shift(0.4 * LEFT)
        tex_R = TexMobject('R', color=tex_color, plot_depth=2).scale(0.8).move_to(dot_R).shift(0.4 * DOWN)

        color_dict = {'a': color_a, 'b': color_b, '2': BLUE_B}
        formula_GM = TexMobject('\\mathbf{\\sqrt{', 'a', 'b}', '.}', color=bold_color[1], plot_depth=2).scale(0.9)
        formula_AM = TexMobject('\\mathbf{{a', '+', 'b}', '\\over', '2}}', color=bold_color[2], plot_depth=2).scale(0.9)
        text_AM = TexMobject('\\mathbf{AM', '=', '{{a', '+', 'b}', '\\over', '2}}', color=WHITE).set_color_by_tex_to_color_map(color_dict)
        text_GM = TexMobject('\\mathbf{GM', '=', '\\sqrt{', 'a', 'b}', '.}', color=WHITE)#.set_color_by_tex_to_color_map(color_dict)
        text_HM = TexMobject('\\mathbf{HM', '=', '{{2', 'a', 'b}', '\\over', '{a', '+', 'b}}}', color=WHITE).set_color_by_tex_to_color_map(color_dict)
        text_RM = TexMobject('\\mathbf{RM', '=', '\\sqrt{{', 'a', '^2', '+', 'b', '^2}', '\\over', '{2}', '.}', color=WHITE)#.set_color_by_tex_to_color_map(color_dict)

        text_HM[0].set_color(bold_color[0]), text_GM[0].set_color(bold_color[1]), text_AM[0].set_color(bold_color[2]), text_RM[0].set_color(bold_color[3])
        text_GM[4].set_color(color_dict['a']), text_GM[5].set_color(color_dict['b'])
        text_RM[3].set_color(color_dict['a']), text_RM[6].set_color(color_dict['b'])
        text_RM[4].set_color(color_dict['a']), text_RM[8].set_color(color_dict['b']), text_RM[10].set_color(color_dict['2'])

        inequality_GM_AM = TexMobject('\\mathbf{GM', '\\leqslant', 'AM}', color=WHITE)
        inequality_GM_AM[0].set_color(bold_color[1]), inequality_GM_AM[2].set_color(bold_color[2])
        inequality_ab = TexMobject('\\mathbf{\\sqrt{', 'a', 'b}', '\\leqslant', '{{a', '+', 'b}', '\\over', '2}', '.}', color=WHITE)
        inequality_ab[2].set_color(color_dict['a']), inequality_ab[5].set_color(color_dict['a'])
        inequality_ab[3].set_color(color_dict['b']), inequality_ab[7].set_color(color_dict['b'])
        # text_HM.shift(RIGHT * 3).to_edge(UP * 1.2)
        # text_GM.next_to(text_HM, DOWN * 0.8).align_to(text_HM, LEFT)
        # text_AM.next_to(text_GM, DOWN * 0.8).align_to(text_HM, LEFT)
        # text_RM.next_to(text_AM, DOWN * 0.8).align_to(text_HM, LEFT)

        text_GM.shift(RIGHT * 3.25).to_edge(UP * 1.8)
        text_AM.next_to(text_GM, DOWN * 1.8).align_to(text_GM, LEFT)
        formula_AM.move_to(AM_bold).shift(RIGHT * 0.75)
        formula_GM.move_to(GM_bold).shift(LEFT * 0.5)
        inequality_GM_AM.next_to(text_AM, DOWN * 1.8).align_to(text_GM, LEFT)
        inequality_ab.next_to(inequality_GM_AM, DOWN * 1.8).align_to(text_GM, LEFT)

        # uodate text
        tex_G.add_updater(lambda t: t.next_to(dot_G, LEFT * 0.2 + DOWN * 0.2))
        tex_M.add_updater(lambda t: t.move_to(dot_M).shift(0.36 * (np.cos(self.theta * 2) * LEFT + np.sin(self.theta * 2) * UP)))
        tex_H.add_updater(lambda t: t.move_to(dot_H).shift(0.4 * LEFT))
        tex_R.add_updater(lambda t: t.move_to(dot_R).shift(0.4 * DOWN))
        a.add_updater(lambda a: a.next_to(brace_GB, DOWN * 0.5))
        b.add_updater(lambda b: b.next_to(brace_GC, DOWN * 0.4))
        # formula_AM.add_updater(lambda f: f.move_to(AM_bold).shift(RIGHT * 0.25))
        # formula_GM.add_updater(lambda f: f.move_to(GM_bold).shift(LEFT * 0.25))

        # title
        # text_01 = Text('这是一个著名的几何平均与算术平均不等关系的证明')

        # animation
        self.play(ShowCreation(circle), FadeIn(dot_A), Write(tex_A))
        self.wait(0.5)
        self.play(ShowCreation(BC), ShowCreation(dot_B), ShowCreation(dot_C))
        self.play(ShowCreation(BM), ShowCreation(CM), ShowCreation(AM))
        self.play(FadeIn(dot_M), Write(tex_M))
        self.play(ShowCreation(GM))
        self.play(FadeIn(dot_G), Write(tex_G), FadeIn(angle_G))
        self.wait()
        self.play(ShowCreation(GB), ShowCreation(GC))
        self.wait(0.4)
        self.play(ShowCreation(brace_GB), ShowCreation(brace_GC), Write(a), Write(b))
        self.wait()

        self.play(ReplacementTransform(GM, GM_bold), ReplacementTransform(AM, AM_bold))
        self.play(Write(formula_GM))
        self.play(Write(formula_AM))

        # test
        # self.add(dot_H, dot_R, HM_bold, RM_bold, tex_H, tex_R, GH, AR, dash_circle, angle_A, angle_H) # only used this line in test
        # self.add(text_HM, text_GM, text_AM, text_RM) # only used this line in test

        self.wait()
        self.play(TransformFromCopy(GM_bold, text_GM[0]))
        self.play(Write(text_GM[1]))
        self.play(ReplacementTransform(formula_GM, text_GM[2:]))
        self.wait(0.5)
        self.play(TransformFromCopy(AM_bold, text_AM[0]))
        self.play(Write(text_AM[1]))
        self.play(ReplacementTransform(formula_AM, text_AM[2:]))

        # update theta
        delta_t = 1/60
        run_time = 2.
        step_num = int(run_time/delta_t)
        delta_theta = (PI/18 - PI/6)/int(run_time/delta_t)
        for i in range(step_num):
            self.theta += delta_theta
            self.wait(delta_t)
        self.wait(0.25)

        run_time = 6.
        step_num = int(run_time/delta_t)
        delta_theta = (PI/3 - PI/18)/int(run_time/delta_t)
        for i in range(step_num):
            self.theta += delta_theta
            self.wait(delta_t)

        self.wait()
        self.play(TransformFromCopy(GM_bold, inequality_GM_AM[0]))
        self.play(TransformFromCopy(AM_bold, inequality_GM_AM[2]))
        self.wait(0.15)
        self.play(Write(inequality_GM_AM[1]))
        self.wait()
        self.play(TransformFromCopy(inequality_GM_AM, inequality_ab), run_time=2)
        self.wait(0.5)
        self.play(ShowCreationThenFadeAround(SurroundingRectangle(inequality_ab, color=GREEN)), run_time=1.5)

        self.wait(4)

class HM_GM_AM_RM(Scene):

    def construct(self):

        # dot position
        A = LEFT * 3 # + DOWN * 0.25
        r = 3.25
        B = r * LEFT + A
        C = r * RIGHT + A
        self.theta = PI/6 # init theta
        get_M = lambda theta: r * np.cos(theta * 2) * LEFT + r * np.sin(theta * 2) * UP + A
        get_G = lambda theta: r * np.cos(theta * 2) * LEFT + A
        get_H = lambda theta: r * np.cos(theta * 2) ** 2 * (np.cos(theta * 2) * LEFT + np.sin(theta * 2) * UP) + A
        get_R = lambda theta: r * np.cos(theta * 2) * (np.sin(theta * 2) * LEFT + np.cos(theta * 2) * DOWN) + A
        M = get_M(self.theta)
        G = get_G(self.theta)
        H = get_H(self.theta)
        R = get_R(self.theta)

        # dot, circle, line & angle ...
        circle = Circle(radius=r, color=BLUE).move_to(A)
        arc_config={'color': GRAY, 'stroke_width': 1.5}
        dash_circle = Dashed_Circle(radius=r * np.cos(self.theta * 2), center=A, arc_config=arc_config, arc_ratio=0.64, plot_depth=-0.5)
        line_color = WHITE
        BC = Line(B, C, color=line_color)
        BM = Line(B, M, color=line_color)
        CM = Line(C, M, color=line_color)
        GM = Line(G, M, color=line_color)
        AM = Line(A, M, color=line_color)
        HM = Line(H, M, color=line_color)
        RM = Line(R, M, color=line_color)
        GH = Line(G, H, color=line_color, plot_depth=0.5)
        AR = Line(A, R, color=line_color)

        angle_G = Right_angle(corner=G, plot_depth=0.5)
        angle_A = Right_angle(corner=A, angle=PI/2 - self.theta * 2, on_the_right=False, plot_depth=0.5)
        angle_H = Right_angle(corner=H, angle=PI/2 - self.theta * 2, on_the_right=False, plot_depth=0.5)

        bold_stroke = 10
        bold_color = color_gradient([RED, PINK, BLUE], 4)
        GM_bold = Line(G, M, color=bold_color[1], stroke_width=bold_stroke, plot_depth=0.6)
        AM_bold = Line(A, M, color=bold_color[2], stroke_width=bold_stroke, plot_depth=0.6)
        HM_bold = Line(H, M, color=bold_color[0], stroke_width=bold_stroke, plot_depth=0.6)
        RM_bold = Line(R, M, color=bold_color[3], stroke_width=bold_stroke, plot_depth=0.6)

        color_a = GREEN
        color_b = YELLOW
        GB = Line(A, B, color=color_a, stroke_width=8)
        GC = Line(A, C, color=color_b, stroke_width=8)

        dot_color = PINK
        dot_scale = 1.4
        dot_A = Dot(A, color=RED, plot_depth=1).scale(dot_scale)
        dot_G = Dot(G, color=dot_color, plot_depth=1).scale(dot_scale)
        dot_M = Dot(M, color=dot_color, plot_depth=1).scale(dot_scale)
        dot_H = Dot(H, color=dot_color, plot_depth=1).scale(dot_scale)
        dot_R = Dot(R, color=dot_color, plot_depth=1).scale(dot_scale)
        dot_B = Dot(B, color=GREEN, plot_depth=1)
        dot_C = Dot(C, color=YELLOW, plot_depth=1)

        brace_GB = Brace(GB, DOWN, color=color_a)
        brace_GC = Brace(GC, DOWN, color=color_b)

        # update obj
        dot_G.add_updater(lambda d: d.become(Dot(get_G(self.theta), color=dot_color, plot_depth=1).scale(dot_scale)))
        dot_M.add_updater(lambda d: d.become(Dot(get_M(self.theta), color=dot_color, plot_depth=1).scale(dot_scale)))
        dot_H.add_updater(lambda d: d.become(Dot(get_H(self.theta), color=dot_color, plot_depth=1).scale(dot_scale)))
        dot_R.add_updater(lambda d: d.become(Dot(get_R(self.theta), color=dot_color, plot_depth=1).scale(dot_scale)))

        BM.add_updater(lambda l: l.become(Line(B, get_M(self.theta), color=line_color)))
        CM.add_updater(lambda l: l.become(Line(C, get_M(self.theta), color=line_color)))
        AR.add_updater(lambda l: l.become(Line(A, get_R(self.theta), color=line_color)))
        GH.add_updater(lambda l: l.become(Line(get_G(self.theta), get_H(self.theta), color=line_color, plot_depth=0.5)))
        GB.add_updater(lambda l: l.become(Line(get_G(self.theta), B, color=color_a, stroke_width=8)))
        GC.add_updater(lambda l: l.become(Line(get_G(self.theta), C, color=color_b, stroke_width=8)))

        AM_bold.add_updater(lambda l: l.become(Line(A, get_M(self.theta), color=bold_color[2], stroke_width=bold_stroke, plot_depth=0.6)))
        GM_bold.add_updater(lambda l: l.become(Line(get_G(self.theta), get_M(self.theta), color=bold_color[1], stroke_width=bold_stroke, plot_depth=0.6)))
        HM_bold.add_updater(lambda l: l.become(Line(get_H(self.theta), get_M(self.theta), color=bold_color[0], stroke_width=bold_stroke, plot_depth=0.6)))
        RM_bold.add_updater(lambda l: l.become(Line(get_R(self.theta), get_M(self.theta), color=bold_color[3], stroke_width=bold_stroke, plot_depth=0.6)))

        dash_circle.add_updater(lambda c: c.become(Dashed_Circle(radius=r * np.cos(self.theta * 2), center=A, arc_config=arc_config, arc_ratio=-0.5)))
        angle_G.add_updater(lambda a: a.move_corner_to(get_G(self.theta)))
        angle_A.add_updater(lambda a: a.become(Right_angle(corner=A, angle=PI/2 - self.theta * 2, on_the_right=False or (self.theta>PI/4), plot_depth=0.5)))
        angle_H.add_updater(lambda a: a.become(Right_angle(corner=get_H(self.theta), angle=PI/2 - self.theta * 2, on_the_right=False or (self.theta>PI/4), plot_depth=0.5)))
        a = TexMobject('a', color=color_a).scale(0.9)
        b = TexMobject('b', color=color_b).scale(0.9)
        brace_GB.add_updater(lambda b: b.become(Brace(GB, DOWN, color=color_a).scale(np.array([1,1.8,1])).shift(DOWN*0.3).put_at_tip(TexMobject('.'))))
        brace_GC.add_updater(lambda b: b.become(Brace(GC, DOWN, color=color_b).scale(np.array([1,1.8,1])).shift(DOWN*0.3).put_at_tip(TexMobject('.'))))

        # text
        tex_color = PINK
        tex_A = TexMobject('A', color=tex_color, plot_depth=2).scale(0.8).next_to(dot_A, LEFT * 0.2 + DOWN * 0.2)
        tex_G = TexMobject('G', color=tex_color, plot_depth=2).scale(0.8).next_to(dot_G, LEFT * 0.2 + DOWN * 0.2)
        tex_M = TexMobject('M', color=tex_color, plot_depth=2).scale(0.8).move_to(dot_M).shift(0.36 * (np.cos(self.theta * 2) * LEFT + np.sin(self.theta * 2) * UP))
        tex_H = TexMobject('H', color=tex_color, plot_depth=2).scale(0.8).move_to(dot_H).shift(0.4 * LEFT)
        tex_R = TexMobject('R', color=tex_color, plot_depth=2).scale(0.8).move_to(dot_R).shift(0.4 * DOWN)

        color_dict = {'a': color_a, 'b': color_b, '2': BLUE_B}
        formula_GM = TexMobject('\\mathbf{\\sqrt{', 'a', 'b}', '.}', color=bold_color[1], plot_depth=2).scale(0.9)
        formula_AM = TexMobject('\\mathbf{{a', '+', 'b}', '\\over', '2}}', color=bold_color[2], plot_depth=2).scale(0.9)
        text_AM = TexMobject('\\mathbf{AM', '=', '{{a', '+', 'b}', '\\over', '2}}', color=WHITE).set_color_by_tex_to_color_map(color_dict)
        text_GM = TexMobject('\\mathbf{GM', '=', '\\sqrt{', 'a', 'b}', '.}', color=WHITE)#.set_color_by_tex_to_color_map(color_dict)
        text_HM = TexMobject('\\mathbf{HM', '=', '{{2', 'a', 'b}', '\\over', '{a', '+', 'b}}}', color=WHITE).set_color_by_tex_to_color_map(color_dict)
        text_RM = TexMobject('\\mathbf{RM', '=', '\\sqrt{{', 'a', '^2', '+', 'b', '^2}', '\\over', '{2}', '.}', color=WHITE)#.set_color_by_tex_to_color_map(color_dict)

        text_HM[0].set_color(bold_color[0]), text_GM[0].set_color(bold_color[1]), text_AM[0].set_color(bold_color[2]), text_RM[0].set_color(bold_color[3])
        text_GM[4].set_color(color_dict['a']), text_GM[5].set_color(color_dict['b'])
        text_RM[4].set_color(color_dict['a']), text_RM[7].set_color(color_dict['b']), text_RM[10].set_color(color_dict['2'])

        inequality_GM_AM = TexMobject('\\mathbf{GM', '\\leqslant', 'AM}', color=WHITE)
        inequality_GM_AM[0].set_color(bold_color[1]), inequality_GM_AM[2].set_color(bold_color[2])
        inequality_ab = TexMobject('\\mathbf{\\sqrt{', 'a', 'b}', '\\leqslant', '{{a', '+', 'b}', '\\over', '2}', '.}', color=WHITE)
        inequality_ab[2].set_color(color_dict['a']), inequality_ab[5].set_color(color_dict['a'])
        inequality_ab[3].set_color(color_dict['b']), inequality_ab[7].set_color(color_dict['b'])

        inequality_HGAR_01 = TexMobject('\\mathbf{HM', '\\leqslant', 'GM', '\\leqslant', 'AM', '\\leqslant', 'RM').scale(1.05)
        inequality_HGAR_02 = TexMobject('\\mathbf{{2', '\\over', '{1', '\\over', 'a}', '+', '{1', '\\over', 'b}}', '\\leqslant', #9
                                '\\sqrt{', 'a', 'b}', '\\leqslant', '{a', '+', 'b', '\\over', '2}', '\\leqslant', # 20
                                '\\sqrt{', 'a', '^2', '+', 'b', '^2', '\\over', '2}', 'nb}',
                                        color=WHITE).set_width(inequality_HGAR_01.get_width())
        inequality_HGAR_01[0].set_color(bold_color[0]), inequality_HGAR_01[2].set_color(bold_color[1])
        inequality_HGAR_01[4].set_color(bold_color[2]), inequality_HGAR_01[6].set_color(bold_color[3])
        list_a = [4, 12, 15, 23]
        list_b = [8, 13, 17, 26]
        list_2 = [0, 19, -1, 0]
        for ia, ib, i2 in zip(list_a, list_b, list_2):
            inequality_HGAR_02[ia].set_color(color_dict['a'])
            inequality_HGAR_02[ib].set_color(color_dict['b'])
            inequality_HGAR_02[i2].set_color(color_dict['2'])

        text_HM.shift(RIGHT * 3).to_edge(UP * 1.2)
        # text_GM.next_to(text_HM, DOWN * 0.8).align_to(text_HM, LEFT)
        # text_AM.next_to(text_GM, DOWN * 0.8).align_to(text_HM, LEFT)
        text_RM.next_to(text_AM, DOWN * 0.8).align_to(text_HM, LEFT)
        text_GM.to_edge(UP * 1.8).align_to(text_HM, LEFT)
        text_AM.next_to(text_GM, DOWN * 1.8).align_to(text_HM, LEFT)

        formula_AM.move_to(AM_bold).shift(RIGHT * 0.75)
        formula_GM.move_to(GM_bold).shift(LEFT * 0.5)
        inequality_GM_AM.next_to(text_AM, DOWN * 1.8).align_to(text_GM, LEFT)
        inequality_ab.next_to(inequality_GM_AM, DOWN * 1.8).align_to(text_GM, LEFT)
        inequality_HGAR_01.next_to(text_RM, DOWN * 1.8).align_to(text_HM, LEFT).shift(LEFT * 1.2)
        inequality_HGAR_02.next_to(text_RM, DOWN * 1.6).align_to(text_HM, LEFT).shift(LEFT * 1.2)

        # uodate text
        tex_G.add_updater(lambda t: t.next_to(dot_G, LEFT * 0.2 + DOWN * 0.2))
        tex_M.add_updater(lambda t: t.move_to(dot_M).shift(0.36 * (np.cos(self.theta * 2) * LEFT + np.sin(self.theta * 2) * UP)))
        tex_H.add_updater(lambda t: t.move_to(dot_H).shift(0.4 * LEFT))
        tex_R.add_updater(lambda t: t.move_to(dot_R).shift(0.4 * DOWN))
        a.add_updater(lambda a: a.next_to(brace_GB, DOWN * 0.5))
        b.add_updater(lambda b: b.next_to(brace_GC, DOWN * 0.4))
        # formula_AM.add_updater(lambda f: f.move_to(AM_bold).shift(RIGHT * 0.25))
        # formula_GM.add_updater(lambda f: f.move_to(GM_bold).shift(LEFT * 0.25))

        # title
        # text_01 = Text('这是一个著名的几何平均与算术平均不等关系的证明')

        # animation
        self.theta = PI/3
        self.add(dot_A, dot_B, dot_C, dot_M, dot_G, circle, GB, GC, BM, CM, AM_bold, GM_bold, brace_GC, brace_GB, angle_G,
                 tex_A, tex_G, tex_M, a, b, text_GM, text_AM, inequality_GM_AM, inequality_ab)
        self.wait(2)
        self.play(FadeOut(inequality_GM_AM), FadeOut(inequality_ab), run_time=1.6)
        self.wait(0.5)
        self.play(ShowCreation(GH))
        self.play(FadeIn(dot_H), Write(tex_H), run_time=1)
        self.play(FadeIn(angle_H), run_time=0.9)
        self.wait(0.5)
        self.play(ShowCreation(HM_bold), run_time=1.5)
        self.play(text_GM.shift, (text_GM.get_height() + 0.8) * DOWN,
                  text_AM.shift, (text_GM.get_height() + 0.8) * DOWN, run_time=1.5)
        self.play(TransformFromCopy(HM_bold, text_HM[0]), run_time=1.5)
        self.wait(0.25)
        self.play(Write(text_HM[1:]), run_time=1.5)
        self.wait(1.5)

        # AG = Line(A, get_G(self.theta), color=WHITE)
        # circle_ag = Circle(radius=AG.get_length(), color=WHITE, plot_depth=2.5).move_to(A)
        # dash_circle.rotate(PI)
        # self.play(Rotate(AG, about_point=A), FadeIn(circle_ag), run_time=1.2)
        # self.play(ReplacementTransform(circle_ag, dash_circle), FadeOut(AG))
        self.play(FadeIn(dash_circle), run_time=1.25)
        self.wait(0.25)
        self.play(ShowCreation(AR))
        self.play(Write(tex_R), FadeInFromLarge(dot_R), run_time=1)
        self.play(FadeIn(angle_A), run_time=0.8)
        self.wait(0.5)
        self.play(ShowCreation(RM_bold), run_time=1.2)
        self.wait()

        self.play(TransformFromCopy(RM_bold, text_RM[0]))
        self.wait(0.2)
        self.play(Write(text_RM[1:]), run_time=2)
        self.wait()

        run_time = 4.
        delta_t = 1/60
        step_num = int(run_time/delta_t)
        delta_theta = (PI/18 - PI/3)/int(run_time/delta_t)
        for i in range(step_num):
            self.theta += delta_theta
            self.wait(delta_t)
        self.wait(0.2)
        run_time = 6.
        step_num = int(run_time/delta_t)
        delta_theta = (PI/3 + PI/36 - PI/18)/int(run_time/delta_t)
        for i in range(step_num):
            self.theta += delta_theta
            self.wait(delta_t)

        self.wait(1.25)

        self.play(TransformFromCopy(HM_bold, inequality_HGAR_01[0]))
        self.wait(0.2)
        self.play(TransformFromCopy(GM_bold, inequality_HGAR_01[2]))
        self.wait(0.2)
        self.play(TransformFromCopy(AM_bold, inequality_HGAR_01[4]))
        self.wait(0.2)
        self.play(TransformFromCopy(RM_bold, inequality_HGAR_01[6]))
        self.wait(0.5)
        self.play(Write(inequality_HGAR_01[1:-1:2]), run_time=1.8)
        self.wait(2)
        self.play(ReplacementTransform(inequality_HGAR_01, inequality_HGAR_02), run_time=1.5)
        self.wait(0.5)
        self.play(ShowCreationThenFadeAround(SurroundingRectangle(inequality_HGAR_02)), run_time=1.5)
        self.wait(4)

class Three_num(Scene):

    CONFIG = {
        'default_font': '思源黑体 bold'
    }

    def construct(self):

        color_a = RED
        color_b = PINK
        color_c = YELLOW

        color_dict = {'a': color_a, 'b': color_b, 'c': color_c, '3': BLUE_B}

        path = 'my_projects\\resource\\svg_files\\'
        svg_a = SVGMobject(path + 'good.svg', color=color_dict['a'])
        svg_b = SVGMobject(path + 'coin.svg', color=color_dict['b'])
        svg_c = SVGMobject(path + 'favo.svg', color=color_dict['c'])

        inequality = TexMobject('\\mathbf{{3', '\\over', '{1', '\\over', 'a}', '+', '{1', '\\over', 'b}', '+', '{1', '\\over', 'c}}', '\\leqslant', #13
                                '\\sqrt{', 'a', 'b', 'c}', '\\leqslant', '{a', '+', 'b', '+', 'c', '\\over', '3}', '\\leqslant', # 27
                                '\\sqrt{', 'a', '^2', '+', 'b', '^2', '+', 'c', '^2', '\\over', '3}', 'nb}', color=WHITE)
        inequality_replaced = inequality.deepcopy() #.shift(DOWN * 3)

        list_a = [4, 16, 20, 30]
        list_b = [8, 17, 22, 33]
        list_c = [12, 18, 24, 36]
        for i in list_a:
            svg_i = svg_a.copy().set_width(inequality[i].get_width()).move_to(inequality_replaced[i])#.align_to(inequality_replaced[i], DOWN)
            inequality_replaced[i].become(svg_i)
        for i in list_b:
            svg_i = svg_b.copy().set_width(inequality[i].get_width()).move_to(inequality_replaced[i]).align_to(inequality_replaced[i], DOWN)
            inequality_replaced[i].become(svg_i)
        for i in list_c:
            svg_i = svg_c.copy().set_width(inequality[i].get_width()).scale(1.15).move_to(inequality_replaced[i])#.align_to(inequality_replaced[i], DOWN)
            inequality_replaced[i].become(svg_i)

        inequality_replaced.scale(1.08).to_corner(LEFT * 1.4)

        t2c_dict = {'均值不等式': ORANGE, 'n个变量': BLUE, '三元形式': BLUE}
        title = Text('均值不等式还可推广到n个变量的情况', font=self.default_font).set_height(0.56)
        title.set_color_by_t2c(t2c_dict)
        title_02 = Text('均值不等式的三元形式如下：', font=self.default_font).set_height(0.56)
        title_02.set_color_by_t2c(t2c_dict)
        title.to_corner(LEFT * 1.5 + UP * 1.6)
        title_02.to_corner(LEFT * 1.5 + UP * 4)

        text_down = Text('取等条件：', font=self.default_font).set_height(0.56)
        text_down.to_corner(LEFT * 1.5 + DOWN * 3.6)
        equation_down = TexMobject('a\\,', '=', '\\,a\\,', '=', '\\,a').set_height(0.4).next_to(text_down, RIGHT * 2)
        equation_down[0].become(svg_a.copy().set_height(0.64).move_to(equation_down[0]))
        equation_down[2].become(svg_b.copy().set_height(0.64).move_to(equation_down[2]))
        equation_down[4].become(svg_c.copy().set_height(0.64).move_to(equation_down[4]))

        # self.play(ShowCreation(inequality))
        self.play(Write(title), run_time=2.5)
        self.wait()
        self.play(Write(title_02), run_time=2.)
        self.wait()
        self.play(ShowCreation(inequality_replaced), run_time=3)
        self.wait()
        self.play(Write(text_down))
        self.play(ShowCreation(equation_down))
        self.wait(5)

class Intro_inequality(Scene):

    CONFIG = {
        'default_font': '思源黑体 bold'
    }

    def construct(self):

        t2c_dict = {'均值不等式': ORANGE, '二元形式': BLUE, 'a': GREEN, 'b': YELLOW}
        text_01 = Text('我们在中学都接触过均值不等式', font=self.default_font).set_height(0.6)
        text_02 = Text('其二元形式如下所示（a、b均为正数）：', font=self.default_font).set_height(0.6)
        text_01.set_color_by_t2c(t2c_dict)
        text_02.set_color_by_t2c(t2c_dict)

        color_dict = {'a': GREEN, 'b': YELLOW, '2': BLUE_B}
        inequality_HGAR_01 = TexMobject('\\mathbf{{2', '\\over', '{1', '\\over', 'a}', '+', '{1', '\\over', 'b}}', '\\leqslant', #9
                                '\\sqrt{', 'a', 'b}', '\\leqslant', '{a', '+', 'b', '\\over', '2}', '\\leqslant', # 20
                                '\\sqrt{', 'a', '^2', '+', 'b', '^2', '\\over', '2}', 'nb}',
                                        color=WHITE).scale(1.25)
        inequality_HGAR_01.align_to(text_01, LEFT)
        list_a = [4, 12, 15, 23]
        list_b = [8, 13, 17, 26]
        list_2 = [0, 19, -1, 0]
        for ia, ib, i2 in zip(list_a, list_b, list_2):
            inequality_HGAR_01[ia].set_color(color_dict['a'])
            inequality_HGAR_01[ib].set_color(color_dict['b'])
            inequality_HGAR_01[i2].set_color(color_dict['2'])

        colors = color_gradient([RED, PINK, BLUE], 4)
        t2c_02 = {'调和平均数': colors[0], '几何平均数': colors[1], '算术平均数': colors[2], '平方平均数': colors[3]}
        text_03 = Text('调和平均数≤几何平均数≤算术平均数≤平方平均数', font=self.default_font).set_height(0.5)
        text_04 = Text('当且仅当a=b时取等号', font=self.default_font).set_height(0.6)
        text_03.set_color_by_t2c(t2c_02)
        text_04.set_color_by_t2c(t2c_dict)


        text_01.to_corner(LEFT * 1.5 + UP * 1.6)
        text_02.to_corner(LEFT * 1.5 + UP * 4)

        inequality_HGAR_01.to_corner(LEFT * 2.5)

        text_03.next_to(inequality_HGAR_01, DOWN * 1.8).align_to(inequality_HGAR_01, LEFT)
        text_04.next_to(text_03, DOWN * 2.4).align_to(text_01, LEFT)

        self.play(Write(text_01), run_time=2.25)
        self.wait(0.5)
        self.play(Write(text_02), run_time=2)
        self.wait(0.5)
        self.play(Write(inequality_HGAR_01), run_time=2.75)
        self.wait()
        self.play(TransformFromCopy(inequality_HGAR_01, text_03), run_time=1.75)
        self.wait()
        self.play(Write(text_04), run_time=2)

        self.wait(5)

class Ending(Scene):

    CONFIG = {
        'default_font': '庞门正道标题体'
    }

    def construct(self):

        colors = color_gradient([RED, PINK, BLUE], 4)
        text_01 = Text('感 谢 观 看', font=self.default_font).set_height(1.)
        text_01.set_color_by_t2c({'感': colors[0], '谢': colors[1], '观': colors[2], '看': colors[3]})
        text_01.shift(UP * 0.5)
        # t2c = {'python 3.7.3': colors[0], 'cigar666': }
        text_02 = Text('作 者：cigar666', color=colors[3], font=self.default_font).scale(0.5)
        text_03 = Text('程序编写：python 3.7.3', color=colors[2], font=self.default_font).scale(0.5)
        text_04 = Text('动画引擎：manim', color=colors[1], font=self.default_font).scale(0.5)
        text_05 = Text('后期剪辑：Premiere', color=colors[0], font=self.default_font).scale(0.5)
        text_02.next_to(text_01, DOWN * 1.8).to_corner(LEFT * 4.)
        text_03.next_to(text_01, DOWN * 1.8).to_corner(LEFT * 15)
        text_04.next_to(text_02, DOWN * 3).to_corner(LEFT * 4.)
        text_05.next_to(text_02, DOWN * 3).to_corner(LEFT * 15)


        self.play(Write(text_01), run_time=2.5)
        self.wait()
        self.play(text_01.shift, UP*0.8)
        self.wait(0.6)
        self.play(Write(text_02), run_time=1.6)
        self.wait(0.4)
        self.play(Write(text_03), run_time=1.6)
        self.wait(0.4)
        self.play(Write(text_04), run_time=1.6)
        self.wait(0.4)
        self.play(Write(text_05), run_time=1.6)

        self.wait(5)

###########################
from my_manim_projects.my_utils.my_text import *

class Intro_RM_AM(Text4animScene):

    def construct(self):

        font = 'Comic Sans MS'

        t0 = Text('如何用几何方法证明:', font='思源黑体 Bold').set_color_by_t2c({'几何方法': YELLOW}).set_height(0.78)
        t1 = Text('n个数的平方平均大于等于算术平均', font='思源黑体 Bold').set_color_by_t2c({'n': PINK, '平方平均': BLUE, '算术平均': GREEN}).set_height(0.78)
        t1.next_to(t0, DOWN * 1.8, aligned_edge=LEFT)
        text = VGroup(t0, t1)

        t2mt = {'X': 'X', '{X': 'X', '_1': '1', '_2': '2', '_n': 'n', '^2': '2', '}^2': '2', '\\cdots': '...', '\\over': '_', }

        text_1 = MyText('(', '{X', '_1', '}^2', '+', '{X', '_2', '}^2', '+', '\\cdots', '+', '{X', '_n', '}^2', ')', '\\over', 'n', default_font=font).get_new_font_texs(t2mt).set_height(1)
        text_1[-2].set_width(text_1.get_width() * 1.02).scale([1, 0.07, 1])
        t = Text('≥', font=font).scale(0.6)
        text_2 = MyText('X', '_1', '+', 'X', '_2', '+', '\\cdots', '+', 'X', '_n', '\\over', 'n', default_font=font).get_new_font_texs(t2mt).set_height(1)
        text_2[-2].set_width(text_2.get_width() * 1.02).scale([1, 0.07, 1])
        text_1.to_corner(LEFT * 1, buff=1), t.next_to(text_1), text_2.next_to(t), text_2.align_to(text_1, DOWN)
        text_1[-1].scale(1.25).shift(UP * 0.05).set_color(PINK), text_2[-1].scale(1.25).shift(UP * 0.05).set_color(PINK)
        text_1.set_height(0.95)

        text_1[1:4].set_color(RED), text_1[5:8].set_color(YELLOW), text_1[9].set_color(GREEN), text_1[11:14].set_color(BLUE)
        text_2[0:2].set_color(RED), text_2[3:5].set_color(YELLOW), text_2[6].set_color(GREEN), text_2[8:10].set_color(BLUE)

        p1, p2, p3 = LEFT * 6.25 + DOWN * 0.51, LEFT * 6.08 + UP * 0.54, LEFT * (5.95 - text_1.get_width()) + UP * 0.54
        sqrt = VGroup(Line(p1, p2),Line(p2, p3), Dot(p1).set_height(0.035), Dot(p2).set_height(0.035), Dot(p3).set_height(0.035))
        ineq = VGroup(VGroup(sqrt, text_1), t, text_2).set_width(12.8).move_to(DOWN * 0.64)
        text.next_to(ineq, UP * 2.5)

        self.ShiftInOneByOne_new(t0, run_speed=0.3, wait_time=0)
        self.ShiftInOneByOne_new(t1, run_speed=0.25,  wait_time=0.4)

        self.play(Write(ineq), run_time=2.8)
        self.wait(4)



class Proof_RM_AM(Text4animScene):

    def construct(self):

        x1, x2, x3, x4 = 1., 1.25, 1.6, 2.

        s1 = Square(fill_color=RED, fill_opacity=0.8).set_height(x1)
        s2 = Square(fill_color=YELLOW, fill_opacity=0.8).set_height(x2)
        s3 = Square(fill_color=GREEN, fill_opacity=0.8).set_height(x3)
        s4 = Square(fill_color=BLUE, fill_opacity=0.8).set_height(x4)
        line_1 = VGroup(s1, s2, s3, s4).arrange(RIGHT, buff=0, aligned_edge=UP).to_edge(UP * 1.25)
        line_2, line_3, line_4 = line_1.copy(), line_1.copy(), line_1.copy()
        s0 = Square(fill_color=LIGHT_GREY, fill_opacity=0.0, stroke_width=0).set_height(x1+x2+x3+x4)

        font = 'Comic Sans MS'
        t2mt = {'X': 'X', '{X': 'X',  '_1': '1', '_2': '2', '_n': 'n', '}^2': '2'}
        t_x1 = MyText('X', '_1', default_font=font).get_new_font_texs(t2mt).set_height(0.4)
        t_x2 = MyText('X', '_2', default_font=font).get_new_font_texs(t2mt).set_height(0.4)
        t_x3 = Text('...', font=font)
        t_x4 = MyText('X', '_n', default_font=font).get_new_font_texs(t2mt).set_height(0.4)

        t_s1 = MyText('{X', '_1', '}^2', default_font=font).get_new_font_texs(t2mt).set_height(0.4).move_to(s1)
        t_s2 = MyText('{X', '_2', '}^2', default_font=font).get_new_font_texs(t2mt).set_height(0.4).move_to(s2)
        t_s3 = Text('...', font=font).scale(0.5).move_to(s3)
        t_s4 = MyText('{X', '_n', '}^2', default_font=font).get_new_font_texs(t2mt).set_height(0.4).move_to(s4)

        line_1 = VGroup(VGroup(s1, t_s1), VGroup(s2, t_s2), VGroup(s3, t_s3), VGroup(s4, t_s4)).arrange(RIGHT, buff=0, aligned_edge=UP).to_edge(UP * 1.)
        line_2, line_3, line_4 = line_1.copy(), line_1.copy(), line_1.copy()

        all = VGroup(line_1, line_2, line_3, line_4)
        all_r, all_y, all_g, all_b = VGroup(*[all[i][0] for i in range(4)]), VGroup(*[all[i][1] for i in range(4)]), \
                                     VGroup(*[all[i][2] for i in range(4)]), VGroup(*[all[i][3] for i in range(4)])

        self.wait(0.5)
        self.play(*[ShowCreation(line_1[i][0]) for i in range(4)], run_time=1.2)
        self.wait(0.2)
        self.play(Write(VGroup(t_s1, t_s2, t_s3, t_s4)), run_time=1.8)

        self.wait(0.8)

        self.play(line_2.shift, DOWN * 2.4)
        self.wait(0.2)
        self.play(line_2[0].next_to, line_2[-1], RIGHT, {"aligned_edge": UP, "buff": 0})
        self.wait(0.2)
        self.play(line_2.shift, x1 * LEFT)
        self.wait(0.2)
        self.play(line_2[1].shift, (2.4 - x1) * UP,
                  line_2[2].shift, (2.4 - x2) * UP,
                  line_2[3].shift, (2.4 - x3) * UP,
                  line_2[0].shift, (2.4 - x4) * UP,
                  )
        self.wait(1.)

        self.play(line_3.shift, DOWN * 4.)
        self.wait(0.2)
        self.play(line_3[0].next_to, line_3[-1], RIGHT, {"aligned_edge": UP, "buff": 0})
        self.play(line_3[1].next_to, line_3[0], RIGHT, {"aligned_edge": UP, "buff": 0})
        self.wait(0.2)
        self.play(line_3.shift, (x1 + x2) * LEFT)
        self.wait(0.2)
        self.play(line_3[2].shift, (4. - x1 - x2) * UP,
                  line_3[3].shift, (4. - x2 - x3) * UP,
                  line_3[0].shift, (4. - x3 - x4) * UP,
                  line_3[1].shift, (4. - x4 - x1) * UP,
                  )
        self.wait(1.)

        self.play(line_4.shift, DOWN * 5)
        self.wait(0.2)
        self.play(line_4[-1].next_to, line_4[0], LEFT, {"aligned_edge": UP, "buff": 0})
        self.wait(0.2)
        self.play(line_4.shift, x4 * RIGHT)
        self.wait(0.2)
        self.play(line_4[3].shift, (5 - x1 - x2 - x3) * UP,
                  line_4[0].shift, (5 - x2 - x3 - x4) * UP,
                  line_4[1].shift, (5 - x3 - x4 - x1) * UP,
                  line_4[2].shift, (5 - x4 - x1 - x2) * UP,
                  )
        self.wait(2)
        # self.play(all.scale, 0.8, all.to_edge, UP * 1.)

        brace_d = Brace(all, DOWN, buff=0.1)
        brace_l = Brace(all, LEFT, buff=0.1)
        t2mt_02 = {'{|': '|', '|': '|', '|}': '|', 'X': 'X', '{X': 'X', '_1': '1', '_2': '2', '_n': 'n', '^2': '2', '}^2': '2', '\\cdots': '...', '\\times': '×', }
        sum_1 = MyText('|', 'X', '_1', '|', '+', '|', 'X', '_2', '|', '+', '\\cdots', '+', '|', 'X', '_n', '|', default_font=font).get_new_font_texs(t2mt_02).set_height(0.5)
        sum_1[1:3].set_color(RED), sum_1[6:8].set_color(YELLOW), sum_1[10].set_color(GREEN), sum_1[13:15].set_color(BLUE)

        sum_2 = sum_1.copy().rotate(PI/2)

        sum_1.next_to(brace_d, DOWN, buff=0.1), sum_2.next_to(brace_l, LEFT, buff=0.1)
        self.play(ShowCreation(brace_d), Write(sum_1), ShowCreation(brace_l), Write(sum_2), run_time=2)
        self.wait()

        all_with_text = VGroup(all, brace_l, brace_d, sum_1, sum_2, s0.move_to(all))
        self.play(all_with_text.to_edge, LEFT * 1.2)
        self.wait()

        text_0 = Text('所有小正方形面积和≥大正方形面积', font='思源黑体 Bold').set_color_by_t2c({'所有小正方形面积和': BLUE, '大正方形面积': GREEN})
        text_0.set_height(0.36).to_corner(RIGHT * 1. + UP * 1.5)

        text_1 = MyText('n', '\\times', '(', '{X', '_1', '}^2', '+', '{X', '_2', '}^2', '+', '\\cdots', '+', '{X', '_n', '}^2', ')', default_font=font).get_new_font_texs(t2mt_02)
        text_2 = MyText('(', '|', 'X', '_1', '|', '+', '|', 'X', '_2', '|', '+', '\\cdots', '+', '|', 'X', '_n', '|', ')', '^2', default_font=font).get_new_font_texs(t2mt_02)
        text_3 = MyText('(', 'X', '_1', '+', 'X', '_2', '+', '\\cdots', '+', 'X', '_n', ')', '^2', default_font=font).get_new_font_texs(t2mt_02)
        text_1.set_height(0.45)
        text_1[0].scale(1.25).set_color(PINK), text_1.next_to(text_0, DOWN, aligned_edge=LEFT).shift(RIGHT * 0.5)
        text_2.set_height(0.45).next_to(text_1, DOWN, aligned_edge=LEFT)
        text_3.set_height(0.45).next_to(text_2, DOWN, aligned_edge=LEFT)

        text_1[3:6].set_color(RED), text_1[7:10].set_color(YELLOW), text_1[11].set_color(GREEN), text_1[13:16].set_color(BLUE)
        text_2[2:6].set_color(RED), text_2[7:9].set_color(YELLOW), text_2[11].set_color(GREEN), text_2[14:16].set_color(BLUE)
        text_3[1:3].set_color(RED), text_3[4:6].set_color(YELLOW), text_3[7].set_color(GREEN), text_3[9:11].set_color(BLUE)

        t4a_0 = self.ShiftInOneByOne_new(text_0, wait_time=0.9)
        t1 = Text('≥', font=font).scale(0.35).next_to(text_1, RIGHT)
        t2 = t1.copy().next_to(text_2, RIGHT)
        self.play(TransformFromCopy(text_0[0:10], text_1), run_time=1.4)
        self.wait(0.25)
        self.play(TransformFromCopy(all_r, text_1[3:6]),   run_time=1.)
        self.wait(0.1)
        self.play(TransformFromCopy(all_y, text_1[7:10]),  run_time=1.)
        self.wait(0.1)
        self.play(TransformFromCopy(all_g, text_1[11]),    run_time=1.)
        self.wait(0.1)
        self.play(TransformFromCopy(all_b, text_1[13:16]), run_time=1.)
        self.wait(1)

        self.play(Write(t1), run_time=0.6)
        self.play(TransformFromCopy(text_0[11:], text_2), run_time=1.4)
        self.wait(0.5)
        s0.set_opacity(0.2)
        self.play(ReplacementTransform(s0, text_2.copy()), run_time=1.4)

        self.wait()
        self.play(Write(t2), run_time=0.6)
        self.wait(0.2)
        self.play(Write(text_3), run_time=1.8)
        self.wait(1.2)

        # arrow = Arrow(ORIGIN, DOWN, buff=0, color=YELLOW).next_to(text_3, DOWN * 0.25)
        arrow = TexMobject('\\mathbf{\\Downarrow}').next_to(text_3, DOWN)

        # text = TexMobject(r'{\sum\limits_{i=1}^{n} {X_i}^2 \over n} \ge \left(\sum\limits_{i=1}^{n} X_i \over n\right)^2').scale(1).next_to(arrow, DOWN * 0.25)
        text = TexMobject(r'\mathbf{\sqrt{\sum\limits_{i=1}^{n} {x_i}^2 \over n} \ge {\sum\limits_{i=1}^{n} x_i \over n}}').scale(0.95).next_to(arrow, DOWN)
        sr = SurroundingRectangle(text)

        self.play(ShowCreation(arrow))
        self.wait(0.4)
        self.play(Write(text), run_time=2)
        self.wait(0.2)
        self.play(ShowCreation(sr))
        self.wait(0.6)

        checkmark = TexMobject('\\checkmark', color=GREEN).scale(2).next_to(sr, RIGHT)
        self.play(Write(checkmark), run_time=1.5)

        self.wait(4)


class Proof_RM_AM_from2toN(Scene):

    def construct(self):

        s = VGroup(*[self.create_squares(i, l=6.4) for i in range(1,10)])
        t = VGroup(*[Text('n = %d' % i, font='思源黑体 Bold').set_height(0.6).to_corner(UL * 1.5) for i in range(1,10)])
        self.play(ShowCreation(s[0]), Write(t[0]))
        self.wait(0.9)
        for i in range(8):
            self.play(ReplacementTransform(s[i], s[i+1]), ReplacementTransform(t[i], t[i+1]), run_time=1.8)
            self.wait(1.2)

        self.wait(3)

    def create_squares(self, n=4, l=6):

        x = np.array(2 * [0.6 * 1.2 ** i for i in range(n)])
        colors = color_gradient([RED, YELLOW, GREEN, BLUE], n)
        squares = VGroup()
        for i in range(n):
            line_i = VGroup()
            for j in range(n):
                s_ij = Square(fill_color=colors[int((i+j)%n)], fill_opacity=0.8, stroke_width=1. + 8/n).set_height(x[int((i+j)%n)]).to_corner(UL)
                s_ij.shift(RIGHT * (sum(x[i:i+j])) + DOWN * (sum(x[j:i+j])))
                line_i.add(s_ij)
            squares.add(line_i)

        return squares.move_to(ORIGIN).set_height(l)

