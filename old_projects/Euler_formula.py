from manimlib.imports import *

class EulerFormula_01(Scene):

    CONFIG = {
        'camera_config': {'background_color': WHITE}
    }

    def construct(self):

        formula_01 = TexMobject('\\mathbf{{{a', '^k}', '\\over{(', 'a', '-', 'b', ')', '(', 'a', '-', 'c', ')}} +',
                                '{{b', '^k}', '\\over{(', 'b', '-', 'c', ')', '(', 'b', '-', 'a', ')}}',
                                # '{{c', '^k}', '\\over{(', 'c', '-', 'a', ')', '(', 'c', '-', 'b', ')}}}',
                                color=BLACK, background_stroke_color=BLACK, background_stroke_width=3.6)
        formula_01_2 = TexMobject('\mathbf{+', '{{c', '^k}', '\\over{(', 'c', '-', 'a', ')', '(', 'c', '-', 'b', ')}}}',
                                color=BLACK, background_stroke_color=BLACK, background_stroke_width=3.6)
        formula_01.set_color_by_tex_to_color_map({'k': BLUE_D, 'a': RED_D, 'b': YELLOW_D, 'c': GREEN_D})
        formula_01.scale(1.6).shift(UP * 2.5)

        formula_01_2.set_color_by_tex_to_color_map({'k': BLUE_D, 'a': RED_D, 'b': YELLOW_D, 'c': GREEN_D})
        formula_01_2[0].set_color(BLACK)
        formula_01_2.scale(1.6).next_to(formula_01, DOWN * 3.).align_to(formula_01, LEFT)

        eq_symbol = TexMobject('=', color=BLACK, background_stroke_color=BLACK, background_stroke_width=3.2)\
            .scale(1.4).next_to(formula_01_2, RIGHT * 1.2)

        formula_02_1 = TexMobject('0\\, \\, (', 'k', '=0\\text{或}1)', color=BLACK, background_stroke_color=BLACK,
                                  background_stroke_width=3.2).scale(1.2).next_to(eq_symbol, RIGHT * 2.75).shift(UP * 0.9)
        formula_02_2 = TexMobject('1\\, \\, (', 'k', '=2)', color=BLACK, background_stroke_color=BLACK,
                                  background_stroke_width=3.2).scale(1.2).next_to(eq_symbol, RIGHT * 2.75) # .shift(UP * 0)
        formula_02_3 = TexMobject('a', '+', 'b', '+', 'c\\, \\, (', 'k', '=3)', color=BLACK, background_stroke_color=BLACK,
                                  background_stroke_width=3.2).scale(1.2).next_to(eq_symbol, RIGHT * 2.75).shift(DOWN * 0.9)
        formula_02_1.set_color_by_tex_to_color_map({'k': BLUE_D})
        formula_02_2.set_color_by_tex_to_color_map({'k': BLUE_D})
        formula_02_3.set_color_by_tex_to_color_map({'k': BLUE_D, 'a': RED_D, 'b': YELLOW_D, 'c': GREEN_D})
        formula_02 = VGroup(formula_02_1, formula_02_2, formula_02_3)


        brace = Brace(formula_02, LEFT, color=BLACK)

        self.play(Write(formula_01))
        self.play(Write(formula_01_2))

        self.wait(0.8)

        self.play(Write(eq_symbol), run_time=0.8)
        self.play(ShowCreation(brace), run_time=0.8)
        self.play(Write(formula_02), run_time=2)

        self.wait(10)

class Dot3d(VGroup):

    def __init__(self, loc, size=0.2, color=WHITE, **kwargs):
        VGroup.__init__(self, **kwargs)
        dot_01 = Dot(loc, color=color).set_height(size)
        self.add(dot_01)
        num = 4
        for i in range(1, num):
            dot_i = dot_01.copy().rotate(PI * i/num, axis=UP)
            self.add(dot_i)
        for i in range(1, num):
            dot_i = dot_01.copy().rotate(PI * i/num, axis=RIGHT)
            self.add(dot_i)



