from manimlib.imports import *
from my_manim_projects.my_utils.my_3D_mobject import *

class Update_boxes_test(SpecialThreeDScene):

    CONFIG = {
        "default_angled_camera_position": {
            "phi": 70 * DEGREES,
            "theta": -45 * DEGREES,
            "distance": 50,
            },
        }
    def construct(self):

        self.set_camera_to_default_position()
        axes = self.get_axes()
        boxes = MyBoxes(fill_color=GRAY, resolution=(18, 18), bottom_size=(0.25, 0.25))
        self.var_phi = 0
        func_01 = lambda x, y: np.sin(x ** 2 / 2.1 + y ** 2 / 2.1 + self.var_phi) * 1.8 + 2.25

        boxes.update_height_by_func(func_01)
        boxes.update_color_by_func(func_01)
        def update_boxes(b, dt):
            # b.update_height_by_func(func_01)
            # boxes_i = MyBoxes(fill_color=GRAY, resolution=(18, 18), bottom_size=(0.25, 0.25))
            # boxes_i.update_height_by_func(func_01)
            # boxes_i.update_color_by_func(func_01)
            # b.become(boxes)
            b.update_height_by_func(func_01)
            b.update_color_by_func(func_01)
            self.var_phi += 2 * DEGREES
        self.add(boxes)
        boxes.add_updater(update_boxes)
        # self.wait(2)
        # boxes.remove_updater(update_boxes)
        self.wait(10)

class Boxes_waves(SpecialThreeDScene):

    CONFIG = {
        "default_angled_camera_position": {
            "phi": 70 * DEGREES,
            "theta": -45 * DEGREES,
            "distance": 50,
            },
        }
    def construct(self):

        self.set_camera_to_default_position()
        axes = self.get_axes()
        boxes = MyBoxes(fill_color=GRAY, resolution=(20, 20), bottom_size=(0.25, 0.25), gap=0.05)
        self.var_phi = 0
        func_01 = lambda x, y: np.sin(x ** 2 / 2.4 + y ** 2 / 2.4 + self.var_phi) * 1.
        func_02 = lambda x, y: np.sin(x ** 2 / 2.4 + y ** 2 / 2.4 + self.var_phi) * 1. - 0.25

        boxes.update_top_and_bottom_by_func(func_01, func_02)
        boxes.update_color_by_func(func_01)
        def update_boxes(b, dt):
            b.update_top_and_bottom_by_func(func_01, func_02)
            b.update_color_by_func(func_01)
            self.var_phi += 1 * DEGREES
        self.add(boxes)
        boxes.add_updater(update_boxes)
        # self.wait(2)
        # boxes.remove_updater(update_boxes)
        self.wait(12)

class Boxes_waves_02(SpecialThreeDScene):

    CONFIG = {
        "default_angled_camera_position": {
            "phi": 70 * DEGREES,
            "theta": -45 * DEGREES,
            "distance": 50,
            },
        }
    def construct(self):

        self.set_camera_to_default_position()
        axes = self.get_axes()
        boxes = MyBoxes(fill_color=GRAY, resolution=(18, 18), bottom_size=(0.25, 0.25))
        self.var_phi = 0
        func_01 = lambda x, y: np.sin(x ** 2 / 2.1 + y ** 2 / 2.1 + self.var_phi) * 1.8 + 2.25

        boxes.update_height_by_func(func_01)
        boxes.update_color_by_func(func_01)
        def update_boxes(b, dt):
            # b.update_height_by_func(func_01)
            # boxes_i = MyBoxes(fill_color=GRAY, resolution=(18, 18), bottom_size=(0.25, 0.25))
            # boxes_i.update_height_by_func(func_01)
            # boxes_i.update_color_by_func(func_01)
            # b.become(boxes)
            b.update_height_by_func(func_01)
            b.update_color_by_func(func_01)
            self.var_phi += 1 * DEGREES
        self.add(boxes)
        boxes.add_updater(update_boxes)
        # self.wait(2)
        # boxes.remove_updater(update_boxes)
        self.wait(6)

