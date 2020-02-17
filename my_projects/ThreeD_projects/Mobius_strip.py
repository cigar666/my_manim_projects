from manimlib.imports import *

class Mobius_strip(SpecialThreeDScene):
    CONFIG = {
        "default_angled_camera_position": {
            "phi": 66 * DEGREES,
            "theta": -60 * DEGREES,
            "distance": 50,
            },
        'camera_config': {'background_color': WHITE},
    }
    def construct(self):
        self.set_camera_to_default_position()
        R, r = 3.2, 0.8
        mobius_surface = ParametricSurface(lambda u, v: R * np.array([np.cos(u), np.sin(u), 0])
                                                + v * np.cos(u/2) * np.array([np.cos(u), np.sin(u), 0])
                                                + v * np.sin(u/2) * OUT,
                                           u_min=0, u_max=TAU, v_min=-r, v_max=r, resolution=(40, 10),
                                           checkerboard_colors=None, stroke_color=PINK, stroke_opacity=0.6,
                                           stroke_width=1.5, fill_color=BLUE, fill_opacity=0.4)
        mobius_edge = ParametricFunction(lambda t: R * np.array([np.cos(t), np.sin(t), 0])
                                                + r * np.cos(t/2) * np.array([np.cos(t), np.sin(t), 0])
                                                + r * np.sin(t/2) * OUT,
                                         t_min=0, t_max=TAU * 2, color=RED, stroke_width=10, stroke_opacity=0.5)
        h = 0.09
        ball_path = lambda t: R * np.array([np.cos(t), np.sin(t), 0] + h * np.sin(-t/2) * np.array([np.cos(t), np.sin(t), 0]) + h * np.cos(t/2) * OUT)
        ball = Sphere(checkerboard_colors=None, fill_color=RED).set_height(0.48)
        self.time = 0
        def update_ball(b, dt):
            self.time+=dt
            b.move_to(ball_path(self.time))

        self.play(ShowCreation(mobius_surface))
        self.wait(1)
        self.play(ShowCreation(mobius_edge))
        self.wait()
        ball.add_updater(update_ball)
        self.add(ball)
        self.wait(10)