class Regular_Dodecahedron(VGroup):

    CONFIG = {
        'size': 3,
        'vertex_size': 0.2,
        'vertex_color': None,
        'edge_color': WHITE,
        'face_color': YELLOW,
        'edge_stroke': 3,
        'face_opacity': 0.25,
    }

    def __init__(self, **kwargs):
        VGroup.__init__(self, **kwargs)
        self.create_vertices()
        self.create_edges()
        self.create_faces()

        # self.add(self.vertices, self.edges, self.faces)
        self.add(self.faces, self.edges, self.vertices)

        self.set_height(self.size)

        # self.vertices.add_updater(self.vertex_direction_updater)

    def create_vertices(self):

        phi = (np.sqrt(5)+1)/2
        orange_points = np.array([[+1, +1, +1],
                                  [+1, -1, +1],
                                  [-1, -1, +1],
                                  [-1, +1, +1],
                                  [+1, +1, -1],
                                  [+1, -1, -1],
                                  [-1, -1, -1],
                                  [-1, +1, -1],
                                  ])

        green_points = np.array([[0, +phi, +1/phi],
                                 [0, -phi, +1/phi],
                                 [0, -phi, -1/phi],
                                 [0, +phi, -1/phi],
                                 ])

        blue_points = np.array([[+1/phi, 0, +phi],
                                [+1/phi, 0, -phi],
                                [-1/phi, 0, -phi],
                                [-1/phi, 0, +phi],
                                ])

        red_points = np.array([[+phi, +1/phi, 0],
                               [+phi, -1/phi, 0],
                               [-phi, -1/phi, 0],
                               [-phi, +1/phi, 0],
                               ])
        self.O_dots, self.G_dots, self.B_dots, self.R_dots = VGroup(), VGroup(), VGroup(), VGroup()

        for i in range(8):
            color=ORANGE
            if not self.vertex_color == None:
                color = self.vertex_color
            # dot_i = Dot(orange_points[i], color=color).set_height(self.vertex_size)
            dot_i = Dot3d(orange_points[i], color=color, size=self.vertex_size)
            self.O_dots.add(dot_i)
        for i in range(4):
            color = GREEN
            if not self.vertex_color == None:
                color = self.vertex_color
            # dot_i = Dot(green_points[i], color=color).set_height(self.vertex_size)
            dot_i = Dot3d(green_points[i], color=color, size=self.vertex_size)
            self.G_dots.add(dot_i)
        for i in range(4):
            color=BLUE
            if not self.vertex_color == None:
                color = self.vertex_color
            # dot_i = Dot(blue_points[i], color=color).set_height(self.vertex_size)
            dot_i = Dot3d(blue_points[i], color=color, size=self.vertex_size)
            self.B_dots.add(dot_i)
        for i in range(4):
            color=RED
            if not self.vertex_color == None:
                color = self.vertex_color
            # dot_i = Dot(red_points[i], color=color).set_height(self.vertex_size)
            dot_i = Dot3d(red_points[i], color=color, size=self.vertex_size)
            self.R_dots.add(dot_i)
        self.vertices = VGroup(self.O_dots, self.G_dots, self.B_dots, self.R_dots)
        # self.vertices.set_height(self.size)

    def create_edges(self):
        def Line_by2dots(d1, d2, stroke_width=self.stroke_width, color=self.edge_color, **kwargs):
            return Line(d1.get_center(), d2.get_center(), color=color, stroke_width=stroke_width, **kwargs)

        self.edges = VGroup()

        # edges from up to down, anti-clockwise order
        O, G, B, R = self.O_dots, self.G_dots, self.B_dots, self.R_dots
        self.edges.add(Line_by2dots(B[0], B[3]))

        self.edges.add(Line_by2dots(B[0], O[0]))
        self.edges.add(Line_by2dots(B[0], O[1]))
        self.edges.add(Line_by2dots(B[3], O[2]))
        self.edges.add(Line_by2dots(B[3], O[3]))

        self.edges.add(Line_by2dots(O[0], G[0]))
        self.edges.add(Line_by2dots(O[1], G[1]))
        self.edges.add(Line_by2dots(O[2], G[1]))
        self.edges.add(Line_by2dots(O[3], G[0]))

        self.edges.add(Line_by2dots(O[0], R[0]))
        self.edges.add(Line_by2dots(O[1], R[1]))
        self.edges.add(Line_by2dots(O[2], R[2]))
        self.edges.add(Line_by2dots(O[3], R[3]))

        self.edges.add(Line_by2dots(G[0], G[3]))
        self.edges.add(Line_by2dots(G[1], G[2]))

        self.edges.add(Line_by2dots(R[0], R[1]))
        self.edges.add(Line_by2dots(R[2], R[3]))

        self.edges.add(Line_by2dots(R[0], O[4]))
        self.edges.add(Line_by2dots(R[1], O[5]))
        self.edges.add(Line_by2dots(R[2], O[6]))
        self.edges.add(Line_by2dots(R[3], O[7]))

        self.edges.add(Line_by2dots(G[3], O[4]))
        self.edges.add(Line_by2dots(G[2], O[5]))
        self.edges.add(Line_by2dots(G[2], O[6]))
        self.edges.add(Line_by2dots(G[3], O[7]))

        self.edges.add(Line_by2dots(O[4], B[1]))
        self.edges.add(Line_by2dots(O[5], B[1]))
        self.edges.add(Line_by2dots(O[6], B[2]))
        self.edges.add(Line_by2dots(O[7], B[2]))

        self.edges.add(Line_by2dots(B[2], B[1]))

    # def vertex_direction_updater(self, vertices):
    #     for group in vertices:
    #         for vertex in group:
    #             pos = vertex.get_center()
    #             color = vertex.get_color()
    #             size = vertex.get_height()
    #             dot = Dot(pos, color=color).set_height(size)
    #             vertex.become(dot)

    def create_faces(self):

        self.faces = VGroup()
        def Polygon_by_dots(*dots):
            pos_list = [dots[i].get_center() for i in range(len(dots))]
            return Polygon(*pos_list, color=self.edge_color, fill_color=self.face_color, fill_opacity=self.face_opacity, stroke_width=0)

        # edges from up to down, anti-clockwise order
        O, G, B, R = self.O_dots, self.G_dots, self.B_dots, self.R_dots
        self.faces.add(Polygon_by_dots(B[0], B[3], O[3], G[0], O[0]))
        self.faces.add(Polygon_by_dots(B[0], O[1], G[1], O[2], B[3]))
        self.faces.add(Polygon_by_dots(B[0], O[0], R[0], R[1], O[1]))
        self.faces.add(Polygon_by_dots(B[3], O[3], R[3], R[2], O[2]))
        self.faces.add(Polygon_by_dots(O[3], R[3], O[7], G[3], G[0]))
        self.faces.add(Polygon_by_dots(G[0], G[3], O[4], R[0], O[0]))
        self.faces.add(Polygon_by_dots(O[1], R[1], O[5], G[2], G[1]))
        self.faces.add(Polygon_by_dots(G[2], G[1], O[2], R[2], O[6]))
        self.faces.add(Polygon_by_dots(R[2], R[3], O[7], B[2], O[6]))
        self.faces.add(Polygon_by_dots(R[1], R[0], O[4], B[1], O[5]))
        self.faces.add(Polygon_by_dots(G[2], O[6], B[2], B[1], O[5]))
        self.faces.add(Polygon_by_dots(G[3], O[7], B[2], B[1], O[4]))