class Boxes_waves_rotating(SpecialThreeDScene):

    CONFIG = {
        "default_angled_camera_position": {
            "phi": 70 * DEGREES,
            "theta": -45 * DEGREES,
            "distance": 50,
            },
        }
    def construct(self):

        self.set_camera_to_default_position()
        axes = self.get_axes()
        boxes = MyBoxes(fill_color=GRAY, resolution=(18, 18), bottom_size=(0.25, 0.25))
        self.var_phi = 0
        func_01 = lambda x, y: np.sin(x ** 2 / 2.1 + y ** 2 / 2.1 + self.var_phi) * 1.8 + 2.25

        boxes.update_height_by_func(func_01)
        boxes.update_color_by_func(func_01)
        def update_boxes(b, dt):
            # b.update_height_by_func(func_01)
            # boxes_i = MyBoxes(fill_color=GRAY, resolution=(18, 18), bottom_size=(0.25, 0.25))
            # boxes_i.update_height_by_func(func_01)
            # boxes_i.update_color_by_func(func_01)
            # b.become(boxes)
            b.update_height_by_func(func_01)
            b.update_color_by_func(func_01)
            self.var_phi += 1 * DEGREES
        self.add(boxes)
        boxes.add_updater(update_boxes)
        # self.wait(2)
        # boxes.remove_updater(update_boxes)

        for i in range(360):
            self.set_camera_orientation(theta=-45 * DEGREES + i * TAU/360)
            self.wait(1/30)
        # self.wait(1)

class Boxes_waves_03(SpecialThreeDScene):

    CONFIG = {
        "default_angled_camera_position": {
            "phi": 70 * DEGREES,
            "theta": -45 * DEGREES,
            "distance": 50,
            },
        }

    def construct(self):

        self.set_camera_to_default_position()
        self.var_phi = 0

        boxes = MyBoxes(fill_color=average_color(BLUE_D, GRAY), bottom_size=(0.25, 0.25))

        func_01 = lambda x, y: np.sin(x ** 2 + y ** 2 + self.var_phi) + 2

        boxes.update_height_by_func(func_01)

        def update_boxes(b, dt):
            b.update_height_by_func(func_01)
            self.var_phi += 1 *DEGREES

        self.add(boxes)
        boxes.add_updater(update_boxes)
        self.wait(6)

def solve_PDE_onestep(array, dx=1, dy=1, kx=1e-1, ky=1e-1, Q=None, s=1.):
    m, n = len(array) + 2, len(array[0]) + 2
    T = np.zeros((m, n))
    T[1:-1, 1:-1] = array
    if type(Q) != np.ndarray:
        Q = np.zeros((m, n))
    # T_new = (kx * T[1:-1, 2:n+1] * dy ** 2 + kx * T[1:-1, 0:-2] * dy ** 2 +
    #          ky * T[2:n+1, 1:-1] * dx ** 2 + ky * T[0:-2, 1:-1] * dx ** 2 -
    #          (kx * dy ** 2 + ky * dx ** 2) * T[1:-1, 1:-1] +
    #          dx ** 2 * dy ** 2 * Q[1:-1, 1:-1]) / (kx * dy ** 2 + ky * dx ** 2)
    T_new = (kx * T[1:-1, 2:n+1] * dy ** 2 + kx * T[1:-1, 0:-2] * dy ** 2 +
             ky * T[2:n+1, 1:-1] * dx ** 2 + ky * T[0:-2, 1:-1] * dx ** 2 +
             dx ** 2 * dy ** 2 * Q[1:-1, 1:-1]) / (kx * dy ** 2 + ky * dx ** 2) / 2
    err = abs((T_new - array) ** 2).sum()/ abs(array).sum()
    # print(T_new)
    print(err)
    return T_new * s + array * (1 - s)

