from manimlib.imports import *

class Draw_touching_circles(ZoomedScene):

    CONFIG = {
        'camera_config': {
            'background_color': WHITE,
            'cairo_line_width_multiple': 0.008,
        },
        "zoomed_display_height": 7,
        "zoomed_display_width": 7,
        "zoomed_display_center": RIGHT * 6,
        # "zoomed_display_corner_buff": DEFAULT_MOBJECT_TO_EDGE_BUFFER,
        "zoomed_camera_config": {
            "default_frame_stroke_width": 3,
            "default_frame_stroke_color": YELLOW,
            "background_opacity": 0.9,
            'background_color': WHITE,
            'frame_center': DOWN * 1.5 + LEFT * 0.75,
            'cairo_line_width_multiple': 0.016,
        },
        "zoomed_camera_frame_starting_position": DOWN * 1.5 + LEFT * 0.75,
        "zoom_factor": 0.24,
        "zoom_activated": False,
    }

    def construct(self):

        d = 1.5
        r = d/2
        grid = NumberPlane().set_color(GRAY).scale(d).set_opacity(0.4)
        line = Line(LEFT * 12, RIGHT * 12, color=BLACK, stroke_width=4)
        circle = Circle(radius=r, color=BLACK, stroke_width=3.2).shift((DOWN + LEFT * 0.5) * d)
        dot_0 = Dot(ORIGIN, fill_color=RED, stroke_width=2.5, stroke_color=BLACK, plot_depth=2).scale(0.6) # driving point
        dot_fix = Dot(DOWN * d, fill_color=PINK, stroke_width=2.5, stroke_color=BLACK, plot_depth=2).scale(0.6) # fixed point
        dot_1 = Dot() # driven point
        rect = Polygon(UR, UL, DL, DR)
        rect_group = VGroup(rect, dot_0, dot_fix, dot_1)

        def update_rect_group(rg):
            rect, dot_0, dot_fix, dot_1 = rg[0], rg[1], rg[2], rg[3]
            p_0, p_f = dot_0.get_center(), dot_fix.get_center()
            p_1 = complex_to_R3(d ** 2 / abs(R3_to_complex(p_0 - p_f)) * np.exp((np.angle(R3_to_complex(p_0 - p_f)) + PI/2) * 1j)) + p_f
            dot_1.become(Dot(p_1, fill_color=YELLOW, stroke_width=2.5, stroke_color=BLACK, plot_depth=2).scale(0.6))
            rect.become(Polygon(p_f, p_0, p_0 + p_1 - p_f, p_1, fill_color=BLUE, fill_opacity=0.4, stroke_width=4, stroke_color=BLACK, plot_depth=0))
        rect_group.add_updater(update_rect_group)

        path_circles = VGroup(Circle(radius=r).move_to(UL * r).rotate(-PI/2))
        circle_num = 120
        pos = UR * r
        velocity = RIGHT * d
        max_layer = 4
        i = 1
        while i < circle_num:
            if pos[1] < max_layer * d:
                path_circles.add(Circle(radius=r).move_to(pos).rotate(-PI/2))
                pos += velocity
                i += 1
            else:
                pos += velocity
            if pos[1] < d:
                if velocity[1] == 0:
                    if pos[0] > 0:
                        velocity = UL * d
                    else:
                        velocity = UR * d
                else:
                    velocity *= RIGHT # to make velocity[1]=0
            else:
                if abs(pos[0]) < d:
                    velocity += DOWN * d
        print(len(path_circles))
        circle_above, circle_inner = VGroup(), VGroup()
        self.camera.set_frame_center(RIGHT * 3)
        self.add(circle_above, circle_inner)

        def move_alone_circle(c, t0=1, t1=2):

            self.play(dot_0.move_to, c.get_start(), run_time=t0 * 0.9)
            self.wait(t0 * 0.1)
            c0 = TracedPath(dot_0.get_center, strock_color=BLACK, stroke_width=3, min_distance_to_new_point=0.01, plot_depth=0).add_updater(lambda c: c.set_color(BLACK))
            c1 = TracedPath(dot_1.get_center, strock_color=BLACK, stroke_width=3, min_distance_to_new_point=0.01 * (i + 1) ** (-1) + 1e-4, plot_depth=0).add_updater(lambda c: c.set_color(BLACK))
            circle_above.add(c0), circle_inner.add(c1)

            self.play(MoveAlongPath(dot_0, c), run_time=t1)
            c0.stop_trace(), c1.stop_trace()

        self.add(grid, circle, line, rect_group)
        self.wait(0.6)
        self.play(dot_0.shift, 3 * RIGHT, run_time=1.6)
        self.wait(0.6)

        self.play(dot_0.move_to, LEFT * 3, run_time=2)
        self.wait(0.8)
        self.play(dot_0.move_to, UP * 2 + LEFT, run_time=1.2)

        for i in range(12+1):
            move_alone_circle(path_circles[i], t0=0.6, t1=2)
            self.wait(0.6)
        self.activate_zooming(animate=True)
        self.zoomed_display.set_plot_depth(3)
        self.play(ShowCreation(SurroundingRectangle(self.zoomed_display).set_width(7.05)))
        for i in range(13, circle_num):
            move_alone_circle(path_circles[i], t0=0.2, t1=1.8)
            self.wait(0.2)
        self.wait(1)
        self.play(FadeOut(rect_group))
        self.wait()
        circle_n = Circle(radius=r/5, color=BLACK, stroke_width=3.2).shift((DOWN + LEFT * 0.5/5) * d)
        self.play(ShowCreation(circle_n), run_time=1.2)
        self.wait(2.5)

