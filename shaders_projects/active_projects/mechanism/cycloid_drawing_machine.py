from manimlib.imports import *
from my_projects.active_projects.mechanism.basic_component import *

class Test_Curve(Scene):

    def construct(self):

        s = 0.6
        P2A, P3B, CD, AC = 1.5, 1., 2, 4
        phi_A, phi_B, theta_BCD = PI/6, PI/4, PI/2

        z0, z1, z2, z3 = 20, 45, 30, 20
        # z0, z1, z2, z3 = 25, 50, 25 * 1.6, 0.7 * 25

        P2 = np.array([-1.8, 3.6, 0])
        P3 = np.array([2 * np.sqrt(3), 0., 0])

        t = ValueTracker(0)
        w = 0.5

        dot = Dot(color=BLUE)

        def update_dot(d):
            A = P2 + P2A * complex_to_R3(np.exp(1j * z0/z2 * w * t.get_value() + phi_A))
            B = P3 + P3B * complex_to_R3(np.exp(-1j * z0/z3 * w * t.get_value() + phi_B))
            AB = B - A
            C = A + AB / get_norm(AB) * AC
            D = C + CD * complex_to_R3(np.exp(1j * (np.angle(complex(*AB[0:2])) - theta_BCD)))
            # print('A:', A)
            # print('B:', B)
            # print('C:', C)
            # print('D:', D)
            # d.move_to(get_norm(D))
            d.move_to(s * get_norm(D) * complex_to_R3(np.exp(-1j * z0/z1 * w * t.get_value())))
        dot.add_updater(update_dot)
        self.wait(0.5)
        path = TracedPath(dot.get_center, min_distance_to_new_point=0.05)

        self.add(dot, path)
        self.play(t.set_value, 200, rate_func=linear, run_time=50)
        self.wait(2)


class Test_Gears_02(Scene):

    CONFIG = {
        'camera_config': {
            'background_color': WHITE,
        }
    }

    def construct(self):

        r1 = 2.8
        z0, z1, z2, z3 = 36, 75, 37, 30
        r0, r2, r3 = r1 * z0 / z1, r1 * z2 / z1, r1 * z3 / z1
        center = DOWN * 0.72
        # P2A, P3B, CD, AC = 1., 0.72, 1.6, 2.8
        P2A, P3B, CD, AC = 1., 0.8, 1.2, 4.
        phi_A, phi_B, theta_BCD = PI/6, PI/4, PI/2

        gear_1 = Gear(pitch_circle_radius=r1, tooth_hight=0.16, tooth_num=z1, inner_radius=0.3, center=center, stroke_color=BLUE)
        gear_0 = Gear(pitch_circle_radius=r0, tooth_hight=0.16, tooth_num=z0, inner_radius=0.16, speed=1 * DEGREES,
                      center=gear_1.center + complex_to_R3((r0+r1) * np.exp(-1j * 15 * DEGREES)), stroke_color=RED)
        gear_2 = Gear(pitch_circle_radius=r2, tooth_hight=0.16, tooth_num=z2, inner_radius=0.16,
                      center=gear_1.center + complex_to_R3((r1+r2) * np.exp(1j * 3 * PI/4)), stroke_color=GREEN)
        gear_3 = Gear(pitch_circle_radius=r3, tooth_hight=0.16, tooth_num=z3, inner_radius=0.16,
                      center=gear_0.center + complex_to_R3((r0+r3) * np.exp(1j * 75 * DEGREES)), stroke_color=PINK)

        P0 = Dot(gear_0.center, color=RED).set_height(0.25)
        P1 = Dot(gear_1.center, color=BLUE).set_height(0.45)
        P2 = Dot(gear_2.center, color=GREEN).set_height(0.25)
        P3 = Dot(gear_3.center, color=PINK).set_height(0.25)
        points = VGroup(P0, P1, P2, P3)

        gear_1.match_angle(gear_0).match_speed(gear_0)
        gear_2.match_angle(gear_1).match_speed(gear_1)
        gear_3.match_angle(gear_0).match_speed(gear_0)

        dot_A = Dot(gear_2.center + complex_to_R3(P2A * np.exp(1j * phi_A)), color=GREEN).scale(0.8)
        dot_B = Dot(gear_3.center + complex_to_R3(P3B * np.exp(1j * phi_B)), color=PINK).scale(0.8)

        rect = Rectangle(height=0.4, width=11, stroke_width=2, stroke_color=YELLOW).round_corners(0.2)
        hole = Circle(radius=0.1, stroke_width=2, stroke_color=YELLOW).align_to(rect, LEFT).shift(RIGHT * 0.1)
        hole_2 = Dot().set_opacity(0).align_to(rect, RIGHT).shift(LEFT * 0.1)
        line_hole = Rectangle(height=0.18, width=10, stroke_width=2, stroke_color=YELLOW).round_corners(0.09).align_to(rect, RIGHT).shift(LEFT * 0.11)

        rod = VGroup(rect, hole, line_hole, hole_2)
        gear_2.add(dot_A), gear_3.add(dot_B)

        poly_5 = Polygon([-0.2, 3., 0], [0.2, 3., 0], [0.2, 0, 0], [0, -0.2 * np.sqrt(3), 0], [-0.2, 0, 0],
                         stroke_width=2, stroke_color=YELLOW).round_corners(0.2)
        hole_01 = Circle(radius=0.1, stroke_width=2, stroke_color=YELLOW).align_to(poly_5, DOWN).shift(UP * 0.1)
        line_hole_01 = Rectangle(height=2.5, width=0.18, stroke_width=2, stroke_color=YELLOW).round_corners(0.09).align_to(poly_5, UP).shift(DOWN * 0.11)
        dot_D = Dot(hole_01.get_center(), color=BLUE).scale(0.8)
        rod_2 = VGroup(poly_5, hole_01, line_hole_01, dot_D)
        rod_2.shift(hole.get_center()-hole_01.get_center() + AC * RIGHT + CD * DOWN)

        c0 = Circle(radius=0.18, stroke_width=2, stroke_color=YELLOW).shift(hole.get_center()+AC*RIGHT)
        c1 = Dot(color=YELLOW).scale(0.85).shift(hole.get_center()+AC*RIGHT)
        rods = VGroup(rod, rod_2, VGroup(c0, c1))

        def update_rod(r):
            r.shift(dot_A.get_center() - hole.get_center())
            AB = dot_B.get_center() - dot_A.get_center()
            vect_old = hole_2.get_center() - hole.get_center()
            r.rotate(np.angle(complex(*AB[:2]))-np.angle(complex(*vect_old[:2])), about_point=hole.get_center())

        rods.add_updater(update_rod)

        gears = Gear_system(gear_0, gear_1, gear_2, gear_3)
        gears.update_gears()
        path = TracedPath(dot_D.get_center, stroke_color=BLUE, min_distance_to_new_point=0.02, stroke_width=1.)
        path.add_updater(lambda p: p.rotate(gears.w.get_value() * gear_1.speed, about_point=gear_1.center))


        self.add(points)
        self.add(gears, rods, path)
        self.wait()
        self.play(
            gears.set_stroke, {'opacity':0.4},
            rods.set_stroke, {'opacity':0.4},
            points.set_opacity, 0.4, run_time=2)

        self.wait(0.4)
        self.play(gears.w.set_value, 4, run_time=8)
        self.wait(10/2)
        self.wait(20/2)
        self.wait(30/2)
        self.wait(40/2)
        self.wait(60/2)
        self.wait(60/2)
        gears.stop_update()
        # self.play(FadeOut(gears), FadeOut(rods), FadeOut(points), run_time=2)
        self.play(path.move_to, ORIGIN)
        self.play(path.set_height, 7.2, run_time=2)
        self.wait(5)


