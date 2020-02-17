from manimlib.imports import *

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

        self.add(Arc(start_angle=Line(O, B).get_angle(), angle=theta, radius=self.radius/2,
                     stroke_width=100 * self.radius, color=self.color).set_stroke(opacity=self.opacity).move_arc_center_to(O))
        self.add(Arc(start_angle=Line(O, B).get_angle(), angle=theta, radius=self.radius,
                     stroke_width=self.stroke_width, color=self.color).move_arc_center_to(O))

class Unit_root(Scene):

    def construct(self):

        ## Create ComplexPlane ##
        cp_scale = 1.75
        cp = ComplexPlane().scale(cp_scale)
        cp.add_coordinates(0, 1, 2, 3, 4, 5, 6, 7, 8, -1, -2, -3, -4, -5)
        cp.add_coordinates(1j, 2j, 3j, -1j, -2j, -3j)

        ### about z^n ###
        color_dict = {'z': PINK, 'x': BLUE, 'y': YELLOW, 'i': RED, '\\cos': BLUE, '\\sin': YELLOW, '\\theta}': BLUE,
                      'r': PINK, 'e': GREEN, 'n': YELLOW, 'k': YELLOW, '\\omega': PINK, '\\pi': BLUE}
        complex_z = 0.9+0.6j
        vect_z = Arrow(cp.n2p(0), cp.n2p(complex_z), buff=0, color=ORANGE)
        dot_z = Dot(cp.n2p(complex_z), color=PINK)
        angle_z = Angle(cp.n2p(1), cp.n2p(0), cp.n2p(complex_z), radius=0.6, color=BLUE)

        ## 3 forms of complex num
        xy_form = TexMobject('z', '=', 'x', '+', 'y', 'i').set_color_by_tex_to_color_map(color_dict)
        cs_form = TexMobject('z', '=', 'r', '(', '\\cos{', '\\theta}', '+', 'i', '\\sin{', '\\theta}', ')').set_color_by_tex_to_color_map(color_dict)
        exp_form = TexMobject('z', '=', 'r', 'e^{', 'i', '\\theta}', color=WHITE).set_color_by_tex_to_color_map(color_dict).scale(1.2)
        exp_form[-1].set_color(BLUE)
        xy_form.next_to(dot_z, RIGHT * 0.6)
        cs_form.next_to(dot_z, RIGHT * 0.6)
        exp_form.next_to(dot_z, RIGHT * 0.6).shift(UP * 0.25)

        ## vgroup for z_i
        vect_group = VGroup(vect_z)
        dot_group = VGroup(dot_z)
        text_group = VGroup(exp_form)
        angle_group = VGroup(angle_z)
        line_group = VGroup(Line(cp.n2p(1), cp.n2p(complex_z), color=PINK))

        n = 10
        for i in range(n-1):
            zn_1 = complex_z ** (i+2-1)
            zn = complex_z ** (i+2)
            dot_i = Dot(cp.n2p(zn), color=PINK)
            vect_i = Arrow(cp.n2p(0), cp.n2p(zn), buff=0, color=ORANGE)
            text_i = TexMobject('z^{', '%d}' % (i+2), color=PINK).shift(cp.n2p(zn)/abs(zn) * (abs(zn) + 0.25))
            angle_i = Angle(cp.n2p(zn_1), cp.n2p(0), cp.n2p(zn), radius=0.6, color=BLUE)
            vect_group.add(vect_i)
            dot_group.add(dot_i)
            text_group.add(text_i)
            angle_group.add(angle_i)
            line_group.add(VGroup(Line(cp.n2p(zn_1), cp.n2p(zn), color=PINK)))

        ### conclusions from z^n =1 ###
        text_zn = TexMobject('z^', 'n', '=', 'r^', 'n', 'e^{', 'n', '\\theta', 'i}', '=', '1').set_color_by_tex_to_color_map(color_dict)
        text_zn[7].set_color(BLUE)
        text_zn.scale(1.2).to_corner(RIGHT * 3.25 + UP * 1.2)

        right_arrow = TexMobject('\\Rightarrow').next_to(text_zn, DOWN * 3.75).align_to(text_zn, LEFT)

        text_01 = TexMobject('r', '=', '1').set_color_by_tex_to_color_map(color_dict).next_to(right_arrow, RIGHT * 2.4).shift(UP * 0.5)
        text_02 = TexMobject('n', '\\theta', '=', '2', 'k', '\\pi').set_color_by_tex_to_color_map(color_dict).next_to(right_arrow, RIGHT * 2.4).shift(DOWN * 0.5)
        text_12 = VGroup(text_01, text_02)
        brace = Brace(text_12, LEFT)

        text_03 = TexMobject('\\therefore', '\\omega^', 'n', '=', '1', '\\text{的}', 'n', '\\text{个根为：}',)\
            .set_color_by_tex_to_color_map(color_dict).next_to(text_02, DOWN * 1.4).align_to(text_zn, LEFT)

        text_wi_01 = TexMobject('\\omega', '_k', '=', 'e^{', 'i', '{2', 'k', '\\pi', '\\over', 'n}}',
                              ).set_color_by_tex_to_color_map(color_dict)
        text_wi_01.next_to(text_03, DOWN * 1.5).align_to(text_zn, LEFT)
        text_wi_02 = TexMobject('=', '\\cos{', '2', 'k', '\\pi', '\\over', 'n}', '+', 'i', '\\sin{',
                             '2', 'k', '\\pi', '\\over', 'n}').set_color_by_tex_to_color_map(color_dict)
        text_wi_02.next_to(text_wi_01, DOWN * 1.5).align_to(text_zn, LEFT)
        text_wi_02[1:].scale(0.9)
        text_k = TexMobject('(', 'k', '=', '0', ',', '1', ',', '2', ',','\\cdots', ',', 'n-1', ')').set_color_by_tex_to_color_map(color_dict)
        text_k.scale(0.75).next_to(text_wi_02, DOWN * 1.5).align_to(text_zn, LEFT)

        ### display w_i in unit circle ###
        # moved to animation part 3 #

        ### animation part 1 ###

        self.play(ShowCreation(cp))
        self.wait(1)

        self.play(ShowCreation(vect_z))
        self.wait(0.5)
        self.play(ShowCreation(dot_z))
        self.play(Write(xy_form))
        self.wait(1)
        self.play(ReplacementTransform(xy_form, cs_form))
        self.wait(1)
        self.play(ReplacementTransform(cs_form, exp_form))
        self.wait()
        self.play(ShowCreation(angle_z))

        # self.add(vect_group, text_group, dot_group, angle_group, line_group)
        for i in range(1, n):
            self.play(ShowCreation(vect_group[i]), run_time=0.8)
            self.play(ShowCreation(dot_group[i]), run_time=0.4)
            self.play(Write(text_group[i]), run_time=0.6)
            self.wait(0.2)
            self.play(ShowCreation(angle_group[i]), run_time=0.6)
            self.wait(0.4)
        self.wait()
        for i in range(0, n):
            self.play(ShowCreation(line_group[i]), run_time=0.4)
            self.wait(0.1)
        self.wait()

        all_exist = VGroup(cp, vect_group, text_group, dot_group, angle_group, line_group)
        self.play(all_exist.shift, cp.n2p(-2), run_time=1.5)
        self.wait()

        ### part 2 ###
        text_bg = Polygon(cp.n2p(2.6+2.2j), cp.n2p(5.8+2.2j), cp.n2p(5.8-2.2j), cp.n2p(2.6-2.2j),
                          stroke_width=0, fill_color=BLACK, fill_opacity=0.75)
        self.play(FadeIn(text_bg), run_time=1.2)
        self.wait(0.5)
        self.play(TransformFromCopy(text_group, text_zn[0:9]), run_time=1.2)
        self.wait()
        self.play(Write(text_zn[9:11]))
        self.wait()
        self.play(Write(right_arrow))
        self.play(ShowCreation(brace))

        self.play(TransformFromCopy(text_zn[3:5], text_01))
        self.wait()

        self.play(TransformFromCopy(text_zn[6:8], text_02[0:2]))
        self.play(Write(text_02[2:6]))
        self.wait()

        self.play(Write(text_03), run_time=2)
        self.wait(0.5)
        self.play(Write(text_wi_01), run_time=2)
        self.wait()
        self.play(Write(text_wi_02), run_time=3)
        self.wait()
        self.play(Write(text_k), run_time=2)
        self.wait(2)

        ### part 3 ###
        unit_circle = Circle(radius=cp.n2p(1)[0], color=BLUE_B).move_to(cp.n2p(0))
        self.play(ShowCreation(unit_circle))
        self.wait(0.5)
        z_new = np.exp(1j * TAU/11)
        w_1 = TexMobject('\\omega', '_1', '=', 'e^{', 'i', '{2', '\\pi', '\\over', 'n}}',).scale(0.9)\
            .set_color_by_tex_to_color_map(color_dict).move_to(cp.n2p(0)).shift((cp.n2p(z_new)-cp.n2p(0))*1.2+RIGHT*1.2)
        dot_1 = Dot(cp.n2p(z_new), color=PINK)
        vect_1 = Arrow(cp.n2p(0), cp.n2p(z_new), buff=0, color=ORANGE)
        line_1 = Line(cp.n2p(1), cp.n2p(z_new), color=PINK)
        dot_0 = Dot(cp.n2p(1), color=PINK)
        vect_0 = Arrow(cp.n2p(0), cp.n2p(1), buff=0, color=ORANGE)
        w_0 = TexMobject('\\omega', '_0', color=PINK).scale(0.8).move_to(cp.n2p(1.2))
        self.play(ShowCreation(vect_0))
        self.play(ShowCreation(dot_0), Write(w_0))
        self.play(ReplacementTransform(vect_group[0], vect_1), run_time=0.3)
        self.play(ReplacementTransform(dot_group[0], dot_1), run_time=0.3)
        self.play(ReplacementTransform(text_group[0], w_1), run_time=0.3)
        self.play(ReplacementTransform(line_group[0], line_1), run_time=0.3)
        vect_new, dot_new, line_new, text_new = VGroup(vect_1), VGroup(dot_1), VGroup(line_1), VGroup(w_1)

        for i in range(1, n):
            zn_1 = z_new ** (i+1-1)
            zn = z_new ** (i+1)
            dot_i = Dot(cp.n2p(zn), color=PINK)
            vect_i = Arrow(cp.n2p(0), cp.n2p(zn), buff=0, color=ORANGE)
            text_i = TexMobject('\\omega_{', '%d}' % (i+1), color=PINK).scale(0.8).move_to(cp.n2p(0)).shift((cp.n2p(zn)-cp.n2p(0))/abs(zn) * (abs(zn) + 0.2))
            line_i = Line(cp.n2p(zn_1), cp.n2p(zn), color=PINK)
            angle_i = Angle(cp.n2p(zn_1), cp.n2p(0), cp.n2p(zn), radius=0.6, color=BLUE)
            vect_new.add(vect_i), dot_new.add(dot_i), line_new.add(line_i), text_new.add(text_i)
            # vect_group[i].become(vect_i)
            # self.wait(dt)
            self.play(ReplacementTransform(vect_group[i], vect_i), run_time=0.32-0.08*np.sqrt(i))
            self.play(ReplacementTransform(angle_group[i], angle_i), run_time=0.32-0.08*np.sqrt(i))
            self.play(ReplacementTransform(dot_group[i], dot_i), run_time=0.32-0.08*np.sqrt(i))
            self.play(ReplacementTransform(text_group[i], text_i), run_time=0.32-0.08*np.sqrt(i))
            self.play(ReplacementTransform(line_group[i], line_i), run_time=0.32-0.08*np.sqrt(i))

        angle_11 = Angle(cp.n2p(1), cp.n2p(0), cp.n2p(np.exp(-1j * TAU/11)), radius=0.6, color=BLUE)
        line_11 = Line(cp.n2p(np.exp(-1j * TAU/11)), cp.n2p(1), color=PINK)
        self.play(ShowCreation(angle_11))
        self.play(ShowCreation(line_11))
 
        self.wait(5)

