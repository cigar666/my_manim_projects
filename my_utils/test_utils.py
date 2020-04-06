from manimlib.imports import *
from my_manim_projects.my_utils.my_geometry import *

## test Arcs
class Arcs_Test(Scene):

    def construct(self):

        arcs_01 = Arcs(stroke_width=80).shift(LEFT * 4.5)
        arcs_02 = Arcs(angle_list=np.array([10, 20, 30, 40, 50, 60, 70, 80]) * DEGREES, stroke_width=200)
        arcs_03 = Arcs(angle_list=np.array([10, 15, 20, 30]) * DEGREES, stroke_width=200).set_stroke(opacity=0.25).shift(RIGHT * 4)
        arcs_04 = Arcs(angle_list=np.array([10, 15, 20, 30]) * DEGREES, radius=2, stroke_width=10).shift(RIGHT * 4)

        self.play(ShowCreation(arcs_01))
        self.wait()
        self.play(ShowCreation(arcs_02))
        self.wait()
        self.play(ShowCreation(VGroup(arcs_03, arcs_04)))

        self.wait(4)

## test Angle
class Angle_test(Scene):

    def construct(self):

        A = LEFT * 4.5 + DOWN * 2
        B = RIGHT * 6 + DOWN * 1
        C = UP * 2

        tri_abc = Polygon(A, B, C, color=WHITE)

        dot_A = Dot(A, color=RED, radius=0.15)
        angle_A = Angle(B, A, C, color=RED, radius=1.6)

        dot_B = Dot(B, color=YELLOW, radius=0.15)
        angle_B = Angle(A, B, C, color=YELLOW, radius=1.5)

        dot_C = Dot(C, color=BLUE, radius=0.15)
        angle_C = Angle(A, C, B, color=BLUE, radius=1.)

        self.add((tri_abc))
        self.wait()
        self.play(FadeInFromLarge(dot_A))
        self.play(ShowCreation(angle_A))
        self.wait()
        self.play(FadeInFromLarge(dot_B))
        self.play(ShowCreation(angle_B))
        self.wait()
        self.play(FadeInFromLarge(dot_C))
        self.play(ShowCreation(angle_C))

        self.wait(2)

## test Tracked_Point 01
class Test_Tracked_Point(Scene):

    def construct(self):
        numberplane = NumberPlane()
        self.play(ShowCreation(numberplane))
        self.wait()
        point = Tracked_Point(RIGHT * 3, size=0.25)

        self.play(FadeIn(point), ShowCreation(point.coordinates_text))
        self.wait()
        self.play(Rotating(point, radians=TAU, about_point=ORIGIN), run_time=10)
        self.wait(2)

## test Tracked_Point 02
class Point_move_along_sinX(Scene):

    def construct(self):

        numberplane = NumberPlane()

        path = ParametricFunction(lambda t: np.sin(t*PI/2) * UP + t * RIGHT, t_min=-2, t_max=2, color=PINK)

        point = Tracked_Point(LEFT * 2, size=0.2)

        self.add(numberplane)
        self.play(ShowCreation(path))
        self.wait()
        self.play(ShowCreation(point))
        self.wait()
        self.add(point.coordinates_text)
        self.play(MoveAlongPath(point, path, rate_func=linear), run_time=5)
        self.wait(2)

## test Right_angle and Dashed_Circle
class Test_Right_Angle(Scene):

    def construct(self):

        cp = ComplexPlane().scale(2.4)

        arrow_01 = Arrow(cp.n2p(1), cp.n2p(0.5), color=BLUE, buff=0, plot_depth=1)
        arrow_02 = Arrow(cp.n2p(1), cp.n2p(1+0.5j), color=YELLOW, buff=0, plot_depth=1)
        dot = Dot(cp.n2p(1), color=GREEN, plot_depth=2)
        group_01 = VGroup(dot, arrow_01, arrow_02)
        ra = Right_angle(corner=dot.get_center(), on_the_right=False)

        # the Right_angle 'ra' will not rotate with group_01,
        # but use method 'move_corner_to' & 'change_angle_to' to adjust its position and attitude
        ra.add_updater(lambda ra: ra.move_corner_to(dot.get_center()))
        ra.add_updater(lambda ra: ra.change_angle_to(arrow_01.get_angle() + PI))

        dash_circle = Dashed_Circle(radius=cp.n2p(1)[0], arc_config={'color': GREEN, 'stroke_width': 1.5})

        self.play(ShowCreation(cp))
        self.wait()
        self.play(ShowCreation(dot))
        self.play(ShowCreation(arrow_01), ShowCreation(arrow_02))
        self.play(ShowCreation(ra))
        self.wait()
        self.play(ShowCreation(dash_circle))

        self.play(Rotating(group_01, about_point=ORIGIN))

        self.wait(2)