class Cycloid_drawing_machine_test(Scene):

    CONFIG = {
        'camera_config': {
            'background_color': WHITE,
        }
    }

    def construct(self):

        r1 = 2.8
        z0, z1, z2, z3 = 36, 75, 47, 30
        r0, r2, r3 = r1 * z0 / z1, r1 * z2 / z1, r1 * z3 / z1
        center = DOWN * 0.72
        # P2A, P3B, CD, AC = 1., 0.72, 1.6, 2.8
        P3A, P2B, CD, AC = 0.8, 1.2, 0.9, 4.2
        phi_A, phi_B, theta_BCD = PI/4, PI/6, PI/2

        gear_1 = Gear(pitch_circle_radius=r1, tooth_hight=0.16, tooth_num=z1, inner_radius=0.3, center=center, stroke_color=BLUE)
        gear_0 = Gear(pitch_circle_radius=r0, tooth_hight=0.16, tooth_num=z0, inner_radius=0.16, speed=1 * DEGREES,
                      center=gear_1.center + complex_to_R3((r0+r1) * np.exp(-1j * 15 * DEGREES)), stroke_color=RED)
        gear_2 = Gear(pitch_circle_radius=r2, tooth_hight=0.16, tooth_num=z2, inner_radius=0.16,
                      center=gear_1.center + complex_to_R3((r1+r2) * np.exp(1j * 3 * PI/4)), stroke_color=GREEN)
        gear_3 = Gear(pitch_circle_radius=r3, tooth_hight=0.16, tooth_num=z3, inner_radius=0.16,
                      center=gear_0.center + complex_to_R3((r0+r3) * np.exp(1j * 75 * DEGREES)), stroke_color=PINK)

        P0 = Dot(gear_0.center, color=RED).set_height(0.25)
        P1 = Dot(gear_1.center, color=BLUE).set_height(0.45)
        P2 = Dot(gear_2.center, color=GREEN).set_height(0.25)
        P3 = Dot(gear_3.center, color=PINK).set_height(0.25)

        gear_1.match_angle(gear_0).match_speed(gear_0)
        gear_2.match_angle(gear_1).match_speed(gear_1)
        gear_3.match_angle(gear_0).match_speed(gear_0)

        dot_A = Dot(gear_3.center + complex_to_R3(P3A * np.exp(1j * phi_A)), color=PINK).scale(0.8)
        dot_B = Dot(gear_2.center + complex_to_R3(P2B * np.exp(1j * phi_B)), color=GREEN).scale(0.8)

        rect = Rectangle(height=0.4, width=11.5, stroke_width=2, stroke_color=YELLOW).round_corners(0.2)
        hole = Circle(radius=0.1, stroke_width=2, stroke_color=YELLOW).align_to(rect, LEFT).shift(RIGHT * 0.1)
        hole_2 = Dot().set_opacity(0).align_to(rect, RIGHT).shift(LEFT * 0.1)
        line_hole = Rectangle(height=0.18, width=10.5, stroke_width=2, stroke_color=YELLOW).round_corners(0.09).align_to(rect, RIGHT).shift(LEFT * 0.11)

        rod = VGroup(rect, hole, line_hole, hole_2)
        gear_3.add(dot_A), gear_2.add(dot_B)

        poly_5 = Polygon([-0.2, 3., 0], [0.2, 3., 0], [0.2, 0, 0], [0, -0.2 * np.sqrt(3), 0], [-0.2, 0, 0],
                         stroke_width=2, stroke_color=YELLOW).round_corners(0.2)
        hole_01 = Circle(radius=0.1, stroke_width=2, stroke_color=YELLOW).align_to(poly_5, DOWN).shift(UP * 0.1)
        line_hole_01 = Rectangle(height=2.5, width=0.18, stroke_width=2, stroke_color=YELLOW).round_corners(0.09).align_to(poly_5, UP).shift(DOWN * 0.11)
        dot_D = Dot(hole_01.get_center(), color=BLUE).scale(0.8)
        rod_2 = VGroup(poly_5, hole_01, line_hole_01, dot_D).rotate(PI)
        rod_2.shift(hole.get_center()-hole_01.get_center() + AC * RIGHT + CD * UP)

        c0 = Circle(radius=0.18, stroke_width=2, stroke_color=YELLOW).shift(hole.get_center()+AC*RIGHT)
        c1 = Dot(color=YELLOW).scale(0.85).shift(hole.get_center()+AC*RIGHT)
        rods = VGroup(rod, rod_2, VGroup(c0, c1))

        def update_rod(r):
            r.shift(dot_A.get_center() - hole.get_center())
            AB = dot_B.get_center() - dot_A.get_center()
            vect_old = hole_2.get_center() - hole.get_center()
            r.rotate(np.angle(complex(*AB[:2]))-np.angle(complex(*vect_old[:2])), about_point=hole.get_center())

        rods.add_updater(update_rod)

        gears = Gear_system(gear_0, gear_1, gear_2, gear_3)
        gears.update_gears()
        path = TracedPath(dot_D.get_center, stroke_color=BLUE, min_distance_to_new_point=0.02, stroke_width=1.)
        path.add_updater(lambda p: p.rotate(gears.w.get_value() * gear_1.speed, about_point=gear_1.center))
        self.add(P0, P1, P2, P3)
        self.add(gears, rods, path)
        gears.set_stroke(opacity=0.5)
        rods.set_stroke(opacity=0.5)

        self.wait(1)
        self.play(gears.w.set_value, 2.5, run_time=10)
        self.wait(10)
        self.wait(20)
        self.wait(30)
        self.wait(40)
        self.wait(60)
        self.wait(60)

        self.wait(60)
        self.wait(60)


