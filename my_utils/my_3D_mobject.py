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

    def apply_mask(self):

        m, n = self.resolution[0], self.resolution[1]
        for i in range(m):
            for j in range(n):
                if self.mask_array[i, j] == 1.: # if self.mask_array[i, j]:
                    self[i*n+j].set_fill(opacity=0)