class EulerFormula_02(Scene):
    CONFIG = {
        'camera_config': {'background_color': WHITE}
    }

    def construct(self):

        # text = Text('V-E+F=2', font='庞门正道标题体', color=BLACK).shift(DOWN * 1.6).set_height(1.2)
        # text.set_color_by_t2c({'V': RED, 'E': BLUE_D, 'F': YELLOW_D})

        formula = TexMobject('\\mathbf{V', '-', 'E', '+', 'F', '=', '2}', color=BLACK, background_stroke_color=BLACK,
                             background_stroke_width=4.5).shift(DOWN * 1.6).set_height(1.)
        formula.set_color_by_tex_to_color_map({'V': RED, 'E': BLUE_D, 'F': YELLOW_D})


        graph = Regular_Dodecahedron(edge_color=BLACK, size=4).shift(UP * 1.6)
        # graph.rotate(PI/2, axis=UP)

        # self.play(ShowCreation(graph), run_time=2)
        self.add(graph)
        self.wait()
        self.play(Rotating(graph, radians=(270 + 30)*DEGREES, axis=UP), run_time=4)
        self.wait()
        # self.play(ShowCreation(text), run_time=2)
        self.play(ShowCreation(formula), run_time=2)

        self.wait(10)

class Jagged_func_test(Scene):

    def construct(self):
        func_smooth = ParametricFunction(lambda t: np.sign(t) * UP + t * RIGHT, t_min=-2, t_max=2).shift(UP * 1.6)
        func_jagged = ParametricFunction(lambda t: np.sign(t) * UP + t * RIGHT, t_min=-2, t_max=2).shift(DOWN * 1.6).make_jagged()

        self.play(ShowCreation(func_smooth))
        self.wait()
        self.play(ShowCreation(func_jagged))
        self.wait(2)

