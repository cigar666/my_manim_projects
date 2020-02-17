# this file need to do some changes to run on the new version of manim
from manimlib.imports import *
from active_projects.diffyq.part2.fourier_series import FourierOfTrebleClef, FourierOfPiSymbol
from active_projects.diffyq.part4.fourier_series_scenes import ComplexFourierSeriesExample
svg_path = 'my_projects\\resource\\svg_files\\'

class Show_misaka_long_y(Scene):

    def construct(self):

        misaka = SVGMobject(svg_path + 'misaka_new.svg').scale(3.6).set_fill(BLACK, 1).set_stroke(YELLOW, 2.5, 1)

        self.play(ShowCreation(misaka), run_time=20)
        self.wait(5)

class Change_misaka2text(Scene):


    def construct(self):

        misaka = SVGMobject(svg_path + 'misaka_new.svg').scale(3.75).set_fill(BLACK, 1).set_stroke(YELLOW, 2.5, 1)

        self.add(misaka)
        self.play(ReplacementTransform(misaka, TextMobject('感 谢 收 看', color=YELLOW).scale(3.6).shift(UP * 0.75)), run_time=2.5)
        self.wait(5)



class One(FourierOfPiSymbol):
    CONFIG = {
        "tex": "1",
        "n_vectors": 100,
    }
class Two(FourierOfPiSymbol):
    CONFIG = {
        "tex": "2",
        "n_vectors": 100,
    }
class Three(FourierOfPiSymbol):
    CONFIG = {
        "tex": "3",
        "n_vectors": 100,
    }

class Go(Scene):
    def construct(self):
        text = TextMobject('go!', color=YELLOW).scale(7.2)
        self.play(FadeInFromLarge(text))
        self.wait(1)


class Show_svg_text(Scene):


    def construct(self):

        # misaka = SVGMobject(svg_path + 'misaka.svg').scale(3.6).set_fill(BLACK, 1).set_stroke(WHITE, 2, 1)

        # self.play(ShowCreation(misaka))
        # self.wait(5)

        text_color = '#C82627'

        text01 = SVGMobject(svg_path + 'text_mkxd.svg').scale(2.5).set_color(text_color)
        text02 = TextMobject(*['$\\emph{\\kaishu{傅}}$', '$\\emph{立}$', '$\\emph{葉}$', '$\\emph{級}$', '$\\emph{數}$'], color=text_color).scale(1.5)
        text02_0 = TextMobject('$\\emph{\\kaishu{傅}}$', background_stroke_color=WHITE).scale(1.5).move_to(text02[0])
        text02_0.scale(1.78).next_to(text01, LEFT * 0.72).shift(UP * 0.6).set_color(WHITE).set_stroke(WHITE)
        rect = SurroundingRectangle(text02_0, color=text_color, fill_color=text_color, fill_opacity=1).scale(0.82)

        text02[2].scale(0.9).next_to(rect, DOWN * 0.45).align_to(rect, RIGHT)
        text02[1].scale(0.9).next_to(text02[2], LEFT * 0.4)#.align_to(text02[0], RIGHT)
        text02[3].scale(1.4).next_to(text02[2], DOWN * 0.5).align_to(rect, RIGHT).shift(RIGHT * 0.05)
        text02[4].scale(1.8).next_to(text02[3], DOWN * 0.54).align_to(rect, RIGHT).shift(RIGHT * 0.075)

        text_group = VGroup(text01, rect, text02_0, text02[1:5]).move_to(ORIGIN)

        # self.play(FadeIn(text01), run_time=1.5)
        # self.play(FadeInFromLarge(VGroup(rect, text02[0])))
        # self.play(Write(text02[1]))
        # self.play(Write(text02[2]))
        # self.play(Write(text02[3]))
        # self.play(Write(text02[4]))
        self.add(text_group)
        self.wait(4)