class Cycloid_drawing_machine_generation_new(Scene):

    CONFIG = {
        'camera_config': {
            'background_color': WHITE,
        }
    }

    def construct(self):

        r1 = 2.8
        z0, z1, z2, z3 = 36, 75, 37, 30
        r0, r2, r3 = r1 * z0 / z1, r1 * z2 / z1, r1 * z3 / z1
        center = DOWN * 0.72
        # P2A, P3B, CD, AC = 1., 0.72, 1.6, 2.8
        P3A, P2B, CD, AC = 0.9, 1., 1.2, 3.6
        phi_A, phi_B, theta_BCD = PI/6, 36 *DEGREES, PI/2

        gear_1 = Gear(pitch_circle_radius=r1, tooth_hight=0.16, tooth_num=z1, inner_radius=0.3, center=center, stroke_color=BLUE)
        gear_0 = Gear(pitch_circle_radius=r0, tooth_hight=0.16, tooth_num=z0, inner_radius=0.16, speed=1 * DEGREES,
                      center=gear_1.center + complex_to_R3((r0+r1) * np.exp(-1j * 15 * DEGREES)), stroke_color=RED)
        gear_2 = Gear(pitch_circle_radius=r2, tooth_hight=0.16, tooth_num=z2, inner_radius=0.16,
                      center=gear_1.center + complex_to_R3((r1+r2) * np.exp(1j * 3 * PI/4)), stroke_color=GREEN)
        gear_3 = Gear(pitch_circle_radius=r3, tooth_hight=0.16, tooth_num=z3, inner_radius=0.16,
                      center=gear_0.center + complex_to_R3((r0+r3) * np.exp(1j * 75 * DEGREES)), stroke_color=PINK)

        P0 = Dot(gear_0.center, color=RED).set_height(0.25)
        P1 = Dot(gear_1.center, color=BLUE).set_height(0.45)
        P2 = Dot(gear_2.center, color=GREEN).set_height(0.25)
        P3 = Dot(gear_3.center, color=PINK).set_height(0.25)
        points = VGroup(P0, P1, P2, P3)

        gear_1.match_angle(gear_0).match_speed(gear_0)
        gear_2.match_angle(gear_1).match_speed(gear_1)
        gear_3.match_angle(gear_0).match_speed(gear_0)

        # dot_A = Dot(gear_2.center + complex_to_R3(P2A * np.exp(1j * phi_A)), color=GREEN).scale(0.8)
        # dot_B = Dot(gear_3.center + complex_to_R3(P3B * np.exp(1j * phi_B)), color=PINK).scale(0.8)
        dot_A = Dot(gear_3.center + complex_to_R3(P3A * np.exp(1j * phi_A)), color=PINK).scale(0.8)
        dot_B = Dot(gear_2.center + complex_to_R3(P2B * np.exp(1j * phi_B)), color=GREEN).scale(0.8)

        rect = Rectangle(height=0.4, width=11.5, stroke_width=2, stroke_color=YELLOW).round_corners(0.2)
        hole = Circle(radius=0.1, stroke_width=2, stroke_color=YELLOW).align_to(rect, LEFT).shift(RIGHT * 0.1)
        hole_2 = Dot().set_opacity(0).align_to(rect, RIGHT).shift(LEFT * 0.1)
        line_hole = Rectangle(height=0.18, width=10.5, stroke_width=2, stroke_color=YELLOW).align_to(rect, RIGHT).shift(LEFT * 0.11).round_corners(0.09)

        rod = VGroup(rect, hole, line_hole, hole_2)
        gear_3.add(dot_A), gear_2.add(dot_B)

        poly_5 = Polygon([-0.2, 3., 0], [0.2, 3., 0], [0.2, 0, 0], [0, -0.2 * np.sqrt(3), 0], [-0.2, 0, 0],
                         stroke_width=2, stroke_color=YELLOW).round_corners(0.2)
        hole_01 = Circle(radius=0.1, stroke_width=2, stroke_color=YELLOW).align_to(poly_5, DOWN).shift(UP * 0.1)
        line_hole_01 = Rectangle(height=2.5, width=0.18, stroke_width=2, stroke_color=YELLOW).align_to(poly_5, UP).shift(DOWN * 0.11).round_corners(0.09)
        dot_D = Dot(hole_01.get_center(), color=BLUE).scale(0.8)
        rod_2 = VGroup(poly_5, hole_01, line_hole_01, dot_D).rotate(PI)
        rod_2.shift(hole.get_center()-hole_01.get_center() + AC * RIGHT + CD * UP)

        c0 = Circle(radius=0.18, stroke_width=2, stroke_color=YELLOW).shift(hole.get_center()+AC*RIGHT)
        c1 = Dot(color=YELLOW).scale(0.85).shift(hole.get_center()+AC*RIGHT)
        rods = VGroup(rod, rod_2, VGroup(c0, c1))

        self.play(FadeInFromLarge(P1), FadeInFromLarge(P0), run_time=1.5)
        self.wait(0.5)
        self.play(ShowCreation(gear_1))
        self.play(ShowCreation(gear_0))
        self.wait(0.5)
        gears = Gear_system(gear_0, gear_1, gear_2, gear_3)
        gears.update_gears()
        self.play(gears.w.set_value, 4, rate_func=there_and_back, run_time=5)
        self.wait(0.4)

        self.play(FadeInFromLarge(P2))
        self.play(ShowCreation(gear_2))
        self.play(FadeInFromLarge(P3))
        self.play(ShowCreation(gear_3))
        self.wait(0.4)

        rods.shift(dot_A.get_center() - hole.get_center())
        AB = dot_B.get_center() - dot_A.get_center()
        vect_old = hole_2.get_center() - hole.get_center()
        rods.rotate(np.angle(complex(*AB[:2]))-np.angle(complex(*vect_old[:2])), about_point=hole.get_center())
        self.play(FadeInFromLarge(rod))
        self.play(FadeInFromLarge(rod_2))
        self.play(FadeInFromLarge(rods[-1]))
        self.wait(0.4)

        def update_rod(mob):
            mob.shift(dot_A.get_center() - hole.get_center())
            AB = dot_B.get_center() - dot_A.get_center()
            vect_old = hole_2.get_center() - hole.get_center()
            mob.rotate(np.angle(complex(*AB[:2]))-np.angle(complex(*vect_old[:2])), about_point=hole.get_center())

        gears.update_gears()
        rods.add_updater(update_rod)
        gears.w.set_value(0)

        # self.play(gears.w.set_value, 1.5, run_time=5)

        # self.wait(2)
        self.play(gears.set_stroke, {'opacity': 0.4}, rods.set_stroke, {'opacity': 0.4}, points.set_opacity, 0.4, run_time=2.)
        path = TracedPath(dot_D.get_center, stroke_color=BLUE_D, min_distance_to_new_point=0.02, stroke_width=1.)
        path.add_updater(lambda p: p.rotate(gears.w.get_value() * gear_1.speed, about_point=gear_1.center))
        self.add(path)
        self.play(gears.w.set_value, 4, run_time=5)
        self.wait(10)
        self.wait(20)
        self.wait(30)
        self.wait(40)
        self.wait(60)
        self.wait(60)
        self.wait(60)
        gears.stop_update(), gears.w.set_value(0)
        self.play(FadeOut(gears), FadeOut(rods), FadeOut(points), run_time=2)
        self.play(path.move_to, ORIGIN)
        self.play(path.set_height, 7.2, run_time=2)
        self.wait(5)


