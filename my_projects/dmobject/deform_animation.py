from my_manim_projects.my_projects.dmobject.deformable_mobject import *
MY_BLACK = '#060606'
MY_WHITE = '#EEEEEE' #'#F5F5F5'

class Test_CIRLCE9(Scene):

    CONFIG = {
        'camera_config': {
            'background_color': WHITE,
        }
    }

    def construct(self):
        svg_path = 'E:\\GitHub\\manim\\my_manim_projects\\my_projects\\resource\\svg_files\\'
        grid = VGroup(*[Square(stroke_width=1, stroke_color=BLUE_D).shift(2*RIGHT*(i%10) + 2*UP*int(i/10)) for i in range(100)]).set_height(4).move_to(ORIGIN)
        coin = SVGMobject(svg_path + 'coin.svg', color='#FF7E00').set_height(3.2)
        # circles = VGroup(*[Circle(radius=(i+1)*0.25, stroke_color='#FF7E00', stroke_width=3.5) for i in range(8)])

        # dmobs = DeformableVMobject(grid, coin, elem_range=[DL, UR])
        # square = Square(stroke_width=3.6, stroke_color=BLUE_D).set_height(4)
        circle = Circle(stroke_width=3.6, stroke_color=BLUE_D).set_height(4)
        dmobs = Dmob_CIRCLE9(circle, grid, coin)

        self.play(FadeInFromLarge(coin), run_time=1)
        self.wait(0.2)
        self.play(AnimationGroup(ShowCreation(grid), ShowCreation(circle), FadeIn(dmobs.nodes), lag_ratio=0.4), run_time=2.1)
        self.wait()
        self.remove(grid, circle)
        self.add(dmobs, dmobs.nodes)

        n1, n2, n3, n4, n5, n6, n7, n8, n9 = dmobs.get_nodes()
        dmobs.always_update()
        n2.set_fill(BLUE_D, 1)
        n4.set_fill(BLUE_D, 1)
        n6.set_fill(BLUE_D, 1)
        n8.set_fill(BLUE_D, 1)
        self.play(
            n2.shift, UR * (2-np.sqrt(2)),
            n4.shift, UL * (2-np.sqrt(2)),
            n6.shift, DL * (2-np.sqrt(2)),
            n8.shift, DR * (2-np.sqrt(2)),
            tun_time=2.5)
        n2.set_fill(WHITE, 1)
        n4.set_fill(WHITE, 1)
        n6.set_fill(WHITE, 1)
        n8.set_fill(WHITE, 1)

        self.wait()
        self.play(AnimationGroup(FadeOut(dmobs.nodes), Uncreate(dmobs.mobs[0]), Uncreate(dmobs.mobs[1]), lag_ratio=0.4), run_time=1.8)
        self.wait(3)

class Test_RECT4(Scene):

    CONFIG = {
        'camera_config': {
            'background_color': WHITE,
        }
    }

    def construct(self):
        svg_path = 'E:\\GitHub\\manim\\my_manim_projects\\my_projects\\resource\\svg_files\\'
        grid = VGroup(*[Square(stroke_width=1, stroke_color=BLUE_D).shift(2*RIGHT*(i%10) + 2*UP*int(i/10)) for i in range(100)]).set_height(3).move_to(ORIGIN)
        coin = SVGMobject(svg_path + 'coin.svg', color=GREY_E).set_height(3).set_plot_depth(1)
        square = Square(stroke_width=3.6, stroke_color=BLUE_D).set_height(3)
        dmobs = Dmob_RECT4(grid, square, coin)
        # self.add(coin)
        # self.wait(0.8)
        # self.play(FadeIn(grid), FadeIn(dmobs.nodes))
        # self.add(dmobs, dmobs.nodes)
        self.wait()
        self.play(FadeInFromLarge(coin), run_time=1)
        self.wait(0.2)
        self.play(AnimationGroup(ShowCreation(grid), ShowCreation(square), FadeIn(dmobs.nodes), lag_ratio=0.4), run_time=2.1)
        self.wait()
        self.remove(*self.mobjects)
        self.add(dmobs, dmobs.nodes)
        n1, n2, n3, n4 = dmobs.get_nodes()
        dmobs.always_update()
        for n in dmobs.nodes: n.active_if_moved()
        self.play(AnimationGroup(ApplyMethod(n1.move_to, LEFT * 1.6 + UP* 0.4),
                                 ApplyMethod(n2.move_to, DR * 3),
                                 ApplyMethod(n3.move_to,UP * 3 + RIGHT *0.8),
                                 ApplyMethod(n4.move_to, DOWN * 2 + LEFT * 3), lag_ratio=0.4), run_time=2.4)
        self.play(AnimationGroup(ApplyMethod(n1.move_to, UR * 2),
                                 ApplyMethod(n4.move_to, DL * 2),
                                 ApplyMethod(n3.move_to, DR * 1.2), lag_ratio=0.4), run_time=1.8)

        # dmobs.update_by_interpolation()
        self.wait(1.2)
        self.play(n1.move_to, DL * 2.5, n2.move_to, DR * 2.5,
                  n3.move_to, UR * 2.5, n4.move_to, UL * 2.5,
                  run_time=1.)

        self.wait(2)

class Deformation_Tex_test(Scene):

    CONFIG = {
        'camera_config': {
            'background_color': WHITE,
        }
    }

    def construct(self):


        grid = VGroup(*[Square(stroke_width=1, stroke_color=BLUE_D).shift(2*RIGHT*(i%16) + 2*UP*int(i/16)) for i in range(32)]).set_width(8).move_to(ORIGIN)
        rect = Square(stroke_width=3.6, stroke_color=BLUE_D).set_width(8).set_height(1, stretch=True)
        # hw = Text('Hello World', color=GREY_E, font='思源黑体 Bold').set_height(1.)
        text = TexMobject('\\mathbf{manim\\ kindergarten}', color=MY_BLACK, stroke_width=1).set_width(7.5)

        # self.add(rect, grid, hw[0])

        d_text = Dmob_RECT9(rect, grid, text)
        n1, n2, n3, n4, n5, n6, n7, n8, n9= d_text.get_nodes()
        self.add(d_text, d_text.nodes)
        d_text.always_update()

        c1 = Arc(arc_center=DOWN * 2, start_angle=PI/4, radius=4.0, color=BLUE, stroke_width=2)
        c2 = Arc(arc_center=DOWN * 2, start_angle=PI/4, radius=4.4, color=BLUE, stroke_width=2)
        c3 = Arc(arc_center=DOWN * 2, start_angle=PI/4, radius=4.8, color=BLUE, stroke_width=2)
        self.add(c1, c2, c3)

        n_list_1 = [n1 ,n2, n3]
        n_list_2 = [n4 ,n5, n6]
        n_list_3 = [n7 ,n8, n9]
        put_nodes_on_curve(n_list_1, c1, reverse=True)
        put_nodes_on_curve(n_list_2, c2, reverse=True)
        put_nodes_on_curve(n_list_3, c3, reverse=True)

        self.wait()

