from manimlib.imports import *

class Test_MoveAlongPath(Scene):

    def construct(self):

        dot = Dot(color=GREEN).set_height(0.25)
        curve = ParametricFunction(lambda t: np.sin(t) * UP + t * RIGHT, t_min=0, t_max=TAU * 2, color=BLUE).scale(0.8)
        curve.to_corner(UP * 1 + LEFT * 1, buff=1)

        self.play(ShowCreation(curve))
        self.play(FadeInFromLarge(dot))
        self.wait()

        # 将点移动到curve的25%处
        self.play(dot.move_to, curve.point_from_proportion(0.25), run_time=2)
        self.wait()
        # 从0.25处移动到0.75处
        self.play(MoveAlongPath(dot, curve), rate_func=lambda t: 0.25 + 0.5 * t, run_time=4)

        # 使用updater，用一个ValueTracker对象来控制移动
        curve_2 = curve.copy().shift(DOWN * 3)
        dot_2 = dot.copy().set_color(PINK)
        self.play(ShowCreation(curve_2))

        t = ValueTracker(0)
        dot_2.add_updater(lambda d: d.move_to(curve_2.point_from_proportion(t.get_value())))

        self.play((FadeInFromLarge(dot_2)))

        # 将dot_2移动到curve_2的25%处
        self.play(t.set_value, 0.25, run_time=2)
        self.wait()
        # 从curve_2的0.25处移动到0.75处
        self.play(t.set_value, 0.75, run_time=4)
        self.wait()

        # 反复横跳
        for i in range(3): self.play(t.set_value, 0.25, run_time=1.5, rate_func=there_and_back)
        self.wait()

        # 让曲线动起来，并让点在上面移动
        phi = ValueTracker(0)
        curve_2.add_updater(lambda c, dt: [c.become(ParametricFunction(lambda t_: np.sin(t_+phi.get_value()) * UP + t_ * RIGHT,
                                                                  t_min=0, t_max=TAU * 2, color=BLUE).scale(0.8)
                                               .to_corner(UP * 1 + LEFT * 1, buff=1).shift(DOWN * 3)), phi.increment_value(DEGREES * 2)])
        self.wait(3)
        self.play(t.set_value, 0.25, rate_func=there_and_back_with_pause, run_time=4)

        self.wait(4)

