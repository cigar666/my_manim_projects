from manimlib.imports import *


class Gear_outline(VMobject):

    CONFIG = {
        'arc_segments': 4,
        'curve_segments': 6,
    }

    def __init__(self, pitch_circle_radius=2, tooth_hight=0.5, tooth_num=17, **kwargs):

        VMobject.__init__(self, **kwargs)
        self.pitch_circle_radius = pitch_circle_radius
        self.tooth_hight = tooth_hight
        self.tooth_num = tooth_num

        self.rb = self.pitch_circle_radius - self.tooth_hight/2
        self.pitch = self.pitch_circle_radius * 2 * PI / self.tooth_num
        theta_pitch = np.tan(np.arccos(self.rb/self.pitch_circle_radius)) - np.arccos(self.rb/self.pitch_circle_radius)
        theta_top = np.tan(np.arccos(self.rb/(self.rb + self.tooth_hight))) - np.arccos(self.rb/(self.rb + self.tooth_hight))
        alpha_max = np.arccos(self.rb/(self.rb + self.tooth_hight))

        alphas = np.linspace(0, alpha_max, self.curve_segments)
        curve01_radius = self.rb/np.cos(alphas)
        curve01_thetas = np.tan(alphas) - alphas - theta_pitch - TAU/self.tooth_num/2/2
        arc_top_thetas = np.linspace(theta_top - theta_pitch - TAU/self.tooth_num/2/2, -(theta_top - theta_pitch - TAU/self.tooth_num/2/2), self.arc_segments)
        curve02_radius = self.rb/np.cos(alphas)
        curve02_thetas = -curve01_thetas
        arc_bottom_thetas = np.linspace(theta_pitch + TAU/self.tooth_num/2/2, -(theta_pitch + TAU/self.tooth_num/2/2) + TAU/self.tooth_num, self.arc_segments)
        arc_top_radius = np.array([(self.rb + self.tooth_hight) for i in range(self.arc_segments)])
        arc_bottom_radius = np.array([self.rb for i in range(self.arc_segments)])
        part_01_thetas = np.concatenate((curve01_thetas, arc_top_thetas[1:-1], curve02_thetas[::-1], arc_bottom_thetas[1:-1]), axis=0)
        part_01_radius = np.concatenate((curve01_radius, arc_top_radius[1:-1], curve02_radius[::-1], arc_bottom_radius[1:-1]), axis=0)

        all_part_thetas = part_01_thetas
        all_part_radius = part_01_radius
        for i in range(1, self.tooth_num):
            all_part_thetas = np.concatenate((all_part_thetas, part_01_thetas + i * TAU/self.tooth_num), axis=0)
            all_part_radius = np.concatenate((all_part_radius, part_01_radius), axis=0)


        vertices = self.polar2xyz(all_part_radius, all_part_thetas)

        self.set_points_as_corners(
            [*vertices, vertices[0]]
        )

    def polar2xyz(self, r, theta):
        if type(theta) == np.ndarray:
            if type(r) == np.ndarray:

                return np.concatenate((np.cos(theta).reshape(-1, 1), np.sin(theta).reshape(-1, 1), theta.reshape(-1, 1) * 0), axis=1) * r.reshape(-1, 1)
            else:
                return np.concatenate((np.cos(theta).reshape(-1, 1), np.sin(theta).reshape(-1, 1), theta.reshape(-1, 1) * 0), axis=1) * r
        else:
            return np.array([np.cos(theta), np.sin(theta), 0]) * r

    def get_vertices(self):
        return self.get_start_anchors()

    def round_corners(self, radius=0.01):
        vertices = self.get_vertices()
        arcs = []
        for v1, v2, v3 in adjacent_n_tuples(vertices, 3):
            vect1 = v2 - v1
            vect2 = v3 - v2
            unit_vect1 = normalize(vect1)
            unit_vect2 = normalize(vect2)
            angle = angle_between_vectors(vect1, vect2)
            # Negative radius gives concave curves
            angle *= np.sign(radius)
            # Distance between vertex and start of the arc
            cut_off_length = radius * np.tan(angle / 2)
            # Determines counterclockwise vs. clockwise
            sign = np.sign(np.cross(vect1, vect2)[2])
            arc = ArcBetweenPoints(
                v2 - unit_vect1 * cut_off_length,
                v2 + unit_vect2 * cut_off_length,
                angle=sign * angle
            )
            arcs.append(arc)

        self.clear_points()
        # To ensure that we loop through starting with last
        arcs = [arcs[-1], *arcs[:-1]]
        for arc1, arc2 in adjacent_pairs(arcs):
            self.append_points(arc1.points)
            line = Line(arc1.get_end(), arc2.get_start())
            # Make sure anchors are evenly distributed
            len_ratio = line.get_length() / arc1.get_arc_length()
            line.insert_n_curves(
                int(arc1.get_num_curves() * len_ratio)
            )
            self.append_points(line.get_points())
        return self


