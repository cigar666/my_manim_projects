from manimlib.imports import *
import math

class Test_plot(GraphScene):

    CONFIG = {
        "x_min": -0.2,
        "x_max": 1.2,
        "x_axis_width": 10.5,
        "x_tick_frequency": 0.1,
        "y_min": -0.2,
        "y_max": 0.7,
        "y_axis_height": 6.75,
        "y_tick_frequency": 0.1,
        "axes_color": WHITE,
        "graph_origin": 2 * DOWN + 5 * LEFT,
    }

    def construct(self):

        colors = color_gradient([YELLOW, GREEN, BLUE, PINK, RED], 6)
        self.setup_axes(animate=True)
        graph_000 = self.get_graph(lambda x: np.sqrt(x), color=colors[0]) #.make_jagged()
        graph_00 = self.get_graph(lambda x: np.sqrt(x), color=colors[1]).make_jagged().shift(RIGHT * 10.5/7)
        graph_01 = self.get_graph(lambda x: np.sqrt(x), color=colors[2], x_min=0, x_max=0.8).shift(RIGHT * 10.5/7 * 2)
        graph_02 = self.get_graph(lambda x: math.sqrt(x), color=colors[3], x_min=0, x_max=0.8).shift(RIGHT * 10.5/7 * 3)
        s = 10.5/1.4
        graph_03 = ParametricFunction(lambda t: np.sqrt(t) * s * UP + t * s * RIGHT, step_size=0.1,
                                      color=colors[4], t_min=0, t_max=0.8).shift(self.coords_to_point(0.8, 0))
        graph_04 = ParametricFunction(lambda t: np.sqrt(t) * s * UP + t * s * RIGHT, step_size=1e-3,
                                      color=colors[5], t_min=0, t_max=0.8).shift(self.coords_to_point(1, 0))

        self.play(ShowCreation(graph_000))
        self.wait()
        self.play(ShowCreation(graph_00))
        self.wait()
        self.play(ShowCreation(graph_01))
        self.wait()
        self.play(ShowCreation(graph_02))
        self.wait()
        self.play(ShowCreation(graph_03))
        self.wait()
        self.play(ShowCreation(graph_04))

        self.wait(5)


