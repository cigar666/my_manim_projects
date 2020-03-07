from manimlib.constants import *
from manimlib.mobject.types.vectorized_mobject import VMobject, VGroup
from manimlib.mobject.geometry import Arc, Line, Dot, Polygon
from manimlib.utils.color import color_gradient
from manimlib.mobject.number_line import DecimalNumber
from manimlib.mobject.svg.tex_mobject import TexMobject
from manimlib.utils.rate_functions import linear, smooth

class Arcs(VGroup):

    CONFIG = {
        'colors': [RED, YELLOW, BLUE, PINK],
        'radius': 1,
        'start_angle':0,
        'angle_list': [30 * DEGREES, 60 * DEGREES, 90 * DEGREES],
        'stroke_width': 40,
    }

    def __init__(self, **kwargs):

        VMobject.__init__(self, **kwargs)
        self.create_arcs()

    def create_arcs(self, **kwargs):
        angle = self.start_angle
        colors = color_gradient(self.colors, len(self.angle_list))
        for i in range(len(self.angle_list)):
            self.add(Arc(radius=self.radius, start_angle=angle, angle=self.angle_list[i], color=colors[i], stroke_width=self.stroke_width, **kwargs))
            angle += self.angle_list[i]

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

class Tracked_Point(VGroup):
    CONFIG = {
        'size': 0.1,
        'point_color': BLUE,
        'num_decimal_places': 2,
        'coordinates_scale': 0.8,
        'coordinates_color': GREEN,
        'coordinates_direction': DOWN * 0.25,
        'bracket_color': WHITE,
    }
    def __init__(self, init_loc=ORIGIN, **kwargs):

        VGroup.__init__(self, **kwargs)
        self.point = Dot(init_loc, color=self.point_color).set_height(self.size)
        self.value_x = DecimalNumber(0, color=self.coordinates_color, num_decimal_places=self.num_decimal_places).scale(self.coordinates_scale)
        self.value_y = DecimalNumber(0, color=self.coordinates_color, num_decimal_places=self.num_decimal_places).scale(self.coordinates_scale)
        text = TexMobject('(', ',', ')').scale(self.coordinates_scale)
        self.coordinates_text = VGroup(text[0], self.value_x, text[1], self.value_y, text[2])
        self.coordinates_text.add_updater(self.update_coordinates_text)
        self.add(self.point)

    def update_coordinates_text(self, coords):
        for i in range(1, len(coords)):
            coords[i].next_to(coords[i-1], RIGHT * 0.5)
        coords[2].align_to(coords[1], DOWN)
        pos = self.point.get_center()
        x, y = self.mapping_func(pos[0], pos[1])
        coords[1].set_value(x)
        coords[3].set_value(y)
        coords.next_to(self.point, self.coordinates_direction)

    def mapping_func(self, x, y):
        return x, y

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

