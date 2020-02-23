from manimlib.imports import *

class Box(Cube):

    CONFIG = {
        'pos': ORIGIN,
        'box_height': 2,
        'bottom_size': [1, 1]
    }

    def __init__(self, **kwargs):
        Cube.__init__(self, **kwargs)
        self.box_size = np.array([self.bottom_size[0], self.bottom_size[1], self.box_height])
        self.scale(self.box_size/2)
        self.move_to(self.pos + self.box_height * OUT/2)
        self.reset_color_()

    def update_height(self, new_height):
        self.scale(np.array([1,1, new_height/self.height])).shift(OUT * (new_height - self.height)/2)
        self.height = new_height

    def reset_color_(self):
        colors = color_gradient([WHITE, self.get_color(), BLACK], 11)
        self[0].set_fill(color=colors[7])
        self[1].set_fill(color=colors[4])
        self[2].set_fill(color=colors[7])
        self[3].set_fill(color=colors[3])
        self[4].set_fill(color=colors[5])
        self[5].set_fill(color=colors[6])

class Wave_of_boxes(SpecialThreeDScene):

    CONFIG = {
        "default_angled_camera_position": {
            "phi": 56 * DEGREES,
            "theta": -50 * DEGREES,
            "distance": 50,
            },
        'camera_config': {'background_color': DARK_GRAY,
                          'open_plot_depth': False},
        }

    def construct(self):

        self.set_camera_to_default_position()

        self.var_phi = 0
        a = 0.4
        self.wave_func = lambda u, v: np.array([u, v, 1.2 + 1.5 * np.sin((u ** 2 + v ** 2)/2 + self.var_phi) * np.exp(-a * (np.sqrt(u ** 2 + v ** 2)))])
        # self.wave_func = lambda u, v: np.array([u, v, 2.1 + 2 * np.sin(u ** 2 + v ** 2)])

        self.box_bottom = [0.18, 0.18]
        self.colors = color_gradient([RED, YELLOW, GREEN_D, BLUE, PINK, RED_D], 100)

        boxes = self.create_boxes(gap=0.06)

        delta_theta = 2 * DEGREES
        def update_boxes(b, dt):
            b.become(self.create_boxes(gap=0.06))
            self.var_phi -= -delta_theta # 网上看到的牛逼写法，很有意思就用了

        boxes.add_updater(update_boxes)
        self.add(boxes)
        self.wait(12)

    def create_boxes(self, x_range=4, y_range=4, gap=0.05):
        boxes = VGroup()
        a, b = self.box_bottom[0] + gap * 2, self.box_bottom[1] + gap * 2
        m = int(y_range * 2/b)
        n = int(x_range * 2/a)
        for i in range(m):
            for j in range(n):
                xyz = a * j * RIGHT + b * i * UP + (x_range - a/2) * LEFT + (y_range - b/2) * DOWN
                box_ij = Box(pos=xyz, box_height=self.wave_func(xyz[0], xyz[1])[-1], color=BLUE,
                             bottom_size=self.box_bottom, fill_opacity=1,
                             fill_color=self.colors[int(np.sqrt(sum(xyz **2))/np.sqrt(x_range ** 2 + y_range ** 2) * 100)])
                boxes.add(box_ij)
        return boxes

class Box_02(Cube):

    CONFIG = {
        'pos': ORIGIN,
        'box_height': 2,
        'bottom_size': [1, 1]
    }

    def __init__(self, **kwargs):
        Cube.__init__(self, **kwargs)
        self.box_size = np.array([self.bottom_size[0], self.bottom_size[1], self.box_height])
        self.scale(self.box_size/2)
        # self.move_to(self.pos + self.box_height * OUT/2)
        self.move_to(self.pos)
        self.reset_color_()

    def update_height(self, new_height):
        self.scale(np.array([1,1, new_height/self.height])) #.shift(OUT * (new_height - self.height)/2)
        self.height = new_height

    def reset_color_(self):
        colors = color_gradient([WHITE, self.get_color(), BLACK], 11)
        self[0].set_fill(color=colors[7])
        self[1].set_fill(color=colors[4])
        self[2].set_fill(color=colors[7])
        self[3].set_fill(color=colors[3])
        self[4].set_fill(color=colors[5])
        self[5].set_fill(color=colors[6])

