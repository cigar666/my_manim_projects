from manimlib.imports import *
from my_manim_projects.my_utils.my_geometry import Trail, Sun, Three_Body

class Test_parameters(Scene):

    CONFIG = {
        'camera_config': {'background_image': 'my_manim_projects\\my_projects\\resource\\images\\universe_02.jpg'},
    }
    def construct(self):

        sun_01 = Sun(colors=[BLUE_B, BLUE_A], radius=5, plot_depth=5)
        sun_02 = Sun(colors=[RED_D, RED_A], radius=7, plot_depth=5)
        sun_03 = Sun(colors=[ORANGE, RED_A], radius=6, plot_depth=5)
        planet = Dot(color=BLUE_E, plot_depth=5).scale(0.5)

        # t_01 = Trail(sun_01, color=BLUE_A)
        # t_02 = Trail(sun_02, color=RED_A)
        # t_03 = Trail(sun_03, color=average_color(ORANGE, WHITE))
        # t_04 = Trail(planet, color=BLUE, max_width=3)

        # three_body = Three_Body(sun_01, sun_02, sun_03, planet)

        three_body_config = {
            'mass': np.array([0.98, 1.25, 1]) * 1.,
            'pos': np.array([[-3., -np.sqrt(3), 0], [0., 3 * np.sqrt(3) - 1, 0], [3, -np.sqrt(3), 0]]) * 0.8,
            'velocity': np.array([[1, -np.sqrt(3), 0], [-2, 0, 0], [1, np.sqrt(3), 0]]) * 2,
            'p_pos': np.array([3, -np.sqrt(3), 0]) * 0.8 + np.array([0, 1, 0]) * 0.8,
            'p_velocity':np.array([1, np.sqrt(3), 0]) * 2 + np.array([-1, 0, 0]) * 5,
            } # 后面不稳定
        three_body_config_02 = {
            'mass': np.array([0.98, 1.02, 1]) * 0.9,
            'pos': np.array([[-3., -np.sqrt(3), 0], [0., 3 * np.sqrt(3) - 1, 0], [3, -np.sqrt(3), 0]]) * 0.8,
            'velocity': np.array([[1, -np.sqrt(3), 0], [-2, 0, 0], [1, np.sqrt(3), 0]]) * 1.2,
            'p_pos': np.array([3, -np.sqrt(3), 0]) * 0.8 + np.array([0, 1, 0]) * 0.8,
            'p_velocity':np.array([1, np.sqrt(3), 0]) * 1.2 + np.array([-1, 0, 0]) * 6,
            } # 乱纪元

        three_body_config_03 = {
            'mass': np.array([0.25, 0.6, 1]) * 2,
            'pos': np.array([[-3., -np.sqrt(3), 0], [0., 3 * np.sqrt(3) - 1, 0], [3, -np.sqrt(3), 0]]) * 0.8,
            'velocity': np.array([[1, -np.sqrt(3), 0], [-2, 0, 0], [1, np.sqrt(3), 0]]) * 0.8,
            'p_pos': np.array([3, -np.sqrt(3), 0]) * 0.8 + np.array([0, 1, 0]) * 0.56,
            'p_velocity':np.array([1, np.sqrt(3), 0]) * 1.4 + np.array([-1, 0, 0]) * 10,
            } #

        three_body_config_04 = {
            'mass': np.array([0.5, 0.72, 1.]) * 1.6,
            'pos': np.array([[-3., -np.sqrt(3), 0], [0., 3 * np.sqrt(3) - 1, 0], [3, -np.sqrt(3), 0]]) * 0.5,
            'velocity': np.array([[1, -np.sqrt(3), 0], [-2, 0, 0], [1, np.sqrt(3), 0]]) * 2,
            'p_pos': np.array([3, -np.sqrt(3), 0]) * 0.5 + np.array([0, 1, 0]) * 0.3,
            'p_velocity':np.array([1, np.sqrt(3), 0]) * 2 + np.array([-1, 0, 0]) * 12,
            } # 终止于大撕裂
        three_body_config_04_2 = {
            'mass': np.array([0.5, 0.72, 1.]) * 1.89,
            'pos': np.array([[-3., -np.sqrt(3), 0], [0., 3 * np.sqrt(3) - 1, 0], [3, -np.sqrt(3), 0]]) * 0.64,
            'velocity': np.array([[1, -np.sqrt(3), 0], [-2, 0, 0], [1, np.sqrt(3), 0]]) * 2,
            'p_pos': np.array([3, -np.sqrt(3), 0]) * 0.64 + np.array([0, 1, 0]) * 0.225,
            'p_velocity':np.array([1, np.sqrt(3), 0]) * 2 + np.array([-1, 0, 0]) * 16,
            } # 恒纪元（后面还是乱了）
        three_body_config_05 = {
            'mass': np.array([20, 0.1, 0.12]) * 1,
            'pos': np.array([[0, 0, 0], [4, 0, 0], [4, 1, 0]]) * 0.8,
            'velocity': np.array([[0, 0, 0], [0, 1, 0], [-1, 1, 0]]) * 16,
            'p_pos': np.array([4, 1, 0]) * 0.8 + np.array([0, 1, 0]) * 0.2,
            'p_velocity':np.array([-1, 1, 0]) * 4. + np.array([1, 0, 0]) * 10.,
            } #

        three_body_config_06 = {
            'mass': np.array([0.5, 0.72, 1.]) * 1.25,
            'pos': np.array([[-2., -np.sqrt(3), 0], [0., 2 * np.sqrt(3) - 1, 0], [4, -np.sqrt(3), 0]]) * 0.6,
            'velocity': np.array([[1, -np.sqrt(3), 0], [-2, 0, 0], [1, np.sqrt(3), 0]]) * 1.5,
            'p_pos': np.array([4, -np.sqrt(3), 0]) * 0.6 + np.array([0., 1, 0]) * 0.6,
            'p_velocity':np.array([1, np.sqrt(3), 0]) * 1.5 + np.array([-1, 0, 0]) * 7.2,
            } # 300 * 30 帧后居然没乱掉

        three_body_config_06 = {
            'mass': np.array([0.64, 0.72, 1.]) * 1.6,
            'pos': np.array([[-2., -np.sqrt(3), 0], [0., 2 * np.sqrt(3) - 1, 0], [4, -np.sqrt(3), 0]]) * 0.6,
            'velocity': np.array([[1, -np.sqrt(3), 0], [-2, 0, 0], [1, np.sqrt(3), 0]]) * 1.8,
            'p_pos': np.array([4, -np.sqrt(3), 0]) * 0.6 + np.array([0., 1, 0]) * 0.5,
            'p_velocity':np.array([1, np.sqrt(3), 0]) * 1.8 + np.array([-1.2, 0.1, 0]) * 8,
            } # 300 * 30 帧后居然没乱掉

        three_body = Three_Body(Dot(color=RED).scale(1.2), Dot(color=ORANGE), Dot(color=YELLOW),
                                Dot(color=BLUE_D).scale(0.6), **three_body_config_06)
        three_body.reset_velocity()

        self.add(three_body)
        # three_body.add_updater(update_three_body)
        three_body.start_move()
        # t_01.start_trace(), t_02.start_trace(), t_03.start_trace(), t_04.start_trace()
        self.wait(160)