# draw curves without displaying gears and rods
class OnlyCurve(Scene):

    CONFIG = {
        'camera_config': {
            'background_color': WHITE,
        },
        'gears_config':{
            'r1': 3,
            'z': [36, 75, 36, 30],
            'l': [0.95, 1.25, 0.9, 3.6],
            'a': [PI/6, 40 *DEGREES, PI/2],
            'w': 10,
        },
        'step_num': 2000,
        'wait_time': 2.5,
        'stroke_config': {
            'color': BLUE_D,
            'width': 1,
        },
    }

    def construct(self):

        r1 = self.gears_config['r1']
        z = self.gears_config['z']
        l = self.gears_config['l']
        a = self.gears_config['a']
        z0, z1, z2, z3 = z[0], z[1], z[2], z[3]
        r0, r2, r3 = r1 * z0 / z1, r1 * z2 / z1, r1 * z3 / z1
        center = ORIGIN
        # P2A, P3B, CD, AC = 1., 0.72, 1.6, 2.8
        P3A, P2B, CD, AC = l[0], l[1], l[2], l[3]
        phi_A, phi_B, theta_BCD = a[0], a[1], a[2]

        gear_1 = Virtual_Gear(pitch_circle_radius=r1, tooth_hight=0.16, tooth_num=z1, inner_radius=0.3, center=center, stroke_color=BLUE)
        gear_0 = Virtual_Gear(pitch_circle_radius=r0, tooth_hight=0.16, tooth_num=z0, inner_radius=0.16, speed=1 * DEGREES,
                           center=gear_1.center + complex_to_R3((r0+r1) * np.exp(-1j * 15 * DEGREES)), stroke_color=RED)
        gear_2 = Virtual_Gear(pitch_circle_radius=r2, tooth_hight=0.16, tooth_num=z2, inner_radius=0.16,
                           center=gear_1.center + complex_to_R3((r1+r2) * np.exp(1j * 3 * PI/4)), stroke_color=GREEN)
        gear_3 = Virtual_Gear(pitch_circle_radius=r3, tooth_hight=0.16, tooth_num=z3, inner_radius=0.16,
                      center=gear_0.center + complex_to_R3((r0+r3) * np.exp(1j * 75 * DEGREES)), stroke_color=PINK)

        gear_1.match_angle(gear_0).match_speed(gear_0)
        gear_2.match_angle(gear_1).match_speed(gear_1)
        gear_3.match_angle(gear_0).match_speed(gear_0)

        dot_A = Dot(gear_3.center + complex_to_R3(P3A * np.exp(1j * phi_A)), color=PINK).scale(0.8)
        dot_B = Dot(gear_2.center + complex_to_R3(P2B * np.exp(1j * phi_B)), color=GREEN).scale(0.8)

        rect = Rectangle(height=0.4, width=11.5, stroke_width=2, stroke_color=YELLOW) # .round_corners(0.2)
        hole = Circle(radius=0.1, stroke_width=2, stroke_color=YELLOW).align_to(rect, LEFT).shift(RIGHT * 0.1)
        hole_2 = Dot().set_opacity(0).align_to(rect, RIGHT).shift(LEFT * 0.1)
        line_hole = Rectangle(height=0.18, width=10.5, stroke_width=2, stroke_color=YELLOW).align_to(rect, RIGHT).shift(LEFT * 0.11)

        rod = VGroup(rect, hole, line_hole, hole_2)
        gear_3.add(dot_A), gear_2.add(dot_B)

        poly_5 = Polygon([-0.2, 3., 0], [0.2, 3., 0], [0.2, 0, 0], [0, -0.2 * np.sqrt(3), 0], [-0.2, 0, 0],
                         stroke_width=2, stroke_color=YELLOW) # .round_corners(0.2)
        hole_01 = Circle(radius=0.1, stroke_width=2, stroke_color=YELLOW).align_to(poly_5, DOWN).shift(UP * 0.1)
        line_hole_01 = Rectangle(height=2.5, width=0.18, stroke_width=2, stroke_color=YELLOW).align_to(poly_5, UP).shift(DOWN * 0.11)
        dot_D = Dot(hole_01.get_center(), color=BLUE).scale(0.8)
        rod_2 = VGroup(poly_5, hole_01, line_hole_01, dot_D).rotate(PI)
        rod_2.shift(hole.get_center()-hole_01.get_center() + AC * RIGHT + CD * UP)

        c0 = Circle(radius=0.18, stroke_width=2, stroke_color=YELLOW).shift(hole.get_center()+AC*RIGHT)
        c1 = Dot(color=YELLOW).scale(0.85).shift(hole.get_center()+AC*RIGHT)
        rods = VGroup(rod, rod_2, VGroup(c0, c1))

        def update_rod(r):
            r.shift(dot_A.get_center() - hole.get_center())
            AB = dot_B.get_center() - dot_A.get_center()
            vect_old = hole_2.get_center() - hole.get_center()
            r.rotate(np.angle(complex(*AB[:2]))-np.angle(complex(*vect_old[:2])), about_point=hole.get_center())

        rods.add_updater(update_rod)

        gears = Gear_system(gear_0, gear_1, gear_2, gear_3)
        # gears.update_gears()
        path = TracedPath(dot_D.get_center, stroke_color=self.stroke_config['color'],
                          min_distance_to_new_point=0.02, stroke_width=self.stroke_config['width'])
        path.add_updater(lambda p: p.rotate(gears.w.get_value() * gear_1.speed, about_point=gear_1.center))

        self.add(gears, rods, path)
        gears.set_opacity(0)
        rods.set_opacity(0)

        self.wait(1)
        gears.w.set_value(self.gears_config['w'])
        self.wait(1/60)
        for i in range(self.step_num):
            for g in gears:
                g.rotate_gear(g.speed * gears.w.get_value())
            if i % int(PI * 2 / (gears.w.get_value() * gear_1.speed)) == 0:
                self.wait(1/self.camera.frame_rate)
                # self.wait(0)
            else:
                self.wait(0)
            print('step_%d' % i, end='\t')
            print('frame_%d' % int(abs(i / int(PI * 2 / (gears.w.get_value() * gear_1.speed)))))
        self.wait(self.wait_time)


class OnlyCurve_mode01(OnlyCurve):

    CONFIG = {}


class OnlyCurve_mode01_2(Scene):

    CONFIG = {
        'camera_config': {
            'background_color': WHITE,
        },
        'gears_config':{
            'r1': 3,
            'z': [36, 75, 36, 30],
            'l': [0.95, 1.25, 0.9, 3.6],
            'a': [PI/6, 40 *DEGREES, PI/2],
            'w': 10,
        },
        'step_num': 2000,
        'wait_time': 2.5,
        'stroke_config': {
            'color': BLUE_D,
            'width': 1,
        },
    }

    def construct(self):

        r1 = self.gears_config['r1']
        z = self.gears_config['z']
        l = self.gears_config['l']
        a = self.gears_config['a']
        z0, z1, z2, z3 = z[0], z[1], z[2], z[3]
        r0, r2, r3 = r1 * z0 / z1, r1 * z2 / z1, r1 * z3 / z1
        center = ORIGIN
        # P2A, P3B, CD, AC = 1., 0.72, 1.6, 2.8
        P2A, P3B, CD, AC = l[0], l[1], l[2], l[3]
        phi_A, phi_B, theta_BCD = a[0], a[1], a[2]

        gear_1 = Virtual_Gear(pitch_circle_radius=r1, tooth_hight=0.16, tooth_num=z1, inner_radius=0.3, center=center, stroke_color=BLUE)
        gear_0 = Virtual_Gear(pitch_circle_radius=r0, tooth_hight=0.16, tooth_num=z0, inner_radius=0.16, speed=1 * DEGREES,
                           center=gear_1.center + complex_to_R3((r0+r1) * np.exp(-1j * 15 * DEGREES)), stroke_color=RED)
        gear_2 = Virtual_Gear(pitch_circle_radius=r2, tooth_hight=0.16, tooth_num=z2, inner_radius=0.16,
                           center=gear_1.center + complex_to_R3((r1+r2) * np.exp(1j * 3 * PI/4)), stroke_color=GREEN)
        gear_3 = Virtual_Gear(pitch_circle_radius=r3, tooth_hight=0.16, tooth_num=z3, inner_radius=0.16,
                      center=gear_0.center + complex_to_R3((r0+r3) * np.exp(1j * 75 * DEGREES)), stroke_color=PINK)

        gear_1.match_angle(gear_0).match_speed(gear_0)
        gear_2.match_angle(gear_1).match_speed(gear_1)
        gear_3.match_angle(gear_0).match_speed(gear_0)

        dot_A = Dot(gear_2.center + complex_to_R3(P2A * np.exp(1j * phi_A)), color=GREEN).scale(0.8)
        dot_B = Dot(gear_3.center + complex_to_R3(P3B * np.exp(1j * phi_B)), color=PINK).scale(0.8)

        rect = Rectangle(height=0.4, width=11, stroke_width=2, stroke_color=YELLOW).round_corners(0.2)
        hole = Circle(radius=0.1, stroke_width=2, stroke_color=YELLOW).align_to(rect, LEFT).shift(RIGHT * 0.1)
        hole_2 = Dot().set_opacity(0).align_to(rect, RIGHT).shift(LEFT * 0.1)
        line_hole = Rectangle(height=0.18, width=10, stroke_width=2, stroke_color=YELLOW).round_corners(0.09).align_to(rect, RIGHT).shift(LEFT * 0.11)

        rod = VGroup(rect, hole, line_hole, hole_2)
        gear_2.add(dot_A), gear_3.add(dot_B)

        poly_5 = Polygon([-0.2, 3., 0], [0.2, 3., 0], [0.2, 0, 0], [0, -0.2 * np.sqrt(3), 0], [-0.2, 0, 0],
                         stroke_width=2, stroke_color=YELLOW).round_corners(0.2)
        hole_01 = Circle(radius=0.1, stroke_width=2, stroke_color=YELLOW).align_to(poly_5, DOWN).shift(UP * 0.1)
        line_hole_01 = Rectangle(height=2.5, width=0.18, stroke_width=2, stroke_color=YELLOW).round_corners(0.09).align_to(poly_5, UP).shift(DOWN * 0.11)
        dot_D = Dot(hole_01.get_center(), color=BLUE).scale(0.8)
        rod_2 = VGroup(poly_5, hole_01, line_hole_01, dot_D)
        rod_2.shift(hole.get_center()-hole_01.get_center() + AC * RIGHT + CD * DOWN)

        c0 = Circle(radius=0.18, stroke_width=2, stroke_color=YELLOW).shift(hole.get_center()+AC*RIGHT)
        c1 = Dot(color=YELLOW).scale(0.85).shift(hole.get_center()+AC*RIGHT)
        rods = VGroup(rod, rod_2, VGroup(c0, c1))

        def update_rod(r):
            r.shift(dot_A.get_center() - hole.get_center())
            AB = dot_B.get_center() - dot_A.get_center()
            vect_old = hole_2.get_center() - hole.get_center()
            r.rotate(np.angle(complex(*AB[:2]))-np.angle(complex(*vect_old[:2])), about_point=hole.get_center())

        rods.add_updater(update_rod)

        gears = Gear_system(gear_0, gear_1, gear_2, gear_3)
        # gears.update_gears()
        path = TracedPath(dot_D.get_center, stroke_color=self.stroke_config['color'],
                          min_distance_to_new_point=0.02, stroke_width=self.stroke_config['width'])
        path.add_updater(lambda p: p.rotate(gears.w.get_value() * gear_1.speed, about_point=gear_1.center))

        self.add(gears, rods, path)
        gears.set_opacity(0)
        rods.set_opacity(0)

        self.wait(1)
        gears.w.set_value(self.gears_config['w'])
        self.wait(1/60)
        for i in range(self.step_num):
            for g in gears:
                g.rotate_gear(g.speed * gears.w.get_value())
            if i % int(PI * 2 / (gears.w.get_value() * gear_1.speed)) == 0:
                self.wait(1/self.camera.frame_rate)
                # self.wait(0)
            else:
                self.wait(0)
            print('step_%d' % i, end='\t')
            print('frame_%d' % int(abs(i / int(PI * 2 / (gears.w.get_value() * gear_1.speed)))))
        self.wait(self.wait_time)


