from manimlib.constants import *
from manimlib.mobject.types.vectorized_mobject import VGroup
from manimlib.mobject.three_dimensions import Cube
from manimlib.utils.color import color_gradient

class MyBox(Cube):

    CONFIG = {
        'pos': ORIGIN,
        'box_height': 2,
        'bottom_size': [1, 1],
        'fill_opacity': 1,
    }

    def __init__(self, **kwargs):
        Cube.__init__(self, **kwargs)
        self.box_size = np.array([self.bottom_size[0], self.bottom_size[1], self.box_height])
        self.scale(self.box_size/2)
        # self.move_to(self.pos + self.box_height * OUT/2)
        self.move_to(self.pos)
        self.reset_color()

    def update_height(self, new_height):
        self.scale(np.array([1, 1, new_height/self.box_height])) #.shift(OUT * (new_height - self.height)/2)
        self.box_height = new_height

    def update_top_and_bottom(self, top, bottom):
        new_height = abs(top-bottom)
        old_center = self.get_center()
        self.update_height(new_height)
        self.shift(((top+bottom)/2 - old_center[-1]) * OUT)

    def update_top(self, top):
        bottom = self.get_center()[-1] - self.box_height/2
        self.update_top_and_bottom(top, bottom)

    def update_bottom(self, bottom):
        top = self.get_center()[-1] + self.box_height/2
        self.update_top_and_bottom(top, bottom)

    def reset_color(self):
        colors = color_gradient([WHITE, self.get_color(), BLACK], 11)
        self[0].set_fill(color=colors[8])
        self[1].set_fill(color=colors[3])
        self[2].set_fill(color=colors[8])
        self[3].set_fill(color=colors[2])
        self[4].set_fill(color=colors[5])
        self[5].set_fill(color=colors[7])

class MyBoxes(VGroup):

    CONFIG = {
        'center': ORIGIN,
        'bottom_size': [0.25, 0.25],
        'box_height': 2,
        'gap': 0,
        'fill_color': BLUE,
        'resolution': (20, 20),
    }

    def __init__(self, **kwargs):

        VGroup.__init__(self, **kwargs)
        self.create_boxes(self.resolution)
        self.mask_array = np.zeros(self.resolution)
        self.colors = color_gradient([BLUE_D, YELLOW, RED, RED_D], 110)

    def create_boxes(self, resolution=(20, 20)):
        a, b = self.bottom_size[0] + self.gap, self.bottom_size[1] + self.gap
        m, n = resolution[0], resolution[1]
        for i in range(m):
            for j in range(n):
                box_ij = MyBox(pos=a * (j - n/2 + 1/2) * RIGHT + b * (i - m/2 + 1/2) * UP, bottom_size=self.bottom_size,
                               box_height=self.box_height, fill_color=self.fill_color)
                box_ij.reset_color()
                self.add(box_ij)

    def update_height_by_2darray(self, arr_2d):
        m, n = self.resolution[0], self.resolution[1]
        if len(arr_2d)>=m and len(arr_2d[0])>=n:
            for i in range(m):
                for j in range(n):
                    self[i*n+j].update_height(arr_2d[i, j])

    def update_height_by_func(self, func, s=1):
        for box in self:
            center = box.get_center()
            box.update_height(func(center[0], center[1]) * s)

    def update_top_and_bottom_by_2darray(self, arr_top, arr_bottom):
        m, n = self.resolution[0], self.resolution[1]
        if len(arr_top)>=m and len(arr_top[0])>=n and len(arr_bottom)>=m and len(arr_bottom[0])>=n:
            for i in range(m):
                for j in range(n):
                    self[i*n+j].update_top_and_bottom(arr_top[i, j], arr_bottom[i, j])

    def update_top_and_bottom_by_func(self, func_top, func_bottom, s=1):
        for box in self:
            center = box.get_center()
            box.update_top_and_bottom(func_top(center[0], center[1]) * s, func_bottom(center[0], center[1]) * s)

    def update_top_by_func(self, func_top, s=1):
        for box in self:
            center = box.get_center()
            box.update_top(func_top(center[0], center[1]) * s)

    def update_bottom_by_func(self, func_bottom, s=1):
        for box in self:
            center = box.get_center()
            box.update_top(func_bottom(center[0], center[1]) * s)

    def update_color_by_func(self, func):

        a, b = self.bottom_size[0] + self.gap, self.bottom_size[1] + self.gap
        m, n = self.resolution[0], self.resolution[1]
        x, y = np.linspace(-a * n/2, a * n/2, n), np.linspace(-b * m/2, b * m/2, m)
        X, Y = np.meshgrid(x, y)
        Z = func(X, Y)
        z_min, z_max = Z.min(), Z.max()
        # print(z_min, z_max)

        for box in self:
            center = box.get_center() + box.box_height/2 * OUT
            # print(int((func(center[0], center[1]) - z_min)/(z_max-z_min) * 100))
            box.set_color(self.colors[int((func(center[0], center[1]) - z_min)/(z_max-z_min) * 100)])
            box.reset_color()

    def update_color_by_2darray(self, top_array):
        Z = top_array
        m, n = self.resolution[0], self.resolution[1]
        z_min, z_max = Z.min(), Z.max()
        if len(Z) >= m and len(Z) >= n:
            for i in range(m):
                for j in range(n):
                    self[i*n+j].set_color(self.colors[int((Z[i, j] - z_min)/(z_max-z_min) * 100)])
                    self[i*n+j].reset_color()

    def set_mask_array(self, mask):
        self.mask_array = mask

    def divide_by_height(self, h_min=1e-4):
        self.high_boxes, self.short_boxes = VGroup(), VGroup()
        for box in self:
            if box.get_depth() < h_min:
                self.short_boxes.add(box)
            else:
                self.high_boxes.add(box)
        return self.high_boxes, self.short_boxes

    def get_high_boxes(self, h=1e-2):
        return self.divide_by_height(h_min=h)[0]

    def get_short_boxes(self, h=1e-2):
        return self.divide_by_height(h_min=h)[1]

    def apply_mask(self):

        m, n = self.resolution[0], self.resolution[1]
        for i in range(m):
            for j in range(n):
                if self.mask_array[i, j] == 1.: # if self.mask_array[i, j]:
                    self[i*n+j].set_fill(opacity=0)

    def set_mask_by_min_height(self, min_height):

        pass