class Test_parameters_02(Scene):
    ## 测一些参数，有些测好的参数由于Three_Body类后面有所改动所以又不好用了 ##
    CONFIG = {
        'camera_config': {'background_image': 'my_manim_projects\\my_projects\\resource\\images\\universe_02.jpg'},
    }
    def construct(self):

        # sun_01 = Sun(colors=[BLUE_B, BLUE_A], radius=5, plot_depth=5)
        # sun_02 = Sun(colors=[RED_D, RED_A], radius=7, plot_depth=5)
        # sun_03 = Sun(colors=[ORANGE, RED_A], radius=6, plot_depth=5)
        # planet = Dot(color=BLUE_E, plot_depth=5).scale(0.5)

        # t_01 = Trail(sun_01, color=BLUE_A)
        # t_02 = Trail(sun_02, color=RED_A)
        # t_03 = Trail(sun_03, color=average_color(ORANGE, WHITE))
        # t_04 = Trail(planet, color=BLUE, max_width=3)

        # three_body = Three_Body(sun_01, sun_02, sun_03, planet)

        new_config = {
            'mass': np.array([0.9, 1.25, 1]) * 2.,
            'pos': np.array([[-3., -np.sqrt(3), 0], [0., 3 * np.sqrt(3) - 1, 0], [3, -np.sqrt(3), 0]]) * 0.8,
            'velocity': np.array([[1, -np.sqrt(3), 0], [-2, 0, 0], [1, np.sqrt(3), 0]]) * 1.25,
            'p_pos': np.array([3, -np.sqrt(3), 0]) * 0.8 + np.array([0, 1, 0]) * 0.8,
            'p_velocity':np.array([1, np.sqrt(3), 0]) * 2 + np.array([-1, 0, 0]) * 6,
            } # 后面不稳定
        new_config_02 = {
            'mass': np.array([0.98, 1.02, 1]) * 0.9,
            'pos': np.array([[-3., -np.sqrt(3), 0], [0., 3 * np.sqrt(3) - 1, 0], [3, -np.sqrt(3), 0]]) * 0.8,
            'velocity': np.array([[1, -np.sqrt(3), 0], [-2, 0, 0], [1, np.sqrt(3), 0]]) * 1.2,
            'p_pos': np.array([3, -np.sqrt(3), 0]) * 0.8 + np.array([0, 1, 0]) * 0.8,
            'p_velocity':np.array([1, np.sqrt(3), 0]) * 1.2 + np.array([-1, 0, 0]) * 6,
            } # 乱纪元

        new_config_03 = {
            'mass': np.array([0.25, 0.6, 1]) * 2,
            'pos': np.array([[-3., -np.sqrt(3), 0], [0., 3 * np.sqrt(3) - 1, 0], [3, -np.sqrt(3), 0]]) * 0.8,
            'velocity': np.array([[1, -np.sqrt(3), 0], [-2, 0, 0], [1, np.sqrt(3), 0]]) * 0.8,
            'p_pos': np.array([3, -np.sqrt(3), 0]) * 0.8 + np.array([0, 1, 0]) * 0.56,
            'p_velocity':np.array([1, np.sqrt(3), 0]) * 1.4 + np.array([-1, 0, 0]) * 10,
            } #

        new_config_04 = {
            'mass': np.array([0.5, 0.72, 1.]) * 1.6,
            'pos': np.array([[-3.2, 0.4-np.sqrt(3), 0], [0.5, 3 * np.sqrt(3) - 1.2, 0], [2.9, -1.2-np.sqrt(3), 0]]) * 0.5,
            'velocity': np.array([[1, -np.sqrt(3), 0], [-2, 0, 0], [1, np.sqrt(3), 0]]) * 1.75,
            'p_pos': np.array([2.9, -1.2-np.sqrt(3), 0]) * 0.5 + np.array([0, 1, 0]) * 0.5,
            'p_velocity':np.array([1, np.sqrt(3), 0]) * 2 + np.array([-1, 0, 0]) * 11.8,
            } # 终止于大撕裂
        new_config_04_2 = {
            'mass': np.array([0.5, 0.72, 1.]) * 2,
            'pos': np.array([[-3., -np.sqrt(3), 0], [0., 3 * np.sqrt(3) - 1, 0], [3, -np.sqrt(3), 0]]) * 0.6,
            'velocity': np.array([[1, -np.sqrt(3), 0], [-2, 0, 0], [1, np.sqrt(3), 0]]) * 1.6,
            'p_pos': np.array([3, -np.sqrt(3), 0]) * 0.64 + np.array([0, 1, 0]) * 0.225,
            'p_velocity':np.array([1, np.sqrt(3), 0]) * 1.6 + np.array([-1, 0, 0]) * 15,
            } # 恒纪元（后面还是乱了）
        new_config_05 = {
            'mass': np.array([20, 0.1, 0.12]) * 1,
            'pos': np.array([[0, 0, 0], [4, 0, 0], [4, 1, 0]]) * 0.8,
            'velocity': np.array([[0, 0, 0], [0, 1, 0], [-1, 1, 0]]) * 16,
            'p_pos': np.array([4, 1, 0]) * 0.8 + np.array([0, 1, 0]) * 0.2,
            'p_velocity':np.array([-1, 1, 0]) * 4. + np.array([1, 0, 0]) * 10.,
            } #
        new_config_06 = {
            'mass': np.array([0.64, 0.72, 1.]) * 1.6,
            'pos': np.array([[-2., -np.sqrt(3), 0], [0., 2 * np.sqrt(3) - 1, 0], [4, -np.sqrt(3), 0]]) * 0.6,
            'velocity': np.array([[1, -np.sqrt(3), 0], [-2, 0, 0], [1, np.sqrt(3), 0]]) * 1.8,
            'p_pos': np.array([4, -np.sqrt(3), 0]) * 0.6 + np.array([0., 1, 0]) * 0.5,
            'p_velocity':np.array([1, np.sqrt(3), 0]) * 1.8 + np.array([-1.2, 0.1, 0]) * 8,
            }

        three_body = Three_Body(Dot(color=RED).scale(1.2), Dot(color=ORANGE), Dot(color=YELLOW),
                                Dot(color=BLUE_D).scale(0.6), **new_config)
        three_body.reset_velocity()

        self.add(three_body)
        # three_body.add_updater(update_three_body)
        three_body.start_move()
        # t_01.start_trace(), t_02.start_trace(), t_03.start_trace(), t_04.start_trace()
        self.wait(60)