class Deformation_Tex_01(Scene):

    CONFIG = {
        'camera_config': {
            'background_color': WHITE,
        }
    }

    def construct(self):

        text = TexMobject('\\mathbf{MANIM\\ KINDERGARTEN}', color=MY_BLACK, stroke_width=1).set_width(7.5)
        dmobs = VGroup(*[Dmob_RECT9(text[0][i]) for i in range(len(text[0]))])

        self.add(dmobs)
        for dm in dmobs: dm.always_update()

        c1 = Arc(arc_center=DOWN * 2, start_angle=PI/4, radius=4.0, color=BLUE, stroke_width=2)
        c2 = Arc(arc_center=DOWN * 2, start_angle=PI/4, radius=4.4, color=BLUE, stroke_width=2)
        c3 = Arc(arc_center=DOWN * 2, start_angle=PI/4, radius=4.8, color=BLUE, stroke_width=2)
        self.add(c1, c2, c3)

        n_list_1 = []
        n_list_2 = []
        n_list_3 = []
        for dm in dmobs:
            n_list_1 += dm.nodes[0:3]
            n_list_2 += dm.nodes[3:6]
            n_list_3 += dm.nodes[6:]
        put_nodes_on_curve(n_list_1, c1, reverse=True)
        put_nodes_on_curve(n_list_2, c2, reverse=True)
        put_nodes_on_curve(n_list_3, c3, reverse=True)

        self.wait()

class Deformation_Tex_02(Scene):

    CONFIG = {
        'camera_config': {
            'background_color': MY_WHITE,
        }
    }

    def construct(self):
        text = TexMobject('\\textbf{MANIM\\  KINDERGARTEN}', color=MY_BLACK, stroke_width=1.5).set_width(7.5)
        # text = TexMobject('\\textbf{MANIM\\  COMMUNITY}', color=MY_BLACK, stroke_width=1.5).set_width(7.5)
        # text = TexMobject('\\mathbb{ONE\\ RING\\ TO\\ RULE\\ THEM\\ ALL}', color=MY_BLACK, stroke_width=1).set_width(7.5)
        # background_stroke_width
        text_copy_02 = text.copy().set_stroke(color=MY_BLACK, width=1.6).set_fill(MY_WHITE, 1).set_plot_depth(-1).scale(1.6).to_edge(UP, buff=0.75)
        text_copy = text.copy().scale(1.6).to_edge(UP, buff=0.75)
        # self.add(rect, grid, hw[0])
        dmobs = VGroup(*[Dmob_RECT9(text[0][i], node=Small_Node()) for i in range(len(text[0]))])

        c1 = Arc(radius=2.6, start_angle=PI+PI/6, angle=TAU, color=BLUE, stroke_width=2).scale([1, 0.45, 1]).shift(-UP * 0.4)
        c2 = Arc(radius=2.8, start_angle=PI+PI/6, angle=TAU, color=BLUE, stroke_width=2).scale([1, 0.45, 1]).shift( UP * 0.0)
        c3 = Arc(radius=2.6, start_angle=PI+PI/6, angle=TAU, color=BLUE, stroke_width=2).scale([1, 0.45, 1]).shift( UP * 0.4)
        circles = VGroup(c1, c2, c3).rotate(PI/6).shift(DOWN * 0.4)

        self.play(Write(text_copy), run_time=2)
        # self.play(FadeIn(text_copy_02), run_time=0.8)
        self.add(text_copy_02)
        self.wait(0.4)
        self.play(ShowCreation(c1), run_time=0.4)
        self.play(ShowCreation(c2), run_time=0.5)
        self.play(ShowCreation(c3), run_time=0.6)
        self.wait(0.8)

        # self.add(dmobs)
        for dm in dmobs: dm.always_update()
        n_list_1 = []
        n_list_2 = []
        n_list_3 = []
        for dm in dmobs:
            n_list_1 += dm.nodes[0:3]
            n_list_2 += dm.nodes[3:6]
            n_list_3 += dm.nodes[6:]
        n_vg_1, n_vg_2, n_vg_3 = VGroup(*n_list_1), VGroup(*n_list_2), VGroup(*n_list_3)

        put_nodes_on_curve(n_vg_1, c1, end_alpha=0.96)
        put_nodes_on_curve(n_vg_2, c2, end_alpha=0.96)
        put_nodes_on_curve(n_vg_3, c3, end_alpha=0.96)
        for dm in dmobs: dm.stop_update()
        for i in range(5):
            self.play(ReplacementTransform(text_copy[0][i], dmobs[i]), run_time=0.8)
        self.wait(0.5)
        # self.play(ReplacementTransform(text_copy[0][5:], dmobs[5:]), run_time=1.6)
        n = len(dmobs)
        t0 = 1
        self.play(AnimationGroup(*[ReplacementTransform(text_copy[0][i], dmobs[i]) for i in range(5, n)], lag_ratio=1/(n-5), run_time=t0/3 * (n-5+1)))
        # self.wait()
        # for dm in dmobs: dm.always_update()
        # n_vg_1.add_updater(lambda n: put_nodes_on_curve(n, c1))
        # n_vg_2.add_updater(lambda n: put_nodes_on_curve(n, c2))
        # n_vg_3.add_updater(lambda n: put_nodes_on_curve(n, c3))
        #
        # self.play(c1.scale, 1.25, rate_func=there_and_back, run_time=1.5)

        self.wait(4)

