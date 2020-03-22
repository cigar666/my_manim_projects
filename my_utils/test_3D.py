from manimlib.imports import *
from my_manim_projects.my_utils.my_3D_mobject import *

class Test_boxes(SpecialThreeDScene):
    CONFIG = {
        "default_angled_camera_position": {
            "phi": 70 * DEGREES,
            "theta": -45 * DEGREES,
            "distance": 50,
            },
        }
    def construct(self):

        self.set_camera_to_default_position()

        boxes = MyBoxes(fill_color=GRAY, resolution=(24, 24), bottom_size=(0.3, 0.3), gap=0.1)
        # func_01 = lambda x, y: np.sin(x ** 2 / 2.1 + y ** 2 / 2.1 + 5 * DEGREES) * 1.8 + 2.
        R = lambda x, y: np.sqrt(x ** 2 * 4 + y ** 2 * 4) + 1e-8
        func_02 = lambda u, v: 8 * np.sin(R(u, v))/R(u, v) * 0.45 - 0.2
        boxes.update_top_by_func(func_02)
        boxes.update_color_by_func(func_02)

        mask = np.zeros((24, 24))
        for i in range(24):
            for j in range(24):
                if np.sqrt((i - 11.5) ** 2 + (j - 11.5) ** 2) > 9:
                    mask[i, j] = 1

        boxes.set_mask_array(mask)
        boxes.apply_mask()

        self.add(boxes)
        self.wait(2)

import matplotlib.pyplot as plt

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

class Boxes_by_image(SpecialThreeDScene):

    CONFIG = {
        "default_angled_camera_position": {
            "phi": 45 * DEGREES,
            "theta": -0 * DEGREES,
            "distance": 50,
            },
        }
    def construct(self):

        self.set_camera_to_default_position()
        im = plt.imread(r'E:\GitHub\manim\my_manim_projects\my_projects\resource\png_files\china_test_60_45.bmp')
        Z = 1 - im[:, :, 0]/225 + 1e-6
        print(Z)
        Z = (Z - Z.min()) * 4
        Z = Z.T
        print(len(Z), len(Z[0]))
        print(Z.min(), Z.max())

        # print(Z)
        boxes = MyBoxes(fill_color=average_color(BLUE_D, GRAY), bottom_size=(0.18, 0.18), resolution=(60, 45))
        boxes.colors = color_gradient([BLUE_D, YELLOW, ORANGE, RED, RED_D], 110)

        # for i in range(3):
        #     Z = solve_PDE_onestep(Z)

        boxes.update_top_and_bottom_by_2darray(Z, np.zeros((60, 45)))
        boxes.update_color_by_2darray(Z)

        for box in boxes:
            print(box.box_height)
            if box.box_height < 1e-4:
                box.set_fill(opacity=0)

        self.add(boxes)
        self.wait(4)

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

# test Cube_array

class Test_cube_array(ThreeDScene):

    CONFIG = {
        'camera_init': {
            'phi': 52.5 * DEGREES,
            'gamma': 0,
            'theta': -45 * DEGREES,
        },
        # 'camera_config': {
        #     'should_apply_shading': False,
        # },
    }

    def construct(self):

        self.set_camera_orientation(**self.camera_init)

        cubes = Cube_array(fill_color=BLUE, fill_opacity=0.6, resolution=(3,3,3), cube_size=1)
        self.add(cubes)
        self.wait()
        self.play(cubes.outer_faces.shift, DL * 1.5, cubes.inner_faces.shift, UR * 2, run_time=2)

        self.wait(3)

class Rubik_Cube_test(ThreeDScene):

    CONFIG = {
        'camera_init': {
            'phi': 52.5 * DEGREES,
            'gamma': 0,
            'theta': -45 * DEGREES,
        },
    }

    def construct(self):

        self.set_camera_orientation(**self.camera_init)

        rc = Rubik_Cube()

        self.add(rc)
        self.wait()

        t = 1.6
        self.play(Rotating(rc.get_layer(1, 1), radians=PI/2, axis=RIGHT, run_time=t))

        self.play(Rotating(rc.get_layer(1, 3), radians=-PI/2, axis=OUT, run_time=t))

        self.play(Rotating(rc.get_layer([1,3], 2), radians=PI, axis=UP, run_time=t), Rotating(rc.get_layer(2, 2), radians=PI*0, axis=UP, run_time=t))

        self.play(Rotating(rc.get_layer(2, 1), radians=PI/2, axis=RIGHT, run_time=t), Rotating(rc.get_layer([1,3], 1), radians=PI/2 * 0, axis=RIGHT, run_time=t))

        self.play(Rotating(rc.get_layer(1, 3), radians=-PI/2, axis=OUT, run_time=t))

        self.play(Rotating(rc.get_layer([1,2], 2), radians=-PI/2, axis=UP, run_time=t), Rotating(rc.get_layer(3, 2), radians=PI*0, axis=UP, run_time=t))

        self.play(Rotating(rc.get_layer([3,2], 1), radians=PI/2, axis=RIGHT, run_time=t), Rotating(rc.get_layer(1, 1), radians=PI/2 * 0, axis=RIGHT, run_time=t))

        self.wait(2)

class Play_rubic_order3(Rubik_Scene):

    CONFIG = {
        'order': 3,
    }

    def construct(self):

        self.wait()
        self.rotate_rubik_anim(1, 3, 1)       # U'
        self.rotate_rubik_anim(1, 1, -1)      # R
        self.rotate_rubik_anim(0, 2, 1)       # y
        self.rotate_rubik_anim(1, 3, 2)       # U'2
        self.rotate_rubik_anim(2, 1, -2)      # M'2
        self.rotate_rubik_anim([1,2], 3, -2)  # u2
        self.rotate_rubik_anim(1, 1, -1)      # L'
        self.rotate_rubik_anim([2,3], 2, 1)   # b
        self.rotate_rubik_anim(1, 3, -1)      # U
        self.wait()


class Play_rubic_order5(Rubik_Scene):

    CONFIG = {
        'order': 5,
    }

    def construct(self):

        self.wait()
        self.rotate_rubik_anim(1, 3, 1)
        self.rotate_rubik_anim(1, 1, -1)
        self.rotate_rubik_anim(0, 2, 1)
        self.rotate_rubik_anim(1, 3, 2)
        self.rotate_rubik_anim(2, 1, -2)
        self.rotate_rubik_anim([1,2], 3, -2)
        self.rotate_rubik_anim(1, 1, -1)
        self.rotate_rubik_anim([2,3], 2, 1)
        self.rotate_rubik_anim(1, 3, -1)
        self.wait()