## test my_text ##
from my_manim_projects.my_utils.my_text import MyText
class Test_mytext(Scene):

    def construct(self):

        color_dict = {'R': PINK, 'd': YELLOW, 'r': ORANGE, '\\theta': BLUE, '\\over': WHITE,
              't': BLUE, 'e': GREEN, 'i': RED, '\\sin': WHITE, '\\cos': WHITE}

        font_list = ['Comic Sans MS', '庞门正道标题体', 'Consolas', 'SWGothe', 'Rough___Dusty_Chalk',
                     'SWScrps', '新蒂小丸子体']

        origin_formula = TexMobject('f', '(', 't', ')', '=', 'x', '(', 't', ')', '+', 'y', '(', 't', ')', 'i', '=',
                             '(', 'R', '-', 'r', ')', 'e^{', 'i', 't}', '+', 'd', 'e^{', '-', 'i', '{R', '-',
                             'r', '\\over', 'r}', 't}').scale(1)\
                        .set_color_by_tex_to_color_map(color_dict).to_corner(LEFT * 2 + UP * 1.5)
        formulas = VGroup(origin_formula)

        for i in range(len(font_list)):
            formula_i = MyText('f', '(', 't', ')', '=', 'x', '(', 't', ')', '+', 'y', '(', 't', ')', 'i', '=',
                             '(', 'R', '-', 'r', ')', 'e^{', 'i', 't}', '+', 'd', 'e^{', '-', 'i', '{R', '-',
                             'r', '\\over', 'r}', 't}', default_font=font_list[i], tex_scale_factor=0.75)
            formula_i.set_color_by_tex_to_color_map(color_dict)
            replace_dict = {'e^{': 'e', 't}': 't', '{R': 'R', 'r}': 'r', '\\over': '-'}
            new_formula = formula_i.get_new_font_texs(replace_dict)
            new_formula.to_corner(LEFT * 2 + UP * 1.5).shift(DOWN * 0.8 * (i+1))
            formulas.add(new_formula)

        self.add(formulas)
        self.wait(5)

## test Trail ##

class Test_trail(Scene):

    def construct(self):

        dot = Dot(color=BLUE).shift(LEFT)
        trail = Trail(dot, trail_color=BLUE_B, max_width=4)
        trail.start_trace()

        self.add(trail)
        self.play(Rotating(dot, about_point=ORIGIN, run_time=4))

        trail.retrieve_trail(rate=5)

        self.wait(2)

class Test_trail_02(Scene):

    def construct(self):

        poly = RegularPolygon(5).scale(1.6)
        dot = Dot().set_fill(opacity=0).move_to(poly.get_start())
        trail_dot = Trail(dot, rate_func=lambda t: 1, trail_color=[RED, ORANGE, YELLOW, GREEN, BLUE, PINK, RED],
                          nums=300, max_width=2.5)
        trail_dot.start_trace()
        self.add(trail_dot.trail)
        self.play(MoveAlongPath(dot, poly), run_time=10)
        self.wait(4)

## test MySectors by data visualisation ##