class Deformation_Tex_03(Scene):

    CONFIG = {
        'camera_config': {
            'background_color': MY_WHITE,
        }
    }

    def construct(self):

        c2r = lambda c: complex_to_R3(c)

        s = 0.8
        c = UP * 2
        x, y, z = c2r(s * np.exp(1j * (-PI/6))), c2r(s * np.exp(1j * (PI/6))), c2r(s * np.exp(1j * (PI/2)))

        # t1 = TexMobject('\\textsf{祝数心酱}', color=MY_BLACK, background_stroke_width=2).set_height(0.6)
        # for t in t1[0]:
        #     t.rotate(PI/2)
        # t2 = TexMobject('\\textsf{六一儿童节快乐}', color=MY_BLACK, background_stroke_width=2).set_height(0.6)
        t1 = TexMobject('\\textbf{MANIM}', color=MY_BLACK, background_stroke_width=0).set_height(0.4)
        t2 = TexMobject('\\textbf{KINDERGARTEN}', color=MY_BLACK, background_stroke_width=0).set_height(0.4)
        t1.to_corner(UL, buff=1)
        t2.next_to(t1, DOWN, aligned_edge=LEFT, buff=0.25)
        # self.add(t1, t2)

        p0 = c - y - 2 * z
        p1, p2, p3, p4 = c - 2 * z, c + 2 * (x + y), c + x + 2 * y, c - y - z
        p5, p6, p7, p8 = c - 2 * y - 3 * z, c + 3 * x + 2 * y, c + 2 * x + 3 * y, c - 2 * (y + z)

        p_list = p0, p7, c - 2 * x + 3 * z, c - 3 * x + 2 * z, p3, p4

        poly = Polygon(*p_list, stroke_width=2.4, stroke_color=BLUE).shift(DOWN * 2)
        # poly_01 = Polygon(p0, p2, p3, p4, stroke_width=1.5, stroke_color=BLUE)
        # poly_02 = Polygon(p5, p6, p7, p8, stroke_width=1.5, stroke_color=BLUE)
        dmob1, dmob2 = Dmob_RECT4(t1, side_offset=0.04),  Dmob_RECT4(t2, side_offset=0.04)
        polys = VGroup(poly, poly.copy().rotate(TAU/3, about_point=ORIGIN), poly.copy().rotate(-TAU/3, about_point=ORIGIN))

        self.play(Write(VGroup(dmob1, dmob2)), run_time=1.8)
        self.wait(0.25)

        l1 = Line(p4, p3, stroke_width=1.5, stroke_color=BLUE)
        l2 = Line(p8, p7, stroke_width=1.5, stroke_color=BLUE)
        l3 = Line(p5, p6, stroke_width=1.5, stroke_color=BLUE)

        self.play(ShowCreation(l1), run_time=0.4)
        self.play(ShowCreation(l2), run_time=0.5)
        self.play(ShowCreation(l3), run_time=0.6)
        self.wait(0.2)
        self.play(*[FadeInFromLarge(n) for n in dmob1.nodes], run_time=0.6)
        self.wait(0.2)
        dmob1.always_update(), dmob2.always_update()
        self.play(dmob1.nodes[0].move_to, p1, dmob1.nodes[1].move_to, p2,
                  dmob1.nodes[2].move_to, p3, dmob1.nodes[3].move_to, p4, run_time=1.)
        self.wait(0.6)
        self.play(*[FadeInFromLarge(n) for n in dmob2.nodes], run_time=0.6)
        self.wait(0.2)
        self.play(dmob2.nodes[0].move_to, p5, dmob2.nodes[1].move_to, p6,
                  dmob2.nodes[2].move_to, p7, dmob2.nodes[3].move_to, p8, run_time=1.)
        self.wait(0.2)
        self.play(FadeOut(dmob1.nodes), FadeOut(dmob2.nodes), run_time=0.6)
        self.play(Uncreate(l1), Uncreate(l2), Uncreate(l3), run_time=0.4)
        self.wait(1.2)
        dmob1.stop_update(), dmob2.stop_update()
        vg_1 = VGroup(dmob1, dmob2)
        self.play(vg_1.shift, DOWN * 2, run_time=0.8)
        self.wait(0.6)
        vg_2 = vg_1.copy()
        self.play(Rotating(vg_2, radians=TAU/3, about_point=ORIGIN, rate_func=smooth), run_time=1)
        self.wait(0.1)
        vg_3 = vg_2.copy()
        self.play(Rotating(vg_3, radians=TAU/3, about_point=ORIGIN, rate_func=smooth), run_time=1)
        self.wait(0.25)
        self.play(ShowCreation(polys), rate_func=there_and_back_with_pause, run_Time=3.)

        # vg_2[0].rotate(PI), vg_2[1].rotate(PI)
        #
        # # vg_1[0].set_color(GREY_C), vg_2[1].set_color(GREY_C)
        # # vg_2[0].set_color('#CCCCCC'), vg_3[1].set_color('#CCCCCC')
        # # vg_3[0].set_color(MY_BLACK), vg_1[1].set_color(MY_BLACK)
        # self.add(vg_1, vg_2, vg_3)

        self.wait(3)

class D_tube(ThreeDScene):

    CONFIG = {
        'camera_config': {
            'background_color': MY_WHITE,
            'should_apply_shading': False,
        },
    }

    def construct(self):

        self.set_camera_orientation(phi=60*DEGREES, theta=-70*DEGREES)
        grid = VGroup(*[Square(stroke_width=1, stroke_color=GREY_B).shift(2 * RIGHT*(i%10) + 2 * UP*int(i/10)) for i in range(100)]).set_width(10).move_to(IN * 1)
        grid.set_shade_in_3d()
        tube = DeformableTube(radius=1, start=IN * 1, end=OUT * 1, subtube_num=1, side_offset=0.25, angle=TAU,
                              circle_config={'stroke_width': 2.5, 'stroke_color': BLUE_D, 'fill_opacity': 0},
                              tube_config={'resolution': (15, 6), 'stroke_width': 2, 'fill_opacity':0.8})
        # tube.control_circle.set_shade_in_3d()
        self.add(grid, tube, tube.control_circle)
        self.wait()
        tube.always_update()

        c1, c2, c3 = tube.control_circle
        # self.play(c2.scale, 1.6, rate_func=there_and_back, run_time=1.)
        s = 1
        self.play(c3.shift, OUT * 2, c2.shift, OUT * 1., rate_func=smooth, run_time=0.8 * s)
        self.wait(0.2)
        self.play(c3.shift, -OUT * 4, c2.shift, -OUT * 2, rate_func=smooth, run_time=0.8 * s)
        self.wait(0.2)

        self.play(Rotating(c2, radians=PI/6, about_point=3*RIGHT+IN, axis=UP),
                  Rotating(c3, radians=PI/3, about_point=3*RIGHT+IN, axis=UP), run_time=1 * s)
        self.wait(0.2)

        self.play(Rotating(c2, radians=-PI/6, about_point=IN+OUT * 3 * np.sin(PI/12), axis=UP),
                  Rotating(c3, radians=-PI/3, about_point=IN+OUT * 3 * np.sin(PI/6), axis=UP), run_time=1 * s)
        self.wait(0.2)
        self.play(c2.scale, 2, c3.scale, 3, c3.shift, IN-c3.get_center(), run_time=1 * s)
        self.wait(0.2)
        self.play(c1.scale, 3, c1.shift, (c2.get_center() - IN) * 2, run_time=1 * s)
        self.wait(0.2)
        self.play(c1.scale, 2/3, c3.scale, 2/3, run_time=1 * s)
        self.wait(4)

