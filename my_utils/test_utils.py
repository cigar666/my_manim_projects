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