class Test_MySectors(Scene):

    CONFIG = {
        'camera_config':{
            'background_color': WHITE,
        },
    }

    def construct(self):

        values = [2, 2, 2, 3, 9, 9, 10, 11, 14, 15, 15, 15, 15, 16, 18, 18, 18,
                  19, 22, 23, 23, 24, 24, 25, 26, 37, 44]
        labels = ['广东', '山东', '河南', '黑龙江', '四川', '浙江', '宁夏', '辽宁',
                  '湖南', '天津', '河北', '江西', '安徽', '福建', '山西', '广西', '重庆',
                  '吉林', '云南', '海南', '陕西', '内蒙古', '江苏', '新疆', '贵州', '青海', '西藏']

        center = UP * 0.5 + LEFT * 2.25

        graph_01 = MySectors(inner_radius=1.5, values=values, labels=labels, start_direction=RIGHT,
                             unit='天', center=center)
        color = average_color(BLUE_C, BLACK, BLACK)
        graph_01.create_cicles(color)
        graph_01.create_circle_shadow(color=color)

        font='华光标题宋_CNKI'
        text_01 = Text('多个省市区', font=font, color=color, size=0.32)
        text_02 = Text('确诊病例连续多日', font=font, color=color, size=0.32).next_to(text_01, DOWN * 0.25)
        text_03 = Text('零新增', font=font, color=color, size=0.75).next_to(text_02, DOWN * 0.4)
        texts = VGroup(text_01, text_02, text_03).move_to(center)

        rect_1 = Rectangle(width=0.1, height=0.24, stroke_width=0, fill_color=color, fill_opacity=1)
        text_11 = Text('数据为3月14日前无新增确诊病例的27个省（市，区）', font='思源黑体 Bold', color=color).set_height(0.24).next_to(rect_1, RIGHT * 0.32).align_to(rect_1, DOWN)
        text_11.set_color_by_t2c({'3月14日': BLUE})
        text_line_01 = VGroup(rect_1, text_11).to_corner(LEFT * 16 + UP * 1.)
        rect_2 = Rectangle(width=0.1, height=0.24, stroke_width=0, fill_color=color, fill_opacity=1)
        text_12 = Text('数据来源：@央视新闻', font='思源黑体 Bold', color=color).set_height(0.24).next_to(rect_2, RIGHT * 0.32).align_to(rect_2, DOWN)
        text_12.set_color_by_t2c({'@央视新闻': ORANGE})
        text_line_02 = VGroup(rect_2, text_12).to_corner(LEFT * 16 + UP * 1.75)
        rect_3 = Rectangle(width=0.1, height=0.24, stroke_width=0, fill_color=color, fill_opacity=1)
        text_13 = Text('作者：@cigar666', font='思源黑体 Bold', color=color).set_height(0.24).next_to(rect_3, RIGHT * 0.32).align_to(rect_3, DOWN)
        text_13.set_color_by_t2c({'@cigar666': PINK})
        text_line_03 = VGroup(rect_3, text_13).to_corner(LEFT * 16 + UP * 2.5)

        self.add(graph_01, texts, text_line_01, text_line_02, text_line_03)
        self.wait(5)

class Test_MySectors_0315(Scene):

    CONFIG = {
        'camera_config':{
            'background_color': WHITE,
        },
    }

    def construct(self):

        values = [3, 3, 4, 10, 11, 12, 15, 16, 16, 16, 16, 17, 19, 19, 19,
                  20, 23, 24, 24, 25, 25, 26, 27, 38, 45]
        labels = ['山东', '河南', '黑龙江', '四川', '宁夏', '辽宁',
                  '湖南', '天津', '河北', '江西', '安徽', '福建', '山西', '广西', '重庆',
                  '吉林', '云南', '海南', '陕西', '内蒙古', '江苏', '新疆', '贵州', '青海', '西藏']

        center = UP * 0.5 + LEFT * 2.25

        graph_01 = MySectors(inner_radius=1.5, values=values, labels=labels, start_direction=RIGHT,
                             unit='天', center=center)
        color = average_color(BLUE_B, BLACK, BLACK)
        graph_01.create_cicles(color)
        graph_01.create_circle_shadow(color=color)

        font='华光标题宋_CNKI'
        text_01 = Text('多个省市区', font=font, color=color, size=0.32)
        text_02 = Text('确诊病例连续多日', font=font, color=color, size=0.32).next_to(text_01, DOWN * 0.25)
        text_03 = Text('零新增', font=font, color=color, size=0.75).next_to(text_02, DOWN * 0.4)
        texts = VGroup(text_01, text_02, text_03).move_to(center)

        rect_1 = Rectangle(width=0.1, height=0.24, stroke_width=0, fill_color=color, fill_opacity=1)
        text_11 = Text('数据为3月15日前无新增确诊病例的25个省（市，区）', font='思源黑体 Bold', color=color).set_height(0.24).next_to(rect_1, RIGHT * 0.32).align_to(rect_1, DOWN)
        text_11.set_color_by_t2c({'3月15日': BLUE})
        text_line_01 = VGroup(rect_1, text_11).to_corner(LEFT * 16 + UP * 1.)
        rect_2 = Rectangle(width=0.1, height=0.24, stroke_width=0, fill_color=color, fill_opacity=1)
        text_12 = Text('数据来源：@央视新闻', font='思源黑体 Bold', color=color).set_height(0.24).next_to(rect_2, RIGHT * 0.32).align_to(rect_2, DOWN)
        text_12.set_color_by_t2c({'@央视新闻': ORANGE})
        text_line_02 = VGroup(rect_2, text_12).to_corner(LEFT * 16 + UP * 1.75)
        rect_3 = Rectangle(width=0.1, height=0.24, stroke_width=0, fill_color=color, fill_opacity=1)
        text_13 = Text('作者：@cigar666', font='思源黑体 Bold', color=color).set_height(0.24).next_to(rect_3, RIGHT * 0.32).align_to(rect_3, DOWN)
        text_13.set_color_by_t2c({'@cigar666': PINK})
        text_line_03 = VGroup(rect_3, text_13).to_corner(LEFT * 16 + UP * 2.5)

        self.add(graph_01, texts, text_line_01, text_line_02, text_line_03)
        self.wait(5)