class Three_body_test(Scene):
    CONFIG = {
        'camera_config': {'background_image': 'my_manim_projects\\my_projects\\resource\\images\\universe_02.jpg'},
    }

    def construct(self):

        sun_01 = Sun(colors=[BLUE_B, BLUE_A], radius=5, plot_depth=5)
        sun_02 = Sun(colors=[RED_D, RED_A], radius=7, plot_depth=5)
        sun_03 = Sun(colors=[ORANGE, RED_A], radius=6, plot_depth=5)
        planet = Dot(color=BLUE_E, plot_depth=5).scale(0.4)

        t_01 = Trail(sun_01, trail_color=BLUE_B, max_width=4)
        t_02 = Trail(sun_02, trail_color=RED_A, max_width=5.6)
        t_03 = Trail(sun_03, trail_color=average_color(ORANGE, WHITE), max_width=4.8)
        t_04 = Trail(planet, trail_color=BLUE_D, max_width=2, nums=720)

        three_body = Three_Body(sun_01, sun_02, sun_03, planet)
        # three_body = Three_Body(Dot(color=RED), Dot(color=ORANGE), Dot(color=YELLOW),
        #                         Dot(color=BLUE_E).scale(0.6))
        three_body.reset_velocity()
        self.add(three_body, t_01.trail, t_02.trail, t_03.trail, t_04.trail)

        # three_body.add_updater(update_three_body)
        three_body.start_move()
        t_01.start_trace(), t_02.start_trace(), t_03.start_trace(), t_04.start_trace()
        self.wait(16)