class Trail(VGroup):

    CONFIG = {
        'max_width': 5,
        'nums': 500,
        'trail_color': BLUE_B,
        # 'rate_func': linear,
        'rate_func': lambda t: t ** 1.25,
    }

    def __init__(self, mob, **kwargs):
        VGroup.__init__(self, **kwargs)
        self.add(mob)
        self.trail = VGroup()
        self.path_xyz = []
        self.add(self.trail)
        self.pos_old = self[0].get_center()

    def update_trail(self, trail):
        err=1e-9
        pos_new = self[0].get_center()
        pos_old = self.pos_old
        self.pos_old = pos_new
        # if np.sqrt(sum((pos_new - pos_old) ** 2))>err:
        if sum(abs(pos_new - pos_old))>err:
            trail.add(Line(pos_old, pos_new, color=self.trail_color, plot_depth=0))

        if len(trail) > self.nums:
            trail.remove(trail[0])
            # for k in range(self.nums):
            #     trail[k].set_stroke(width=self.max_width * self.rate_func(k/self.nums),
            #                         opacity=self.rate_func(k/self.nums))
            for l in trail:
                k = trail.submobjects.index(l)
                l.set_stroke(width=self.max_width * self.rate_func(k/self.nums),
                             opacity=self.rate_func(k/self.nums))

        if len(trail) <= self.nums and len(trail) > 0:
            # for k in range(len(trail)):
            #     trail[k].set_stroke(width=self.max_width * self.rate_func(k/len(trail)),
            #                         opacity=self.rate_func(k/len(trail)))
            for l in trail:
                k = trail.submobjects.index(l)
                l.set_stroke(width=self.max_width * self.rate_func(k/len(trail)),
                             opacity=self.rate_func(k/len(trail)))

    def get_path_xyz(self, err=1e-9):
        pos_new = self[0].get_center()
        pos_old = self.pos_old
        if sum(abs(pos_new - pos_old))>err:
            self.path_xyz.append(pos_new)
        self.pos_old = pos_new
        while len(self.path_xyz) > self.nums:
            self.path_xyz.remove(self.path_xyz[0])

    def create_path(self):
        path = VGroup()
        self.get_path_xyz()
        if len(self.path_xyz) > 1:
            for i in range(len(self.path_xyz)-1):
                path.add(Line(self.path_xyz[i], self.path_xyz[i+1], stroke_color=self.trail_color,
                              stroke_opacity=self.rate_func(i/len(self.path_xyz)), plot_depth=self.rate_func(i/len(self.path_xyz)),
                              stroke_width=self.max_width * self.rate_func(i/len(self.path_xyz))))
                # print('i = %d' % i)
                # # print(self.path_xyz)
                # print(self.color)
                # print(self.rate_func(i/len(self.path_xyz)))
                # print(self.max_width*self.rate_func(i/len(self.path_xyz)))
        return path


    def update_path(self, trail):
        trail.become(self.create_path())

    def start_trace(self):
        # self.trail.add_updater(self.update_trail)
        self.trail.add_updater(self.update_path)

class Sun(VGroup):
    CONFIG = {
        'colors': [RED_B, ORANGE, WHITE],
        # 'opacity_func': lambda t: 1.1 - t ** 0.24 if t < 0.1 else 1 - 0.95 * t ** 0.18 - 0.05 * t ** 0.05,

        # 'opacity_func': lambda t: 1000 * (1 - t ** 0.00012) if t < 0.1 else 0.75 * (1 - t ** 0.21),
        # 'opacity_func': lambda t: 1250 * (1 - abs(t-0.006) ** 0.0001) if t < 0.12 else 0.72 * (1 - t ** 0.2),
        'opacity_func': lambda t: 1500 * (1 - abs(t-0.009) ** 0.0001),
        'radius': 4,
        'layer_num': 80,
        # 'rate_func': smooth,
        'rate_func': lambda t: t ** 2,
    }
    def __init__(self, **kwargs):

        VGroup.__init__(self, **kwargs)
        self.color_list = color_gradient(self.colors, self.layer_num)
        self.add(Dot(color=average_color(self.colors[0], WHITE), plot_depth=4).set_height(0.015 * self.radius))
        for i in range(self.layer_num):
            # self.add(Arc(radius= self.radius/self.layer_num * (0.5 + i), angle=TAU, color=self.color_list[i],
            #              stroke_width=100 * self.radius/self.layer_num,
            #              stroke_opacity=self.opacity_func(i/self.layer_num), plot_depth=5))
            self.add(Arc(radius= self.radius * self.rate_func((0.5 + i)/self.layer_num), angle=TAU, color=self.color_list[i],
                         stroke_width=101 * (self.rate_func((i + 1)/self.layer_num) - self.rate_func(i/self.layer_num)) * self.radius,
                         stroke_opacity=self.opacity_func(self.rate_func(i/self.layer_num)), plot_depth=5))