class Deformation_Tex_infinity(Scene):

    CONFIG = {
        'camera_config': {
            'background_color': WHITE,
        }
    }

    def construct(self):
        svg_path = 'E:\\GitHub\\manim\\my_manim_projects\\my_projects\\resource\\svg_files\\'
        curve = SVGMobject(svg_path + 'infinity.svg', stroke_color=BLUE, stroke_width=3, fill_opacity=0).set_width(8)
        c1, c3 = curve[0], curve[1]
        c2 = ParametricFunction(lambda t: (c1.point_from_proportion(t) + c3.point_from_proportion(1-t))/2,
                                t_min=0, t_max=1, stroke_color=BLUE, stroke_width=3)


        text = TexMobject('\\mathbf{3.1415926535 8979323846 2643383279 5028841971 6939937510'
                                   '5820974944 5923078164 0628620899 8628034825 3421170679'
                                   # '8214808651 3282306647 0938446095 5058223172 5359408128'
                                   # '4811174502 8410270193 8521105559 6446229489 5493038196'
                                   # '4428810975 6659334461 2847564823 3786783165 2712019091'
                                   # '4564856692 3460348610 4543266482 1339360726 0249141273'
                                   # '7245870066 0631558817 4881520920 9628292540 9171536436'
                                   # '7892590360 0113305305 4882046652 1384146951 9415116094'
                                   # '3305727036 5759591953 0921861173 8193261179 3105118548'
                          '}', color=MY_BLACK, stroke_width=1).set_width(7.5)
        # text = TexMobject('\\mathfrak{ONE\\ RING\\ TO\\ RULE\\ THEM\\ ALL}', color=MY_BLACK, stroke_width=1).set_width(7.5)

        # self.add(rect, grid, hw[0])
        dmobs = VGroup(*[Dmob_RECT9(text[0][i]) for i in range(len(text[0]))])

        self.add(dmobs)
        for dm in dmobs: dm.always_update()


        # c1 = Arc(radius=3.4, start_angle=PI+PI/6, angle=TAU, color=BLUE, stroke_width=2).scale([1, 0.8, 1]).shift(UP * 0.24)
        # c2 = Arc(radius=3.0, start_angle=PI+PI/6, angle=TAU, color=BLUE, stroke_width=2).scale([1, 0.8, 1]).shift(UP * 0.20)
        # c3 = Arc(radius=2.6, start_angle=PI+PI/6, angle=TAU, color=BLUE, stroke_width=2).scale([1, 0.8, 1]).shift(UP * 0.00)
        # circles = VGroup(c1, c2, c3).rotate(PI/3)

        self.add(c1, c2, c3)
        c1.set_stroke(color=BLUE)
        c2.set_stroke(color=YELLOW)
        c3.set_stroke(color=RED)

        n_list_1 = []
        n_list_2 = []
        n_list_3 = []
        for dm in dmobs:
            n_list_1 += dm.nodes[0:3]
            n_list_2 += dm.nodes[3:6]
            n_list_3 += dm.nodes[6:]

        put_nodes_on_curve(n_list_1, c1, start_alpha=0.3, end_alpha=0.99, reverse=True)
        put_nodes_on_curve(n_list_2, c2, start_alpha=0.27, end_alpha=0.99, reverse=True)
        put_nodes_on_curve(n_list_3, c3, start_alpha=0.24, end_alpha=0.99)

        self.wait(4)

class Warma_01(Scene):

    CONFIG = {
        'camera_config': {
            'background_color': WHITE,
        }
    }

    def construct(self):
        s = 1.2
        svg_path = 'E:\\GitHub\\manim\\my_manim_projects\\my_projects\\resource\\svg_files\\'
        grid = VGroup(*[Square(stroke_width=1, stroke_color=BLUE_D).shift(2*RIGHT*(i%10) + 2*UP*int(i/10)) for i in range(60)]).set_width(5*s).move_to(ORIGIN)
        rect = Square(stroke_width=3.6, stroke_color=BLUE_D).set_width(5*s).set_height(3*s, stretch=True)
        warma = SVGMobject(svg_path + 'warma_sleep.svg', color=WHITE).set_width(4.8*s)
        warma[0].set_color(GREY_E)
        warma[6:].set_color(GREY_E)

        p4, p3, p2, p1 = rect.get_vertices()
        p5, p6, p7, p8 = (p1+p2)/2, (p2+p3)/2, (p3+p4)/2, (p4+p1)/2
        dmobs = DeformableVMobject(rect, grid, warma, elem_range=[p1, p2, p3, p4, p5, p6, p7, p8, ORIGIN], type='QUAD9')
        dmobs.shift(DOWN * 1.5), dmobs.nodes.shift(DOWN * 1.5)

        ground = Line(LEFT, RIGHT, stroke_color=GREY_E, stroke_width=5).scale(8).shift(DOWN * 2.5)
        self.add(ground, dmobs, dmobs.nodes, )
        self.wait()
        n1, n2, n3, n4, n5, n6, n7, n8, n9= dmobs.get_nodes()
        dmobs.always_update()

        for i in range(2):
            self.play(n3.shift, UR * 0.1 * (s + i * 0.05), n4.shift, UL * 0.1 * (s + i * 0.05),
                      n7.shift, UP * 0.25 * (s + i * 0.05), n9.shift, UP * 0.1 * (s + i * 0.05),
                      rate_func=there_and_back, run_time=2.6)
            self.wait(1.2)
        rect.set_opacity(0), grid.set_opacity(0), dmobs.nodes.set_opacity(0)
        for i in range(5):
            self.play(n3.shift, UR * 0.1 * (s + i ** 2 * 0.05 + 0.15), n4.shift, UL * 0.1 * (s + i ** 2 * 0.05 + 0.15),
                      n7.shift, UP * 0.25 * (s + i ** 2 * 0.05 + 0.15), n9.shift, UP * 0.1 * (s + i ** 2 * 0.05 + 0.15),
                      n6.shift, UP * 0.1 * (s + i ** 2 * 0.05), n8.shift, UP * 0.1 * (s + i ** 2 * 0.02),
                      rate_func=there_and_back, run_time=2.6)
            self.wait(1)


        self.wait(2)

class ThreeD_Heart(ThreeDScene):

    CONFIG = {
        'camera_config': {
            'background_color': MY_WHITE,
            'should_apply_shading': False,
        },
    }

    def construct(self):

        self.set_camera_orientation(phi=75*DEGREES, theta=-80*DEGREES)
        axis_config = {
            "color": GREY_E,
            "include_tip": True,
            "exclude_zero_from_default_numbers": True,
        }
        axis = ThreeDAxes(axis_config=axis_config)
        r = 2.5
        half_sphere = ParametricSurface(lambda u, v: r * np.cos(u) * OUT + r * np.sin(u) * complex_to_R3(np.exp(1j * v)),
                                     u_min=0, u_max=PI, v_min=PI/2, v_max=3 * PI/2, resolution=[16, 16],
                                     checkerboard_colors=None, stroke_color=GREY_D, stroke_width=1.8,
                                     fill_opacity=1, fill_color=WHITE)
        cube_node = Cube(fill_color=BLUE_D, fill_opacity=1, stroke_width=2, stroke_color=BLUE_D, side_length=0.1) # .set_shade_in_3d(False)
        cube = Cube(fill_color=BLUE_D, fill_opacity=0, stroke_width=1, stroke_color=BLUE_D, side_length=5) # .set_shade_in_3d(False)
        cube.set_width(2.5, stretch=True).shift(LEFT * 1.25)

        xyz = np.meshgrid(*[np.array([-2.5, -1.25, 0]), np.array([-2.5, 0, 2.5]), np.array([-2.5, 0, 2.5])])
        x, y, z = xyz[0].flatten(), xyz[1].flatten(), xyz[2].flatten()
        p = np.array([x, y, z]).T

        dmobs = DeformableVMobject(cube, half_sphere, node=cube_node, elem_range=p, type='HEXA27')
        self.add(dmobs, dmobs.nodes)

        self.wait(1.2)
        dmobs.always_update()
        ## 一堆节点处理起来好蛋疼
        nodes = dmobs.get_nodes()
        node_id = list(range(27))
        y_n = node_id[0:9]
        y_0 = node_id[9:18]
        y_p = node_id[18:27]
        x_n = [id for id in node_id if (id%9) in [0, 1, 2]]
        x_0 = [id for id in node_id if (id%9) in [3, 4, 5]]
        x_p = [id for id in node_id if (id%9) in [6, 7, 8]]
        z_n = [id for id in node_id if id%3 == 0]
        z_0 = [id for id in node_id if id%3 == 1]
        z_p = [id for id in node_id if id%3 == 2]

        n1 = VGroup(*[nodes[i] for i in x_n if i in z_n])
        n2 = VGroup(*[nodes[i] for i in x_0 if i in z_n])
        n3 = VGroup(*[nodes[i] for i in x_p if i in z_n])
        n4 = VGroup(*[nodes[i] for i in x_n if i in z_0])
        n5 = VGroup(*[nodes[i] for i in x_0 if i in z_0])
        n6 = VGroup(*[nodes[i] for i in x_p if i in z_0])
        n7 = VGroup(*[nodes[i] for i in x_n if i in z_p])
        n8 = VGroup(*[nodes[i] for i in x_0 if i in z_p])
        n9 = VGroup(*[nodes[i] for i in x_p if i in z_p])

        # n1.shift(OUT * 1.2 + LEFT * 0.25)
        # n2.shift(OUT * 0.8 + LEFT* 0.1)
        # n4.shift(OUT)
        # n5.shift(OUT * 0.75)
        # n7.shift(OUT * 0.25)
        # n8.shift(RIGHT * 0.12)
        # n9.shift(IN)
        s = 1
        self.play(n7.shift, OUT * 0.25, n8.shift, RIGHT * 0.12,  n9.shift, IN, run_time=1.*s)
        self.wait(0.6)
        self.play(n4.shift, OUT, n5.shift, OUT * 0.75, run_time=1.*s)
        self.wait(0.6)
        self.play(n1.shift, OUT * 1.2 + LEFT * 0.25, n2.shift, OUT * 0.8 + LEFT* 0.1, run_time=1.*s)
        self.wait(0.6)
        dmobs.stop_update()
        self.play(nodes.scale, [1,0.6,1], dmobs.scale, [1, 0.6, 1], run_time=1. * s)
        heart_r = dmobs.get_result()[1].flip(axis=OUT, about_point=ORIGIN)
        self.play(FadeIn(heart_r), run_time=1.25)
        self.wait(4)