class Three_body_config_02(Scene):

    CONFIG = {
        'camera_config': {'background_image': 'my_manim_projects\\my_projects\\resource\\images\\universe_02.jpg'},
    }

    def construct(self):

        three_body_config_02 = {
            'mass': np.array([0.98, 1.02, 1]) * 0.9,
            'pos': np.array([[-3., -np.sqrt(3), 0], [0., 3 * np.sqrt(3) - 1, 0], [3, -np.sqrt(3), 0]]) * 0.8,
            'velocity': np.array([[1, -np.sqrt(3), 0], [-2, 0, 0], [1, np.sqrt(3), 0]]) * 1.2,
            'p_pos': np.array([3, -np.sqrt(3), 0]) * 0.8 + np.array([0, 1, 0]) * 0.8,
            'p_velocity':np.array([1, np.sqrt(3), 0]) * 1.2 + np.array([-1, 0, 0]) * 6,
            } # 乱纪元

        sun_01 = Sun(colors=[BLUE_B, BLUE_A], radius=4.2, plot_depth=5)
        sun_02 = Sun(colors=[ORANGE, YELLOW_B], radius=5, plot_depth=5)
        sun_03 = Sun(colors=[RED, RED_A], radius=6, plot_depth=5)
        planet = Dot(color=BLUE_D, plot_depth=5).scale(0.5)

        t_01 = Trail(sun_01, trail_color=BLUE_B, max_width=3.8)
        t_02 = Trail(sun_02, trail_color=ORANGE, max_width=4.)
        t_03 = Trail(sun_03, trail_color=average_color(RED, WHITE), max_width=4.2)
        t_04 = Trail(planet, trail_color=BLUE_D, max_width=2., nums=640)

        three_body = Three_Body(sun_01, sun_02, sun_03, planet, **three_body_config_02)
        # three_body = Three_Body(Dot(color=RED), Dot(color=ORANGE), Dot(color=YELLOW),
        #                         Dot(color=BLUE_E).scale(0.6))
        three_body.reset_velocity()
        self.add(three_body, t_01.trail, t_02.trail, t_03.trail, t_04.trail)

        # three_body.add_updater(update_three_body)
        three_body.start_move()
        t_01.start_trace(), t_02.start_trace(), t_03.start_trace(), t_04.start_trace()
        self.wait(1)
        self.wait(4)
        self.wait(10)
        self.wait(40)