class Rotate_vect(Scene):

    CONFIG = {
        'camera_config': {'background_color': WHITE}
    }

    def construct(self):

        ## Create ComplexPlane ##

        axis_config={
            "stroke_color": BLACK,
            "stroke_width": 2,
            "include_ticks": False,
            "include_tip": False,
            "line_to_number_buff": SMALL_BUFF,
            "label_direction": DR,
            "number_scale_val": 0.5,
        }

        cp_scale = 2.25
        cp = ComplexPlane(axis_config=axis_config).scale(cp_scale)
        cp.add_coordinates(0, 1, 2, 3, 4, 5, -1, -2, -3, -4, -5)
        cp.add_coordinates(1j, 2j, 3j, -1j, -2j, -3j)

        self.add(cp)
        arrow = Arrow(cp.n2p(0), cp.n2p(1), buff=0, color=ORANGE)
        self.play(ShowCreation(arrow))
        self.wait(4)

class Rotate_vect_3D(SpecialThreeDScene):

    CONFIG = {
        "default_angled_camera_position": {
            "phi": 75 * DEGREES,
            "theta": 10 * DEGREES,
            'gamma': 0.5 * DEGREES,
            "distance": 1000,
        },
        'camera_config': {'background_color': WHITE},
        "three_d_axes_config": {
            "num_axis_pieces": 1,
            "number_line_config": {
                'color': BLACK,
                "unit_size": 2,
                "tick_frequency": 1,
                "numbers_with_elongated_ticks": [0, 1, 2],
                "stroke_width": 2,
            }
        },
    }

    def construct(self):

        axis_config={
            "stroke_color": BLACK,
            "stroke_width": 2,
            "include_ticks": False,
            "include_tip": False,
            "line_to_number_buff": SMALL_BUFF,
            "label_direction": DR,
            "number_scale_val": 0.5,
        }
        axes_origin = OUT * 0.75
        axes_scale = 0.32
        axes = self.get_axes().scale(axes_scale).shift(axes_origin)
        self.set_camera_to_default_position()

        cp_scale = 2
        cp = ComplexPlane(axis_config=axis_config).scale(cp_scale*axes_scale)
        cp.add_coordinates(0, 1, 2, 3, 4, 5, 6, -1, -2, -3, -4, -5, -6)
        cp.add_coordinates(1j, 2j, 3j, -1j, -2j, -3j)
        cp.rotate(PI/2).rotate(PI/2, UP).shift(axes_origin)

        # self.add(axes)

        r_vect = Arrow(axes.c2p(0, 0, 0), axes.c2p(0, 1, 0), buff=0, color=RED).rotate(PI/2, UP)
        i_vect = Arrow(axes.c2p(0, 0, 0), axes.c2p(0, 1, 0), buff=0, color=YELLOW).rotate(PI/2, UP).rotate(PI/2, RIGHT, about_point=ORIGIN)

        r = axes.c2p(1, 0, 0)[0] - axes.c2p(0, 0, 0)[0]
        w = 2.5
        t_max = 4 / w * TAU

        unit_circle = Circle(radius=r, color=ORANGE).rotate(PI/2, UP).shift(axes_origin)

        curve_3d = ParametricFunction(lambda t: (np.cos(w * t) * UP + np.sin(w*t) * OUT) * r + t * RIGHT, color=RED,
                                      t_min=0, t_max=t_max, stroke_width=5).set_stroke(color=BLACK, opacity=0.8).shift(axes_origin)

        surface_func = lambda u, v: np.array([u, np.cos(w * u) * v * r, np.sin(w * u) * v * r])
        u_num = 80
        surface = ParametricSurface(surface_func, u_min=0, u_max=t_max, v_min=0.001, v_max=1., resolution=(u_num, 8),
                                    color=ORANGE, checkerboard_colors=None, stroke_color=BLACK, stroke_opacity=0.6,
                                    stroke_width=1.2, fill_color=BLUE, fill_opacity=0.4).shift(axes_origin)
        # surface.set_depth(2)
        # surface_02 = self.get_surface(axes, lambda u, v: np.array([u, np.cos(w * u) * v, np.sin(w * u) * v]),
        #                               u_min=0, u_max=t_max, v_min=0.001, v_max=1., resolution=(50, 10))
        colors = color_gradient([RED, BLUE], u_num)
        for face in surface:
            face.set_fill(colors[face.u_index], opacity=0.75)

        self.play(ShowCreation(cp))
        # self.play(ShowCreation(r_vect))
        # self.play(ShowCreation(i_vect))
        # self.play(ShowCreation(unit_circle))
        self.wait()
        self.play(ShowCreation(curve_3d))
        self.wait()
        self.play(ShowCreation(surface))

        self.wait(4)

