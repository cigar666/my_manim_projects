from manimlib.imports import *
from my_projects.active_projects.mechanism.basic_component import *

class Jansen_mechanism_test(Scene):

    def construct(self):

        s = 0.05 # scale_factor
        a = 38 * s
        b = 41.5 * s
        c = 39.3 * s
        d = 40.1 * s
        e = 55.8 * s
        f = 39.4 * s
        g = 37.7 * s
        h = 65.7 * s
        i = 49.0 * s
        j = 50.0 * s
        k = 61.9 * s
        l = 7.8 * s
        m = 15.0 * s

        center = UP * 1.6
        dot_1 = Dot(center, color=PINK).set_plot_depth(1)
        dot_2 = Dot(center + l * DOWN + LEFT * a, color=PINK).set_plot_depth(1)
        rod_m = Bar(start=center, angle=-10*DEGREES, length=m, color=ORANGE)
        rod_j = Bar(start=rod_m.get_end(), angle=137.5 * DEGREES, length=j, end_type=[2,2])
        rod_b = Bar(start=dot_2.get_center(), angle=75 * DEGREES, length=b)
        solve_2rods_new(rod_j, rod_b)
        rod_e = Bar(rod_b.get_end(), angle=-155*DEGREES, length=e, end_type=[1,2])
        rod_d = Bar(rod_b.get_start(), angle=160*DEGREES, length=d, end_type=[1,1])
        solve_2rods_new(rod_e, rod_d)
        rod_c = Bar(rod_b.get_start(), angle=-80 * DEGREES, length=c, end_type=[2,2])
        rod_k = Bar(rod_m.get_end(), angle=-140 * DEGREES, length=k)
        solve_2rods_new(rod_c, rod_k)
        rod_f = Bar(rod_d.get_end(), angle=-75 * DEGREES, length=f)
        rod_g = Bar(rod_c.get_end(), angle=150 * DEGREES, length=g)
        solve_2rods_new(rod_f, rod_g)
        rod_h = Bar(rod_f.get_end(), angle=-85 * DEGREES, length=h, end_type=[2,2])
        rod_i = Bar(rod_c.get_end(), angle=-115 * DEGREES, length=i)
        solve_2rods_new(rod_h, rod_i)

        rods = VGroup(rod_m, rod_j, rod_b, rod_e, rod_d, rod_c, rod_k, rod_f, rod_g, rod_h, rod_i)

        w = ValueTracker(0)

        def update_rods(r, dt):
            r.rotate_about_start(w.get_value())
            rod_j.reposition(r.get_end())
            rod_k.reposition(r.get_end())
            solve_2rods_new(rod_j, rod_b)
            rod_e.reposition(rod_j.get_end())
            solve_2rods_new(rod_e, rod_d)
            rod_f.reposition(rod_d.get_end())
            solve_2rods_new(rod_c, rod_k)
            rod_g.reposition(rod_k.get_end())
            solve_2rods_new(rod_f, rod_g)
            rod_h.reposition(rod_f.get_end())
            rod_i.reposition(rod_k.get_end())
            solve_2rods_new(rod_h, rod_i)

        rod_m.add_updater(update_rods)


        self.add(dot_1, dot_2, rods)

        self.wait()
        self.play(w.set_value, 5 * DEGREES, run_time=5)
        self.wait(10)