class EulerFormula_03(Scene):

    CONFIG = {
        'camera_config': {'background_color': WHITE}
    }

    def construct(self):

        R = 2.8
        O = UP * 1
        point_on_circle = lambda theta: (RIGHT * np.cos(theta) + UP * np.sin(theta)) * R + O
        A = point_on_circle(200 * DEGREES)
        B = point_on_circle(-20 * DEGREES)
        C = point_on_circle(60 * DEGREES)
        a = np.sqrt(sum((B-C) ** 2))
        b = np.sqrt(sum((A-C) ** 2))
        c = np.sqrt(sum((A-B) ** 2))
        I = a/(a+b+c) * A + b/(a+b+c) * B + c/(a+b+c) * C
        r = (R ** 2 - sum((O-I) ** 2))/2/R

        dot_a = Dot(A, color=GREEN_D).scale(1.2)
        dot_b = Dot(B, color=GREEN_D).scale(1.2)
        dot_c = Dot(C, color=GREEN_D).scale(1.2)
        dot_o = Dot(O, color=BLUE_D).scale(1.2)
        dot_i = Dot(I, color=RED).scale(1.2)

        tri_abc = Polygon(A, B, C, color=BLACK, stroke_width=6)

        circle_o = Circle(radius=R, color=BLUE_D, stroke_width=6).move_to(O)
        circle_i = Circle(radius=r, color=RED, stroke_width=6).move_to(I)

        arrow_R = Arrow(O, point_on_circle(220*DEGREES), buff=0, color=BLUE_D)
        arrow_r = Arrow(I, I + (RIGHT * np.cos(40 * DEGREES) + UP * np.sin(45 * DEGREES)) * r, buff=1, color=RED).scale(0.95)

        OI = DashedLine(O, I, color=PINK, stroke_width=6, dash_length=0.12, positive_space_ratio=0.75)

        tex_o = TexMobject('O', color=BLUE_D, background_stroke_color=BLUE_D, background_stroke_width=2).scale(0.8).next_to(O, LEFT * 0.16 + UP * 0.2)
        tex_i = TexMobject('I', color=RED, background_stroke_color=RED, background_stroke_width=2).scale(0.8).next_to(I, RIGHT * 0.16 + DOWN * 0.2)
        tex_R = TexMobject('R', color=BLUE_D, background_stroke_color=BLUE_D, background_stroke_width=2).scale(0.8).next_to(arrow_R.get_end(), RIGHT * 2.5 + UP * 0.4)
        tex_r = TexMobject('r', color=RED, background_stroke_color=RED, background_stroke_width=2).scale(0.8).next_to(arrow_r.get_end(), LEFT * 2 + DOWN * 0.4)

        self.add(tri_abc, circle_o, circle_i, OI, dot_a, dot_b, dot_c, dot_i, dot_o, arrow_R, arrow_r, tex_o, tex_i, tex_R, tex_r)

        self.wait(1)
        formula = TexMobject('\\mathbf{OI', '^2', '=', 'R', '^2', '-', '2', 'R', 'r}', color=BLACK,
                             background_stroke_color=BLACK, background_stroke_width=3.6).scale(1.6).shift(DOWN * 2.4)
        formula.set_color_by_tex_to_color_map({'OI': PINK, 'R': BLUE_D, 'r': RED})

        self.play(Write(formula), run_time=2)

        self.wait(10)