class ComplexFourierSeriesExample(FourierOfTrebleClef):
    CONFIG = {
        "file_name": svg_path + 'misaka_new.svg',
        "run_time": 12,
        "n_vectors": 2400,
        "n_cycles": 2,
        "max_circle_stroke_width": 0.8,
        "drawing_height": 5.4,
        "center_point": DOWN * 1.1,
        "top_row_center": 3 * UP,
        "top_row_label_y": 2,
        "top_row_x_spacing": 1.75,
        "top_row_copy_scale_factor": 0.9,
        "start_drawn": False,
        "plane_config": {
            "axis_config": {"unit_size": 2},
            "y_min": -1.25,
            "y_max": 1.25,
            "x_min": -2.5,
            "x_max": 2.5,
            "background_line_style": {
                "stroke_width": 1,
                "stroke_color": LIGHT_GREY,
            },
        },
        "top_rect_height": 2.5,
    }

    def construct(self):
        self.add_vectors_circles_path()
        self.add_top_row(self.vectors, self.circles)
        self.write_title()
        self.highlight_vectors_one_by_one()
        # self.change_shape()

    def write_title(self):
        title = TextMobject("Misaka By\\\\Fourier series")
        title.scale(1.5)
        title.to_edge(LEFT)
        title.match_y(self.path)

        self.wait(11)
        self.play(FadeInFromDown(title))
        self.wait(2)
        self.title = title

    def highlight_vectors_one_by_one(self):
        # Don't know why these vectors can't get copied.
        # That seems like a problem that will come up again.
        labels = self.top_row[-1]
        next_anims = []
        for vector, circle, label in zip(self.vectors, self.circles, labels):
            # v_color = vector.get_color()
            c_color = circle.get_color()
            c_stroke_width = circle.get_stroke_width()

            rect = SurroundingRectangle(label, color=PINK)
            self.play(
                # vector.set_color, PINK,
                circle.set_stroke, RED, 3,
                FadeIn(rect),
                *next_anims
            )
            self.wait()
            next_anims = [
                # vector.set_color, v_color,
                circle.set_stroke, c_color, c_stroke_width,
                FadeOut(rect),
            ]
        self.play(*next_anims)

    def change_shape(self):
        # path_mob = TexMobject("\\pi")
        path_mob = SVGMobject("Nail_And_Gear")
        new_path = path_mob.family_members_with_points()[0]
        new_path.set_height(4)
        new_path.move_to(self.path, DOWN)
        new_path.shift(0.5 * UP)

        self.transition_to_alt_path(new_path)
        for n in range(self.n_cycles):
            self.run_one_cycle()

    def transition_to_alt_path(self, new_path, morph_path=False):
        new_coefs = self.get_coefficients_of_path(new_path)
        new_vectors = self.get_rotating_vectors(
            coefficients=new_coefs
        )
        new_drawn_path = self.get_drawn_path(new_vectors)

        self.vector_clock.suspend_updating()

        vectors = self.vectors
        anims = []

        for vect, new_vect in zip(vectors, new_vectors):
            new_vect.update()
            new_vect.clear_updaters()

            line = Line(stroke_width=0)
            line.put_start_and_end_on(*vect.get_start_and_end())
            anims.append(ApplyMethod(
                line.put_start_and_end_on,
                *new_vect.get_start_and_end()
            ))
            vect.freq = new_vect.freq
            vect.coefficient = new_vect.coefficient

            vect.line = line
            vect.add_updater(
                lambda v: v.put_start_and_end_on(
                    *v.line.get_start_and_end()
                )
            )
        if morph_path:
            anims.append(
                ReplacementTransform(
                    self.drawn_path,
                    new_drawn_path
                )
            )
        else:
            anims.append(
                FadeOut(self.drawn_path)
            )

        self.play(*anims, run_time=3)
        for vect in self.vectors:
            vect.remove_updater(vect.updaters[-1])

        if not morph_path:
            self.add(new_drawn_path)
            self.vector_clock.set_value(0)

        self.vector_clock.resume_updating()
        self.drawn_path = new_drawn_path

    #
    def get_path(self):
        path = super().get_path()
        path.set_height(self.drawing_height)
        path.to_edge(DOWN)
        return path

    def add_top_row(self, vectors, circles, max_freq=3):
        self.top_row = self.get_top_row(
            vectors, circles, max_freq
        )
        self.add(self.top_row)

    def get_top_row(self, vectors, circles, max_freq=3):
        vector_copies = VGroup()
        circle_copies = VGroup()
        for vector, circle in zip(vectors, circles):
            if vector.freq > max_freq:
                break
            vcopy = vector.copy()
            vcopy.clear_updaters()
            ccopy = circle.copy()
            ccopy.clear_updaters()
            ccopy.original = circle
            vcopy.original = vector

            vcopy.center_point = op.add(
                self.top_row_center,
                vector.freq * self.top_row_x_spacing * RIGHT,
            )
            ccopy.center_point = vcopy.center_point
            vcopy.add_updater(self.update_top_row_vector_copy)
            ccopy.add_updater(self.update_top_row_circle_copy)
            vector_copies.add(vcopy)
            circle_copies.add(ccopy)

        dots = VGroup(*[
            TexMobject("\\dots").next_to(
                circle_copies, direction,
                MED_LARGE_BUFF,
            )
            for direction in [LEFT, RIGHT]
        ])
        labels = self.get_top_row_labels(vector_copies)
        return VGroup(
            vector_copies,
            circle_copies,
            dots,
            labels,
        )

    def update_top_row_vector_copy(self, vcopy):
        vcopy.become(vcopy.original)
        vcopy.scale(self.top_row_copy_scale_factor)
        vcopy.shift(vcopy.center_point - vcopy.get_start())
        return vcopy

    def update_top_row_circle_copy(self, ccopy):
        ccopy.become(ccopy.original)
        ccopy.scale(self.top_row_copy_scale_factor)
        ccopy.move_to(ccopy.center_point)
        return ccopy

    def get_top_row_labels(self, vector_copies):
        labels = VGroup()
        for vector_copy in vector_copies:
            freq = vector_copy.freq
            label = Integer(freq)
            label.move_to(np.array([
                freq * self.top_row_x_spacing,
                self.top_row_label_y,
                0
            ]))
            labels.add(label)
        return labels

    def setup_plane(self):
        plane = ComplexPlane(**self.plane_config)
        plane.shift(self.center_point)
        plane.add_coordinates()

        top_rect = Rectangle(
            width=FRAME_WIDTH,
            fill_color=BLACK,
            fill_opacity=1,
            stroke_width=0,
            height=self.top_rect_height,
        )
        top_rect.to_edge(UP, buff=0)

        self.plane = plane
        self.add(plane)
        self.add(top_rect)

    def get_path_end(self, vectors, stroke_width=None, **kwargs):
        if stroke_width is None:
            stroke_width = self.drawn_path_st
        full_path = self.get_vector_sum_path(vectors, **kwargs)
        path = VMobject()
        path.set_stroke(
            self.drawn_path_color,
            stroke_width
        )

        def update_path(p):
            alpha = self.get_vector_time() % 1
            p.pointwise_become_partial(
                full_path,
                np.clip(alpha - 0.01, 0, 1),
                np.clip(alpha, 0, 1),
            )
            p.points[-1] = vectors[-1].get_end()

        path.add_updater(update_path)
        return path

    def get_drawn_path_alpha(self):
        return super().get_drawn_path_alpha() - 0.002

    def get_drawn_path(self, vectors, stroke_width=2, **kwargs):
        odp = super().get_drawn_path(vectors, stroke_width, **kwargs)
        return VGroup(
            odp,
            self.get_path_end(vectors, stroke_width, **kwargs),
        )

    def get_vertically_falling_tracing(self, vector, color, stroke_width=3, rate=0.25):
        path = VMobject()
        path.set_stroke(color, stroke_width)
        path.start_new_path(vector.get_end())
        path.vector = vector

        def update_path(p, dt):
            p.shift(rate * dt * DOWN)
            p.add_smooth_curve_to(p.vector.get_end())
        path.add_updater(update_path)
        return path