class Three_body_config_06_02(Scene):

    CONFIG = {
        'camera_config': {'background_image': 'my_manim_projects\\my_projects\\resource\\images\\universe_02.jpg'},
    }

    def construct(self):

        three_body_config_06 = {
            'mass': np.array([0.5, 0.72, 1.]) * 1.25,
            'pos': np.array([[-2., -np.sqrt(3), 0], [0., 2 * np.sqrt(3) - 1, 0], [4, -np.sqrt(3), 0]]) * 0.6,
            'velocity': np.array([[1, -np.sqrt(3), 0], [-2, 0, 0], [1, np.sqrt(3), 0]]) * 1.5,
            'p_pos': np.array([4, -np.sqrt(3), 0]) * 0.6 + np.array([0., 1, 0]) * 0.6,
            'p_velocity':np.array([1, np.sqrt(3), 0]) * 1.5 + np.array([-1, 0, 0]) * 7.2,
            }

        # new_config_04 = {
        #     'mass': np.array([0.5, 0.72, 1.]) * 1.6,
        #     'pos': np.array([[-3.2, 0.4-np.sqrt(3), 0], [0.5, 3 * np.sqrt(3) - 1.2, 0], [2.9, -1.2-np.sqrt(3), 0]]) * 0.5,
        #     'velocity': np.array([[1, -np.sqrt(3), 0], [-2, 0, 0], [1, np.sqrt(3), 0]]) * 1.75,
        #     'p_pos': np.array([2.9, -1.2-np.sqrt(3), 0]) * 0.5 + np.array([0, 1, 0]) * 0.5,
        #     'p_velocity':np.array([1, np.sqrt(3), 0]) * 2 + np.array([-1, 0, 0]) * 12,
        #     }

        sun_01 = Sun(colors=[BLUE_B, BLUE_A], radius=4.5, plot_depth=5)
        sun_02 = Sun(colors=[ORANGE, YELLOW_B], radius=5.4, plot_depth=5)
        sun_03 = Sun(colors=[RED, RED_A], radius=6.6, plot_depth=5)
        planet = Dot(color=BLUE_D, plot_depth=5).scale(0.5)

        t_01 = Trail(sun_01, trail_color=BLUE_B, max_width=3.8)
        t_02 = Trail(sun_02, trail_color=ORANGE, max_width=4.2)
        t_03 = Trail(sun_03, trail_color=average_color(RED, WHITE), max_width=4.8)
        t_04 = Trail(planet, trail_color=BLUE_D, max_width=2., nums=640)

        three_body = Three_Body(sun_01, sun_02, sun_03, planet, **three_body_config_06)
        # three_body = Three_Body(Dot(color=RED), Dot(color=ORANGE), Dot(color=YELLOW),
        #                         Dot(color=BLUE_E).scale(0.6))
        three_body.reset_velocity()
        self.add(three_body, t_01.trail, t_02.trail, t_03.trail, t_04.trail)

        # three_body.add_updater(update_three_body)
        three_body.start_move()
        t_01.start_trace(), t_02.start_trace(), t_03.start_trace(), t_04.start_trace()
        self.wait(1)
        self.wait(2)
        self.wait(4)
        self.wait(10)
        self.wait(15)
        # self.wait(25)
        # self.wait(32)