class Rotate_outof_screen(SpecialThreeDScene):

    CONFIG = {
        "background_image": 'my_projects\\resource\\png_files\\screen_test.png',
        "default_angled_camera_position": {
            "phi": 80 * DEGREES,
            "theta": 10 * DEGREES,
            'gamma': 0.0 * DEGREES,
            "distance": 100,
        },
        'camera_config': {'background_color': WHITE},
        "three_d_axes_config": {
            "num_axis_pieces": 1,
            "number_line_config": {
                'color': BLACK,
                "unit_size": 2,
                "tick_frequency": 1,
                "numbers_with_elongated_ticks": [0, 1, 2],
                "stroke_width": 2,
            }
        },
    }

    def construct(self):

        axis_config={
            "stroke_color": BLACK,
            "stroke_width": 2,
            "include_ticks": False,
            "include_tip": False,
            "line_to_number_buff": SMALL_BUFF,
            "label_direction": DR,
            "number_scale_val": 0.5,
        }
        # self.camera.init_background()

        image_bg = ImageMobject(self.background_image)

        image_bg.rotate(PI/2).rotate(self.default_angled_camera_position['phi'], UP).rotate(self.default_angled_camera_position['theta'], OUT)
        image_bg.scale(4.2)
        self.add(image_bg)
        axes_origin = OUT * 0.75 + UP * 0.5
        axes_scale = 0.35
        axes = self.get_axes().scale(axes_scale).shift(axes_origin)
        self.set_camera_to_default_position()

        cp_scale = 2
        cp = ComplexPlane(axis_config=axis_config).scale(cp_scale*axes_scale)
        cp.add_coordinates(0, 1, 2, 3, 4, 5, 6, -1, -2, -3, -4, -5, -6)
        cp.add_coordinates(1j, 2j, 3j, -1j, -2j, -3j)
        cp.rotate(PI/2).rotate(PI/2, UP).shift(axes_origin)

        # self.add(axes)

        r_vect = Arrow(axes.c2p(0, 0, 0), axes.c2p(0, 1, 0), buff=0, color=RED).rotate(PI/2, UP)
        i_vect = Arrow(axes.c2p(0, 0, 0), axes.c2p(0, 1, 0), buff=0, color=YELLOW).rotate(PI/2, UP).rotate(PI/2, RIGHT, about_point=ORIGIN)

        r = axes.c2p(1, 0, 0)[0] - axes.c2p(0, 0, 0)[0]
        w = 2.5
        t_max = 4 / w * TAU

        # unit_circle = Circle(radius=r, color=ORANGE).rotate(PI/2, UP).shift(axes_origin)

        curve_3d = ParametricFunction(lambda t: (np.cos(w * t) * UP + np.sin(w*t) * OUT) * r + t * RIGHT, color=RED,
                                      t_min=0, t_max=t_max, stroke_width=5).set_stroke(color=ORANGE, opacity=0.8).shift(axes_origin)

        surface_func = lambda u, v: np.array([u, np.cos(w * u) * v * r, np.sin(w * u) * v * r])
        u_num = 80
        surface = ParametricSurface(surface_func, u_min=0, u_max=t_max, v_min=0.001, v_max=1., resolution=(u_num, 8),
                                    color=ORANGE, checkerboard_colors=None, stroke_color=BLACK, stroke_opacity=0.6,
                                    stroke_width=1.2, fill_color=BLUE, fill_opacity=0.4).shift(axes_origin)
        # surface.set_depth(2)
        # surface_02 = self.get_surface(axes, lambda u, v: np.array([u, np.cos(w * u) * v, np.sin(w * u) * v]),
        #                               u_min=0, u_max=t_max, v_min=0.001, v_max=1., resolution=(50, 10))
        colors = color_gradient([RED, BLUE], u_num)
        for face in surface:
            face.set_fill(colors[face.u_index], opacity=0.75)

        self.play(ShowCreation(cp))
        # self.play(ShowCreation(r_vect))
        # self.play(ShowCreation(i_vect))
        # self.play(ShowCreation(unit_circle))
        self.wait()
        self.play(ShowCreation(curve_3d))
        self.wait()
        self.play(ShowCreation(surface))

        self.wait(4)