class Cube_array(VGroup):

    CONFIG = {
        'center': ORIGIN,
        'cube_size': 0.5,
        'gap': 0,
        'fill_color': BLUE,
        'fill_opacity': 1,
        'stroke_color': WHITE,
        'stroke_width': 0,
        'resolution': (4, 4, 1),
        # 'mask_array': None,
        # 'reset_color': True,

    }

    def __init__(self, **kwargs):
        VGroup.__init__(self, **kwargs)
        self.create_cubes()
        self.faces = self.get_all_faces()
        # self.classify_faces()
        self.move_to(self.center)
        self.get_outer_faces()

    def create_cubes(self):
        size, gap = self.cube_size, self.gap
        u, v, w = self.resolution[0], self.resolution[1], self.resolution[2]
        for i in range(u):
            for j in range(v):
                for k in range(w):
                    # box_ijk = MyBox(pos=(size + gap) * ((j - v/2 + 1/2) * RIGHT + (i - u/2 + 1/2) * UP + (k - w/2 + 1/2) * OUT),
                    #                 bottom_size=[size, size], box_height=size, fill_color=self.fill_color,
                    #                 opacity=self.fill_opacity, stroke_color=self.stroke_color, stroke_width=self.stroke_width)
                    box_ijk = Cube(side_length=size, fill_color=self.fill_color, opacity=self.fill_opacity,
                                   stroke_color=self.stroke_color, stroke_width=self.stroke_width)
                    box_ijk.shift((size + gap) * ((j - v/2 + 1/2) * RIGHT + (i - u/2 + 1/2) * UP + (k - w/2 + 1/2) * OUT))

                    # if self.reset_color:
                    #     box_ijk.reset_color()
                    self.add(box_ijk)

    def scale_each_cube(self, scale_factor):
        for cube in self:
            cube.scale(scale_factor)

    def rotate_each_cube(self, angle, axis=OUT, **kwargs):
        for cube in self:
            cube.rotate(angle, axis=OUT, **kwargs)

    def get_all_faces(self):
        faces = VGroup()
        for cube in self:
            faces.add(*cube)
        return faces

    def get_faces_by_range(self, max, min, dim=3):
        max, min = (min, max) if max < min else (max, min)
        faces = VGroup()
        for face in self.faces:
            if face.get_center()[dim-1] <= max and face.get_center()[dim-1] >= min:
                faces.add(face)
        return faces

    def get_top_face(self, err=1e-3):
        a = self.get_zenith()[2]
        self.top_faces = self.get_faces_by_range(a+err, a-err, dim=3)
        return self.top_faces

    def get_bottom_face(self, err=1e-3):
        a = self.get_nadir()[2]
        self.bottom_faces = self.get_faces_by_range(a+err, a-err, dim=3)
        return self.bottom_faces

    def get_front_face(self, err=1e-3):
        a = self.get_bottom()[1]
        self.front_faces = self.get_faces_by_range(a+err, a-err, dim=2)
        return self.front_faces

    def get_back_face(self, err=1e-3):
        a = self.get_top()[1]
        self.back_faces = self.get_faces_by_range(a+err, a-err, dim=2)
        return self.back_faces

    def get_left_face(self, err=1e-3):
        a = self.get_left()[0]
        self.left_faces = self.get_faces_by_range(a+err, a-err, dim=1)
        return self.left_faces

    def get_right_face(self, err=1e-3):
        a = self.get_right()[0]
        self.right_faces = self.get_faces_by_range(a+err, a-err, dim=1)
        return self.right_faces

    def classify_faces(self):

        # max_or_min = np.array([self.get_top()[1], self.get_bottom()[1], self.get_right()[0], self.get_left()[0],
        #               self.get_zenith()[2], self.get_nadir()[2]])
        max_or_min = np.array([self.get_top()[1], self.get_bottom()[1], self.get_right()[0], self.get_left()[0],
                      self.get_zenith()[2], self.get_nadir()[2]])
        print(max_or_min)
        self.outer_faces, self.inner_faces = VGroup(), VGroup()
        err = 1e-4 * self.cube_size ** 2
        for face in self.faces:
            x, y, z = face.get_center()[0], face.get_center()[1], face.get_center()[2]

            a = abs((max_or_min - x) * (max_or_min - y) * (max_or_min - z))
            print('before:', abs(a[0] * a[1] * a[2] * a[3] * a[4] * a[5])/self.cube_size ** 6)
            if abs(a[0] * a[1] * a[2] * a[3] * a[4] * a[5])/(self.cube_size/2) ** 6 < err:
                print('outer:', abs(a[0] * a[1] * a[2] * a[3] * a[4] * a[5])/self.cube_size ** 6)
                self.outer_faces.add(face)
            else:
                print('inner:', abs(a[0] * a[1] * a[2] * a[3] * a[4] * a[5])/self.cube_size ** 6)
                self.inner_faces.add(face)

            # a0 = abs(max_or_min - x)[0] * abs(max_or_min - x)[1]
            # a1 = abs(max_or_min - y)[2] * abs(max_or_min - y)[3]
            # a2 = abs(max_or_min - z)[4] * abs(max_or_min - z)[5]
            # if a0 < err or a1 < err or a2 < err:
            #     self.outer_faces.add(face)
            #     print('outer')
            # else:
            #     print('inner')
            #     self.inner_faces.add(face)
        # return self.outer_faces, self.inner_faces

    def get_outer_faces(self):
        self.outer_faces = VGroup(self.get_top_face(), self.get_bottom_face(),
                                  self.get_front_face(), self.get_back_face(),
                                  self.get_left_face(), self.get_right_face())
        return self.outer_faces

    # def get_innter_faces(self):
    #     return self.inner_faces

