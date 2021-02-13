from manimlib.imports import *

# 思路：把轮廓上布上一定密度的点，然后确定对应的轮廓，交并补差等操作通过对这些轮廓图形的选择来实现

class VGroup_(VGroup):

    CONFIG = {
        'step_size': 0.01,
    }

    def __init__(self, *vmobjects, **kwargs):

        VGroup.__init__(self, *vmobjects, **kwargs)

    def get_outline_points(self, mobject):
        perimeter = self.get_mob_perimeter(mobject)
        num = int(perimeter/self.step_size+1)
        start, end = 0, 1
        points_list = [mobject.point_from_proportion(start + i * (end - start) / num) for i in range(num+1)]
        return points_list

    def get_all_outline_points(self):
        p_list = []
        for mob in self:
            p_list += self.get_outline_points(mob)
        self.points_list = p_list
        return self.points_list

    def get_mob_perimeter(self, mobject, num=10000, start=0, end=1):
        points = np.array([mobject.point_from_proportion(start + i * (end - start) / num) for i in range(num+1)])
        p1, p2 = points[0:-1], points[1:]
        l = (p2 - p1) ** 2
        perimeter = sum((l[:,0] + l[:,1] + l[:,2]) ** 0.5)
        return perimeter

    # def get_loop_old(self, center=ORIGIN):
    #     def get_angle(p):
    #         return np.angle(R3_to_complex(p-center))
    #     p_list = self.points_list
    #     p_list.sort(key=get_angle)
    #     d_list = [get_norm(p - center) for p in p_list]
    #     n = len(p_list)
    #     s = d_list.index(min(d_list))
    #     loop_list = [p_list[s]]
    #     p_old = p_list[s]
    #     p_new = center
    #     for i in range(1, n):
    #         id = (i + s) % n
    #         p_new = p_list[id]
    #         if get_norm(p_new - p_old) <= self.step_size * 1.25:
    #             loop_list.append(p_new)
    #             p_old = p_new
    #
    #     return loop_list

    def get_loop(self, center=ORIGIN):

        # 这部分写得过于蛋疼
        # TODO 当中心点对应的某个角度上不止一个点时靠外的就会被忽略

        def get_angle(p):
            return np.angle(R3_to_complex(p-center))
        def get_distance(p):
            return get_norm(p-center)

        p_list = self.points_list
        p_list.sort(key=get_distance)
        i = 0
        loop_list = []
        angle_range = []

        def in_range(a, r):
            if max(r) > PI and a < 0:
                a += TAU
            if a >= min(r) and a <= max(r):
                return True
            else:
                return False

        def accept_point(point, a_range):
            a = get_angle(point)
            for r in a_range:
                if in_range(a, r):
                    return False
            return True

        def update_angle_range():
            angle_range = []
            n = len(loop_list)
            r_temp, r_temp_new = (100, 101), (100, 101)
            for i in range(n-1):
                if get_norm(loop_list[i] - loop_list[i+1]) <= self.step_size * 1.25:
                    r_temp_new = (get_angle(loop_list[i]), get_angle(loop_list[i+1]))
                    if abs(r_temp_new[0]-r_temp[1])<1e-5:
                        r_temp = (r_temp[0], r_temp_new[1])
                        angle_range.remove(angle_range[-1])
                        r_temp = (min(r_temp), max(r_temp))
                        angle_range.append(r_temp)
                    else:
                        r_temp = r_temp_new
                        r_temp = (min(r_temp), max(r_temp))
                        angle_range.append(r_temp)

            if get_norm(loop_list[-1] - loop_list[0]) <= self.step_size * 1.25 and n > 10:
                r_temp_new = (get_angle(loop_list[-1]), get_angle(loop_list[0]) + TAU)
                r_temp = min(r_temp_new), max(r_temp_new)
                angle_range.append(r_temp)

            return angle_range

        for i in range(len(p_list)):
            if accept_point(p_list[i], angle_range):
                loop_list.append(p_list[i])
            loop_list.sort(key=get_angle)
            angle_range = update_angle_range()

        return loop_list

    def create_poly(self, loop_list, **kwargs):
        return Polygon(*loop_list, **kwargs)

    def get_shape(self, center=ORIGIN, **kwargs):
        return self.create_poly(self.get_loop(center), **kwargs)

class Test(Scene):

    def construct(self):

        s = Square(side_length=4, stroke_width=10, stroke_color=BLUE).rotate(PI/6)
        c = Circle(radius=4, stroke_width=10, stroke_color=RED).shift(UL * 1.6)
        p = RegularPolygon(5, stroke_width=10, stroke_color=YELLOW).scale(2).shift(RIGHT * 2.)

        vg = VGroup_(s, c, p,step_size=0.25)
        p_list = vg.get_all_outline_points()
        dots = VGroup(*[Dot(p, radius=0.025) for p in p_list])
        poly_1 = vg.get_shape(center=RIGHT, fill_color=PINK, fill_opacity=1)
        poly_2 = vg.get_shape(center=LEFT, fill_color=ORANGE, fill_opacity=1)
        poly_3 = vg.get_shape(center=s.get_vertices()[-1] + RIGHT * 0.4, fill_color=GREEN, fill_opacity=1)

        self.add(s, c, p,
                 poly_1, poly_2, poly_3,
                 dots,
                 )
        self.wait()

class Test_02(Scene):

    def construct(self):

        c1 = Circle(radius=3, stroke_width=10, stroke_color=RED)
        c2 = Circle(radius=1, stroke_width=10, stroke_color=RED).shift(RIGHT * 2)
        vg = VGroup_(c1, c2, step_size=0.25)
        p_list = vg.get_all_outline_points()
        dots = VGroup(*[Dot(p, radius=0.025) for p in p_list])
        poly_1 = vg.get_shape(center=LEFT *1.5, fill_color=PINK, fill_opacity=1)

        self.add(c1, c2,
                 poly_1,
                 dots,
                 )
        self.wait()