class Three_body_new_config_04(Scene):

    CONFIG = {
        'camera_config': {'background_image': 'my_manim_projects\\my_projects\\resource\\images\\universe_02.jpg'},
    }

    def construct(self):

        # three_body_config_06 = {
        #     'mass': np.array([0.5, 0.72, 1.]) * 1.25,
        #     'pos': np.array([[-2., -np.sqrt(3), 0], [0., 2 * np.sqrt(3) - 1, 0], [4, -np.sqrt(3), 0]]) * 0.6,
        #     'velocity': np.array([[1, -np.sqrt(3), 0], [-2, 0, 0], [1, np.sqrt(3), 0]]) * 1.5,
        #     'p_pos': np.array([4, -np.sqrt(3), 0]) * 0.6 + np.array([0., 1, 0]) * 0.6,
        #     'p_velocity':np.array([1, np.sqrt(3), 0]) * 1.5 + np.array([-1, 0, 0]) * 7.2,
        #     }

        new_config_04 = {
            'mass': np.array([0.5, 0.72, 1.]) * 1.6,
            'pos': np.array([[-3.2, 0.4-np.sqrt(3), 0], [0.5, 3 * np.sqrt(3) - 1.2, 0], [2.9, -1.2-np.sqrt(3), 0]]) * 0.5,
            'velocity': np.array([[1, -np.sqrt(3), 0], [-2, 0, 0], [1, np.sqrt(3), 0]]) * 1.75,
            'p_pos': np.array([2.9, -1.2-np.sqrt(3), 0]) * 0.5 + np.array([0, 1, 0]) * 0.5,
            'p_velocity':np.array([1, np.sqrt(3), 0]) * 2 + np.array([-1, 0, 0]) * 12,
            }

        sun_01 = Sun(colors=[BLUE_B, BLUE_A], radius=4.5, plot_depth=5)
        sun_02 = Sun(colors=[ORANGE, YELLOW_B], radius=5.4, plot_depth=5)
        sun_03 = Sun(colors=[RED, RED_A], radius=6.6, plot_depth=5)
        planet = Dot(color=BLUE_D, plot_depth=5).scale(0.5)

        t_01 = Trail(sun_01, trail_color=BLUE_B, max_width=3.8)
        t_02 = Trail(sun_02, trail_color=ORANGE, max_width=4.2)
        t_03 = Trail(sun_03, trail_color=average_color(RED, WHITE), max_width=4.8)
        t_04 = Trail(planet, trail_color=BLUE_D, max_width=2., nums=640)

        three_body = Three_Body(sun_01, sun_02, sun_03, planet, **new_config_04)
        # three_body = Three_Body(Dot(color=RED), Dot(color=ORANGE), Dot(color=YELLOW),
        #                         Dot(color=BLUE_E).scale(0.6))
        three_body.reset_velocity()
        self.add(three_body, t_01.trail, t_02.trail, t_03.trail, t_04.trail)

        # three_body.add_updater(update_three_body)
        three_body.start_move()
        t_01.start_trace(), t_02.start_trace(), t_03.start_trace(), t_04.start_trace()
        self.wait(1)
        self.wait(2)
        self.wait(4)
        self.wait(10)
        self.wait(15)
        self.wait(25)
        self.wait(32)