class Change_pigeon2deer(ComplexFourierSeriesExample):
    CONFIG = {
        "file_name": svg_path + 'pigeon.svg',
        "run_time": 12,
        "n_vectors": 240,
        "n_cycles": 2,
        "max_circle_stroke_width": 0.8,
        "drawing_height": 4.5,
        "center_point": DOWN * 1.5,
        "top_row_center": 2.5 * UP,
        "top_row_label_y": 2,
        "top_row_x_spacing": 1.8,
        "top_row_copy_scale_factor": 0.9,
        "start_drawn": False,
        "plane_config": {
            "axis_config": {"unit_size": 2},
            "y_min": -1.25,
            "y_max": 1.25,
            "x_min": -2.5,
            "x_max": 2.5,
            "background_line_style": {
                "stroke_width": 1,
                "stroke_color": LIGHT_GREY,
            },
        },
        "top_rect_height": 2.5,
    }

    def construct(self):
        self.add_vectors_circles_path()
        self.add_top_row(self.vectors, self.circles)
        self.wait(6)
        self.highlight_vectors_one_by_one()
        self.change_shape()
        self.wait(2)
        # self.highlight_vectors_one_by_one()

    def change_shape(self):
        # path_mob = TexMobject("\\pi")
        path_mob = SVGMobject(svg_path + 'deer.svg')
        new_path = path_mob.family_members_with_points()[0]
        new_path.set_height(4.5)
        new_path.move_to(self.path)
        # new_path.shift(0.5 * UP)

        self.transition_to_alt_path(new_path)
        # self.wait(0.25)
        for n in range(self.n_cycles):
            self.run_one_cycle()