class Jansen_Leg_Mechanism(VGroup):

    CONFIG = {
        'scale_factor': 1,
        'init_angle': 0,
        'updater_on': True,
        'dot_color': PINK,
        'rod_color': [ORANGE, BLUE],
        'mirror_to_right': False,
    }

    def __init__(self, **kwargs):

        VGroup.__init__(self, **kwargs)


        s = 0.05 * self.scale_factor # scale_factor
        a = 38 * s
        b = 41.5 * s
        c = 39.3 * s
        d = 40.1 * s
        e = 55.8 * s
        f = 39.4 * s
        g = 37.7 * s
        h = 65.7 * s
        i = 49.0 * s
        j = 50.0 * s
        k = 61.9 * s
        l = 7.8 * s
        m = 15.0 * s

        center = UP * 1.6
        if not self.mirror_to_right:
            self.dot_1 = Dot(center, color=self.dot_color)
            self.dot_2 = Dot(center + l * DOWN + LEFT * a, color=self.dot_color)
            self.rod_m = Bar(start=center, angle=-10*DEGREES, length=m, color=self.rod_color[0])
            self.rod_j = Bar(start=self.rod_m.get_end(), angle=137.5 * DEGREES, length=j, end_type=[2,3], color=self.rod_color[1])
            self.rod_b = Bar(start=self.dot_2.get_center(), angle=75 * DEGREES, length=b, end_type=[2,3], color=self.rod_color[1])
            solve_2rods_new(self.rod_j, self.rod_b)
            self.rod_e = Bar(self.rod_b.get_end(), angle=-155*DEGREES, length=e, end_type=[3,3], color=self.rod_color[1])
            self.rod_d = Bar(self.rod_b.get_start(), angle=160*DEGREES, length=d, end_type=[2,3], color=self.rod_color[1])
            solve_2rods_new(self.rod_e, self.rod_d)
            self.rod_c = Bar(self.rod_b.get_start(), angle=-80 * DEGREES, length=c, end_type=[2,3], color=self.rod_color[1])
            self.rod_k = Bar(self.rod_m.get_end(), angle=-140 * DEGREES, length=k, end_type=[2,3], color=self.rod_color[1])
            solve_2rods_new(self.rod_c, self.rod_k)
            self.rod_f = Bar(self.rod_d.get_end(), angle=-75 * DEGREES, length=f, end_type=[3,3], color=self.rod_color[1])
            self.rod_g = Bar(self.rod_c.get_end(), angle=150 * DEGREES, length=g, end_type=[3,3], color=self.rod_color[1])
            solve_2rods_new(self.rod_f, self.rod_g)
            self.rod_h = Bar(self.rod_f.get_end(), angle=-85 * DEGREES, length=h, end_type=[3,3], color=self.rod_color[1])
            self.rod_i = Bar(self.rod_c.get_end(), angle=-115 * DEGREES, length=i, end_type=[3,3], color=self.rod_color[1])
            solve_2rods_new(self.rod_h, self.rod_i)
        else:
            self.dot_1 = Dot(center, color=self.dot_color)
            self.dot_2 = Dot(center + l * DOWN + RIGHT * a, color=self.dot_color)
            self.rod_m = Bar(start=center, angle=-170*DEGREES, length=m, color=self.rod_color[0])
            self.rod_j = Bar(start=self.rod_m.get_end(), angle=(180 - 137.5) * DEGREES, length=j, end_type=[2,3], color=self.rod_color[1])
            self.rod_b = Bar(start=self.dot_2.get_center(), angle=(180 - 75) * DEGREES, length=b, end_type=[2,3], color=self.rod_color[1])
            solve_2rods_new(self.rod_j, self.rod_b)
            self.rod_e = Bar(self.rod_b.get_end(), angle=-(180 - 155)*DEGREES, length=e, end_type=[3,3], color=self.rod_color[1])
            self.rod_d = Bar(self.rod_b.get_start(), angle=(180 - 160)*DEGREES, length=d, end_type=[2,3], color=self.rod_color[1])
            solve_2rods_new(self.rod_e, self.rod_d)
            self.rod_c = Bar(self.rod_b.get_start(), angle=-(180 - 80) * DEGREES, length=c, end_type=[2,3], color=self.rod_color[1])
            self.rod_k = Bar(self.rod_m.get_end(), angle=-(180 - 140) * DEGREES, length=k, end_type=[2,3], color=self.rod_color[1])
            solve_2rods_new(self.rod_c, self.rod_k)
            self.rod_f = Bar(self.rod_d.get_end(), angle=-(180 - 75) * DEGREES, length=f, end_type=[3,3], color=self.rod_color[1])
            self.rod_g = Bar(self.rod_c.get_end(), angle=(180 - 150) * DEGREES, length=g, end_type=[3,3], color=self.rod_color[1])
            solve_2rods_new(self.rod_f, self.rod_g)
            self.rod_h = Bar(self.rod_f.get_end(), angle=-(180 - 85) * DEGREES, length=h, end_type=[3,3], color=self.rod_color[1])
            self.rod_i = Bar(self.rod_c.get_end(), angle=-(180 - 115) * DEGREES, length=i, end_type=[3,3], color=self.rod_color[1])
            solve_2rods_new(self.rod_h, self.rod_i)

        self.dots = VGroup(self.dot_1, self.dot_2)
        self.rods = VGroup(self.rod_m, self.rod_j, self.rod_b, self.rod_e, self.rod_d, self.rod_c,
                           self.rod_k, self.rod_f, self.rod_g, self.rod_h, self.rod_i)
        self.add(self.rods, self.dots)
        self.theta = ValueTracker()

        n_steps = int((self.init_angle - (-10 * DEGREES))/5/DEGREES) if not self.mirror_to_right else int((self.init_angle - (-170 * DEGREES))/5/DEGREES)
        for i in range(n_steps):
            if not self.mirror_to_right:
                self.theta.set_value(-10 * DEGREES + (i+1) * 5 * DEGREES)
            else:
                self.theta.set_value(-170 * DEGREES + (i+1) * 5 * DEGREES)
            # print(self.theta.get_value()/DEGREES)
            self.update_by_theta(self)

        self.theta = ValueTracker(self.init_angle)
        self.update_by_theta(self)

    def update_by_theta(self, jlm):

        jlm.rod_m.reposition_by_angle(jlm.theta.get_value())
        jlm.rod_j.reposition(jlm.rod_m.get_end())
        jlm.rod_k.reposition(jlm.rod_m.get_end())
        solve_2rods_new(jlm.rod_j,jlm.rod_b)
        jlm.rod_e.reposition(jlm.rod_j.get_end())
        solve_2rods_new(jlm.rod_e,jlm.rod_d)
        jlm.rod_f.reposition(jlm.rod_d.get_end())
        solve_2rods_new(jlm.rod_c,jlm.rod_k)
        jlm.rod_g.reposition(jlm.rod_k.get_end())
        solve_2rods_new(jlm.rod_f,jlm.rod_g)
        jlm.rod_h.reposition(jlm.rod_f.get_end())
        jlm.rod_i.reposition(jlm.rod_k.get_end())
        solve_2rods_new(jlm.rod_h,jlm.rod_i)

    def update_start(self):
        self.add_updater(self.update_by_theta)

    def update_rod_m(self, rod_m):
        rod_m.reposition_by_angle(self.theta.get_value())

    def update_4bar_linkage_by_rod_m(self, rods):
        rods[0].reposition(self.rod_m.get_end())
        solve_2rods_new(rods[0], rods[1])
        print(1)