class Counting_time(Scene):

    def construct(self):

        nums = VGroup(*[Text('%d' % i, color='#51FC18', font='ADMUI3Lg').set_height(0.5).shift(0.5 * i * RIGHT) for i in range(10)]).move_to(ORIGIN)

        text = Text('恒 纪 元', color='#51FC18', font='思源黑体 Bold').set_height(0.54).shift(UP)
        self.add(nums, text)
        self.wait()

        ## 算了，没时间了，不写了 ##

class SanLian(Scene):

    ## 利用三体运动，得到三连运动，以方便更好的骗三连 ##

    def construct(self):

        path = 'my_manim_projects\\my_projects\\resource\\svg_files\\'
        good = SVGMobject(path + 'good.svg', color=PINK, plot_depth=6).set_height(0.3)
        coin = SVGMobject(path + 'coin.svg', color=BLUE, plot_depth=6).set_height(0.32)
        favo = SVGMobject(path + 'favo.svg', color=ORANGE, plot_depth=6).set_height(0.32)

        circle_01 = Circle(radius=0.24, stroke_width=5, color=PINK, plot_depth=6)
        circle_02 = Circle(radius=0.24, stroke_width=5, color=BLUE, plot_depth=6)
        circle_03 = Circle(radius=0.24, stroke_width=5, color=ORANGE, plot_depth=6)

        sun_01, sun_02, sun_03 = VGroup(circle_01, good), VGroup(circle_02, coin), VGroup(circle_03, favo)

        new_config_04 = {
            'mass': np.array([0.5, 0.72, 1.]) * 1.6,
            'pos': np.array([[-3.2, 0.4-np.sqrt(3), 0], [0.5, 3 * np.sqrt(3) - 1.2, 0], [2.9, -1.2-np.sqrt(3), 0]]) * 0.5,
            'velocity': np.array([[1, -np.sqrt(3), 0], [-2, 0, 0], [1, np.sqrt(3), 0]]) * 1.75,
            'p_pos': np.array([2.9, -1.2-np.sqrt(3), 0]) * 0.5 + np.array([0, 1, 0]) * 0.5,
            'p_velocity':np.array([1, np.sqrt(3), 0]) * 2 + np.array([-1, 0, 0]) * 12,
            }

        planet = Dot(color=BLUE_D, plot_depth=5).scale(0.5)

        t_01 = Trail(sun_01, trail_color=PINK, max_width=4, nums=750)
        t_02 = Trail(sun_02, trail_color=BLUE, max_width=4, nums=750)
        t_03 = Trail(sun_03, trail_color=ORANGE, max_width=4, nums=750)
        # t_04 = Trail(planet, trail_color=BLUE_D, max_width=2., nums=640)

        three_body = Three_Body(sun_01, sun_02, sun_03, **new_config_04)
        # three_body = Three_Body(Dot(color=RED), Dot(color=ORANGE), Dot(color=YELLOW),
        #                         Dot(color=BLUE_E).scale(0.6))
        three_body.reset_velocity()

        three_body.start_move()
        self.add(three_body)
        self.add(t_01.trail, t_02.trail, t_03.trail)
        t_01.start_trace(), t_02.start_trace(), t_03.start_trace()
        self.wait(1)
        self.wait(4)
        self.wait(10)
        self.wait(15)
        self.wait(30)