class Deer_by_fourier(ComplexFourierSeriesExample):
    CONFIG = {
        "file_name": svg_path + 'deer.svg',
        "run_time": 18,
        "n_vectors": 240,
        "n_cycles": 2,
        "max_circle_stroke_width": 0.8,
        "drawing_height": 4.5,
        "center_point": DOWN * 1.5,
        "top_row_center": 2.5 * UP,
        "top_row_label_y": 2,
        "top_row_x_spacing": 1.8,
        "top_row_copy_scale_factor": 0.9,
        "start_drawn": False,
        "plane_config": {
            "axis_config": {"unit_size": 2},
            "y_min": -1.25,
            "y_max": 1.25,
            "x_min": -2.5,
            "x_max": 2.5,
            "background_line_style": {
                "stroke_width": 1,
                "stroke_color": LIGHT_GREY,
            },
        },
        "top_rect_height": 2.5,
    }

    def construct(self):
        self.add_vectors_circles_path()
        self.add_top_row(self.vectors, self.circles)
        self.wait(20)
        # self.highlight_vectors_one_by_one()
        # self.change_shape()
        # self.wait(2)
        # self.highlight_vectors_one_by_one()

class Misaka_by_ComplecxFourierSeries(FourierOfTrebleClef):

    CONFIG = {
        "file_name": svg_path + 'misaka_new.svg',
        # "run_time": 64,
        "slow_factor": 0.02,
        "n_vectors": 2400,
        "n_cycles": 1,
        "max_circle_stroke_width": 0.8,
        "height": 7.5,
        "center_point": ORIGIN,
    }

class Misaka_100_250_5s(Misaka_by_ComplecxFourierSeries):
    CONFIG = {

        "slow_factor": 0.004,
        "n_vectors": 2400,
        "n_cycles": 1,
        "max_circle_stroke_width": 0.8,
        "height": 7.5,
        "center_point": ORIGIN,
    }
    def construct(self):
        self.vector_clock.set_value(100/250)
        self.add_vectors_circles_path()
        self.wait(5)

class Misaka_with_rect20X(Misaka_by_ComplecxFourierSeries):

    CONFIG = {
        "file_name": svg_path + 'misaka_new.svg',
        "run_time": 24,
        "n_vectors": 2400,
        "slow_factor": 0.001,
    }
    def construct(self):
        #self.always_continually_update = True
        rect = Rectangle(color=BLUE, stroke_width=2).scale(2 * 4 / 20)
        self.add(rect)
        rect.add_updater(self.update_rect)
        self.add_vectors_circles_path()
        for n in range(self.n_cycles):
            self.run_one_cycle()

    def update_rect(self, rect):
        path = self.get_path()
        coefs = self.get_coefficients_of_path(path)
        vectors = self.get_rotating_vectors(coefficients=coefs)
        circles = self.get_circles(vectors)
        rect.move_to(circles[-1].get_center())
        return rect