class Part_1(Scene):

    CONFIG = {
        'camera_config': {'background_color': WHITE}
    }

    def construct(self):

        axis_config={
            "stroke_color": BLACK,
            "stroke_width": 2,
            "include_ticks": False,
            "include_tip": False,
            "line_to_number_buff": SMALL_BUFF,
            "label_direction": DR,
            "number_scale_val": 0.5,
            'decimal_number_config': {'color': BLACK},
        }

        cp_scale = 2.
        cp = ComplexPlane(axis_config=axis_config).scale(cp_scale)
        cp.add_coordinates(0, 1, 2, 3, 4, -1, -2, -3, -4)
        cp.add_coordinates(1j, 2j, 3j, -1j, -2j, -3j)

        c_num = 100
        c_list = [BLUE_D, BLUE, GREEN, ORANGE, RED_D]
        colors = color_gradient(c_list, c_num)
        color_bar = Line(cp.n2p(-2.), cp.n2p(2.), stroke_width=24).to_corner(UP * 1.75).set_color(c_list[::-1])
        c_line = Line(cp.n2p(-2.), cp.n2p(2.), stroke_width=4.5, stroke_color=BLACK).next_to(color_bar, DOWN * 0.5)
        w_tick = VGroup()
        for i in range(5):
            tick = Line(ORIGIN, UP * 0.12, color=BLACK, stroke_width=2.5).next_to(c_line, UP * 0.01).shift((i-2)*cp.n2p(1.))
            w_tick.add(tick)
        w_label_01 = TexMobject('-10', color=BLACK).scale(0.6).next_to(w_tick[0], DOWN * 0.4)
        w_label_02 = TexMobject('-1', color=BLACK).scale(0.6).next_to(w_tick[1], DOWN * 0.4)
        w_label_03 = TexMobject('0', color=BLACK).scale(0.6).next_to(w_tick[2], DOWN * 0.4)
        w_label_04 = TexMobject('1', color=BLACK).scale(0.6).next_to(w_tick[3], DOWN * 0.4)
        w_label_05 = TexMobject('10', color=BLACK).scale(0.6).next_to(w_tick[4], DOWN * 0.4)
        w_label = VGroup(w_label_01, w_label_02, w_label_03, w_label_04, w_label_05)
        w_axes = VGroup(w_tick, w_label)

        w_color = RED
        omega_text = TexMobject('\\omega', '=', color=BLACK, background_stroke_color=BLACK, background_stroke_width=2.5).scale(1.2).next_to(color_bar, RIGHT * 0.5)
        omega_text[0].set_color(w_color).set_background_stroke(color=w_color)
        omega_value = DecimalNumber(1.0, num_decimal_places=2, color=w_color).next_to(omega_text, RIGHT * 0.5).shift(UP * 0.025)
        omega_tracker = Triangle(color=RED, stroke_color=w_color, fill_color=w_color, fill_opacity=1).set_background_stroke(color=w_color).scale(0.2).rotate(PI).next_to(w_tick[3], UP * 0.5)

        omega_value.add_updater(lambda v: v.set_value(np.sign(cp.p2n(omega_tracker.get_center()).real - 0) * 10 ** (abs(cp.p2n(omega_tracker.get_center()).real)-1)))
        omega_tracker.add_updater(lambda t: t.set_color(colors[int((cp.p2n(t.get_center()).real + 2)/4*(c_num-1))]))
        self.add(cp)
        d_theta = 2.5*DEGREES
        arrow = Arrow(cp.n2p(0), cp.n2p(1), buff=0, color=RED)
        arrow.add_updater(lambda a, dt: a.rotate(d_theta * omega_value.get_value(), about_point=ORIGIN))
        dot = Dot(color=RED).scale(1.5).add_updater(lambda d: d.move_to(arrow.get_end()))
        circle = Circle(radius=cp.n2p(1)[0], color=YELLOW, stroke_width=8)

        color_dict = {'e': GREEN, 'i': PINK, 't': BLUE, '\\omega': RED, '=': BLACK, 'z': YELLOW}
        formula_01 = TexMobject('\\mathbf{z', '=', 'e^{', 'i', '\\omega', 't}}', background_stroke_color=WHITE).set_color_by_tex_to_color_map(color_dict).set_height(0.9)
        formula_01.move_to(cp.n2p(2+0.5j))

        self.play(FadeIn(color_bar), FadeIn(c_line), FadeIn(w_axes))
        self.play(Write(omega_text), ShowCreation(omega_value), ShowCreation(omega_tracker))
        self.wait(0.5)
        # self.play(omega_tracker.shift, cp.n2p(1), run_time=1)

        self.add(circle, arrow, dot)
        self.wait()
        self.play(Write(formula_01))
        self.wait(4)

        self.play(omega_tracker.shift, cp.n2p(0.5), run_time=2.5)
        self.wait(4)
        self.play(omega_tracker.shift, cp.n2p(0.5), run_time=2.5)
        self.wait(4)

        self.play(omega_tracker.shift, cp.n2p(-3), run_time=5)

        self.wait(10)

        self.play(FadeOut(circle), FadeOut(arrow), FadeOut(dot), FadeOut(formula_01), FadeOut(color_bar),
                  FadeOut(c_line), FadeOut(w_axes), FadeOut(omega_text), FadeOut(omega_value), FadeOut(omega_tracker), run_time=1.5)

        self.wait(2)

        self.play(FadeOut(cp), run_time=1.5)

        self.wait(2)

class Dot3d(VGroup):

    def __init__(self, loc=ORIGIN, size=0.2, color=WHITE, **kwargs):
        VGroup.__init__(self, **kwargs)
        dot_01 = Dot(loc, color=color).set_height(size)
        self.add(dot_01)
        num=8
        for i in range(1, num):
            dot_i = dot_01.copy().rotate(PI * i/num, axis=UP)
            self.add(dot_i)
        for i in range(1, num):
            dot_i = dot_01.copy().rotate(PI * i/num, axis=RIGHT)
            self.add(dot_i)

class Part_3(SpecialThreeDScene):

    CONFIG = {
    # "background_image": 'my_projects\\resource\\png_files\\screen_test.png',
    "default_angled_camera_position": {
        "phi": 56 * DEGREES,
        "theta": -56 * DEGREES,
        'gamma': 0.0 * DEGREES,
        "distance": 80,
        },
    'camera_config': {'background_color': WHITE},
    "three_d_axes_config": {
        "num_axis_pieces": 1,
        "number_line_config": {
            'color': BLACK,
            "unit_size": 2,
            "tick_frequency": 1,
            "numbers_with_elongated_ticks": [0, 1, 2],
            "stroke_width": 2,
            }
        },
    }

    def construct(self):

        axis_config={
            "stroke_color": BLACK,
            "stroke_width": 2,
            "include_ticks": False,
            "include_tip": False,
            "line_to_number_buff": SMALL_BUFF,
            "label_direction": DR,
            "number_scale_val": 0.5,
            'decimal_number_config': {'color': BLACK},
        }
        # self.camera.init_background()

        # image_bg = ImageMobject(self.background_image)
        #
        # image_bg.rotate(PI/2).rotate(self.default_angled_camera_position['phi'], UP).rotate(self.default_angled_camera_position['theta'], OUT)
        # image_bg.scale(4.2)
        # self.add(image_bg)
        axes_origin = DOWN * 1.6 + RIGHT * 1.6
        axes_scale = 1
        axes = self.get_axes().scale(axes_scale, about_point=ORIGIN).shift(axes_origin)

        self.set_camera_to_default_position()

        cp_scale = 2
        cp = ComplexPlane(axis_config=axis_config).scale(cp_scale*axes_scale, about_point=ORIGIN).shift(axes_origin)
        cp.add_coordinates(0, 1, 2, 3, 4, 5, 6, -1, -2, -3, -4, -5, -6)
        cp.add_coordinates(1j, 2j, 3j, 4j, -1j, -2j, -3j, -4j)

        ##
        arrow = Line(cp.n2p(0), cp.n2p(1), buff=0, color=ORANGE, stroke_width=8)
        dot = Dot3d(color=RED, size=0.25).add_updater(lambda d: d.move_to(arrow.get_end()))
        self.delta_t = 0 * 1/60
        self.w = 0
        # arrow.add_updater(lambda a, dt: a.shift((axes.c2p(0,0,0) - a.get_start()) * np.array([1,1,0])).rotate(self.w, axis=OUT, about_point=a.get_start()).shift((axes.c2p(0, 0, 1)-axes.c2p(0,0,0)) * self.delta_t))
        arrow.add_updater(lambda a, dt: a.rotate(self.w, axis=OUT, about_point=a.get_start()).shift((axes.c2p(0, 0, 1)-axes.c2p(0,0,0)) * self.delta_t))

        line_group = VGroup()
        self.t_num = 0
        def update_line(g):
            self.t_num+=1*int(np.sign(self.w)%2)
            if self.t_num%10 == 0:
                g.add(Line(arrow.get_start(), arrow.get_end(), stroke_width=2, stroke_color=ORANGE))

        curve_3d = VGroup()
        self.p_old = dot.get_center()
        def update_curve(g):
            if not self.w == 0:
                p_new = dot.get_center()
                g.add(Line(self.p_old, p_new, stroke_width=5, stroke_color=ORANGE))
                self.p_old = p_new
        curve_3d.add_updater(update_curve)

        line_group.add_updater(update_line)
        r = axes.c2p(1,0,0)[0]-cp.c2p(0,0,0)[0]
        w=1
        surface_func = lambda u, v: np.array([np.cos(w * u) * v * r, np.sin(w * u) * v * r, u * w / PI * 2])
        u_num = 480/10
        surface = ParametricSurface(surface_func, u_min=0, u_max=2*PI, v_min=0.001, v_max=1., resolution=(u_num, 8),
                                    color=ORANGE, checkerboard_colors=None, stroke_color=ORANGE, stroke_opacity=0.6,
                                    stroke_width=1.5, fill_color=BLUE, fill_opacity=0.25).shift(axes_origin)

        self.add(axes)
        self.play(ShowCreation(cp), run_time=1.2)
        self.wait()
        self.play(ShowCreation(arrow), FadeIn(dot))
        self.wait(1)
        self.add(line_group, curve_3d)
        self.start_rotate()
        self.wait(8)
        self.stop_rotate()
        self.wait()
        self.play(ReplacementTransform(line_group, surface), run_time=2.5)
        self.wait(4)

    def start_rotate(self, delta_t=1/120/2, w=TAU/240/2):
        self.delta_t = delta_t
        self.w = w

    def stop_rotate(self):
        self.delta_t = 0 * 1/60
        self.w = 0

