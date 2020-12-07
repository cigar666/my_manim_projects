from manimlib.constants import *
from manimlib.mobject.types.vectorized_mobject import VGroup
from manimlib.mobject.svg.tex_mobject import TexMobject
from manimlib.mobject.svg.text_mobject import Text
from manimlib.imports import *


class MyText(TexMobject):

    CONFIG = {
        'default_font': 'Consolas',
        'tex_scale_factor': 1,
    }

    def __init__(self, *tex_strings, **kwargs):
        self.tex_list = tex_strings
        TexMobject.__init__(self, *tex_strings, **kwargs)
        self.new_font_texs = VGroup()

    def reset_tex_with_font(self):
        self.new_font_texs = VGroup()

    def get_color_by_tex(self, tex, **kwargs):
        parts = self.get_parts_by_tex(tex, **kwargs)
        colors = []
        for part in parts:
            colors.append(part.get_color())
        return colors[0]

    def get_new_font_texs(self, replace_dict):
        for i in range(len(self.tex_strings)):
            tex = self.tex_strings[i]
            color=self.get_color_by_tex(tex)
            if tex in replace_dict:
                tex = replace_dict[tex]
            tex_new = Text(tex, font=self.default_font, color=color)
            tex_new.set_height(self[i].get_height())
            # if tex == '-' or tex == '=':
            #     tex_new.set_width(self[i].get_width(), stretch=True)
            if tex == '-':
                tex_new.set_width(self[i].get_width(), stretch=True).scale([0.8, 2.4, 1])
            elif tex == '+':
                tex_new.set_width(self[i].get_width(), stretch=True).scale(0.8)
            elif tex == '×':
                tex_new.set_width(self[i].get_width(), stretch=True).scale(0.9)
            elif tex == '=':
                tex_new.set_width(self[i].get_width(), stretch=True).scale([0.9, 1.35, 1])

            tex_new.scale(self.tex_scale_factor)
            tex_new.move_to(self[i])
            if tex == '-':
                tex_new.shift(UP * 0.5 * tex_new.get_height())
            elif tex == '=':
                tex_new.shift(UP * 0.15 * tex_new.get_height())
            self.new_font_texs.add(tex_new)
        return self.new_font_texs

# class PStyle_Text(VGroup):
#
#     CONFIG = {
#         'size': 1,
#         'colors': [BLACK, WHITE, ORANGE],
#         'font': '思源黑体 Bold',
#     }
#
#     def __init__(self, tex_1, tex_2, **kwargs):
#
#         VGroup.__init__(self, **kwargs)
#         self.text_1 = Text(tex_1, font=self.font, color=self.colors[1], plot_depth=0.2, size=self.size * 0.64)
#         self.text_2 = Text(tex_2, font=self.font, color=self.colors[0], plot_depth=0.2, size=self.size * 0.56)
#         # self.text_2.shift(RIGHT * (self.size * 0.3 + self.text_1.get_width()/2 + self.text_2.get_width()/2))
#         self.text_2.next_to(self.text_1, RIGHT * self.size * 0.32, buff=1)
#         self.bg_2 = SurroundingRectangle(self.text_2, stroke_width=0, fill_color=self.colors[2], fill_opacity=1, plot_depth=0.1).scale([1.02, 1.15, 1]).round_corners(self.size * 0.1)
#         self.bg_all = SurroundingRectangle(VGroup(self.text_1, self.text_1, self.bg_2), stroke_width=0, fill_color=self.colors[0], fill_opacity=1, plot_depth=0).scale(1.15)
#         self.add(self.bg_all, self.text_1, VGroup(self.bg_2, self.text_2))

# def flat(nestedlist):
#     outcome = [nestedlist[i][j] for i in range(len(nestedlist)) for j in range(len(nestedlist[i]))]
#     return outcome
#
# class Test01(Scene):
#
#     def construct(self):
#
#         t = TexMobject('12', '3', '456').to_edge(UP)
#         t_sub = VGroup(*flat(t)).to_edge(UP * 3)
#         for tex in t:
#             self.play(Write(tex))
#         self.wait()
#         for tex in t_sub:
#             self.play(Write(tex))
#         self.wait()

class Text4anim(VGroup):

    CONFIG = {
        'rate_func': there_and_back,
        'proportion': 0.4,
        'shift_vect': UP,
        'scale_factor': 1,
        # 'rotate_angle': 0,
        'change_opacity': False,
        'init_opacity': 1,
        'reverse_order': False,
    }

    def __init__(self, texmob, **kwargs):

        self.texmob = texmob
        self.anim_controller = ValueTracker(0.)
        VGroup.__init__(self, *[self.texmob[i][j] for i in range(len(self.texmob)) for j in range(len(self.texmob[i]))], **kwargs)
        self.submob_pos = [mob.get_center() for mob in self]
        self.submob_size = [mob.get_height() for mob in self]
        if self.change_opacity:
            self.submob_opacity = [self.init_opacity for mob in self]
        else:
            self.submob_opacity = [1 for mob in self]
        # self.get_new_ratefunc()
        self.activate_anim()

    def shift_(self, *vectors):
        self.shift(*vectors)
        for pos in self.submob_pos:
            pos += reduce(op.add, vectors)

    def anim_updater(self, texmob, dt):
        n = len(texmob)
        for i in range(n):
            t = i/n
            t_i = self.rate_func((self.anim_controller.get_value() * (1.02 + self.proportion) - t)/self.proportion)

            if not self.reverse_order:
                texmob[i].move_to(self.submob_pos[i] + self.shift_vect * t_i)\
                    .set_height(self.submob_size[i] * (1 + (self.scale_factor - 1) * t_i))
                if self.change_opacity:
                    opacity_i = self.submob_opacity[i] + t_i
                    texmob[i].set_opacity(opacity_i if opacity_i < 1 else 1)
            else:
                texmob[n-1-i].move_to(self.submob_pos[n-1-i] + self.shift_vect * t_i)\
                    .set_height(self.submob_size[n-1-i] * (1 + (self.scale_factor - 1) * t_i))
                if self.change_opacity:
                    opacity_i = self.submob_opacity[n-1-i] + t_i
                    texmob[n-1-i].set_opacity(opacity_i if opacity_i < 1 else 1)

    def activate_anim(self):
        self.add_updater(self.anim_updater)

