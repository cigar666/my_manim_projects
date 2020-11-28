from manimlib.imports import *

# by @cigar666
class Test_rotate_anim(Scene):

    def construct(self):

        title = Title("Different rotate anim effect", color=BLUE)
        pentagon = RegularPolygon(5, color=BLUE, fill_opacity=1)
        pentagon_2, pentagon_3, pentagon_4 = pentagon.copy(), pentagon.copy(), pentagon.copy()
        mobs = VGroup(pentagon, pentagon_2, pentagon_3, pentagon_4).arrange(direction=RIGHT * 1.2, buff=1)

        time = 5 # animation time
        angle = 240 * DEGREES # rotating angle
        t = ValueTracker(0)

        timer = DecimalNumber(0, color=GREEN).scale(2).next_to(mobs, UP * 1.5, aligned_edge=LEFT)
        timer.add_updater(lambda t_: t_.set_value(t.get_value()))
        show_angle = DecimalNumber(0, color=RED).scale(2).next_to(mobs, UP * 1.5, aligned_edge=RIGHT)
        show_angle.add_updater(lambda s: s.set_value(t.get_value()/5 * angle/DEGREES))

        def rotate_mob(mob):
            mob.rotate(angle/time/self.camera.frame_rate)

        self.add(title, mobs, timer, show_angle)

        pentagon_4.add_updater(rotate_mob)               # method 4
        self.play(pentagon.rotate, angle,                # method 1
                  Rotate(pentagon_2, angle=angle),       # method 2
                  Rotating(pentagon_3, radians=angle),   # method 3
                  t.set_value, time,
                  rate_func=linear, run_time=time)

        pentagon_4.remove_updater(rotate_mob)

        self.wait()