class FourierSeriesExampleWithRectForZoom(ComplexFourierSeriesExample):
    CONFIG = {
        "n_vectors": 100,
        "slow_factor": 0.002,
        "rect_scale_factor": 0.1,
        "start_drawn": True,
        "drawing_height": 7,
        "rect_stroke_width": 1,

    }

    def construct(self):
        self.vector_clock.set_value(100/250)
        self.add_vectors_circles_path()
        self.circles.set_stroke(opacity=0.6)
        rect = self.rect = self.get_rect()
        rect.set_height(self.rect_scale_factor * FRAME_HEIGHT)
        rect.add_updater(lambda m: m.move_to(
            self.get_rect_center()
        ))
        self.add(rect)
        # self.run_one_cycle()
        self.wait(6)


    def get_rect_center(self):
        return center_of_mass([
            v.get_end()
            for v in self.vectors
        ])

    def get_rect(self):
        return ScreenRectangle(
            color=BLUE,
            stroke_width=self.rect_stroke_width,
        )

class Misaka_with_rect_X10(FourierSeriesExampleWithRectForZoom):

    CONFIG = {
        "file_name": svg_path + 'misaka_new.svg',
        # "run_time": 5,
        "n_vectors": 2400,
        "slow_factor": 0.002,
        "rect_stroke_width": 2.5,
        "rect_scale_factor": 0.1,

    }

    def construct(self):
        self.vector_clock.set_value(45/500)
        self.add_vectors_circles_path()
        self.circles.set_stroke(opacity=0.6)
        rect = self.rect = self.get_rect()
        rect.set_height(self.rect_scale_factor * FRAME_HEIGHT)
        rect.add_updater(lambda m: m.move_to(
            self.get_rect_center()
        ))
        self.add(rect)
        self.wait(20)

class ZoomedInFourierSeriesExample(FourierSeriesExampleWithRectForZoom, MovingCameraScene):
    CONFIG = {
        "vector_config": {
            "max_tip_length_to_length_ratio": 0.15,
            "tip_length": 0.05,
        },
        "parametric_function_step_size": 0.001,
    }

    def setup(self):
        ComplexFourierSeriesExample.setup(self)
        MovingCameraScene.setup(self)

    def get_rect(self):
        return self.camera_frame

    def add_vectors_circles_path(self):
        super().add_vectors_circles_path()
        for v in self.vectors:
            if v.get_stroke_width() < 1:
                v.set_stroke(width=1)


class ZoomedInFourierSeriesExample100x(ZoomedInFourierSeriesExample):
    CONFIG = {

        # "run_time": 12,
        #"n_vectors": 4800,
        "n_cycles": 1,

        "vector_config": {
            "max_tip_length_to_length_ratio": 0.5 * 0.4,
            "tip_length": 0.8 * 0.2,
            "max_stroke_width_to_length_ratio": 80,
            "stroke_width": 3,
        },
        "max_circle_stroke_width": 0.5,
        "rect_scale_factor": 0.01,
        # "parametric_function_step_size": 0.01,
    }

    def get_rect_center(self):
        return self.vectors[-1].get_end()

    # def get_drawn_path(self, vectors, stroke_width=2, **kwargs):
    #     return self.get_path_end(vectors, stroke_width, **kwargs)


class SigmaFourierSeriesExampleWithRectForZoom(FourierSeriesExampleWithRectForZoom):
    CONFIG = {
        "n_vectors": 200,
        "drawn_path_color": PINK,
        "rect_stroke_width": 0,
    }

    def get_shape(self):
        return TexMobject("\\Sigma")


class FourierOfFourier(FourierSeriesExampleWithRectForZoom):
    CONFIG = {
        "file_name": "FourierOneLine",
        "n_vectors": 300,
        "rect_stroke_width": 1,
    }


class FourierOfFourierZoomedIn_misaka(ZoomedInFourierSeriesExample):
    CONFIG = {
        "file_name": svg_path + 'misaka.svg',
        "max_circle_stroke_width": 0.5,
        "n_vectors": 2400,
    }