class Gear(VGroup):

    CONFIG = {
        'center': ORIGIN,
        'inner_radius': 0.5,
        'stroke_width': 2,
        'stroke_color': WHITE,
        'init_angle': 0,
        'speed': 0,
    }

    def __init__(self, pitch_circle_radius=2, tooth_hight=0.5, tooth_num=17, **kwargs):

        VGroup.__init__(self, **kwargs)
        self.r = pitch_circle_radius
        self.z = tooth_num
        self.outline = Gear_outline(pitch_circle_radius, tooth_hight, tooth_num).set_stroke(self.stroke_color, self.stroke_width)
        self.hole = Circle(radius=self.inner_radius).set_stroke(self.stroke_color, self.stroke_width)
        self.add(self.outline, self.hole)
        self.shift(self.center)
        self.angle = 0
        self.rotate_gear(self.init_angle)


    def rotate_gear(self, theta):
        self.rotate(theta, about_point=self.center)
        self.angle += theta
        return self

    def set_speed(self, w):
        self.speed = w
        return self

    def match_angle(self, gear_1, revese=True):
        # 只针对外啮合， 内啮合不用减d_theta，转过角度的符号也会改变 #
        O, O1 = self.center, gear_1.center
        OO1 = O1 - O
        a = np.angle(complex(*OO1[0:2]))
        d_theta = TAU / self.z / 2
        if a > 0:
            self.rotate_gear(a - (gear_1.angle - (PI - a)) * gear_1.z / self.z + d_theta - self.angle)
        else:
            self.rotate_gear(a - (gear_1.angle + (PI - a)) * gear_1.z / self.z + d_theta - self.angle)
        return self

    def match_speed(self, gear_1, revese=True):
        self.set_speed(gear_1.speed * gear_1.z / self.z * (-1 if revese else 1))
        return self


class Virtual_Gear(Gear):
    def __init__(self, pitch_circle_radius=2, tooth_hight=0.5, tooth_num=17, **kwargs):
        Gear.__init__(self, pitch_circle_radius=pitch_circle_radius,
                      tooth_hight=tooth_hight, tooth_num=tooth_num, **kwargs)
        self.remove(self.outline), self.remove(self.hole)


class Test_Gears(Scene):

    def construct(self):

        r1 = 2.4
        z0, z1, z2, z3 = 20, 54, 24, 18
        r0, r2, r3 = r1 * z0 / z1, r1 * z2 / z1, r1 * z3 / z1
        center = DOWN * 0.5

        gear_1 = FakeGear(pitch_circle_radius=r1, tooth_hight=0.15, tooth_num=z1, inner_radius=0.3, center=center)
        gear_0 = Gear(pitch_circle_radius=r0, tooth_hight=0.15, tooth_num=z0, inner_radius=0.16, speed=1 * DEGREES,
                      center=gear_1.center + complex_to_R3((r0+r1) * np.exp(-1j * PI/6)))
        gear_2 = Gear(pitch_circle_radius=r2, tooth_hight=0.15, tooth_num=z2, inner_radius=0.16,
                      center=gear_1.center + complex_to_R3((r1+r2) * np.exp(1j * 2 * PI/3)))
        gear_3 = Gear(pitch_circle_radius=r3, tooth_hight=0.15, tooth_num=z3, inner_radius=0.16,
                      center=gear_0.center + complex_to_R3((r0+r3) * np.exp(1j * PI/3)))


        gear_1.match_angle(gear_0).match_speed(gear_0)
        gear_2.match_angle(gear_1).match_speed(gear_1)
        gear_3.match_angle(gear_0).match_speed(gear_0)
        self.add(gear_0, gear_1, gear_2, gear_3)

        # w = ValueTracker(0)
        #
        # gears = VGroup(gear_0, gear_1, gear_2, gear_3)
        #
        # def update_gear(g, dt):
        #     g.rotate_gear(g.speed * w.get_value())
        # gear_0.add_updater(update_gear)
        # gear_1.add_updater(update_gear)
        # gear_2.add_updater(update_gear)
        # gear_3.add_updater(update_gear)

        gears = Gear_system(gear_0, gear_1, gear_2, gear_3)
        gears.update_gears()

        self.wait(1)
        self.play(gears.w.set_value, 2.5, run_time=4)
        self.wait()
        self.play(gears.w.set_value, -5, rate_func=there_and_back, run_time=8)
        self.wait(2)