class Test_02(Scene):

    def construct(self):

        jlm_l1 = Jansen_Leg_Mechanism(init_angle=0)
        jlm_r1 = Jansen_Leg_Mechanism(init_angle=0, mirror_to_right=True)

        self.add(jlm_l1, jlm_r1)
        jlm_l1.update_start()
        jlm_r1.update_start()
        # jlm3.update_start()
        self.wait()
        self.play(jlm_l1.theta.set_value, TAU * 5,
                  jlm_r1.theta.set_value, TAU * 5,
                  rate_func=linear, run_time=5)
        self.wait()


class Jansen_walking_anim(Scene):

    def construct(self):

        jlm_l1 = Jansen_Leg_Mechanism(init_angle=0, rod_color=[ORANGE, YELLOW])
        jlm_r1 = Jansen_Leg_Mechanism(init_angle=0, rod_color=[ORANGE, YELLOW], mirror_to_right=True)
        jlm_l2 = Jansen_Leg_Mechanism(init_angle=TAU/3, rod_color=[ORANGE, GREEN])
        jlm_r2 = Jansen_Leg_Mechanism(init_angle=TAU/3, rod_color=[ORANGE, GREEN], mirror_to_right=True)
        jlm_l3 = Jansen_Leg_Mechanism(init_angle=TAU/3 * 2)
        jlm_r3 = Jansen_Leg_Mechanism(init_angle=TAU/3 * 2, mirror_to_right=True)

        body = VGroup(Line(jlm_l1.dot_2.get_center(), jlm_r1.dot_2.get_center(), color=PINK, stroke_width=9),
                      Line(jlm_l1.dot_1.get_center(), jlm_r1.dot_2.get_center()[1] * UP, color=PINK, stroke_width=9), plot_depth=-1)

        jlm_vg = VGroup(body, jlm_l1, jlm_r1, jlm_l2, jlm_r2, jlm_l3, jlm_r3)

        ground_line = Line(LEFT, RIGHT, color=BLUE, stroke_width=6).next_to(jlm_vg, DOWN, buff=0).set_width(FRAME_WIDTH)

        t = ValueTracker(0)
        w = 2.5 * DEGREES

        def update_jlms(vg):

            vg[1].theta.set_value(t.get_value() * w)
            vg[2].theta.set_value(t.get_value() * w)
            vg[3].theta.set_value(t.get_value() * w + TAU/3)
            vg[4].theta.set_value(t.get_value() * w + TAU/3)
            vg[5].theta.set_value(t.get_value() * w + TAU/3 * 2)
            vg[6].theta.set_value(t.get_value() * w + TAU/3 * 2)
            for jlm in vg[1:]:
                jlm.update_by_theta(jlm)

        jlm_vg.add_updater(update_jlms)
        self.add(jlm_vg, ground_line)
        self.wait()
        # self.play(t.set_value, 360 * 4/2.5, rate_func=linear, run_time=5)
        #
        # self.wait()