class OnlyCurve_mode02(Scene):

    CONFIG = {
        'camera_config': {
            'background_color': WHITE,
        },
        'gears_config':{
            'r1': 3,
            'z': [36, 75, 36, 45],
            'l': [1.5, 1.25, 0.9, 3.6],
            'a': [PI/6, 40 *DEGREES, PI/2],
            'w': 10,
        },
        'step_num': 2000,
        'wait_time': 2.5,
        'stroke_config': {
            'color': BLUE_D,
            'width': 1,
        },
    }

    def construct(self):

        r1 = self.gears_config['r1']
        z = self.gears_config['z']
        l = self.gears_config['l']
        a = self.gears_config['a']
        z0, z1, z2, z3 = z[0], z[1], z[2], z[3]
        r0, r2, r3 = r1 * z0 / z1, r1 * z2 / z1, r1 * z3 / z1
        center = ORIGIN
        # P2A, P3B, CD, AC = 1., 0.72, 1.6, 2.8
        P3A, P2B, CD, AC = l[0], l[1], l[2], l[3]
        phi_A, phi_B, theta_BCD = a[0], a[1], a[2]

        gear_1 = Virtual_Gear(pitch_circle_radius=r1, tooth_hight=0.16, tooth_num=z1, inner_radius=0.3, center=center, stroke_color=BLUE)
        gear_0 = Virtual_Gear(pitch_circle_radius=r0, tooth_hight=0.16, tooth_num=z0, inner_radius=0.16, speed=1 * DEGREES,
                           center=gear_1.center + complex_to_R3((r0+r1) * np.exp(-1j * 15 * DEGREES)), stroke_color=RED)
        gear_2 = Virtual_Gear(pitch_circle_radius=r2, tooth_hight=0.16, tooth_num=z2, inner_radius=0.16,
                           center=gear_1.center + complex_to_R3((r1+r2) * np.exp(1j * 150 * DEGREES)), stroke_color=GREEN)
        # gear_3 is different from mode_01
        gear_3 = Virtual_Gear(pitch_circle_radius=r3, tooth_hight=0.16, tooth_num=z3, inner_radius=0.16,
                      center=gear_1.center + complex_to_R3((r1+r3) * np.exp(1j * 45 * DEGREES)), stroke_color=PINK)

        gear_1.match_angle(gear_0).match_speed(gear_0)
        gear_2.match_angle(gear_1).match_speed(gear_1)
        gear_3.match_angle(gear_0).match_speed(gear_0)

        dot_A = Dot(gear_3.center + complex_to_R3(P3A * np.exp(1j * phi_A)), color=PINK).scale(0.8)
        dot_B = Dot(gear_2.center + complex_to_R3(P2B * np.exp(1j * phi_B)), color=GREEN).scale(0.8)

        rect = Rectangle(height=0.4, width=11.5, stroke_width=2, stroke_color=YELLOW) # .round_corners(0.2)
        hole = Circle(radius=0.1, stroke_width=2, stroke_color=YELLOW).align_to(rect, LEFT).shift(RIGHT * 0.1)
        hole_2 = Dot().set_opacity(0).align_to(rect, RIGHT).shift(LEFT * 0.1)
        line_hole = Rectangle(height=0.18, width=10.5, stroke_width=2, stroke_color=YELLOW).align_to(rect, RIGHT).shift(LEFT * 0.11)

        rod = VGroup(rect, hole, line_hole, hole_2)
        gear_3.add(dot_A), gear_2.add(dot_B)

        poly_5 = Polygon([-0.2, 3., 0], [0.2, 3., 0], [0.2, 0, 0], [0, -0.2 * np.sqrt(3), 0], [-0.2, 0, 0],
                         stroke_width=2, stroke_color=YELLOW) # .round_corners(0.2)
        hole_01 = Circle(radius=0.1, stroke_width=2, stroke_color=YELLOW).align_to(poly_5, DOWN).shift(UP * 0.1)
        line_hole_01 = Rectangle(height=2.5, width=0.18, stroke_width=2, stroke_color=YELLOW).align_to(poly_5, UP).shift(DOWN * 0.11)
        dot_D = Dot(hole_01.get_center(), color=BLUE).scale(0.8)
        rod_2 = VGroup(poly_5, hole_01, line_hole_01, dot_D).rotate(PI)
        rod_2.shift(hole.get_center()-hole_01.get_center() + AC * RIGHT + CD * UP)

        c0 = Circle(radius=0.18, stroke_width=2, stroke_color=YELLOW).shift(hole.get_center()+AC*RIGHT)
        c1 = Dot(color=YELLOW).scale(0.85).shift(hole.get_center()+AC*RIGHT)
        rods = VGroup(rod, rod_2, VGroup(c0, c1))

        def update_rod(r):
            r.shift(dot_A.get_center() - hole.get_center())
            AB = dot_B.get_center() - dot_A.get_center()
            vect_old = hole_2.get_center() - hole.get_center()
            r.rotate(np.angle(complex(*AB[:2]))-np.angle(complex(*vect_old[:2])), about_point=hole.get_center())

        rods.add_updater(update_rod)

        gears = Gear_system(gear_0, gear_1, gear_2, gear_3)
        # gears.update_gears()
        path = TracedPath(dot_D.get_center, stroke_color=self.stroke_config['color'],
                          min_distance_to_new_point=0.02, stroke_width=self.stroke_config['width'])
        path.add_updater(lambda p: p.rotate(gears.w.get_value() * gear_1.speed, about_point=gear_1.center))

        self.add(gears, rods, path)
        gears.set_opacity(0)
        rods.set_opacity(0)

        self.wait(1)
        gears.w.set_value(self.gears_config['w'])
        self.wait(1/60)
        for i in range(self.step_num):
            for g in gears:
                g.rotate_gear(g.speed * gears.w.get_value())
            if i % int(PI * 2 / (gears.w.get_value() * gear_1.speed)) == 0:
                self.wait(1/self.camera.frame_rate)
                # self.wait(0)
            else:
                self.wait(0)
            print('step_%d' % i, end='\t')
            print('frame_%d' % int(abs(i / int(PI * 2 / (gears.w.get_value() * gear_1.speed)))))

        self.wait(self.wait_time)


