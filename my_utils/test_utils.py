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
