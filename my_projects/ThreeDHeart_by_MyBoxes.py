from manimlib.imports import *
from my_manim_projects.my_utils.my_3D_mobject import *

class ThreeD_heart(SpecialThreeDScene):

    CONFIG = {
        "default_angled_camera_position": {
            "phi": 64 * DEGREES,
            "theta": 30 * DEGREES,
            "distance": 100,
            },
        'camera_config': {'background_color': BLUE_A},
        }
    def construct(self):
        self.set_camera_to_default_position()
        heart_func = lambda x, y, z: (x ** 2 + 9/4 * z ** 2 + y ** 2 - 1) ** 3 - x ** 2 * y ** 3 - 9/80 * z ** 2 * y ** 3
        m, n = 80, 80
        x, y = np.linspace(-2, 2, n+1), np.linspace(-2, 2, m+1)
        def dichotomy(func, min=0, max=3 + 1, err=1e-4):
            if func(min) * func(max) > 0:
                return 0
            else:
                while max - min > err:
                    mid = (max + min)/2
                    if func(min) * func(mid) <= 0:
                        max = mid
                    else:
                        min = mid
                return (max + min)/2
        z = np.zeros((m+1, n+1))
        for i in range(m+1):
            for j in range(n+1):
                z[i, j] = dichotomy(lambda z: heart_func(x[j], y[i], z)) * 2
        z *= 4.5
        print(z)
        heart_by_boxes = MyBoxes(fill_color=average_color(RED, PINK), resolution=(m+1, n+1), bottom_size=(0.15, 0.15), gap=0)
        heart_by_boxes.update_height_by_2darray(z)
        # heart_by_boxes.update_color_by_func(lambda x, y: (x ** 2 + y ** 2) / 4)
        heart_by_boxes.rotate(PI/2)
        heart_by_boxes.rotate(PI/2, axis=UP)
        # heart = heart_by_boxes.get_high_boxes()
        mask = np.zeros((m+1, n+1))
        for i in range(m+1):
            for j in range(n+1):
                if z[i,j]< 1:
                    mask[i, j] = 1
        heart_by_boxes.set_mask_array(mask)
        heart_by_boxes.apply_mask()
        self.add(heart_by_boxes)
        self.wait(2)


class ThreeD_heart_02(SpecialThreeDScene):

    CONFIG = {
        "default_angled_camera_position": {
            "phi": 64 * DEGREES,
            "theta": 30 * DEGREES,
            "distance": 100,
            },
        'camera_config': {'background_color': BLUE_A},
        }
    def construct(self):
        self.set_camera_to_default_position()
        heart_func = lambda x, y, z: (x ** 2 + 9/4 * z ** 2 + y ** 2 - 1) ** 3 - x ** 2 * y ** 3 - 9/80 * z ** 2 * y ** 3
        m, n = 50, 50
        x, y = np.linspace(-1.6, 1.6, n+1), np.linspace(-1.6, 1.6, m+1)
        def dichotomy(func, min=0, max=3, err=1e-4):
            if func(min) * func(max) > 0:
                return 0
            else:
                while max - min > err:
                    mid = (max + min)/2
                    if func(min) * func(mid) <= 0:
                        max = mid
                    else:
                        min = mid
                return (max + min)/2
        z = np.zeros((m+1, n+1))
        for i in range(m+1):
            for j in range(n+1):
                z[i, j] = dichotomy(lambda z: heart_func(x[j], y[i], z)) * 2
        z *= 2.5
        print(z)
        heart_by_boxes = MyBoxes(fill_color=average_color(RED, PINK), resolution=(m+1, n+1), bottom_size=(0.15, 0.15), gap=0)
        heart_by_boxes.update_height_by_2darray(z)
        heart_by_boxes.update_color_by_func(lambda x, y: np.sin((x ** 2 + y ** 2)/12))
        heart = heart_by_boxes.get_high_boxes()
        heart.rotate(PI/2)
        heart.rotate(PI/2, axis=UP)

        self.add(heart)
        # self.play(Rotating(heart, run_time=8))
        self.wait(2)





