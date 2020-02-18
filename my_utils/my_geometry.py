from manimlib.constants import *
from manimlib.mobject.types.vectorized_mobject import VMobject, VGroup
from manimlib.mobject.geometry import Arc

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