class Curve_1(OnlyCurve):
    CONFIG = {
        'gears_config':{
            'r1': 3.2,
            'z': [36, 75, 37, 30],
            'l': [1, 1.2, 1, 3.6],
            'a': [PI/6, 36 *DEGREES, PI/2],
            'w': 10/4,
        },
        'step_num': 3330 * 2 * 4,
        'wait_time': 5,
    }


class Curve_1_02(OnlyCurve):
    CONFIG = {
        'gears_config':{
            'r1': 3.2 * 1.1,
            'z': [36, 75, 37, 30],
            'l': np.array([0.9, 1., 1.2, 3.6]) * 1.1,
            'a': [PI/6, 36 *DEGREES, PI/2],
            'w': 10,
        },
        'step_num': 3330 * 2,
        'wait_time': 5,
    }


class Curve_2(OnlyCurve):
    CONFIG = {
        'gears_config':{
            'r1': 2.8,
            'z': [36, 75, 47, 60],
            'l': [1.8, 1.25, 1.1, 3.6],
            'a': [PI/6, 36 *DEGREES, PI/2],
            'w': 10/2,
        },
        'step_num': 3930 * 2,
        'wait_time': 5,
    }


class Curve_3(OnlyCurve):
    CONFIG = {
        'gears_config':{
            'r1': 3.25,
            'z': [36, 72, 46, 32],
            'l': [1., 0.9, 1., 4],
            'a': [0 *DEGREES, 45 *DEGREES, PI/2],
            'w': 10/2,
        },
        'step_num': 1656 * 2 * 8,
        'wait_time': 5,
    }


class Curve_4(OnlyCurve):
    CONFIG = {
        'gears_config':{
            'r1': 3,
            'z': [36, 72, 39, 54],
            'l': np.array([1.4, 1.2, 1.4, 3.6]) * 1.05,
            'a': [30 * DEGREES, 15 * DEGREES, PI/2],
            'w': 10/2,
        },
        'step_num': 2808 * 4,
        'wait_time': 5,
    }


class Curve_5(OnlyCurve):
    CONFIG = {
        'gears_config':{
            'r1': 3 * 1.1,
            'z': [36, 72, 39, 48],
            'l': np.array([1.4, 1.2, 2.4, 3.6]) * 1.1,
            'a': [30 * DEGREES, 45 * DEGREES, PI/2],
            'w': 10/4,
        },
        'step_num': 1872*4,
        'wait_time': 5,
    }


class Curve_5_2(OnlyCurve):
    CONFIG = {
        'gears_config':{
            'r1': 3.25,
            'z': [36, 72, 39, 48],
            'l': [1.6, 1.0, 4, 3.6],
            'a': [30 * DEGREES, 45 * DEGREES, PI/2],
            'w': 10/4,
        },
        'step_num': 1872 * 4,
        'wait_time': 5,
    }


class Curve_mode02_1(OnlyCurve_mode02):
    CONFIG = {
        'gears_config':{
            'r1': 4.5,
            'z': [36, 60, 37, 30],
            'l': np.array([3.2, 1.25, 4.5, 3.6]) * 1.05,
            'a': [-30 *DEGREES, 135 *DEGREES, PI/2],
            'w': 10/4,
        },
        'step_num': 2220 * 4,
        'wait_time4': 5,
    }


class Curve_mode02_2(OnlyCurve_mode02):
    CONFIG = {
        'gears_config':{
            'r1': 6,
            'z': [36, 60, 37, 30],
            'l': np.array([1, 1.8, 3.2, 5.6]) * 1.5,
            'a': [-30 *DEGREES, 160 *DEGREES, PI/2],
            'w': 5,
        },
        'step_num': 2220*2,
        'wait_time4': 5,
    }


class Curve_mode01_2_1(OnlyCurve_mode01_2):
    CONFIG = {
        'gears_config':{
            'r1': 4.5,
            'z': [36, 75, 46, 45],
            'l': [1.6, 1.2, 4., 4],
            'a': [140 *DEGREES, -30 *DEGREES, PI/2],
            'w': 10 * 2,
        },
        'step_num': int(2070/2),
        'wait_time4': 5,
    }


class Curve_mode01_2_2(OnlyCurve_mode01_2):
    CONFIG = {
        'gears_config':{
            'r1': 3.6,
            'z': [36, 72, 46, 48],
            'l': np.array([1.5, 1.8, 1.6, 3.1]) * 1.,
            'a': [-50 *DEGREES, 135 *DEGREES, PI/2],
            'w': 10,
        },
        'step_num': int(3312),
        'wait_time4': 5,
    }


class CurveByCoiling(ParametricFunction):

    CONFIG = {
        'T_func': 19,
        'T_rotate': 23,
        'func': None,
        'func_center': 1 * UR / np.sqrt(2),
        "step_size": 0.05,
        "dt": 1e-3,
    }

    def __init__(self, **kwargs):

        Container.__init__(self, **kwargs)

        if self.func == None:
            self.func = lambda t: 1

        function = lambda t: complex_to_R3((self.func(t) * np.exp(1j * t * TAU / self.T_func) + R3_to_complex(self.func_center)) * np.exp(1j * t * TAU / self.T_rotate))
        ParametricFunction.__init__(self, function=function, **kwargs)

from numpy import sin, cos
class Test_CurveByCoiling(Scene):

    CONFIG = {
        'camera_config': {
            'background_color': WHITE,
        }
    }

    def construct(self):

        # T1, T2 = 8, 6
        w1, w2 = 3, 4
        curve_0 = ParametricFunction(function=lambda t: complex_to_R3(1 * cos(t * TAU * w1) + sin(t * TAU * w2) * 1j), t_min=0, t_max=12, color=BLUE_D, stroke_width=1,)
        # curve = CurveByCoiling(func=lambda t: 1 * sin(t * TAU/T1 * 5) + cos(t * TAU/T2 * 4) * 1j,
        #                        color=BLUE_D, stroke_width=1,
        #                        func_center=2.4 * RIGHT, T_func=T1, T_rotate=T2,
        #                        t_min=0, t_max=T1 * T2)

        self.add(curve_0)
        self.wait(2)


