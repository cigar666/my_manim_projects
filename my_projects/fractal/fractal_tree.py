from manimlib.imports import *

class BaseTree(VGroup):

    CONFIG = {
        'base_branch': (DOWN * 3, DOWN * 1),
        'derived_branch': [(DOWN, LEFT), (DOWN, RIGHT)],
        'layer_num': 5,
    }

    def __init__(self, mob=None, change_stroke=True, **kwargs):
        VGroup.__init__(self, **kwargs)
        self.origin_mob = mob if mob!=None else Line(self.base_branch[0], self.base_branch[1], stroke_width=20)
        self.create_tree(change_stroke=change_stroke)

    def create_tree(self, change_stroke=True):
        old_points = self.base_branch
        self.add(self.origin_mob.copy())
        for i in range(self.layer_num):
            layer_i = VGroup()
            for new_points in self.derived_branch:
                layer_i.add(self.generate_new_branch(self[-1], old_points, new_points))
            if change_stroke:
                layer_i.set_stroke(width=self.origin_mob.get_stroke_width() * 1.4 ** (-i))
            self.add(layer_i)
        return self

    def generate_new_branch(self, mob, old_points, new_points):
        old_vect, new_vect = old_points[1] - old_points[0], new_points[1] - new_points[0]

        old_angle, new_angle = np.angle(complex(*old_vect[:2])), np.angle(complex(*new_vect[:2]))

        mob_new = mob.copy().shift(new_points[0] - old_points[0])\
            .rotate(new_angle-old_angle, about_point=new_points[0])\
            .scale(abs(complex(*new_vect[:2]))/(abs(complex(*old_vect[:2]))+1e-6), about_point=new_points[0])
        # if change_stroke:
        #     mob_new.set_stroke(width=mob_new.get_stroke_width() * np.sqrt(abs(complex(*new_vect[:2]))/(abs(complex(*old_vect[:2]))+1e-6)))
        return mob_new

class Test_BaseTree(Scene):

    CONFIG = {
        'camera_config': {
            'background_color': WHITE,
        }
    }

    def construct(self):

        layer_num=10
        colors = color_gradient([RED, GREEN, BLUE], layer_num+1)
        tree = BaseTree(layer_num=layer_num, base_branch=(DOWN * 3.25, DOWN * 1), derived_branch=[(DOWN, LEFT + UP * 0.2), (DOWN, DOWN * 1.25 + 0.9 * LEFT), (DOWN, RIGHT * 1.25)])
        for i in range(layer_num+1):
            tree[i].set_stroke(color=colors[i])

        # text_xgnb = Text('XGNB', font='庞门正道标题体').rotate(PI/2).set_height(2).move_to(2.1*DOWN)
        # tree_xgnb = BaseTree(text_xgnb, layer_num=layer_num, base_branch=(DOWN * 3.1, DOWN * 1), derived_branch=[(DOWN, LEFT - UL * 0.2), (DOWN, RIGHT + UR * 0.2)])
        # for i in range(layer_num+1):
        #     tree_xgnb[i].set_color(colors[i])

        self.add(tree)
        self.wait()


class PythagoreanTree(BaseTree):

    CONFIG = {
        'abc': [3,4,5], # c为水平的斜边，其实不是直角三角形也可以
    }