class ThreeD_Heart_rotate(ThreeDScene):

    CONFIG = {
        'camera_config': {
            'background_color': MY_WHITE,
            'should_apply_shading': False,
        },
    }

    def construct(self):

        self.set_camera_orientation(phi=75*DEGREES, theta=-80*DEGREES)
        axis_config = {
            "color": GREY_E,
            "include_tip": True,
            "exclude_zero_from_default_numbers": True,
        }
        axis = ThreeDAxes(axis_config=axis_config)
        r = 2.5
        half_sphere = ParametricSurface(lambda u, v: r * np.cos(u) * OUT + r * np.sin(u) * complex_to_R3(np.exp(1j * v)),
                                     u_min=0, u_max=PI, v_min=PI/2, v_max=3 * PI/2, resolution=[16, 16],
                                     checkerboard_colors=None, stroke_color=GREY_D, stroke_width=1.8,
                                     fill_opacity=1, fill_color=WHITE)
        cube_node = Cube(fill_color=BLUE_D, fill_opacity=1, stroke_width=2, stroke_color=BLUE_D, side_length=0.1) # .set_shade_in_3d(False)
        cube = Cube(fill_color=BLUE_D, fill_opacity=0, stroke_width=1, stroke_color=BLUE_D, side_length=5) # .set_shade_in_3d(False)
        cube.set_width(2.5, stretch=True).shift(LEFT * 1.25)

        xyz = np.meshgrid(*[np.array([-2.5, -1.25, 0]), np.array([-2.5, 0, 2.5]), np.array([-2.5, 0, 2.5])])
        x, y, z = xyz[0].flatten(), xyz[1].flatten(), xyz[2].flatten()
        p = np.array([x, y, z]).T

        dmobs = DeformableVMobject(cube, half_sphere, node=cube_node, elem_range=p, type='HEXA27')
        self.add(dmobs, dmobs.nodes)
        dmobs.always_update()
        ## 一堆节点处理起来好蛋疼
        nodes = dmobs.get_nodes()
        node_id = list(range(27))
        y_n = node_id[0:9]
        y_0 = node_id[9:18]
        y_p = node_id[18:27]
        x_n = [id for id in node_id if (id%9) in [0, 1, 2]]
        x_0 = [id for id in node_id if (id%9) in [3, 4, 5]]
        x_p = [id for id in node_id if (id%9) in [6, 7, 8]]
        z_n = [id for id in node_id if id%3 == 0]
        z_0 = [id for id in node_id if id%3 == 1]
        z_p = [id for id in node_id if id%3 == 2]

        n1 = VGroup(*[nodes[i] for i in x_n if i in z_n])
        n2 = VGroup(*[nodes[i] for i in x_0 if i in z_n])
        n3 = VGroup(*[nodes[i] for i in x_p if i in z_n])
        n4 = VGroup(*[nodes[i] for i in x_n if i in z_0])
        n5 = VGroup(*[nodes[i] for i in x_0 if i in z_0])
        n6 = VGroup(*[nodes[i] for i in x_p if i in z_0])
        n7 = VGroup(*[nodes[i] for i in x_n if i in z_p])
        n8 = VGroup(*[nodes[i] for i in x_0 if i in z_p])
        n9 = VGroup(*[nodes[i] for i in x_p if i in z_p])

        n1.shift(OUT * 1.2 + LEFT * 0.25)
        n2.shift(OUT * 0.8 + LEFT* 0.1)
        n4.shift(OUT)
        n5.shift(OUT * 0.75)
        n7.shift(OUT * 0.25)
        n8.shift(RIGHT * 0.12)
        n9.shift(IN)
        # s = 1
        # self.play(n7.shift, OUT * 0.25, n8.shift, RIGHT * 0.12,  n9.shift, IN, run_time=1.*s)
        # self.wait(0.6)
        # self.play(n4.shift, OUT, n5.shift, OUT * 0.75, run_time=1.*s)
        # self.wait(0.6)
        # self.play(n1.shift, OUT * 1.2 + LEFT * 0.25, n2.shift, OUT * 0.8 + LEFT* 0.1, run_time=1.*s)
        # self.wait(0.6)
        dmobs.stop_update()
        nodes.scale([1,0.6,1])
        dmobs.scale([1, 0.6, 1])

        heart_r = dmobs.get_result()[1].flip(axis=OUT, about_point=ORIGIN)
        # self.play(FadeIn(heart_r), run_time=1.25)

        self.add(heart_r)
        self.wait()
        self.begin_ambient_camera_rotation(rate=0.4)
        self.wait(15)