class Graph_Curve(Scene):

    CONFIG = {
        'camera_config': {
            'background_color': WHITE,
        },
        'gear_center': [ORIGIN, UL * 4.2, RIGHT * 5 + DOWN * 2],
        'rod_loc': [UR * 2., UP * 3.6],
        'AC_CD': [4., 5.],
        'T': [33, -22, 3 * 17],
        'rotate_D': True,
        # 'total_time': 11 * 21,
        'scale_factor': 0.4,
        'precision_factor': 10,
    }

    def construct(self):

        P1, P2, P3 = self.gear_center
        vect_P2A, vect_P3B= self.rod_loc
        phi_A, phi_B = np.angle(R3_to_complex(vect_P2A)), np.angle(R3_to_complex(vect_P3B))
        P2A, P3B = get_norm(vect_P2A), get_norm(vect_P3B)
        theta_BCD = PI/2
        AC, CD = self.AC_CD
        T1, T2, T3 = self.T

        t = ValueTracker(0)
        w = 1
        s = self.scale_factor
        dot_1, dot_2, dot_3 = Dot(P1 * s, color=PINK), Dot(P2 * s, color=PINK), Dot(P3 * s, color=PINK)

        dot_A = Dot(color=RED)
        dot_B = Dot(color=YELLOW)
        dot_C = Dot(color=GREEN)
        dot_D = Dot(color=BLUE_D)
        dots = VGroup(dot_A, dot_B, dot_C, dot_D)
        rod_P2A = Rod(P2 * s, (P2+vect_P2A) * s, color=ORANGE)
        rod_P3B = Rod(P3 * s, (P3+vect_P3B) * s, color=RED)
        rod_AB = Rod(ORIGIN, ORIGIN + RIGHT * 18 * s, choose_type=[2, 0], color=BLUE)
        rod_CD = Rod(AC * RIGHT * s, (AC * RIGHT + CD * DOWN) * s, choose_type=[1,1], color=BLUE)
        rod_AB.add(rod_CD)
        rods = VGroup(rod_P2A, rod_P3B, rod_AB)
        rod_P2A.add_updater(lambda r: r.reposition(P2 * s, dot_A.get_center()))
        rod_P3B.add_updater(lambda r: r.reposition(P3 * s, dot_B.get_center()).set_plot_depth(2))
        rod_AB.add_updater(lambda r: r.reposition(dot_A.get_center(), dot_B.get_center()).set_plot_depth(0.5))
        slider = Rectangle(color=YELLOW).set_height(0.3).set_plot_depth(1)
        slider.add_updater(lambda s: s.become(Rectangle(color=YELLOW, fill_color=WHITE, fill_opacity=1).set_height(0.3).move_to(dot_B).set_plot_depth(1)
                                              .rotate(np.angle(R3_to_complex(dot_B.get_center()-dot_A.get_center())))))

        def update_dot(d):

            A = P2 + P2A * complex_to_R3(np.exp(1j * (TAU/T2 * w * t.get_value() + phi_A)))
            B = P3 + P3B * complex_to_R3(np.exp(1j * (TAU/T3 * w * t.get_value() + phi_B)))
            AB = B - A
            C = A + AB / get_norm(AB) * AC
            D = C + CD * complex_to_R3(np.exp(1j * (np.angle(complex(*AB[0:2])) - theta_BCD)))

            d[0].move_to(s * A)
            d[1].move_to(s * B)
            d[2].move_to(s * C)
            d[-1].move_to(s * D)

        dots.add_updater(update_dot)
        path = TracedPath(dot_D.get_center, min_distance_to_new_point=0.02, stroke_color=BLUE_D, stroke_width=1.2)

        octagon = RegularPolygon(n=8, stroke_width=0.8, stroke_color=BLUE).rotate(PI/8).set_height(7.2).set_plot_depth(-1)
        if self.rotate_D:
            self.add(octagon)
            octagon.add_updater(lambda o: o.become(RegularPolygon(n=8, stroke_width=0.8, stroke_color=BLUE).rotate(PI/8).set_height(7.2).set_plot_depth(-1)
                                           .rotate(w * TAU / T1 * t.get_value())))
        self.add(dot_1, dot_2, dot_3, dots, path, slider, *rods)
        self.wait(1)

        T23 = abs(T2 * T3/gcd(int(T2), int(T3)))
        if self.rotate_D:
            m = self.precision_factor
            path.add_updater(lambda p: p.rotate(w * TAU/T1 * m / self.camera.frame_rate, about_point=ORIGIN))
            self.play(t.set_value, abs(T1 * T23/gcd(int(T1), int(T23))), rate_func=linear, run_time=abs(T1 * T23/gcd(int(T1), int(T23)))/m)
        else:
            m = self.precision_factor + 15
            self.play(t.set_value, T23, rate_func=linear, run_time=T23/m)
        dots.clear_updaters()
        path.clear_updaters()
        self.wait()
        self.play(FadeOut(dot_1), FadeOut(dot_2), FadeOut(dot_3), FadeOut(dots), FadeOut(rods), Uncreate(slider), run_time=1.2)
        self.wait(4)


class Graph_Curve_NotRotate(Graph_Curve):

    CONFIG = {
        'rotate_D': False,
    }

class Graph_Curve_Rotate(Graph_Curve):

    CONFIG = {
        'rotate_D': True,
    }

class Graph_1(Graph_Curve):

    CONFIG = {
        'camera_config': {
            'background_color': WHITE,
        },
        'gear_center': [ORIGIN, RIGHT * 6 + UP * 2.5, UP * 4.8 + LEFT * 6],
        'rod_loc': [UR * 3., DL * 1.6],
        'AC_CD': [6., -5.6],
        'T': [32, -31, 16],
        'rotate_D': True,
        'scale_factor': 0.5,
        'precision_factor': 10,
    }

class Graph_1_NR(Graph_1):

    CONFIG = {
        'rotate_D': False,
        'scale_factor': 0.5,
        'precision_factor': 10,
    }

class Graph_2(Graph_Curve):

    CONFIG = {
        'camera_config': {
            'background_color': WHITE,
        },
        'gear_center': [ORIGIN, LEFT * 12 + UP * 7.5, LEFT * 3 + UP * 3],
        'rod_loc': [UR * 1.6, DR * 2.],
        'AC_CD': [15, -8],
        'T': [50, -19, 30],
        'rotate_D': True,
        'scale_factor': 0.22,
        'precision_factor': 25,
    }

class Graph_2_NR(Graph_2):

    CONFIG = {
        'rotate_D': False,
        'scale_factor': 0.4,
        'precision_factor': 20,
    }