class Gear_system(VGroup):

    def __init__(self, *gears, **kwargs):
        VGroup.__init__(self, *gears, **kwargs)
        self.w = ValueTracker(0)

    def update_gear(self, g, dt):
        g.rotate_gear(g.speed * self.w.get_value())

    def update_gears(self):
        for gear in self:
            gear.add_updater(self.update_gear)
        return self

    def stop_update(self):
        for gear in self:
            gear.clear_updaters()


class Rod(VGroup):

    CONFIG = {
        # 'start': ORIGIN,
        # 'end': UR,
        'color': BLUE,
        'tip_type_1': {
            'radius': 0.08,
        },
        'tip_type_2': {
            'inner_radius': 0.105,
            'radius': 0.15,
        },
        'rod_width': 0.09,
        'end_type': [2, 1],
        'line_buff': -0.02
    }

    def __init__(self, start=ORIGIN, end=UR, **kwargs):

        VGroup.__init__(self, **kwargs)
        self.start, self.end = start, end

        self.create_rod()
        self.start_dot = Dot(start).set_opacity(0)
        self.end_dot = Dot(end).set_opacity(0)
        self.add(self.start_dot, self.end_dot)
        self.length = self.get_rod_length()

    def create_rod(self):
        start, end = self.start, self.end

        if self.end_type[0] == 1:
            self.start_tip = self.add_tip_1(start)
        elif self.end_type[0] == 2:
            self.start_tip = self.add_tip_2(start)
        else:
            print('tip type error in start point!')
            self.start_tip = Dot(self.start, color=self.color).set_height(self.rod_width)
            self.add(self.start_tip)
        if self.end_type[1] == 1:
            self.end_tip = self.add_tip_1(end)
        elif self.end_type[1] == 2:
            self.end_tip = self.add_tip_2(end)
        else:
            print('tip type error in end point!')
            self.end_tip = Dot(self.end, color=self.color).set_height(self.rod_width)
            self.add(self.end_tip)

        vect = normalize(end - start)
        self.rod = Line(start + (self.start_tip.get_height() - 0.05)/2 * vect,
                        end - (self.end_tip.get_height() - 0.05)/2 * vect,
                        color=self.color, stroke_width=self.rod_width * 100)# .scale(1 - self.line_buff)
        self.add(self.rod)
        return self

    def add_tip_1(self, loc):
        tip = Dot(loc, color=self.color).set_height(2 * self.tip_type_1['radius'])
        self.add(tip)
        return tip

    def add_tip_2(self, loc):
        tip = Annulus(inner_radius=self.tip_type_2['inner_radius'],
                      outer_radius=self.tip_type_2['radius'],
                      color=self.color, stroke_color=self.color).move_to(loc)
        self.add(tip)
        return tip

    def reposition(self, A, B):
        self.shift(A - self.start)
        self.rotate(np.angle(R3_to_complex(B - A)) - self.rod.get_angle(), about_point=A)

        self.start = A
        self.end = A + self.length * (B - A)/get_norm(B - A)
        return self

    def reposition_by_angle(self, angle=None, start=None):
        if type(start) == type(None):
            start = self.start

        if type(angle) == type(None):
            angle = self.get_angle()

        A, B = start, start + complex_to_R3(np.exp(angle * 1j))
        self.reposition(A, B)
        return self

    def rotate_about_start(self, angle):
        self.rotate(angle, about_point=self.start)
        return self

    def rotate_about_end(self, angle):
        self.rotate(angle, about_point=self.end)
        return self

    def get_end(self):
        return self.end_dot.get_center()

    def get_start(self):
        return self.start_dot.get_center()

    def get_angle(self):
        return np.angle(R3_to_complex(self.end - self.start))

    def get_rod_length(self):
        return get_norm(self.end - self.start)

    def generate_rod_by_length(self, l, **kwargs):
        start, end = self.start, self.start + (self.end - self.start) * l/get_norm(self.end - self.start)
        self.__init__(self, start=start, end=end, **kwargs)
        return self


class Bar(Rod):

    def __init__(self, start=ORIGIN, angle=0*DEGREES, length=2, **kwargs):

        end = start + complex_to_R3(length * np.exp(1j * angle))
        Rod.__init__(self, start=start, end=end, **kwargs)


class Test_rod(Scene):

    def construct(self):

        dot_1 = Dot(LEFT * 2, color=GREEN)
        rod_1 = Rod(LEFT * 2, LEFT * 2 + RIGHT * 2 * np.sqrt(3) + DOWN * 2)
        rod_2 = Bar(rod_1.get_end(), 45*DEGREES, 3)
        self.add(dot_1, rod_1, rod_2)
        self.wait(2)