class Klein_bottle(ThreeDScene):

    CONFIG = {
        'camera_config': {
            'background_color': MY_WHITE,
            'should_apply_shading': False,
        },
    }

    def construct(self):

        self.set_camera_orientation(phi=70*DEGREES, theta=-70*DEGREES)
        axis_config = {
            "color": GREY_E,
            "include_tip": True,
            "exclude_zero_from_default_numbers": True,
        }
        axis = ThreeDAxes(axis_config=axis_config)

        tube = DeformableTube(radius=0.5, start=IN * 4.5, end=OUT * 9.5, subtube_num=7, side_offset=0.1, angle=TAU,
                              tube_config={'resolution': (18, 6), 'stroke_width': 1.6, 'fill_opacity':0.4})

        # self.add(tube)

        tube.always_update()
        c = tube.control_circle
        c[0].scale(3.2), c[1].scale(2.2)
        c[2].scale(1.45).shift(IN * 0.4)
        c[0].move_to(c[2])

        c[3:].shift(LEFT * 0.3 + OUT * 0.15).rotate(-10 * DEGREES, axis=UP, about_point=c[3].get_center()), c[3].scale(1.15)
        c[4:].shift(LEFT * 0.7 + OUT * 0.15).rotate(-15 * DEGREES, axis=UP, about_point=c[4].get_center()), c[4].scale(0.95)
        c[5:].shift(LEFT * 0.3 + OUT * 0.15).rotate(15 * DEGREES, axis=UP, about_point=c[5].get_center()), c[5].scale(0.88)
        c[6:].shift(LEFT * 0.2 + OUT * 0.15).rotate(10 * DEGREES, axis=UP, about_point=c[6].get_center()), c[6].scale(0.8)
        c[7].scale(0.8), c[8].scale(0.8), c[9].scale(0.8), c[10].scale(0.8)
        # print(c[6].get_center())
        # c[7].move_to(c[6]).rotate(45 * DEGREES, axis=UP, about_point=c[6].get_center()+1.5 * RIGHT)
        # c[8].move_to(c[6]).rotate(90 * DEGREES, axis=UP, about_point=c[6].get_center()+1.5 * RIGHT)
        c[7:].shift(RIGHT * 0.32 + IN * 0.05).rotate(45 * DEGREES, axis=UP, about_point=c[7].get_center())
        c[8:].rotate(45 * DEGREES, axis=UP, about_point=c[8].get_center()).shift(c[6].get_center() + 1.13 * RIGHT + 1.325 * OUT - c[8].get_center())
        c[9:].rotate(45 * DEGREES, axis=UP, about_point=c[9].get_center()).shift(c[8].get_center() + (c[8].get_center() - c[7].get_center()) * np.array([1,1,-1]) - c[9].get_center())
        c[10:].rotate(45 * DEGREES, axis=UP, about_point=c[10].get_center()).shift(c[6].get_center() * OUT - c[10].get_center())
        c[11].scale(1.1)
        c[11].scale(1.2)
        c[12].scale(2.5).shift(IN * 0.2)
        c[13].scale(3.5).shift(IN * 0.4)
        c[14].scale(3.2).move_to(c[2])
        self.wait()
        self.play(AnimationGroup(*[FadeInFromLarge(c) for c in tube.control_circle], lag_ratio=0.2), run_time=2.1)
        self.wait(0.15)
        self.play(ShowCreation(tube), run_time=2.)
        # t_result = VGroup(*[t.get_result() for t in tube])
        # self.add(t_result)
        self.wait(1.2)
        self.play(AnimationGroup(*[FadeOut(c) for c in tube.control_circle], lag_ratio=0.2), run_time=1.6)
        self.wait(4)