class Part_4(SpecialThreeDScene):

    CONFIG = {
    # "background_image": 'my_projects\\resource\\png_files\\screen_test.png',
    "default_angled_camera_position": {
        "phi": 66 * DEGREES,
        "theta": -60 * DEGREES,
        'gamma': 0.0 * DEGREES,
        "distance": 50,
        },
    'camera_config': {'background_color': WHITE},
    "three_d_axes_config": {
        "num_axis_pieces": 1,
        "number_line_config": {
            'color': BLACK,
            "unit_size": 2,
            "tick_frequency": 1,
            "numbers_with_elongated_ticks": [0, 1, 2],
            "stroke_width": 2,
            }
        },
    }

    def construct(self):

        axis_config={
            "stroke_color": BLACK,
            "stroke_width": 2,
            "include_ticks": False,
            "include_tip": False,
            "line_to_number_buff": SMALL_BUFF,
            "label_direction": DR,
            "number_scale_val": 0.5,
            'decimal_number_config': {'color': BLACK},
        }

        axes_origin = ORIGIN
        axes_scale = 1.2
        axes = self.get_axes().scale(axes_scale, about_point=ORIGIN).shift(axes_origin)

        self.set_camera_to_default_position()

        cp_scale = 2
        cp = ComplexPlane(axis_config=axis_config).scale(cp_scale*axes_scale, about_point=ORIGIN).shift(axes_origin)
        cp.add_coordinates(0, 1, 2, 3, 4, 5, 6, -1, -2, -3, -4, -5, -6)
        cp.add_coordinates(1j, 2j, 3j, 4j, -1j, -2j, -3j, -4j)

        ##
        l = axes_scale

        r = cp.n2p(1)[0]/2

        circle = Circle(radius=r).rotate(PI/2, UP).shift(axes.c2p(-2, 0, 0))
        line_r = Line(circle.get_center(), circle.get_center() + UP * r, color=ORANGE, stroke_width=6)
        dot = Dot3d(color=RED, size=0.18).add_updater(lambda d: d.move_to(line_r.get_end()))

        cube = Cube(color=BLUE, fill_opacity=0.0, stroke_width=4, stroke_color=BLUE_D).scale(np.array([l * 4, l, l]))

        w = TAU/2
        curve_3d = ParametricFunction(lambda t: np.array([t*r, r * np.cos(w * t), r * np.sin(w * t)]), t_min=-0.0001, t_max=8,
                                      color=ORANGE, stroke_width=4).shift(cp.n2p(-2))

        curve_3d.add_updater(lambda c: c.become(ParametricFunction(lambda t: np.array([t*r, r * np.cos(w * t), r * np.sin(w * t)]),
                                                                   t_min=-0.00001, t_max=(cp.p2n(circle.get_center()).real+2)*2,
                                                                   color=ORANGE, stroke_width=4).shift(cp.n2p(-2))))
        # line_r.add_updater(lambda l: l.put_start_and_end_on(circle.get_center(), circle.get_center() +
        #                                                     UP * r * np.cos((cp.p2n(circle.get_center()).real+2)*2*w) +
        #                                                     OUT * (-r) * np.sin((cp.p2n(circle.get_center()).real+2)*2*w)))
        line_r.add_updater(lambda l: l.become(Line(circle.get_center(), circle.get_center() +
                                                   UP * r * np.cos((cp.p2n(circle.get_center()).real+2)*2*w) +
                                                   OUT * r * np.sin((cp.p2n(circle.get_center()).real+2)*2*w),
                                                   color=ORANGE, stroke_width=6)))

        cos_t = ParametricFunction(lambda t: np.array([t*r, r * np.cos(w * t), 0]), t_min=-0.0001, t_max=8,
                                      color=GREEN, stroke_width=4).shift(axes.c2p(-2, 0, 0)).shift(OUT*r*(1+1.45))
        sin_t = ParametricFunction(lambda t: np.array([t*r, 0, r * np.sin(w * t)]), t_min=-0.0001, t_max=8,
                                      color=PINK, stroke_width=4).shift(axes.c2p(-2, 0, 0)).shift(DOWN*r*(1+2))

        cube_g = VGroup()
        A = axes.c2p(-2, -0.5, 0.5)
        B = axes.c2p(-2, 0.5, 0.5)
        C = axes.c2p(-2, 0.5, -0.5)
        D = axes.c2p(-2, -0.5, -0.5)
        E = axes.c2p(2, -0.5, 0.5)
        F = axes.c2p(2, 0.5, 0.5)
        G = axes.c2p(2, 0.5, -0.5)
        H = axes.c2p(2, -0.5, -0.5)
        line_color = BLUE
        s_width = 2

        AB = Line(A, B, color=line_color, stroke_width=s_width)
        BC = DashedLine(C, B, color=line_color, stroke_width=s_width)
        CD = DashedLine(C, D, color=line_color, stroke_width=s_width)
        DA = Line(A, D, color=line_color, stroke_width=s_width)

        AE = Line(A, E, color=line_color, stroke_width=s_width)
        BF = Line(F, B, color=line_color, stroke_width=s_width)
        CG = DashedLine(C, G, color=line_color, stroke_width=s_width)
        DH = Line(H, D, color=line_color, stroke_width=s_width)

        EF = Line(E, F, color=line_color, stroke_width=s_width)
        FG = Line(F, G, color=line_color, stroke_width=s_width)
        GH = Line(G, H, color=line_color, stroke_width=s_width)
        HE = Line(H, E, color=line_color, stroke_width=s_width)

        cube_g.add(AB, BC, CD, DA, AE, BF, CG, DH, EF, FG, GH, HE)

        y_dash = VGroup(DashedLine((A+D)/2, (E+H)/2, color=line_color, stroke_width=s_width*0.75))
        for i in range(1, 16):
            y_dash.add(DashedLine(A + i * (E-A)/16, D + i * (E-A)/16, color=line_color, stroke_width=s_width*0.75))
        yt = VGroup(DA.copy(), AE.copy(), HE.copy(), DH.copy(), y_dash)

        x_dash = VGroup(DashedLine((A+B)/2, (E+F)/2, color=line_color, stroke_width=s_width*0.75))
        for i in range(1, 16):
            x_dash.add(DashedLine(A + i * (E-A)/16, B + i * (E-A)/16, color=line_color, stroke_width=s_width*0.75))
        xt = VGroup(AB.copy(), BF.copy(), EF.copy(), AE.copy(), x_dash)

        color_dict = {'e': GREEN, 'i': YELLOW_D, 't': BLUE, '\\omega': RED, '\\varphi': ORANGE, '\\sin': PINK, '\\cos': GREEN}

        text_eiwt = TexMobject('\\mathbf{e^{', 'i', '(', '\\omega', 't', '+', '\\varphi', ')}}', background_stroke_color=WHITE, color=BLACK).set_color_by_tex_to_color_map(color_dict)
        text_sint = TexMobject('\\mathbf{\\sin{', '(', '\\omega', 't', '+', '\\varphi', ')}}', background_stroke_color=WHITE, color=BLACK).set_color_by_tex_to_color_map(color_dict)
        text_cost = TexMobject('\\mathbf{\\cos{', '(', '\\omega', 't', '+', '\\varphi', ')}}', background_stroke_color=WHITE, color=BLACK).set_color_by_tex_to_color_map(color_dict)
        text_eiwt.scale(1.25).rotate(PI/2, RIGHT).shift(axes.c2p(2.75, 0, 0)).shift(OUT*0.4 + LEFT * 0.2)
        text_sint.scale(1.25).rotate(PI/2, RIGHT).shift(axes.c2p(2.75, 0, 0)).shift(DOWN*r*(1+2))
        text_cost.scale(1.2).rotate(PI/2, RIGHT).shift(axes.c2p(2.75, 0, 0)).shift(OUT*r*(1+1.45)+LEFT*0.75*r+DOWN*0.4*r)

        navi_cube = Cube(stroke_color=ORANGE, stroke_width=0.6, fill_color=ORANGE, fill_opacity=0.2).scale(0.1)
        l_cube = navi_cube.get_height()
        navi_cube.shift(l_cube/2)
        l_x = Line(ORIGIN, l_cube * UP * 4, color=GREEN)
        l_y = Line(ORIGIN, l_cube * OUT * 4, color=PINK)
        l_t = Line(ORIGIN, l_cube * RIGHT * 4, color=ORANGE)
        tex_x = TexMobject('x', background_stroke_color=WHITE, color=GREEN).rotate(PI/2, RIGHT).next_to(l_x, UP*1.25)
        tex_y = TexMobject('y', background_stroke_color=WHITE, color=PINK).rotate(PI/2, RIGHT).next_to(l_y, OUT*0.5)
        tex_t = TexMobject('t', background_stroke_color=WHITE, color=ORANGE).rotate(PI/2, RIGHT).next_to(l_t, RIGHT*0.5)
        navi_group = VGroup(l_x, l_y, l_t, tex_x, tex_y, tex_t, navi_cube).move_to(cp.n2p(-0.6-3.2j))

        ## rotate update ##
        # rotate_group_old = VGroup(curve_3d, line_r, dot)
        # rotate_group = rotate_group_old.deepcopy()
        # def rotate_all(r):
        #     r.rotate(2*DEGREES, RIGHT, about_point=ORIGIN)
        # cos_t.add_updater(lambda c: c.become(ParametricFunction(lambda t: np.array([t*r, r * np.cos(w * t + rotate_group[1].get_angle()), 0]), t_min=-0.0001, t_max=8,
        #                               color=GREEN, stroke_width=4).shift(axes.c2p(-2, 0, 0)).shift(OUT*r*(1+1.45))))
        # sin_t.add_updater(lambda s: s.become(ParametricFunction(lambda t: np.array([t*r, 0, r * np.sin(w * t + rotate_group[1].get_angle())]), t_min=-0.0001, t_max=8,
        #                               color=PINK, stroke_width=4).shift(axes.c2p(-2, 0, 0)).shift(DOWN*r*(1+2))))

        ## animation ##

        # self.add(cp, axes)

        self.add(curve_3d, cube_g, circle, line_r, dot, navi_group)
        self.wait()

        # circle.shift(axes.c2p(4, 0, 0))
        self.play(circle.shift, axes.c2p(4, 0, 0), run_time=6)
        self.play(Write(text_eiwt), run_time=1.5)
        self.wait()
        self.play(yt.shift, DOWN*r*2, run_time=1.5)
        self.wait(0.5)
        self.play(TransformFromCopy(curve_3d, sin_t), run_time=2)
        self.wait(0.4)
        self.play(Write(text_sint), run_time=1.5)
        self.wait()
        self.play(xt.shift, OUT*r*1.45, run_time=1.5)
        self.wait(0.5)
        self.play(TransformFromCopy(curve_3d, cos_t), run_time=2)
        self.wait(0.4)
        self.play(Write(text_cost), run_time=1.5)
        self.wait(4)