class FourierOfFourier100xZoom_misaka(ZoomedInFourierSeriesExample100x):
    CONFIG = {
        "run_time": 12,
        "file_name": svg_path + 'misaka_new.svg',
        "max_circle_stroke_width": 0.6,
        "n_vectors": 2400,
        "slow_factor": 0.001,
        "rect_scale_factor": 0.01,
    }

    def run_one_cycle(self):
        self.vector_clock.set_value(0.2)
        self.wait(40)


class FourierOfFourier100xZoom_misaka_200_1000(ZoomedInFourierSeriesExample100x):
    CONFIG = {
        "run_time": 12,
        "file_name": svg_path + 'misaka_new.svg',
        "max_circle_stroke_width": 0.6,
        "n_vectors": 2400,
        "slow_factor": 0.001,
        "rect_scale_factor": 0.01,
    }

    def run_one_cycle(self):
        self.vector_clock.set_value(0.2)
        self.wait(20)

class FourierOfFourier20xZoom_misaka(ZoomedInFourierSeriesExample100x):
    CONFIG = {
        # "run_time": 5,
        "file_name": svg_path + 'misaka_new.svg',
        "max_circle_stroke_width": 0.6,
        "n_cycles": 1,
        "n_vectors": 2400,
        "slow_factor": 0.002,
        "rect_scale_factor": 0.05,
    }

class FourierOfFourier20xZoom_misaka_60_500(ZoomedInFourierSeriesExample100x):
    CONFIG = {
        # "run_time": 5,
        "file_name": svg_path + 'misaka_new.svg',
        "max_circle_stroke_width": 0.6,
        "n_cycles": 1,
        "n_vectors": 2400,
        "slow_factor": 0.002,
        "rect_scale_factor": 0.05,
    }

class FourierOfFourier5xZoom_misaka_100_250(ZoomedInFourierSeriesExample100x):
    CONFIG = {
        # "run_time": 5,
        "file_name": svg_path + 'misaka_new.svg',
        "max_circle_stroke_width": 0.6,
        "n_cycles": 1,
        "n_vectors": 2400,
        "slow_factor": 0.004,
        "rect_scale_factor": 0.2,
    }





class BreakApartSum(Scene):
    CONFIG = {
        "frequencies" : [0.5, 1.5, 2, 2.5, 5],
        "equilibrium_height" : 2.0,
    }
    def construct(self):
        self.show_initial_sound()
        self.decompose_sound()
        # self.ponder_question()


    def show_initial_sound(self):
        def func(x):
            return self.equilibrium_height + 0.2*np.sum([
                np.cos(2*np.pi*f*x)
                for f in self.frequencies
            ])
        axes = Axes(
            x_min = 0, x_max = 5,
            y_min = -1, y_max = 5,
            x_axis_config = {
                "include_tip" : False,
                "unit_size" : 2.0,
            },
            y_axis_config = {
                "include_tip" : False,
                "unit_size" : 0.5,
            },
        )
        axes.stretch_to_fit_width(FRAME_WIDTH - 2)
        axes.stretch_to_fit_height(3)
        axes.center()
        axes.to_edge(LEFT)
        graph = axes.get_graph(func, num_graph_points = 200)
        graph.set_color(YELLOW)

        v_line = Line(ORIGIN, 4*UP)
        v_line.move_to(axes.coords_to_point(0, 0), DOWN)
        dot = Dot(color = PINK)
        dot.move_to(graph.point_from_proportion(0))

        self.add(axes, graph)
        self.play(
            v_line.move_to, axes.coords_to_point(5, 0), DOWN,
            MoveAlongPath(dot, graph),
            run_time = 8,
            rate_func=linear,
        )
        self.play(*list(map(FadeOut, [dot, v_line])))

        self.set_variables_as_attrs(axes, graph)

    def decompose_sound(self):
        axes, graph = self.axes, self.graph

        pure_graphs = VGroup(*[
            axes.get_graph(
                lambda x : 0.5*np.cos(2*np.pi*freq*x),
                num_graph_points = 100,
            )
            for freq in self.frequencies
        ])
        pure_graphs.set_color_by_gradient(BLUE, RED)
        pure_graphs.arrange(DOWN, buff = MED_LARGE_BUFF)
        h_line = DashedLine(6*LEFT, 6*RIGHT)

        self.play(
            FadeOut(axes),
            graph.to_edge, UP
        )
        pure_graphs.next_to(graph, DOWN, LARGE_BUFF)
        h_line.next_to(graph, DOWN, MED_LARGE_BUFF)
        self.play(ShowCreation(h_line))
        for pure_graph in reversed(pure_graphs):
            self.play(ReplacementTransform(graph.copy(), pure_graph))
        self.wait()

        self.all_graphs = VGroup(graph, h_line, pure_graphs)
        self.pure_graphs = pure_graphs

    def ponder_question(self):
        all_graphs = self.all_graphs
        pure_graphs = self.pure_graphs
        randy = Randolph()
        randy.to_corner(DOWN+LEFT)

        self.play(
            FadeIn(randy),
            all_graphs.scale, 0.75,
            all_graphs.to_corner, UP+RIGHT,
        )
        self.play(randy.change, "pondering", all_graphs)
        self.play(Blink(randy))
        rect = SurroundingRectangle(pure_graphs, color = WHITE)
        self.play(
            ShowCreation(rect),
            LaggedStartMap(
                ApplyFunction, pure_graphs,
                lambda g : (lambda m : m.shift(SMALL_BUFF*UP).set_color(YELLOW), g),
                rate_func = wiggle
            )
        )
        self.play(FadeOut(rect))
        self.play(Blink(randy))
        self.wait()