####################################################################
# some funcs about inversion from @Solara570
# https://github.com/Solara570/demo-solara/blob/master/articles/inversion.py from line 50 to 61
def complex_inversion(z, z0, r):
    return z0 + np.conjugate(r**2 / (z-z0))

def R3_inversion(point, inv_center, radius):
    z = R3_to_complex(point)
    z0 = R3_to_complex(inv_center)
    w = complex_inversion(z, z0, radius)
    return complex_to_R3(w)

def inversion(point, inv_center, radius):
    # Just a rename
    return R3_inversion(point, inv_center, radius)

####################################################################

class Transform_by_Inversion(MovingCameraScene):

    CONFIG = {
        'camera_config': {
            'background_color': WHITE,
        },
    }

    def construct(self):

        d = 1.45
        r = d/2
        grid = NumberPlane().set_color(GRAY).scale(d).set_opacity(0.4)
        line_0 = Line(LEFT * 12, RIGHT * 12, color=BLACK, stroke_width=4)
        line_1 = line_0.copy().shift(UP * d * 3)
        c0 = Circle(radius=r, color=BLACK, stroke_width=3.) # .shift(LEFT * r * 0.25)
        circle = Circle(radius=d, color=PINK, stroke_width=5).shift(DOWN * d)
        circle_0 = Circle(radius=r, color=BLACK, stroke_width=3).shift(DOWN * r).rotate(PI/2)
        circle_1 = Circle(radius=r/4, color=BLACK, stroke_width=3).shift(DOWN * d + UP * r/4).rotate(-PI/2).flip()

        def get_circles(m, n, circle):
            return VGroup(*[VGroup(*[circle.copy().shift(UP * (i + 0.5) * d + RIGHT * (-(n-1)/2 + j) * d) for j in range(n)]) for i in range(m)])

        def get_inversed_circle(circle, z0, r):

            center_old, r_old = circle.get_center(), circle.get_width()/2
            angle = np.angle(R3_to_complex(center_old - z0))
            p1, p2 = center_old + complex_to_R3(r_old * np.exp(angle * 1j)), center_old - complex_to_R3(r_old * np.exp(angle * 1j))
            center_new = (inversion(p1, z0, r) + inversion(p2, z0, r)) / 2
            r_new = get_norm(inversion(p1, z0, r) - inversion(p2, z0, r)) / 2

            # return Circle(radius=r_new, **kwargs).move_to(center_new)
            return circle.copy().set_width(2 * r_new).move_to(center_new)

        def get_inversed_circles(circles, z0, r):
            inv_circles = VGroup()
            for circles_i in circles:
                inv_circles_i = VGroup()
                for circle_ij in circles_i:
                    inv_circles_i.add(get_inversed_circle(circle_ij, z0, r))
                inv_circles.add(inv_circles_i)
            return inv_circles

        m, n = 3, 80
        circles = get_circles(m, n, c0)
        inv_circles = get_inversed_circles(circles, DOWN * d, d)

        self.camera.set_frame_center(UP * 1.)
        text = Text('反演圆', font='思源黑体 Bold', color=PINK)
        center = Dot(circle.get_center(), color=PINK)
        self.play(Write(text), run_time=1.5)
        self.wait(0.5)

        self.play(ReplacementTransform(text, circle), run_time=1.2)
        self.play(FadeInFromLarge(center))
        self.wait(0.5)
        self.play(ShowCreation(line_0), run_time=2)
        self.wait(0.6)
        self.play(TransformFromCopy(line_0, circle_0), line_0.set_stroke, {'opacity': 0.5}, run_time=2)
        self.wait(0.8)

        # self.play(ShowCreation(circles[0]), run_time=3)
        # for i in range(n):
        #     self.wait(0.1)
        #     self.play(TransformFromCopy(circles[0][i], inv_circles[0][i]), circles[0][i].set_stroke, {'opacity': 0.5}, run_time=0.4)

        for i in range(m):
            self.play(ShowCreation(circles[i]), run_time=4)
            self.wait(0.5)
            self.play(TransformFromCopy(circles[i], inv_circles[i]), circles[i].set_stroke, {'opacity': 0.5}, run_time=2)


        self.play(ShowCreation(line_1), run_time=2)
        self.wait(0.6)
        self.play(TransformFromCopy(line_1, circle_1), line_1.set_stroke, {'opacity': 0.5}, run_time=2)
        self.wait(1.5)
        self.play(FadeOut(line_0), FadeOut(line_1), FadeOut(circles), FadeOut(circle), FadeOut(center), run_time=1.2)
        self.wait(0.5)
        scale_group = VGroup(circle_0, inv_circles, circle_1)
        self.play(scale_group.scale, 4.8, {'about_point': DOWN * d + UP * 0.26}, scale_group.move_to, UP, run_time=4)
        self.wait(4)



