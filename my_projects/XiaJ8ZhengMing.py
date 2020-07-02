from manimlib.imports import *
from my_manim_projects.my_utils.my_text import *

class OneIsTheLargestPositiveIneger(Text4animScene):

    def construct(self):

        t2c = {'1': BLUE, 'a': ORANGE, '>': YELLOW, '×': YELLOW}
        text_01 = Text('证明：1 是最大的正整数', font='思源黑体 Bold').shift(UP * 1.5).set_height(0.8)
        text_01.set_color_by_t2c(t2c)
        text4anim_01 = Text4anim(text_01, shift_vect=DOWN * 1.5, rate_func=smooth, change_opacity=True, init_opacity=0)
        self.add(text4anim_01)
        self.play(text4anim_01.anim_controller.set_value, 1, run_time=2)
        text4anim_01.change_opacity=False
        text4anim_01.shift_(DOWN * 1.5), text4anim_01.anim_controller.set_value(0)
        text4anim_01.shift_vect = text_01.copy().to_corner(UP * 1.5 + LEFT * 1.5).get_center() - text_01.get_center() + DOWN * 1.5
        self.wait(0.6)
        self.play(ShowCreationThenDestruction(SurroundingRectangle(text4anim_01, color=ORANGE).scale([1.08, 1.5, 1])), run_time=1.2)
        self.wait(0.5)
        self.play(text4anim_01.anim_controller.set_value, 1, run_time=2.)
        self.wait(0.4)
        text4anim_01.clear_updaters()
        text_11 = Text('假设最大正整数不是 1，', font='思源黑体 Bold').set_height(0.6).next_to(text4anim_01, DOWN * 2.1).to_corner(LEFT * 2.4)
        text_12 = Text('而是 a，', font='思源黑体 Bold').set_height(0.6).next_to(text_11, RIGHT * 1.6)
        text_13 = Text('则有 a > 1', font='思源黑体 Bold').set_height(0.6).next_to(text_12, RIGHT * 1.6)

        text_11.set_color_by_t2c(t2c), text_12.set_color_by_t2c(t2c), text_13.set_color_by_t2c(t2c)

        t4a_11 = self.ShiftInOneByOne_new(text_11, wait_time=0.1)
        t4a_12 = self.ShiftInOneByOne_new(text_12, run_speed=0.42, wait_time=0.2)
        t4a_13 = self.ShiftInOneByOne_new(text_13, run_speed=0.42, wait_time=0.8)


        text_21 = Text('因为 a > 1，', font='思源黑体 Bold').set_height(0.6).next_to(text_11, DOWN * 1.6).to_corner(LEFT * 2.45)
        text_22 = Text('所以 a × a > a', font='思源黑体 Bold').set_height(0.6).next_to(text_21, RIGHT * 1.5)

        text_21.set_color_by_t2c(t2c), text_22.set_color_by_t2c(t2c)

        t4a_21 = self.ShiftInOneByOne_new(text_21, run_speed=0.3, wait_time=0.2)
        t4a_22 = self.ShiftInOneByOne_new(text_22, run_speed=0.36, wait_time=0.8)

        text_31 = Text('但 a × a 为正整数且大于a，', font='思源黑体 Bold').set_height(0.6).next_to(text_21, DOWN * 1.6).to_corner(LEFT * 2.4)
        text_32 = Text('这与假设矛盾', font='思源黑体 Bold').set_height(0.6).next_to(text_31, RIGHT * 1.5)

        text_31.set_color_by_t2c(t2c), text_32.set_color_by_t2c(t2c)
        t4a_31 = self.ShiftInOneByOne_new(text_31, wait_time=0.3)
        t4a_32 = self.ShiftInOneByOne_new(text_32, run_speed=0.35, wait_time=0.8)

        text_41 = Text('故反证假设不成立，', font='思源黑体 Bold').set_height(0.6).next_to(text_31, DOWN * 1.6).to_corner(LEFT * 2.4)
        text_42 = Text('因而原命题成立', font='思源黑体 Bold').set_height(0.6).next_to(text_41, RIGHT * 1.5)
        text_41.set_color_by_t2c(t2c), text_42.set_color_by_t2c(t2c)
        text_51 = Text('所以：', font='思源黑体 Bold').set_height(0.6).next_to(text_41, DOWN * 1.6).to_corner(LEFT * 2.4)
        text_52 = Text('1 是最大的正整数', font='思源黑体 Bold').set_height(0.6).next_to(text_51, RIGHT * 1.5)

        text_51.set_color_by_t2c(t2c), text_52.set_color_by_t2c(t2c)

        t4a_41 = self.ShiftInOneByOne_new(text_41, run_speed=0.26, wait_time=0.15)
        t4a_42 = self.ShiftInOneByOne_new(text_42, run_speed=0.28, wait_time=0.9)

        t4a_51 = self.ShiftInOneByOne_new(text_51, run_speed=0.48, wait_time=0.2)
        t4a_52 = self.ShiftInOneByOne_new(text_52, run_speed=0.3, wait_time=1.)

        proof = VGroup(text4anim_01, t4a_11, t4a_12, t4a_13, t4a_21, t4a_22, t4a_31, t4a_32, t4a_41, t4a_42, t4a_51, t4a_52)

        self.play(proof.scale, 0.72, {'about_point': UP * 2.4 + LEFT * 4.75}, run_time=1.2)
        self.wait(0.5)
        surround_rect = SurroundingRectangle(proof).scale([1.08, 1.11, 1]).set_stroke(ORANGE, 7.5)
        self.play(ShowCreation(surround_rect), run_time=1.2)
        proof.add(surround_rect)

        text_6 = Text('问题出在哪儿呢？', font='思源黑体 Bold').set_height(0.56).next_to(surround_rect, DOWN * 1.5, aligned_edge=LEFT)
        t4a_6 = self.ShiftInOneByOne_new(text_6, shift_vect=DOWN * 1., run_speed=0.32, wait_time=0.1)
        self.play(WiggleOutThenIn(t4a_6))
        text_7 = Text('问题出在这儿：', font='思源黑体 Bold').set_height(0.56).next_to(surround_rect, DOWN * 1.5, aligned_edge=LEFT)

        text_1 = VGroup(t4a_11, t4a_12, t4a_13)
        rect = SurroundingRectangle(text_1).set_stroke(BLUE, 5)
        text_1.add(rect)
        self.wait(0.1)
        self.Countdown_anim(time=5)
        self.wait(0.1)
        self.play(ReplacementTransform(t4a_6, text_7), ShowCreation(rect), run_time=1.2)
        text_72 = text_1.copy().next_to(text_7, RIGHT * 1.5)
        self.wait(0.2)
        self.play(TransformFromCopy(text_1, text_72), run_time=1.4)
        self.wait(0.8)
        text_8 = Text('最大正整数不存在，因此无法这样假设！', font='思源黑体 Bold').set_color(BLUE).set_height(0.56).next_to(text_7, DOWN * 1.5, aligned_edge=LEFT)
        t4a_8 = self.ShiftInOneByOne_new(text_8, wait_time=0.)

        self.wait(4)