class Linkage_Graph_01(Scene):

    CONFIG = {
        'camera_config': {
            'background_color': WHITE,
        },
        'rotate_center': [LEFT * 3.4 + DOWN * 1.5, RIGHT * 0.8 + DOWN * 1.5],
        'bar_1': [140 * DEGREES, 1.2],
        'bar_2': [30 * DEGREES, 0.8],
        'bar_3': [30 * DEGREES, 4.8],
        'bar_5': [-90 * DEGREES, 2., 0.5],
        'T': [19, -12, 18],
        'rotate_D': True,
        # 'total_time': 11 * 21,
        'scale_factor': 1,
        'precision_factor': 10,
    }

    def construct(self):

        s = self.scale_factor
        O1, O2 = self.rotate_center
        dot_O1 = Dot(O1 * s, color=PINK).set_plot_depth(-1)
        dot_O2 = Dot(O2 * s, color=PINK).set_plot_depth(-1)

        init_angle_1, length_1 = self.bar_1
        init_angle_2, length_2 = self.bar_2
        init_angle_3, length_3 = self.bar_3

        bar_1 = Bar(O1 * s, init_angle_1, length_1 * s, color=YELLOW)
        bar_2 = Bar(O2 * s, init_angle_2, length_2 * s, color=RED)
        bar_3 = Bar(bar_1.get_end(), init_angle_3, length_3 * s, end_type=[2, 2], color=BLUE_D)
        bar_4 = Rod(bar_2.get_end(), bar_3.get_end(), end_type=[2, 1], color=BLUE_D)
        bar_5 = Bar((1-self.bar_5[-1]) * bar_3.get_start() + self.bar_5[-1] * bar_3.get_end(), bar_3.get_angle() + self.bar_5[0], self.bar_5[1] * s, end_type=[1, 1], color=BLUE_D)
        bar_4.add(bar_3)
        bars = VGroup(bar_1, bar_2, bar_3, bar_4)
        t = ValueTracker(0)
        T0, T1, T2 = self.T
        w = 1
        w0 = TAU/T0 * w
        w1 = TAU/T1 * w
        w2 = TAU/T2 * w

        def update_bars(b):
            err = 1e-3
            b[0].reposition_by_angle(t.get_value() * w0 + init_angle_1)
            b[1].reposition_by_angle(t.get_value() * w1 + init_angle_2)
            # b[2].reposition_by_angle(angle=None, start=b[0].get_end())
            # b[3].reposition_by_angle(angle=None, start=b[1].get_end())
            b[2].reposition(b[0].get_end(), b[3].get_end())
            b[3].reposition(b[1].get_end(), b[2].get_end())
            # print('theta=%.2f, error=%.5f' % (t.get_value() / PI * 180, get_norm(b[2].get_end() - b[3].get_end())))
            while get_norm(b[2].get_end() - b[3].get_end()) > err:
                b[2].reposition(b[0].get_end(), b[3].get_end())
                b[3].reposition(b[1].get_end(), b[2].get_end())
                # print('theta=%.2f, error=%.5f' % (t.get_value() / PI * 180, get_norm(b[2].get_end() - b[3].get_end())))

        T01 = lcm(T0, T1)
        T012 = lcm(T01, T2)
        rotate_time = T012 / (self.precision_factor + 10)

        self.add(bars, dot_O1, dot_O2)
        bars.add_updater(update_bars)
        path = TracedPath(bar_5.get_end, stroke_color=BLUE_D, stroke_width=1.6)
        self.add(path)
        path.add_updater(lambda p: p.rotate_about_origin(w2 * T012/self.camera.frame_rate/rotate_time))
        self.play(t.set_value, abs(T012), rate_func=linear, run_time=rotate_time)
        # self.play(t.set_value, abs(T01), rate_func=linear, run_time=rotate_time)
        path.clear_updaters()
        bars.clear_updaters()
        self.wait(1.5)
        self.play(FadeOut(dot_O1), FadeOut(dot_O2), FadeOut(bars), run_time=1.2)
        self.wait(4)

func_rotate = lambda t, r0=1, w0=1, phi_0=0, P0=0+0*1j: r0 * np.exp(1j * (w0 * t + phi_0)) + P0

def my_curve(t, r_list, w_list, phi_list, P_list):

    AC, CD = r_list[2], r_list[3]
    get_A = lambda t_: func_rotate(t_, r_list[0], w_list[0], phi_list[0], P_list[0])
    get_B = lambda t_: func_rotate(t_, r_list[1], w_list[1], phi_list[1], P_list[1])
    get_D = lambda t_: np.sqrt(AC ** 2 + CD ** 2) * np.exp(1j * (np.angle(get_B(t_) - get_A(t_)) + np.angle(AC + 1j * CD))) + get_A(t_)
    return get_D(t)

def my_curve_rotate(t, r_list, w_list, phi_list, P_list):

    AC, CD = r_list[2], r_list[3]
    get_A = lambda t_: func_rotate(t_, r_list[0], w_list[0], phi_list[0], P_list[0])
    get_B = lambda t_: func_rotate(t_, r_list[1], w_list[1], phi_list[1], P_list[1])
    get_D = lambda t_: (np.sqrt(AC ** 2 + CD ** 2) * np.exp(1j * (np.angle(get_B(t_) - get_A(t_)) + np.angle(AC + 1j * CD))) + get_A(t_)) * np.exp(w_list[2] * t * 1j)
    return get_D(t)

class Show_Curve_by_func(Scene):

    CONFIG = {
        'camera_config': {
            'background_color': WHITE,
        },
        'P_list': [complex(-4, 2.5), complex(3, -1)],
        'r_list': [1.6, 1.2, 5, -1],
        'phi_list': [120 * DEGREES, 30 * DEGREES],
        'T': [22, -3 * 17, 44],
        'rotate_or_not': True,
        # 'total_time': 11 * 21,
        # 'scale_factor': 1.6,
        'precision_factor': 5, # different from the precision_factor in other class
    }

    def construct(self):

        w = 1
        w_list = TAU/self.T[0] * w, TAU/self.T[1] * w, TAU/self.T[2] * w

        # curve_A = ParametricFunction(function=lambda t: complex_to_R3(func_rotate(t, self.r_list[0], w_list[0], self.phi_list[0], self.P_list[0])), t_min=0, t_max=t_total, color=RED)
        # curve_B = ParametricFunction(function=lambda t: complex_to_R3(func_rotate(t, self.r_list[1], w_list[1], self.phi_list[1], self.P_list[1])), t_min=0, t_max=t_total, color=PINK)

        if self.rotate_or_not:
            t_total = lcm(lcm(self.T[0], self.T[1]), self.T[2])
            print('t_total: %.2f' % t_total)
            curve = ParametricFunction(function=lambda t: complex_to_R3(my_curve_rotate(t, self.r_list, w_list, self.phi_list, self.P_list)), t_min=0, t_max=t_total, color=BLUE_D, stroke_width=1.2, step_size=t_total/1000/self.precision_factor).set_height(7.2).move_to(ORIGIN)
        else:
            t_total = lcm(self.T[0], self.T[1])
            print('t_total: %.2f' % t_total)
            curve = ParametricFunction(function=lambda t: complex_to_R3(my_curve(t, self.r_list, w_list, self.phi_list, self.P_list)), t_min=0, t_max=t_total, color=BLUE_D, stroke_width=1.2, step_size=t_total/1000/self.precision_factor)#.set_height(6).move_to(ORIGIN)

        self.add(curve)
        # self.play(ShowCreation(curve), run_time=50)
        self.wait(2)


class Curve_by_func_01(Show_Curve_by_func):

    CONFIG = {
        'camera_config': {
            'background_color': WHITE,
        },
        'P_list': [complex(-4, 2.5), complex(3, -1)],
        'r_list': [1.8, 1.5, 3., -1.5],
        'phi_list': [120 * DEGREES, 30 * DEGREES],
        'T': [22, -3 * 13, 55],
        'rotate_or_not': True,
        # 'total_time': 11 * 21,
        # 'scale_factor': 1.6,
        'precision_factor': 4, # different from the precision_factor in other class
    }


class Curve_by_func_02(Show_Curve_by_func):

    CONFIG = {
        'camera_config': {
            'background_color': WHITE,
        },
        'P_list': [complex(-4, 2.5), complex(3, -1)],
        'r_list': [4, 1, 6.4, -2.4],
        'phi_list': [120 * DEGREES, 30 * DEGREES],
        'T': [29, -31, 31 * 8],
        'rotate_or_not': True,
        # 'total_time': 11 * 21,
        # 'scale_factor': 1.6,
        'precision_factor': 2, # different from the precision_factor in other class
    }


class Curve_by_func_03(Show_Curve_by_func):

    CONFIG = {
        'camera_config': {
            'background_color': WHITE,
        },
        'P_list': [complex(-4, 2.5), complex(3, -1)],
        'r_list': [4, 1, 6.4, -2.4],
        'phi_list': [120 * DEGREES, 30 * DEGREES],
        'T': [29, -31, 31 * 5],
        'rotate_or_not': True,
        # 'total_time': 11 * 21,
        # 'scale_factor': 1.6,
        'precision_factor': 2, # different from the precision_factor in other class
    }