class EulerFormula_04(Scene):

    CONFIG = {
        'camera_config': {'background_color': WHITE}
    }

    def construct(self):

        formula = TexMobject('\\mathbf{e', '^{i', 'x', '}=', '\\cos{', 'x', '}+', 'i', '\\sin', '{x}}',
                             color=WHITE, background_stroke_color=WHITE, background_stroke_width=4).set_height(1.)

        formula.set_color_by_tex_to_color_map({'i': ORANGE, 'x': BLUE, 'e': GREEN, '\\sin': YELLOW_D, '\\cos': YELLOW_D}).shift(DOWN * 1.8)
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

        tex_i_1 = TexMobject('\\mathbf{i}', color=ORANGE, background_stroke_color=ORANGE, background_stroke_width=1.6).scale(0.8)
        tex_i_2 = TexMobject('\\mathbf{-i}', color=ORANGE, background_stroke_color=ORANGE, background_stroke_width=1.6).scale(0.8)
        tex_i_1.shift(UP * 2.2 + RIGHT * 0.275)
        tex_i_2.shift(DOWN * 2.2 + RIGHT * 0.275)

        tex_1_1 = TexMobject('\\mathbf{1}', color=WHITE, background_stroke_color=WHITE, background_stroke_width=1.6).scale(0.8)
        tex_1_2 = TexMobject('\\mathbf{-1}', color=WHITE, background_stroke_color=WHITE, background_stroke_width=1.6).scale(0.8)
        tex_1_1.shift(RIGHT * 2.25 + DOWN * 0.275)
        tex_1_2.shift(LEFT * 2.35 + DOWN * 0.275)

        tex_cos = TexMobject('\\mathbf{\\cos{', 'x}}', color=YELLOW_D, background_stroke_color=WHITE, background_stroke_width=1).scale(0.8)
        tex_sin = TexMobject('\\mathbf{\\sin{', 'x}}', color=YELLOW_D, background_stroke_color=WHITE, background_stroke_width=1).scale(0.8)
        tex_cos[1].set_color(BLUE)
        tex_sin[1].set_color(BLUE)
        tex_cos.next_to(line_2, DOWN * 0.8)
        tex_sin.next_to(line_3, RIGHT * 1.25)

        tex_group = VGroup(tex_1_1, tex_1_2, tex_i_1, tex_i_2).shift(UP * 1.2)

        self.add(group_1, group_2, tex_group, tex_cos, tex_sin)
        self.wait()

        self.play(Write(formula))

        self.wait(10)

class EulerFormula_05(Scene):

    CONFIG = {
        'camera_config': {'background_color': WHITE}
    }

    def construct(self):

        formula = TexMobject('\\mathbf{a', '^{\\varphi', '(', 'n', ')}', '\\equiv', '1', '(', 'mod', '\\,\\,n', ')}',
                             color=BLACK, background_stroke_color=BLACK, background_stroke_width=4).set_height(1.5)
        formula.set_color_by_tex_to_color_map({'a': RED_D, '\\varphi': PINK, 'n': BLUE, 'mod': GREEN})

        self.play(Write(formula))

        self.wait(10)