class Part_4_2(SpecialThreeDScene):

    CONFIG = {
    # "background_image": 'my_projects\\resource\\png_files\\screen_test.png',
    "default_angled_camera_position": {
        "phi": 66 * DEGREES,
        "theta": -60 * DEGREES,
        'gamma': 0.0 * DEGREES,
        "distance": 50,
        },
    'camera_config': {'background_color': WHITE},
    "three_d_axes_config": {
        "num_axis_pieces": 1,
        "number_line_config": {
            'color': BLACK,
            "unit_size": 2,
            "tick_frequency": 1,
            "numbers_with_elongated_ticks": [0, 1, 2],
            "stroke_width": 2,
            }
        },
    }

    def construct(self):

        axis_config={
            "stroke_color": BLACK,
            "stroke_width": 2,
            "include_ticks": False,
            "include_tip": False,
            "line_to_number_buff": SMALL_BUFF,
            "label_direction": DR,
            "number_scale_val": 0.5,
            'decimal_number_config': {'color': BLACK},
        }

        axes_origin = ORIGIN
        axes_scale = 1.2
        axes = self.get_axes().scale(axes_scale, about_point=ORIGIN).shift(axes_origin)

        self.set_camera_to_default_position()

        cp_scale = 2
        cp = ComplexPlane(axis_config=axis_config).scale(cp_scale*axes_scale, about_point=ORIGIN).shift(axes_origin)
        cp.add_coordinates(0, 1, 2, 3, 4, 5, 6, -1, -2, -3, -4, -5, -6)
        cp.add_coordinates(1j, 2j, 3j, 4j, -1j, -2j, -3j, -4j)

        ##
        l = axes_scale

        r = cp.n2p(1)[0]/2

        circle = Circle(radius=r).rotate(PI/2, UP).shift(axes.c2p(-2, 0, 0))
        line_r = Line(circle.get_center(), circle.get_center() + UP * r, color=ORANGE, stroke_width=6).shift(r*8*RIGHT)
        dot = Dot3d(color=RED, size=0.18).add_updater(lambda d: d.move_to(line_r.get_end()))

        cube = Cube(color=BLUE, fill_opacity=0.0, stroke_width=4, stroke_color=BLUE_D).scale(np.array([l * 4, l, l]))

        w = TAU/2
        curve_3d = ParametricFunction(lambda t: np.array([t*r, r * np.cos(w * t), r * np.sin(w * t)]), t_min=0, t_max=8,
                                      color=ORANGE, stroke_width=4).shift(cp.n2p(-2))
        self.cos_t = ParametricFunction(lambda t: np.array([t*r, r * np.cos(w * t), 0]), t_min=0, t_max=8,
                                      color=GREEN, stroke_width=4).shift(axes.c2p(-2, 0, 0)).shift(OUT*r*(1+1.45))
        self.sin_t = ParametricFunction(lambda t: np.array([t*r, 0, r * np.sin(w * t)]), t_min=0, t_max=8,
                                      color=PINK, stroke_width=4).shift(axes.c2p(-2, 0, 0)).shift(DOWN*r*(1+2))

        cube_g = VGroup()
        A = axes.c2p(-2, -0.5, 0.5)
        B = axes.c2p(-2, 0.5, 0.5)
        C = axes.c2p(-2, 0.5, -0.5)
        D = axes.c2p(-2, -0.5, -0.5)
        E = axes.c2p(2, -0.5, 0.5)
        F = axes.c2p(2, 0.5, 0.5)
        G = axes.c2p(2, 0.5, -0.5)
        H = axes.c2p(2, -0.5, -0.5)
        line_color = BLUE
        s_width = 2

        AB = Line(A, B, color=line_color, stroke_width=s_width)
        BC = DashedLine(C, B, color=line_color, stroke_width=s_width)
        CD = DashedLine(C, D, color=line_color, stroke_width=s_width)
        DA = Line(A, D, color=line_color, stroke_width=s_width)

        AE = Line(A, E, color=line_color, stroke_width=s_width)
        BF = Line(F, B, color=line_color, stroke_width=s_width)
        CG = DashedLine(C, G, color=line_color, stroke_width=s_width)
        DH = Line(H, D, color=line_color, stroke_width=s_width)

        EF = Line(E, F, color=line_color, stroke_width=s_width)
        FG = Line(F, G, color=line_color, stroke_width=s_width)
        GH = Line(G, H, color=line_color, stroke_width=s_width)
        HE = Line(H, E, color=line_color, stroke_width=s_width)

        cube_g.add(AB, BC, CD, DA, AE, BF, CG, DH, EF, FG, GH, HE)

        y_dash = VGroup(DashedLine((A+D)/2, (E+H)/2, color=line_color, stroke_width=s_width*0.75))
        for i in range(1, 16):
            y_dash.add(DashedLine(A + i * (E-A)/16, D + i * (E-A)/16, color=line_color, stroke_width=s_width*0.75))
        yt = VGroup(DA.copy(), AE.copy(), HE.copy(), DH.copy(), y_dash)

        x_dash = VGroup(DashedLine((A+B)/2, (E+F)/2, color=line_color, stroke_width=s_width*0.75))
        for i in range(1, 16):
            x_dash.add(DashedLine(A + i * (E-A)/16, B + i * (E-A)/16, color=line_color, stroke_width=s_width*0.75))
        xt = VGroup(AB.copy(), BF.copy(), EF.copy(), AE.copy(), x_dash)

        color_dict = {'e': GREEN, 'i': YELLOW_D, 't': BLUE, '\\omega': RED, '\\varphi': ORANGE, '\\sin': PINK, '\\cos': GREEN}

        text_eiwt = TexMobject('\\mathbf{e^{', 'i', '(', '\\omega', 't', '+', '\\varphi', ')}}', background_stroke_color=WHITE, color=BLACK).set_color_by_tex_to_color_map(color_dict)
        text_sint = TexMobject('\\mathbf{\\sin{', '(', '\\omega', 't', '+', '\\varphi', ')}}', background_stroke_color=WHITE, color=BLACK).set_color_by_tex_to_color_map(color_dict)
        text_cost = TexMobject('\\mathbf{\\cos{', '(', '\\omega', 't', '+', '\\varphi', ')}}', background_stroke_color=WHITE, color=BLACK).set_color_by_tex_to_color_map(color_dict)
        text_eiwt.scale(1.25).rotate(PI/2, RIGHT).shift(axes.c2p(2.75, 0, 0)).shift(OUT*0.4 + LEFT * 0.2)
        text_sint.scale(1.25).rotate(PI/2, RIGHT).shift(axes.c2p(2.75, 0, 0)).shift(DOWN*r*(1+2))
        text_cost.scale(1.2).rotate(PI/2, RIGHT).shift(axes.c2p(2.75, 0, 0)).shift(OUT*r*(1+1.45)+LEFT*0.75*r+DOWN*0.4*r)

        navi_cube = Cube(stroke_color=ORANGE, stroke_width=0.6, fill_color=ORANGE, fill_opacity=0.2).scale(0.1)
        l_cube = navi_cube.get_height()
        navi_cube.shift(l_cube/2)
        l_x = Line(ORIGIN, l_cube * UP * 4, color=GREEN)
        l_y = Line(ORIGIN, l_cube * OUT * 4, color=PINK)
        l_t = Line(ORIGIN, l_cube * RIGHT * 4, color=ORANGE)
        tex_x = TexMobject('x', background_stroke_color=WHITE, color=GREEN).rotate(PI/2, RIGHT).next_to(l_x, UP*1.25)
        tex_y = TexMobject('y', background_stroke_color=WHITE, color=PINK).rotate(PI/2, RIGHT).next_to(l_y, OUT*0.5)
        tex_t = TexMobject('t', background_stroke_color=WHITE, color=ORANGE).rotate(PI/2, RIGHT).next_to(l_t, RIGHT*0.5)
        navi_group = VGroup(l_x, l_y, l_t, tex_x, tex_y, tex_t, navi_cube).move_to(cp.n2p(-0.6-3.2j))

        ## rotate update ##
        rotate_group = VGroup(curve_3d, line_r, dot)
        self.varphi = 0
        def rotate_all(r, dt):
            r.rotate(2.5*DEGREES, RIGHT, about_point=ORIGIN)
            self.varphi += 2.5*DEGREES
            # self.cos_t.become(ParametricFunction(lambda t: np.array([t * r, r * np.cos(w * t + self.varphi), 0]), t_min=0, t_max=8,
            #                            color=GREEN, stroke_width=4)).shift(axes.c2p(-2, 0, 0)).shift(OUT*r*(1+1.45))
            # self.sin_t.become(ParametricFunction(lambda t: np.array([t * r, 0, r * np.sin(w * t + self.varphi)]), t_min=0, t_max=8,
            #                            color=PINK, stroke_width=4)).shift(axes.c2p(-2, 0, 0)).shift(DOWN*r*(1+2))
        self.cos_t.add_updater(lambda c: c.become(ParametricFunction(lambda t: np.array([t*r, r * np.cos(w * t + self.varphi), 0]), t_min=-0.0001, t_max=8,
                                      color=GREEN, stroke_width=4).shift(axes.c2p(-2, 0, 0)).shift(OUT*r*(1+1.45))))
        self.sin_t.add_updater(lambda s: s.become(ParametricFunction(lambda t: np.array([t*r, 0, r * np.sin(w * t + self.varphi)]), t_min=-0.0001, t_max=8,
                                      color=PINK, stroke_width=4).shift(axes.c2p(-2, 0, 0)).shift(DOWN*r*(1+2))))

        ## animation ##

        # self.add(cp, axes)
        circle.shift(axes.c2p(4, 0, 0))
        self.add(curve_3d, cube_g, circle, line_r, dot, navi_group, yt, xt, self.sin_t, self.cos_t, text_sint, text_cost, text_eiwt)
        yt.shift(DOWN*r*2)
        xt.shift(OUT*r*1.45)
        self.wait()
        self.add(rotate_group)
        rotate_group.add_updater(rotate_all)
        self.wait(15)