class Quadrant(VMobject):
    CONFIG = {
        "radius" : 2,
        "stroke_width": 0,
        "fill_opacity" : 1,
        "density" : 50,
        "density_exp" : 2.0,
    }
    def generate_points(self):
        points = [r*RIGHT for r in np.arange(0, self.radius, 1./self.density)]
        points += [
            self.radius*(np.cos(theta)*RIGHT + np.sin(theta)*UP)
            for theta in np.arange(0, TAU/4, 1./(self.radius*self.density))
        ]
        points += [r*UP for r in np.arange(self.radius, 0, -1./self.density)]
        self.set_points_smoothly(points)

class UnmixMixedPaint(Scene):
    CONFIG = {
        "colors" : [BLUE, RED, YELLOW, GREEN],
    }
    def construct(self):
        angles = np.arange(4)*np.pi/2
        quadrants = VGroup(*[
            Quadrant().rotate(angle, about_point = ORIGIN).set_color(color)
            for color, angle in zip(self.colors, angles)
        ])
        quadrants.add(*it.chain(*[
            quadrants.copy().rotate(angle)
            for angle in np.linspace(0, 0.02*TAU, 10)
        ]))
        quadrants.set_fill(opacity = 0.5)

        mud_color = average_color(*self.colors)
        mud_circle = Circle(radius = 2, stroke_width = 0)
        mud_circle.set_fill(mud_color, 1)
        mud_circle.save_state()
        mud_circle.scale(0)

        def update_quadrant(quadrant, alpha):
            points = quadrant.get_anchors()
            dt = 0.03 #Hmm, this has no dependency on frame rate...
            norms = np.apply_along_axis(get_norm, 1, points)

            points[:,0] -= dt*points[:,1]/np.clip(norms, 0.1, np.inf)
            points[:,1] += dt*points[:,0]/np.clip(norms, 0.1, np.inf)

            new_norms = np.apply_along_axis(get_norm, 1, points)
            new_norms = np.clip(new_norms, 0.001, np.inf)
            radius = np.max(norms)
            multiplier = norms/new_norms
            multiplier = multiplier.reshape((len(multiplier), 1))
            multiplier.repeat(points.shape[1], axis = 1)
            points *= multiplier
            quadrant.set_points_smoothly(points)

        self.add(quadrants)
        run_time = 30
        self.play(
            *[
                UpdateFromAlphaFunc(quadrant, update_quadrant)
                for quadrant in quadrants
            ] + [
                ApplyMethod(mud_circle.restore, rate_func=linear)
            ],
            run_time = run_time
        )