class Jansen_detail(Scene):

    def construct(self):

        jlm = Jansen_Leg_Mechanism(init_angle=0)

        self.play(FadeIn(jlm.dot_1), run_time=0.5)
        self.play(FadeIn(jlm.rod_m), run_time=0.7)
        self.wait(0.2)

        jlm.rod_m.add_updater(jlm.update_rod_m)
        self.play(jlm.theta.set_value, 1.25 * TAU, rate_func=there_and_back, run_time=2.)
        self.wait(0.1)

        self.play(FadeIn(jlm.dot_2), run_time=0.5)
        self.play(FadeIn(jlm.rod_b), FadeIn(jlm.rod_j), run_time=0.6)

        def update_4bar_linkage_01(rod):
            rod.reposition(jlm.rod_m.get_end())
            solve_2rods_new(rod, jlm.rod_b)

        jlm.rod_j.add_updater(update_4bar_linkage_01)
        jlm.theta.set_value(0)
        self.play(jlm.theta.set_value, 1.25 * TAU, rate_func=there_and_back, run_time=3.6)
        self.wait(0.1)
        self.play(FadeIn(jlm.rod_e), FadeIn(jlm.rod_d), run_time=0.6)

        def update_rod_ed(re):
            re.reposition(jlm.rod_j.get_end())
            solve_2rods_new(re,jlm.rod_d)

        jlm.rod_e.add_updater(update_rod_ed)
        self.play(jlm.theta.set_value, 1 * TAU, rate_func=there_and_back, run_time=3.2)
        self.wait(0.1)

        self.play(FadeIn(jlm.rod_c), FadeIn(jlm.rod_k), run_time=0.6)

        def update_4bar_linkage_02(rod):
            rod.reposition(jlm.rod_m.get_end())
            solve_2rods_new(rod, jlm.rod_c)

        jlm.rod_k.add_updater(update_4bar_linkage_02)
        self.play(jlm.theta.set_value, 1 * TAU, rate_func=there_and_back, run_time=3.6)
        self.wait(0.1)

        self.play(FadeIn(jlm.rod_f), FadeIn(jlm.rod_g), run_time=0.6)

        def update_4bar_linkage_03(rod):
            rod.reposition(jlm.rod_d.get_end())
            jlm.rod_g.reposition(jlm.rod_c.get_end())
            solve_2rods_new(rod, jlm.rod_g)

        jlm.rod_f.add_updater(update_4bar_linkage_03)
        self.play(jlm.theta.set_value, 1 * TAU, rate_func=there_and_back, run_time=3.6)
        self.wait(0.1)

        self.play(FadeIn(jlm.rod_h), FadeIn(jlm.rod_i), run_time=0.5)

        def update_rod_hi(rod):
            rod.reposition(jlm.rod_f.get_end())
            jlm.rod_i.reposition(jlm.rod_c.get_end())
            solve_2rods_new(rod, jlm.rod_i)

        jlm.rod_h.add_updater(update_rod_hi)
        self.play(jlm.theta.set_value, 1. * TAU, rate_func=there_and_back, run_time=4)
        self.wait(0.1)
        self.play(jlm.theta.set_value, 10 * TAU, rate_func=linear, run_time=15)

        self.wait(2)

        # self.play(FadeIn(jlm.dot_2))
        # self.wait(0.5)
        #
        # self.play(FadeIn(jlm.rod_j), FadeIn(jlm.rod_b))
        # self.wait(0.5)
        # self.play(jlm.theta.set_value, 2 * TAU, run_time=2.5)
        # self.play(jlm.theta.set_value, 1 * TAU, run_time=1)
        # self.wait()