class Ending(Scene):

    CONFIG = {
        'camera_config': {
            'background_color': MY_WHITE,
        }
    }

    def construct(self):
        bg = Square(stroke_width=0, fill_color=[GREEN_B, YELLOW_A], fill_opacity=1, plot_depth=-100).scale([15/2, 9/2, 1])
        self.add(bg)
        c2r = lambda c: complex_to_R3(c)

        s = 0.8
        c = LEFT * 3.5
        x, y, z = c2r(s * np.exp(1j * (-PI/6))), c2r(s * np.exp(1j * (PI/6))), c2r(s * np.exp(1j * (PI/2)))
        # x, y, z = c2r(s * np.exp(1j * (-PI/2))), c2r(s * np.exp(1j * (-PI/6))), c2r(s * np.exp(1j * (PI/6)))

        t1 = TexMobject('\\textbf{MANIM}', color=MY_BLACK, background_stroke_width=0).set_height(0.4)
        t2 = TexMobject('\\textbf{KINDERGARTEN}', color=MY_BLACK, background_stroke_width=0).set_height(0.4)
        t1.to_corner(UL, buff=1)
        t2.next_to(t1, DOWN, aligned_edge=LEFT, buff=0.25)

        p0 = c - y - 2 * z
        p1, p2, p3, p4 = c - 2 * z, c + 2 * (x + y), c + x + 2 * y, c - y - z
        p5, p6, p7, p8 = c - 2 * y - 3 * z, c + 3 * x + 2 * y, c + 2 * x + 3 * y, c - 2 * (y + z)
        p9 = c + x + 3 * y
        # p1 -= y
        # p4 -= y
        # p5 -= y
        # p8 -= y
        # c -= (x+y)/3
        # v1, v4, v5 = p2 - z, p2, p7
        # v2, v3, v6, v7 = v1 + 3 * x, v4 + 3 * x, v5 + 3 * x, p6 + 3 * x

        p_list = p0, p7, c - 2 * x + 3 * z, c - 3 * x + 2 * z, p3, p4
        poly = Polygon(*p_list, stroke_width=2.4, stroke_color=BLUE, fill_color=BLUE, fill_opacity=1)
        poly_01 = Polygon(p6, p6+3*y, p7+3*y, p7, stroke_width=2.4, stroke_color=BLUE_D, fill_opacity=1, fill_color=BLUE_D, plot_depth=-2.9)
        poly_02 = Polygon(p7, p7+3*y, p9+3*y, p9, stroke_width=2.4, stroke_color=BLUE_C, fill_opacity=1, fill_color=BLUE_C, plot_depth=-2.95)
        poly_03 = Polygon(p2, p6, p7, p9, stroke_width=2.4, stroke_color=BLUE_B, fill_opacity=1, fill_color=BLUE_B, plot_depth=-3)
        dmob1, dmob2 = Dmob_RECT4(t1, side_offset=0.04),  Dmob_RECT4(t2, side_offset=0.04)
        polys = VGroup(poly.copy().rotate(TAU/3, about_point=c).set_color(BLUE_B), poly, poly.copy().rotate(-TAU/3, about_point=c).set_color(BLUE_D)).set_plot_depth(-1)
        dmob1.always_update(), dmob2.always_update()
        for n, p in zip(dmob1.nodes, [p1, p2, p3, p4]): n.move_to(p)
        for n, p in zip(dmob2.nodes, [p5, p6, p7, p8]): n.move_to(p)
        dmob1.stop_update(), dmob2.stop_update()

        vg_1 = VGroup(dmob1, dmob2)
        vg_2 = vg_1.copy()
        vg_2.rotate(TAU/3, about_point=c)
        vg_3 = vg_2.copy()
        vg_3.rotate(TAU/3, about_point=c)

        # vg_2[0].rotate(PI), vg_2[1].rotate(PI)
        vg_1[0].set_color('#EEEEEE'), vg_2[1].set_color('#EEEEEE')
        vg_2[0].set_color(WHITE), vg_3[1].set_color(WHITE)
        vg_3[0].set_color(GREY_B), vg_1[1].set_color(GREY_B)
        self.add(vg_1, vg_2, vg_3, polys)
        # self.add(poly_01, poly_02, poly_03)

        svg_path = 'E:\\GitHub\\manim\\my_manim_projects\\my_projects\\resource\\svg_files\\'

        good = SVGMobject(svg_path + 'good.svg', color=WHITE).scale(0.3).move_to(LEFT)
        coin = SVGMobject(svg_path + 'coin.svg', color=WHITE).scale(0.32)
        favo = SVGMobject(svg_path + 'favo.svg', color=WHITE).scale(0.32).move_to(RIGHT)
        aida = SVGMobject(svg_path + 'aida.svg', color=RED_D).scale(0.5).move_to(p9).shift(-x*0.3)
        aida[2].set_color(MY_BLACK), aida[3].set_color(WHITE)

        d_sl = DeformableVMobject(good, coin, favo, elem_range=[0.5*DOWN+1.5*LEFT, 0.5*UP+1.5*RIGHT], type='RECT')
        d_sl.always_update()
        for n, p in zip(d_sl.nodes, poly_01.get_vertices()): n.move_to(p)
        sl_1 = d_sl.get_result().set_color(GREY_B)
        for n, p in zip(d_sl.nodes, poly_02.get_vertices()): n.move_to(p)
        sl_2 = d_sl.get_result().set_color('#EEEEEE')

        sl_vg = VGroup(poly_03, poly_02, poly_01, sl_1, sl_2, plot_depth=-2).shift(z*2.5)

        #
        p10 = p9 + 3 * y
        poly_04 = Polygon(p10-z, p10+5*x-z, p10+5*x, p10, stroke_width=2.4, stroke_color=BLUE_B, fill_opacity=1, fill_color=BLUE_B, plot_depth=-3.9)
        poly_05 = Polygon(p10, p10+5*x, p10+5*x+y, p10+y, stroke_width=2.4, stroke_color=BLUE, fill_opacity=1, fill_color=BLUE, plot_depth=-3.9)
        poly_06 = Polygon(p10+5*x, p10+5*x-z, p10+6*x, p10+5*x+y, stroke_width=2.4, stroke_color=BLUE_D, fill_opacity=1, fill_color=BLUE_D, plot_depth=-3.9)
        t3 = TexMobject('\\textbf{NEXT}', color=MY_BLACK, background_stroke_width=0).set_height(0.4)
        t4 = TexMobject('\\textbf{VIDEO}', color=MY_BLACK, background_stroke_width=0).set_height(0.4)
        s1 = Square(stroke_width=0, fill_color=BLUE_B, fill_opacity=1)
        sq = VGroup(s1, s1.copy().scale(0.75).set_color(BLUE), s1.copy().scale(0.45))
        d_t3, d_t4, d_sq = Dmob_RECT4(t3, side_offset=0.04), Dmob_RECT4(t4, side_offset=0.04), Dmob_RECT4(sq, side_offset=0.5)
        d_t3.always_update(), d_t4.always_update(), d_sq.always_update()
        for n, p in zip(d_t3.nodes, [p10+x*1.2, p10+3.5*x, p10+3.5*x+y, p10+x*1.2+y]): n.move_to(p)
        for n, p in zip(d_t4.nodes, [p10-z+x*1.2, p10+4.1*x-z, p10+4.1*x, p10+x*1.2]): n.move_to(p)
        for n, p in zip(d_sq.nodes, [p10+4*x, p10+5*x, p10+5*x+y, p10+4*x+y]): n.move_to(p)
        d_t3.stop_update().set_color(MY_WHITE)
        d_t4.stop_update().set_color(WHITE)
        d_sq.stop_update()
        nv_vg = VGroup(poly_06, poly_05, poly_04, d_t3, d_t4, d_sq, plot_depth=-3)
        self.add(nv_vg)
        self.add(aida)
        self.wait(1.5)
        self.play(sl_vg.shift, -z * 2.5, run_time=1.5)
        color2 = average_color(RED_B, RED, PINK)
        color1 = average_color(RED_D, RED, PINK)

        self.play(AnimationGroup(*[ApplyMethod(s.set_color, color1) for s in sl_1], lag_ratio=0.33, rate_fun=there_and_back),
                  AnimationGroup(*[ApplyMethod(s.set_color, color2) for s in sl_2], lag_ratio=0.33, rate_fun=there_and_back), run_time=1.8)

        self.wait(3)