class Part_5(SpecialThreeDScene):

    CONFIG = {
    # "background_image": 'my_projects\\resource\\png_files\\screen_test.png',
    "default_angled_camera_position": {
        "phi": 66 * DEGREES,
        "theta": -60 * DEGREES,
        'gamma': 0.0 * DEGREES,
        "distance": 50,
        },
    'camera_config': {'background_color': WHITE},
    "three_d_axes_config": {
        "num_axis_pieces": 1,
        "number_line_config": {
            'color': BLACK,
            "unit_size": 2,
            "tick_frequency": 1,
            "numbers_with_elongated_ticks": [0, 1, 2],
            "stroke_width": 2,
            }
        },
    }
    def construct(self):

        axis_config = {
            "stroke_color": BLACK,
            "stroke_width": 2,
            "include_ticks": False,
            "include_tip": False,
            "line_to_number_buff": SMALL_BUFF,
            "label_direction": DR,
            "number_scale_val": 0.5,
            'decimal_number_config': {'color': BLACK},
        }

        axes_origin = DOWN * 2.4 + RIGHT * 1.8
        axes_scale = 0.8
        axes = self.get_axes().scale(axes_scale, about_point=ORIGIN).shift(axes_origin)

        self.set_camera_to_default_position()

        cp_scale = 4
        cp = ComplexPlane(axis_config=axis_config).scale(cp_scale*axes_scale, about_point=ORIGIN).shift(axes_origin)
        cp.add_coordinates(0, 1, 2, 3, 4, 5, 6, -1, -2, -3, -4, -5, -6)
        cp.add_coordinates(1j, 2j, 3j, 4j, -1j, -2j, -3j, -4j)

        r = cp.n2p(1)[0]-cp.n2p(0)[0]

        self.w=1
        surface_func = lambda u, v: np.array([np.cos(self.w * u) * v * r, np.sin(self.w * u) * v * r, u / PI * r/2])
        u_num = 80
        surface = ParametricSurface(surface_func, u_min=0, u_max=2*PI, v_min=0.001, v_max=1., resolution=(u_num, 8),
                                    color=ORANGE, checkerboard_colors=None, stroke_color=ORANGE, stroke_opacity=0.6,
                                    stroke_width=1.5, fill_color=BLUE, fill_opacity=0.25).shift(axes_origin)
        curve_3d = ParametricFunction(lambda t: np.array([np.cos(self.w * t) * r, np.sin(self.w * t) * r, t / PI * r/2]), t_min=0, t_max=2*PI,
                                      color=RED, stroke_width=8).shift(axes_origin)
        surface.add_updater(lambda s: s.become(ParametricSurface(surface_func, u_min=0, u_max=2*PI, v_min=0.001, v_max=1., resolution=(u_num, 10),
                                    color=ORANGE, checkerboard_colors=None, stroke_color=ORANGE, stroke_opacity=0.6,
                                    stroke_width=1.5, fill_color=BLUE, fill_opacity=0.25).shift(axes_origin)))
        curve_3d.add_updater(lambda c: c.become(ParametricFunction(lambda t: np.array([np.cos(self.w * t) * r, np.sin(self.w * t) * r, t / PI * r/2]), t_min=0, t_max=2*PI,
                                      color=RED, stroke_width=8).shift(axes_origin)))

        surface_group = VGroup(curve_3d, surface)


        text_pi2 = TexMobject('2\\pi', color=BLACK).set_height(0.2).rotate(PI/2, RIGHT).shift(axes.c2p(-0.2, 0, 2))
        text_pi = TexMobject('\\pi', color=BLACK).set_height(0.2).rotate(PI/2, RIGHT).shift(axes.c2p(-0.2, 0, 1))
        color_dict = {'e': GREEN, 'i': YELLOW_D, 't': BLUE, '\\omega': RED, '\\varphi': ORANGE, '\\sin': PINK, '\\cos': GREEN}
        text_eiwt = TexMobject('\\mathbf{e^{', 'i', '\\omega', 't}}', background_stroke_color=BLACK, color=BLACK, background_stroke_width=2.5).set_color_by_tex_to_color_map(color_dict)
        text_eiwt.scale(2).shift(axes.c2p(1.2, -0.4, 0))

        text_w = TexMobject('w', '=', background_stroke_color=BLACK, color=RED)
        w_value = DecimalNumber(1.0, num_decimal_places=2, color=RED).next_to(text_w, RIGHT * 0.4).shift(UP * 0.05)
        w_value.add_updater(lambda w: w.set_value(self.w))
        w_label = VGroup(w_value, text_w).scale(1.5).next_to(text_eiwt, DOWN * 2).align_to(text_eiwt, LEFT)

        self.add(axes, cp, text_pi, text_pi2, text_eiwt, w_label)

        self.add(surface_group)
        # self.wait(0.4)

        # self.add(text_eiwt, w_label)
        # self.play(Write(text_eiwt), ShowCreation(w_label))
        f_num=60
        self.wait()
        for i in range(3*f_num):
            self.w += +1 / (f_num)
            self.wait(1/f_num)
        self.wait()
        for i in range(6*f_num):
            self.w += -0.5 / (f_num)
            self.wait(1/f_num)
        self.wait()
        for i in range(2*f_num):
            self.w += -0.5 / (f_num)
            self.wait(1/f_num)
        self.wait()
        for i in range(5*f_num):
            self.w += -0.4 / (f_num)
            self.wait(1/f_num)
        self.wait(4)