## test New_Polygon ##

class Test_New_Polygon(Scene):

    def construct(self):

        tri_01 = New_Polygon(ORIGIN, 2.5*UP, 5*RIGHT, color=BLUE, stroke_width=20).shift(LEFT * 5.5)
        tri_02 = Polygon(ORIGIN, 2.5*UP, 5*RIGHT, color=GREEN, stroke_width=20).shift(RIGHT * 0.5)

        text_01 = Text('New_Polygon', font='思源黑体 Bold', color=BLUE)\
            .set_height(0.5).next_to(tri_01, DOWN * 0.75)
        text_02 = Text('Polygon', font='思源黑体 Bold', color=GREEN)\
            .set_height(0.5).next_to(tri_02, DOWN * 0.75)

        self.add(*tri_01, tri_02, text_01, text_02)
        self.play(tri_01[0].set_fill, {'color': YELLOW, 'opacity': 0.6},
                  tri_02.set_fill, {'color': YELLOW, 'opacity': 0.6}, run_time=2.5)
        self.wait(2)

class Test_New_Polygon_02(Scene):

    def construct(self):

        tri_01 = New_Polygon(ORIGIN, 2.5*UP, 5*RIGHT, color=BLUE, stroke_width=30).move_to(ORIGIN)

        self.add(*tri_01)
        self.wait(0.5)
        self.play(tri_01.scale, 2., run_time=1.5)
        self.wait()
        self.play(tri_01[0].set_fill, {'color': YELLOW, 'opacity': 0.6}, run_time=1.5)
        self.wait(2)


## test Shadow ##

class Test_Shadow(Scene):
    CONFIG = {
        'camera_config': {
            'background_color': WHITE,
        },
    }
    def construct(xgnb):
        # circle = Circle(color=BLUE, stroke_width=0)
        text = Text('X G N B !', font='庞门正道标题体', size=1.8)
        shadow = Shadow_2d(text, blur_width=0.5, layer_num=50, show_basic_shape=False, shadow_out=True).shift(UP * 2.5)
        shadow_02 = VGroup(*[Shadow_2d(text[2 * i], blur_width=0.5, layer_num=50, show_basic_shape=False) for i in range(5)]).shift(DOWN * 2)

        path = 'my_manim_projects\\my_projects\\resource\\svg_files\\'
        good = SVGMobject(path + 'good.svg', color=PINK).to_corner(LEFT * 5 + DOWN * 2)
        coin = SVGMobject(path + 'coin.svg', color=BLUE).to_corner(LEFT * 12 + DOWN * 2)
        favo = SVGMobject(path + 'favo.svg', color=ORANGE).to_corner(LEFT * 19 + DOWN * 2)

        shadow_good = Shadow_2d(good, blur_width=0.3, layer_num=50, show_basic_shape=False, shadow_out=True)
        shadow_coin = Shadow_2d(coin, blur_width=0.3, layer_num=50, show_basic_shape=False, shadow_out=True)
        shadow_favo = Shadow_2d(favo, blur_width=0.3, layer_num=50, show_basic_shape=False, shadow_out=True)

        xgnb.add(shadow, shadow_02)
        xgnb.add(shadow_good, shadow_coin, shadow_favo)
        xgnb.wait(5)

class Test_Shadow_02(Scene):
    CONFIG = {
        'camera_config': {
            'background_color': WHITE,
        },
    }
    def construct(xgnb):
        num=8
        colors = color_gradient([RED, PINK, BLUE, GREEN, YELLOW, ORANGE], num)
        s = 0.6
        circles = VGroup(*[Circle(radius=s * (i+0.6)) for i in range(num * 2)])
        shadows_out = VGroup(*[Shadow_2d(circles[i*2], blur_width=0.5 * s, layer_num=50, show_basic_shape=False, shadow_out=True) for i in range(num)], plot_depth=1)
        shadows_in = VGroup(*[Shadow_2d(circles[i*2+1], blur_width=0.5 * s, layer_num=50, show_basic_shape=False, shadow_out=False) for i in range(num-1)], plot_depth=1)
        annulus_group = VGroup(*[Annulus(inner_radius=s * (2 * i - 1 + 0.6), outer_radius=s * (2 * i + 0.6), fill_color=colors[i], fill_opacity=1, stroke_width=0, plot_depth=-5) for i in range(1, num)])
        circle = Circle(radius=0.6 * s, stroke_width=0, fill_color=colors[0], fill_opacity=1, plot_depth=1)

        xgnb.add(shadows_out, shadows_in, annulus_group, circle)
        xgnb.wait(5)