class Ending_02(Scene):

    CONFIG = {
        'camera_config': {
            'background_color': GREY_A,
        }
    }

    def construct(self):
        # TODO bg , emphasize anims
        # bg = Square(stroke_width=0, fill_color=[GREEN_B, YELLOW_B, YELLOW_A], fill_opacity=1, plot_depth=-200).scale([15/2, 9/2, 1])
        # bg.set_sheen_direction(UP * 1 + RIGHT * 0.25) #.set_opacity([1, 0.8, 0.3, 0])
        # self.add(bg)
        c2r = lambda c: complex_to_R3(c)

        s = 0.8
        c = LEFT * 3.5
        x, y, z = c2r(s * np.exp(1j * (-PI/6))), c2r(s * np.exp(1j * (PI/6))), c2r(s * np.exp(1j * (PI/2)))
        # x, y, z = c2r(s * np.exp(1j * (-PI/2))), c2r(s * np.exp(1j * (-PI/6))), c2r(s * np.exp(1j * (PI/6)))
        grid = VGroup(*[Square(stroke_width=1., stroke_color=WHITE).shift(2 * RIGHT*(i%25) + 2 * UP*int(i/25)) for i in range(625)])
        grid.scale(s/2).rotate(PI/4).set_plot_depth(-100).set_height(25 * s * 0.815, stretch=True)
        t1 = TexMobject('\\textbf{MANIM}', color=MY_BLACK, background_stroke_width=0).set_height(0.4)
        t2 = TexMobject('\\textbf{KINDERGARTEN}', color=MY_BLACK, background_stroke_width=0).set_height(0.4)
        t1.to_corner(UL, buff=1)
        t2.next_to(t1, DOWN, aligned_edge=LEFT, buff=0.25)

        p0 = c - y - 2 * z
        p1, p2, p3, p4 = c - 2 * z, c + 2 * (x + y), c + x + 2 * y, c - y - z
        p5, p6, p7, p8 = c - 2 * y - 3 * z, c + 3 * x + 2 * y, c + 2 * x + 3 * y, c - 2 * (y + z)
        p9 = c + x + 3 * y
        p0 -= y
        p1 -= y
        p4 -= y
        p5 -= y
        p8 -= y

        # p_list = p0, p7, c - 2 * x + 3 * z, c - 3 * x + 2 * z, p3, p4
        p_list = p0, p7, c - 3 * x + 3 * z, c - 4 * x + 2 * z, p3, p4
        c -= (x+y)/3
        grid.move_to(c+(x+y)*3)
        # self.add(grid)
        poly = Polygon(*p_list, stroke_width=2.4, stroke_color=BLUE, fill_color=BLUE, fill_opacity=1)
        poly_01 = Polygon(p6, p6+3*y, p7+3*y, p7, stroke_width=2.4, stroke_color=BLUE_D, fill_opacity=1, fill_color=BLUE_D, plot_depth=-2.9)
        poly_02 = Polygon(p7, p7+3*y, p9+3*y, p9, stroke_width=2.4, stroke_color=BLUE_C, fill_opacity=1, fill_color=BLUE_C, plot_depth=-2.95)
        poly_03 = Polygon(p2, p6, p7, p9, stroke_width=2.4, stroke_color=BLUE_B, fill_opacity=1, fill_color=BLUE_B, plot_depth=-3)
        dmob1, dmob2 = Dmob_RECT4(t1, side_offset=0.04),  Dmob_RECT4(t2, side_offset=0.04)
        polys = VGroup(poly.copy().rotate(TAU/3, about_point=c).set_color(BLUE_B), poly, poly.copy().rotate(-TAU/3, about_point=c).set_color(BLUE_D)).set_plot_depth(-1)
        dmob1.always_update(), dmob2.always_update()
        for n, p in zip(dmob1.nodes, [p1, p2, p3, p4]): n.move_to(p)
        for n, p in zip(dmob2.nodes, [p5, p6, p7, p8]): n.move_to(p)
        dmob1.stop_update(), dmob2.stop_update()

        vg_1 = VGroup(dmob1, dmob2)
        vg_2 = vg_1.copy()
        vg_2.rotate(TAU/3, about_point=c)
        vg_3 = vg_2.copy()
        vg_3.rotate(TAU/3, about_point=c)

        # vg_2[0].rotate(PI), vg_2[1].rotate(PI)
        vg_1[0].set_color('#EEEEEE'), vg_2[1].set_color('#EEEEEE')
        vg_2[0].set_color(WHITE), vg_3[1].set_color(WHITE)
        vg_3[0].set_color(GREY_B), vg_1[1].set_color(GREY_B)
        self.add(vg_1, vg_2, vg_3, polys)

        # self.add(poly_01, poly_02, poly_03)

        svg_path = 'E:\\GitHub\\manim\\my_manim_projects\\my_projects\\resource\\svg_files\\'

        good = SVGMobject(svg_path + 'good.svg', color=WHITE).scale(0.3).move_to(LEFT)
        coin = SVGMobject(svg_path + 'coin.svg', color=WHITE).scale(0.32)
        favo = SVGMobject(svg_path + 'favo.svg', color=WHITE).scale(0.32).move_to(RIGHT)
        aida = SVGMobject(svg_path + 'aida.svg', color=RED_D).scale(0.5).move_to(p9).shift(-x*0.3)
        aida[2].set_color(MY_BLACK), aida[3].set_color(WHITE)

        d_sl = DeformableVMobject(good, coin, favo, elem_range=[0.5*DOWN+1.5*LEFT, 0.5*UP+1.5*RIGHT], type='RECT')
        d_sl.always_update()
        for n, p in zip(d_sl.nodes, poly_01.get_vertices()): n.move_to(p)
        sl_1 = d_sl.get_result().set_color(GREY_B)
        for n, p in zip(d_sl.nodes, poly_02.get_vertices()): n.move_to(p)
        sl_2 = d_sl.get_result().set_color('#EEEEEE')

        # sl_vg = VGroup(poly_03, poly_02, poly_01, sl_1, sl_2, plot_depth=-2).shift(z*2.5)
        sl_vg = VGroup(poly_02, poly_01, sl_1, sl_2, plot_depth=-2).shift(z*2.5)
        #
        p10 = p9 + 3 * y
        poly_04 = Polygon(p10-z, p10+5*x-z, p10+5*x, p10, stroke_width=2.4, stroke_color=BLUE_B, fill_opacity=1, fill_color=BLUE_B, plot_depth=-3.9)
        poly_05 = Polygon(p10, p10+5*x, p10+5*x+y, p10+y, stroke_width=2.4, stroke_color=BLUE, fill_opacity=1, fill_color=BLUE, plot_depth=-3.9)
        poly_06 = Polygon(p10+5*x, p10+5*x-z, p10+6*x, p10+5*x+y, stroke_width=2.4, stroke_color=BLUE_D, fill_opacity=1, fill_color=BLUE_D, plot_depth=-3.9)
        t3 = TexMobject('\\textbf{NEXT}', color=MY_BLACK, background_stroke_width=0).set_height(0.4)
        t4 = TexMobject('\\textbf{VIDEO}', color=MY_BLACK, background_stroke_width=0).set_height(0.4)
        s1 = Square(stroke_width=0, fill_color=BLUE_B, fill_opacity=1)
        sq = VGroup(s1, s1.copy().scale(0.75).set_color(BLUE), s1.copy().scale(0.45))
        d_t3, d_t4, d_sq = Dmob_RECT4(t3, side_offset=0.04), Dmob_RECT4(t4, side_offset=0.04), Dmob_RECT4(sq, side_offset=0.5)
        d_t3.always_update(), d_t4.always_update(), d_sq.always_update()
        for n, p in zip(d_t3.nodes, [p10+x*1.2, p10+3.5*x, p10+3.5*x+y, p10+x*1.2+y]): n.move_to(p)
        for n, p in zip(d_t4.nodes, [p10-z+x*1.2, p10+4.1*x-z, p10+4.1*x, p10+x*1.2]): n.move_to(p)
        for n, p in zip(d_sq.nodes, [p10+4*x, p10+5*x, p10+5*x+y, p10+4*x+y]): n.move_to(p)
        d_t3.stop_update().set_color(MY_WHITE)
        d_t4.stop_update().set_color(WHITE)
        d_sq.stop_update()
        nv_vg = VGroup(poly_06, poly_05, poly_04, d_t3, d_t4, d_sq, plot_depth=-3)
        self.add(nv_vg, aida)


        sl_vg.shift(p0-sl_vg[1].get_vertices()[0])
        self.add(sl_vg)
        cover = VGroup(sl_vg[1].copy().set_stroke(width=0), sl_vg[2].copy()).set_plot_depth(10)
        self.add(cover)
        self.wait(1.5)

        self.play(sl_vg.shift, z * 0.99,  cover.shift, z * 0.99, run_time=0.8)
        self.wait(0.1)
        self.play(sl_vg.shift, -0.4 * z, cover.shift, -z * 0.4, rate_func=there_and_back, run_time=0.6)
        self.wait(1.5)
        self.remove(cover)
        self.play(sl_vg.shift, 5.01 * z, run_time=1.4)
        self.wait(0.5)
        self.play(sl_vg.shift, 7 * x, run_time=1.8)
        self.wait(0.1)
        color2 = average_color(RED_B, RED, PINK)
        color1 = average_color(RED_D, RED, PINK)

        self.play(AnimationGroup(*[ApplyMethod(s.set_color, color1) for s in sl_1], lag_ratio=0.33, rate_fun=there_and_back),
                  AnimationGroup(*[ApplyMethod(s.set_color, color2) for s in sl_2], lag_ratio=0.33, rate_fun=there_and_back), run_time=1.2)
        self.wait(0.8)
        aida_02 = aida.copy().shift(d_sq.get_center()-aida.get_bottom()-y*0.12)
        self.play(AnimationGroup(FadeOut(aida), FadeIn(aida_02), lag_ratio=0.25), run_time=1.8)
        self.wait(3)