class Three_Body(VGroup):

    CONFIG = {
        'mass': np.array([0.98, 1.025, 1]) * 1.2,
        'pos': np.array([[-3., -np.sqrt(3), 0], [0., 3 * np.sqrt(3) - 1, 0], [3, -np.sqrt(3), 0]]) * 0.75,
        'velocity': np.array([[1, -np.sqrt(3), 0], [-2, 0, 0], [1, np.sqrt(3), 0]]) * 0.8,
        'p_pos': np.array([2, -np.sqrt(3)+1, 0]) * 1.,
        'p_velocity':np.array([-1, -1.7, 0]) * 2.4,
        'plot_depth':5,
    }

    def __init__(self, *three_Mobject, **kwargs):

        VGroup.__init__(self, **kwargs)

        self.sun_01 = three_Mobject[0].move_to(self.pos[0])
        self.sun_02 = three_Mobject[1].move_to(self.pos[1])
        self.sun_03 = three_Mobject[2].move_to(self.pos[2])
        if len(three_Mobject) > 3:
            self.planet = three_Mobject[3].move_to(self.p_pos)
        self.add(self.sun_01, self.sun_02, self.sun_03)
        if len(three_Mobject) > 3:
            self.planet = three_Mobject[3].move_to(self.p_pos)
            self.add(self.planet)

    def get_force(self, x1, x2, m1, m2, G=1):
        # force of obj_01 to obj_02, this vector start from obj_02 and end in obj_01
        r = np.sqrt(sum((x1 - x2) ** 2))
        return G * m1 * m2 * (x1 - x2) / (r ** 3 + 2e-3)

    def update_xyz(self, G=1, delta_t =2.5e-3):

        m1, m2, m3 = self.mass[0], self.mass[1], self.mass[2]
        x1, x2, x3 = self.pos[0], self.pos[1], self.pos[2]
        v1, v2, v3 = self.velocity[0], self.velocity[1], self.velocity[2]
        f21, f31, f32 = self.get_force(x2, x1, m2, m1, G=G), self.get_force(x3, x1, m3, m1, G=G), self.get_force(x3, x2, m3, m2, G=G)
        a1, a2, a3 = (f21 + f31) / m1, (-f21 + f32) / m2, (-f32 - f31) / m3

        xp, vp = self.p_pos, self.p_velocity
        f1, f2, f3 = self.get_force(x1, xp, m1, 1, G=G), self.get_force(x2, xp, m2, 1, G=G), self.get_force(x3, xp, m3, 1, G=G)
        a = (f1 + f2 + f3) / 1.

        self.velocity[0] += a1 * delta_t
        self.velocity[1] += a2 * delta_t
        self.velocity[2] += a3 * delta_t
        self.p_velocity += a * delta_t

        self.pos[0] += v1 * delta_t
        self.pos[1] += v2 * delta_t
        self.pos[2] += v3 * delta_t
        self.p_pos += vp *delta_t

    def reset_velocity(self):
        v1, v2, v3 = self.velocity[0], self.velocity[1], self.velocity[2]
        m1, m2, m3 = self.mass[0], self.mass[1], self.mass[2]
        momentum = v1 * m1 + v2 * m2 + v3 * m3
        v = momentum/(m1 + m2 + m3)
        v1, v2, v3 = v1 - v, v2 - v, v3 - v
        print(v1, v2, v3)
        self.p_velocity -= v
        self.velocity = np.array([v1, v2, v3])

    def update_three_body(self, tb, dt):
        self.update_xyz(G=40)
        # avervage_pos = (self.pos[0] + self.pos[1] + self.pos[2]) / 3
        # tb[0].move_to(self.pos[0] - avervage_pos)
        # tb[1].move_to(self.pos[1] - avervage_pos)
        # tb[2].move_to(self.pos[2] - avervage_pos)
        # if len(tb)>3:
        #     tb[3].move_to(self.p_pos - avervage_pos)
        tb[0].move_to(self.pos[0])
        tb[1].move_to(self.pos[1])
        tb[2].move_to(self.pos[2])
        if len(tb)>3:
            tb[3].move_to(self.p_pos)

    def start_move(self):
        self.add_updater(self.update_three_body)