class Spread_out(SpecialThreeDScene):

    CONFIG = {
        "default_angled_camera_position": {
            "phi": 60 * DEGREES,
            "theta": -45 * DEGREES,
            "distance": 50,
            },
        }

    def construct(self):

        self.set_camera_to_default_position()

        boxes = MyBoxes(fill_color=average_color(BLUE_D, GRAY), bottom_size=(0.25, 0.25), resolution=(20, 20))

        self.top_arr = np.array([[3.25, 3, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 3, 3.25],
                                 [3, 3.25, 3, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 3, 3.25, 3],
                                 [2, 3, 3.25, 3, 2, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 2, 3, 3.25, 3, 2],
                                 [1, 2, 3, 3.25, 3, 2, 1, 1, 0, 0, 0, 0, 1, 1, 2, 3, 3.25, 3, 2, 1],
                                 [1, 1, 2, 3, 3.25, 3, 2, 1, 1, 0, 0, 1, 1, 2, 3, 3.25, 3, 2, 1, 1],
                                 [0, 1, 1, 2, 3, 3.25, 3, 2, 1, 1, 1, 1, 2, 3, 3.25, 3, 2, 1, 1, 0],
                                 [0, 0, 1, 1, 2, 3, 3.25, 3, 2, 1, 1, 2, 3, 3.25, 3, 2, 1, 1, 0, 0],
                                 [0, 0, 0, 1, 1, 2, 3, 3.25, 3, 2, 2, 3, 3.25, 3, 2, 1, 1, 0, 0, 0],
                                 [0, 0, 0, 0, 1, 1, 2, 3, 3.25, 3, 3, 3.25, 3, 2, 1, 1, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 1, 1, 2, 3, 3.25, 3.25, 3, 2, 1, 1, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 1, 1, 2, 3, 3.25, 3.25, 3, 2, 1, 1, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 1, 1, 2, 3, 3.25, 3, 3, 3.25, 3, 2, 1, 1, 0, 0, 0, 0],
                                 [0, 0, 0, 1, 1, 2, 3, 3.25, 3, 2, 2, 3, 3.25, 3, 2, 1, 1, 0, 0, 0],
                                 [0, 0, 1, 1, 2, 3, 3.25, 3, 2, 1, 1, 2, 3, 3.25, 3, 2, 1, 1, 0, 0],
                                 [0, 1, 1, 2, 3, 3.25, 3, 2, 1, 1, 1, 1, 2, 3, 3.25, 3, 2, 1, 1, 0],
                                 [1, 1, 2, 3, 3.25, 3, 2, 1, 1, 0, 0, 1, 1, 2, 3, 3.25, 3, 2, 1, 1],
                                 [1, 2, 3, 3.25, 3, 2, 1, 1, 0, 0, 0, 0, 1, 1, 2, 3, 3.25, 3, 2, 1],
                                 [2, 3, 3.25, 3, 2, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 2, 3, 3.25, 3, 2],
                                 [3, 3.25, 3, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 3, 3.25, 3],
                                 [3.25, 3, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 3, 3.25],
                                ]) * 0.75 - 0.5
        bottom_arr = np.ones((20, 20)) * (-0.6)
        Q = (np.eye(22) + np.eye(22)[::-1]) * 1e-3

        def update_boxes(b, dt):
            self.top_arr = solve_PDE_onestep(self.top_arr, kx=4e-3, ky=4e-3, Q=Q)
            b.update_top_and_bottom_by_2darray(self.top_arr, bottom_arr)
            b.update_color_by_2darray(self.top_arr)

        boxes.add_updater(update_boxes)
        self.add(boxes)

        self.wait(5)


# import matplotlib.pyplot as plt
#
# im = plt.imread(r'E:\GitHub\manim\my_manim_projects\my_projects\resource\png_files\test.bmp')
# a = im[:,:, 0]
# plt.imshow(a)
# plt.show()
# print(a)