class Part_6(Scene):

    CONFIG = {
        'camera_config': {'background_color': WHITE},
    }

    def construct(self):

        color_dict = {'i': RED, '\\theta': BLUE, 'e': GREEN, '\\sin': PINK, '\\cos': GREEN, '\\varphi': YELLOW, 't': BLUE_D, '\\omega': RED}

        formula = TexMobject('\\mathbf{e', '^{i', '\\theta', '}=', '\\cos{', '\\theta', '}+', 'i', '\\sin', '{\\theta}}',
                             color=BLACK, background_stroke_color=BLACK, background_stroke_width=3).set_height(1.)

        formula.set_color_by_tex_to_color_map({'i': RED, '\\theta': BLUE, 'e': GREEN, '\\sin': PINK, '\\cos': GREEN}).shift(DOWN * 1.8)
        formula[2].set_color(BLUE)
        formula[5].set_color(BLUE)
        formula[-1].set_color(BLUE)

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

        tex_cos = TexMobject('\\mathbf{\\cos{', '\\theta}}', color=GREEN_D, background_stroke_color=WHITE, background_stroke_width=1).scale(0.8)
        tex_sin = TexMobject('\\mathbf{\\sin{', '\\theta}}', color=PINK, background_stroke_color=WHITE, background_stroke_width=1).scale(0.8)
        tex_cos[1].set_color(BLUE)
        tex_sin[1].set_color(BLUE)
        tex_cos.next_to(line_2, DOWN * 0.8)
        tex_sin.next_to(line_3, RIGHT * 1.25)

        text_theta = TexMobject('\\mathbf{\\theta', '=', '\\omega', 't', '+', '\\varphi', color=BLACK,
                                background_stroke_color=BLACK, background_stroke_width=3).set_color_by_tex_to_color_map(color_dict)
        text_theta.set_height(1.).next_to(formula, DOWN * 2)
        text_theta[0].set_color(BLUE)

        tex_group = VGroup(tex_1_1, tex_1_2, tex_i_1, tex_i_2).shift(UP * 1.2)

        self.add(group_1, group_2, tex_group, tex_cos, tex_sin)
        self.wait()

        self.play(Write(formula))
        self.wait()
        self.play(Write(text_theta))

        self.wait(10)