class Test_anim(Scene):

    def construct(self):

        # tex_mob = Text('xgnb xgnb xgnb xgnb xgnb xgnb', font='庞门正道标题体').set_height(0.64)
        tex_mob = TexMobject('\\sum i^3', '=', '1^3', '+', '2^3', '+', '3^3', '+', '4^3', '+', '\\cdots', '+', 'n^3').set_height(0.9)

        tex_anim_mob = Text4anim(tex_mob, proportion=0.6)

        self.add(tex_anim_mob)

        self.wait()
        self.play(tex_anim_mob.anim_controller.set_value, 1, rate_func=there_and_back, run_time=5.6)
        self.wait()
        tex_anim_mob.rate_func = smooth
        self.play(tex_anim_mob.anim_controller.set_value, 1, rate_func=smooth, run_time=2.5)
        self.wait()

        tex_anim_mob.proportion = 0.45
        tex_anim_mob.anim_controller.set_value(0)
        tex_anim_mob.shift_(UP)

        tex_anim_mob.shift_vect = DOWN
        self.play(tex_anim_mob.anim_controller.set_value, 1, rate_func=smooth, run_time=2.5)
        self.wait()

        tex_anim_mob.anim_controller.set_value(0)
        tex_anim_mob.shift_(DOWN)

        tex_anim_mob.rate_func = there_and_back
        tex_anim_mob.shift_vect = ORIGIN
        tex_anim_mob.scale_factor = 1.6
        self.play(tex_anim_mob.anim_controller.set_value, 1, rate_func=smooth, run_time=2.5)
        self.wait()

        tex_anim_mob.anim_controller.set_value(0)
        tex_anim_mob.proportion = 0.75
        tex_anim_mob.rate_func = there_and_back
        tex_anim_mob.shift_vect = UP * 1.6
        tex_anim_mob.scale_factor = 2.4
        self.play(tex_anim_mob.anim_controller.set_value, 1, rate_func=smooth, run_time=2.75)

        self.wait(2)

class Text4animScene(Scene):

    def ShiftInOneByOne(self, text, shift_vect=LEFT * 1.5, run_time=2, wait_time=1, stop_updater=True):
        text.shift(-shift_vect)
        t4a = Text4anim(text, shift_vect=shift_vect, rate_func=smooth, proportion=0.32, change_opacity=True, init_opacity=0)
        self.add(t4a)
        self.play(t4a.anim_controller.set_value, 1, run_time=run_time)
        if stop_updater:
            t4a.suspend_updating(t4a.anim_updater)
        self.wait(wait_time)
        return t4a

    def ShiftInOneByOne_new(self, text, shift_vect=LEFT * 1.5, run_speed=0.24, wait_time=1, rate_func=smooth, stop_updater=True):
        text.shift(-shift_vect)
        t4a = Text4anim(text, shift_vect=shift_vect, rate_func=smooth, proportion=0.45, change_opacity=True, init_opacity=0)
        self.add(t4a)
        self.play(t4a.anim_controller.set_value, 1, run_time=run_speed * len(t4a) + 0.05, rate_func=rate_func)
        if stop_updater:
            # t4a.suspend_updating(t4a.anim_updater)
            t4a.clear_updaters()
        self.wait(wait_time)
        return t4a

    def Countdown_anim(self, time=5):

        num = VGroup(*[Text(str(i), font='思源黑体 Bold', color=GREEN).set_height(1) for i in range(time, 0, -1)]).to_corner(RIGHT * 1.2 + UP * 1.2, buff=1)
        circle = Circle(radius=0.9).move_to(num).set_stroke(GREEN, 12)
        for i in range(time):
            self.add(num[i])
            self.play(WiggleOutThenIn(num[i]), ShowCreationThenDestruction(circle), run_time=1)
            self.remove(num[i])

class MyTitle(Text):

    CONFIG = {
        "scale_factor": 1,
        "include_underline": True,
        "underline_width": FRAME_WIDTH - 2,
        # This will override underline_width
        "match_underline_width_to_text": False,
        "underline_buff": MED_SMALL_BUFF,
    }

    def __init__(self, *text, **kwargs):
        Text.__init__(self, *text, **kwargs)
        self.scale(self.scale_factor)
        self.to_edge(UP)
        if self.include_underline:
            underline = Line(LEFT, RIGHT)
            underline.next_to(self, DOWN, buff=self.underline_buff)
            if self.match_underline_width_to_text:
                underline.match_width(self)
            else:
                underline.set_width(self.underline_width)
            self.add(underline)
            self.underline = underline