class OnePlusOne(Scene):

    def construct(self):

        pass

class FourEqFive(Text4animScene):

    def construct(self):

        t2c = {'2': BLUE, '4': BLUE, '5': BLUE, 'a': ORANGE, '=': YELLOW, '-': YELLOW}
        text_0 = Text('证明：4 等于 5', font='思源黑体 Bold').set_height(0.85)
        text_0.set_color_by_t2c(t2c)
        t4a_0 = self.ShiftInOneByOne_new(text_0, shift_vect = DOWN * 1.5, stop_updater=False)
        t4a_0.change_opacity=False
        t4a_0.shift_(DOWN * 1.5), t4a_0.anim_controller.set_value(0)
        t4a_0.shift_vect = text_0.copy().to_corner(UP * 1.5 + LEFT * 1.5).get_center() - text_0.get_center() + DOWN * 1.5
        self.wait(0.6)
        self.play(ShowCreationThenDestruction(SurroundingRectangle(t4a_0, color=ORANGE).scale([1.1, 1.5, 1])), run_time=1.2)
        self.wait(0.4)
        self.play(t4a_0.anim_controller.set_value, 1, run_time=2.1)
        self.wait(0.6)

        mytext_1 = MyText('-', '20', '=', '-', '20', default_font='思源黑体 Bold')

        replace_dict = {'-': '-', '20': '20', '=': '=', '^2': '2', '\\times': '×', '+': '+'}
        text_1 = mytext_1.get_new_font_texs(replace_dict).set_height(0.6).next_to(t4a_0, DOWN * 2).to_corner(LEFT * 2.4)
        self.add(text_1)

        self.wait(2)