class Rubik_Cube(Cube_array):

    CONFIG = {
        'colors': [GREEN, BLUE, WHITE, YELLOW, RED, ORANGE],
    }

    def __init__(self, size=3, order=3, base_color=LIGHT_GREY, **kwargs):
        Cube_array.__init__(self, cube_size=size/order, resolution=(order, order, order), fill_color=base_color, fill_opacity=1, **kwargs)
        self.scale_each_cube(0.9)
        self.order = order
        self.size = size
        self.setup_color()

    def setup_color(self):
        self.top_faces.set_color(self.colors[0])
        self.bottom_faces.set_color(self.colors[1])
        self.front_faces.set_color(self.colors[2])
        self.back_faces.set_color(self.colors[3])
        self.left_faces.set_color(self.colors[4])
        self.right_faces.set_color(self.colors[5])

    def get_layer(self, layer=[1], dim=3):
        faces = VGroup()
        if type(layer) == int:
            a = self.size/2 - 0.5 - (layer-1) * self.cube_size
            faces.add(self.get_faces_by_range(a + self.cube_size/2 + 0.01, a - self.cube_size/2 - 0.01, dim=dim))

        else:
            for i in layer:
                a = self.size/2 - 0.5 - (i-1) * self.cube_size
                faces.add(self.get_faces_by_range(a + self.cube_size/2 + 0.01, a - self.cube_size/2 - 0.01, dim=dim))

        return faces