class Wave_of_boxes_02(SpecialThreeDScene):

    CONFIG = {
        "default_angled_camera_position": {
            "phi": 56 * DEGREES,
            "theta": -50 * DEGREES,
            "distance": 50,
            },
        'camera_config': {'background_color': DARK_GRAY,
                          'open_plot_depth': False},
        }

    def construct(self):

        self.set_camera_to_default_position()

        self.var_phi = 0
        a = 0.1
        amp = 0.9 # amplitude
        self.wave_func = lambda u, v: np.array([u, v, amp + 0.0001  + amp * np.sin((u ** 2 + v ** 2)/2 + self.var_phi) * np.exp(-a * (np.sqrt(u ** 2 + v ** 2)))])
        # self.wave_func = lambda u, v: np.array([u, v, 2.1 + 2 * np.sin(u ** 2 + v ** 2)])

        self.box_bottom = [0.18, 0.18]
        self.colors = color_gradient([RED, YELLOW, GREEN_D, BLUE, PINK, RED_D], 100)

        boxes = self.create_boxes(gap=0.06)

        delta_theta = 1 * DEGREES
        def update_boxes(b, dt):
            b.become(self.create_boxes(gap=0.06))
            self.var_phi -= -delta_theta # 网上看到的牛逼写法，很有意思就用了

        boxes.add_updater(update_boxes)
        self.add(boxes)
        self.wait(16)

    def create_boxes(self, x_range=4, y_range=4, gap=0.05):
        boxes = VGroup()
        a, b = self.box_bottom[0] + gap * 2, self.box_bottom[1] + gap * 2
        m = int(y_range * 2/b)
        n = int(x_range * 2/a)
        for i in range(m):
            for j in range(n):
                xyz = a * j * RIGHT + b * i * UP + (x_range - a/2) * LEFT + (y_range - b/2) * DOWN
                box_ij = Box_02(pos=xyz, box_height=self.wave_func(xyz[0], xyz[1])[-1], color=BLUE,
                               bottom_size=self.box_bottom, fill_opacity=1,
                               fill_color=self.colors[int(np.sqrt(sum(xyz **2))/np.sqrt(x_range ** 2 + y_range ** 2) * 100)])
                boxes.add(box_ij)
        return boxes

class Wave_of_boxes_2D(Scene):

    def construct(self):

        self.var_phi = 0
        a = 0.1
        amp = 0.9 # amplitude
        self.wave_func = lambda u, v: np.array([u, v, amp + 0.0001  + amp * np.sin((u ** 2 + v ** 2)/2 + self.var_phi) * np.exp(-a * (np.sqrt(u ** 2 + v ** 2)))])
        # self.wave_func = lambda u, v: np.array([u, v, 2.1 + 2 * np.sin(u ** 2 + v ** 2)])

        self.box_bottom = [0.18, 0.18]
        self.colors = color_gradient([RED, YELLOW, GREEN_D, BLUE, PINK, RED_D], 100)

        boxes = self.create_boxes(gap=0.06)

        delta_theta = 1 * DEGREES
        def update_boxes(b, dt):
            b.become(self.create_boxes(gap=0.06))
            self.var_phi -= -delta_theta # 网上看到的牛逼写法，很有意思就用了

        # boxes.add_updater(update_boxes)
        self.add(boxes)
        self.wait(16)


    def create_boxes(self, x_range=4, y_range=4, gap=0.05):
        boxes = VGroup()
        a, b = self.box_bottom[0] + gap * 2, self.box_bottom[1] + gap * 2
        m = int(y_range * 2/b)
        n = int(x_range * 2/a)
        for i in range(m):
            for j in range(n):
                xyz = a * j * RIGHT + b * i * UP + (x_range - a/2) * LEFT + (y_range - b/2) * DOWN
                box_ij = Box_02(pos=xyz, box_height=self.wave_func(xyz[0], xyz[1])[-1], color=BLUE,
                               bottom_size=self.box_bottom, fill_opacity=1,
                               fill_color=self.colors[int(np.sqrt(sum(xyz **2))/np.sqrt(x_range ** 2 + y_range ** 2) * 100)])
                boxes.add(box_ij)
        return boxes
