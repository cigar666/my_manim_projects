from manimlib.imports import *

class Test_01(Scene):

    CONFIG = {'camera_config': {
        'background_color': WHITE,
    }}

    def setup(self):
        l = 1
        A, B, C = l/np.sqrt(3) * complex_to_R3(np.exp(1j * 0)) + RIGHT * 0.125, \
                  l/np.sqrt(3) * complex_to_R3(np.exp(2j * PI/3)), \
                  l/np.sqrt(3) * complex_to_R3(np.exp(-2j * PI/3))

        self.vect_x, self.vect_y = A - C, B - C
        self.tri_01 = Polygon(A, B, C, stroke_width=1, fill_opacity=1)
        self.tri_02 = self.tri_01.copy().rotate(PI, about_point=(A+B)/2)

    def construct(self):
        C = 1/np.sqrt(3) * complex_to_R3(np.exp(-2j * PI/3))
        list_1 = [[0, 0], [-1, 1]]
        list_2 = [[-1, 0], [-1, -1]]
        list_3 = [[0, -1], [0, -2]]
        group_1 = self.create_triangles(list_1, '#1955D6').scale(3, about_point=C)
        group_2 = self.create_triangles(list_2, '#4486E8').scale(3, about_point=C)
        group_3 = self.create_triangles(list_3, '#567ADF').scale(3, about_point=C)
        cube = VGroup(group_1, group_2, group_3).shift(UP)
        list_m = [[-2, -1], [-2, 0], [-2, 1], [-2, 2], [-2, 3], [-1, 2], [-1, 1],
                  [0, 0], [0, 1], [1, 0], [1, -1], [1, -2], [1, -3], [1, -4]]
        tex_m = self.create_triangles(list_m, WHITE).shift(UP)
        self.add(cube, tex_m)
        self.wait()

    def create_triangle(self, i, j):
        if j % 2 == 0:
            return self.tri_01.copy().shift(i * self.vect_x + j/2 * self.vect_y)
        else:
            return self.tri_02.copy().shift(i * self.vect_x + (j-1)/2 * self.vect_y)

    def create_triangles(self, list_ij, color=BLUE):
        tri_group = VGroup()
        for i, j in list_ij:
            tri_group.add(self.create_triangle(i, j))
        return tri_group.set_color(color)

class Triangles(VGroup):

    CONFIG = {
        'stroke_width': 0.6,
        'tri_scale': 1, # there's some bugs
        # 'tri_list': [[0, 0]],
    }

    def __init__(self, X, Y, O, **kwargs):

        VGroup.__init__(self, **kwargs)

        self.vect_x, self.vect_y = (X - O) * self.tri_scale, (Y - O) * self.tri_scale
        self.X, self.Y, self.O = O + self.vect_x, O + self.vect_y, O
        self.tri_01 = Polygon(self.X, self.Y, self.O,  stroke_width=self.stroke_width, fill_opacity=1)
        self.tri_02 = self.tri_01.copy().rotate(PI, about_point=(X+Y)/2)

    def create_triangle(self, i, j):
        if j % 2 == 0:
            return self.tri_01.copy().shift(i * self.vect_x + j/2 * self.vect_y)
        else:
            return self.tri_02.copy().shift(i * self.vect_x + (j-1)/2 * self.vect_y)

    def create_triangles(self, list_ij, color=BLUE, scale=1, plot_depth=0):
        tri_group = VGroup()
        for i, j in list_ij:
            tri_group.add(self.create_triangle(i, j))
        self.add(tri_group.scale(scale, about_point=self.O))
        return tri_group.set_color(color)

    def create_list_by_move(self, move_list, start=[0, 0]):
        list = [start]
        for str in move_list:

            i, j = list[-1]
            if j % 2 == 0:
                if str == 'Y' or str == 'U':
                    list.append([i, j+1])
                elif str == 'y' or str == 'D':
                    list.append([i, j-1])
                elif str == 'X' or str == 'R':
                    list.append([i, j+1])
                elif str == 'x' or str == 'L':
                    list.append([i-1, j+1])
                else:
                    print('error, invalid move instruction')
            else:
                if str == 'Y' or str == 'U':
                    list.append([i, j+1])
                elif str == 'y' or str == 'D':
                    list.append([i, j-1])
                elif str == 'X' or str == 'R':
                    list.append([i+1, j-1])
                elif str == 'x' or str == 'L':
                    list.append([i, j-1])
                else:
                    print('error, invalid move instruction')

        return list

    def create_triangles_by_move(self, move_list, start=[0, 0], color=BLUE, scale=1, plot_depth=0):
        list = self.create_list_by_move(move_list, start=start)
        return self.create_triangles(list, color=color, scale=scale, plot_depth=plot_depth)

class Test_Plot_by_tri(Scene):

    def construct(self):
        l = 0.4
        X, Y, O = l/np.sqrt(3) * complex_to_R3(np.exp(1j * 0)) + RIGHT * 0.15 * l, \
                  l/np.sqrt(3) * complex_to_R3(np.exp(2j * PI/3)), \
                  l/np.sqrt(3) * complex_to_R3(np.exp(-2j * PI/3))


        list_1 = [[0, 0], [-1, 1]]
        list_2 = [[-1, 0], [-1, -1]]
        list_3 = [[0, -1], [0, -2]]
        list_m = [[-2, -1], [-2, 0], [-2, 1], [-2, 2], [-2, 3], [-1, 2], [-1, 1],
                  [0, 0], [0, 1], [1, 0], [1, -1], [1, -2], [1, -3], [1, -4]]
        list_m2 = [[-2, -3], [-2, -2], [-2, -1], [-2, 0], [-2, 1], [-2, 2], [-2, 3], [-1, 2], [-1, 1],
                   [0, 0], [0, 1], [1, 0], [1, -1], [1, -2], [1, -3], [1, -4], [1, -5], [1, -6]]
        tri_m = Triangles(X, Y, O)

        tri_a = Triangles(X, Y, O)
        list_a = tri_a.create_list_by_move('Y' * 6 + 'XYXyX' + 'y' * 6, start=[-2, -3]) +\
                 tri_a.create_list_by_move('yXY', start=[-1, -2])

        tri_n = Triangles(X, Y, O)
        # list_n = tri_a.create_list_by_move('Y' * 4 + 'XyXyX' + 'Y' * 2 + 'y' * 4, start=[-2, -1])
        list_n = tri_n.create_list_by_move('Y' * 6 + 'XyXyX' + 'Y' * 2 + 'y' * 6, start=[-2, -3])

        tri_i = Triangles(X, Y, O)
        # list_n = tri_a.create_list_by_move('Y' * 4 + 'XyXyX' + 'Y' * 2 + 'y' * 4, start=[-2, -1])
        list_i = [[-1, 3], [0, 2]] + tri_i.create_list_by_move('Y' * 3 , start=[-1, -3]) + tri_i.create_list_by_move('Y' * 3, start=[0, -4])


        tri_m.create_triangles(list_1, color='#1955D6', scale=3, plot_depth=-1)
        tri_m.create_triangles(list_2, color='#4486E8', scale=3, plot_depth=-1)
        tri_m.create_triangles(list_3, color='#4579DA', scale=3, plot_depth=-1)
        tri_m.create_triangles(list_m, color=WHITE, scale=1, plot_depth=0)
        tri_m.scale(1.56).shift(LEFT * 4.)

        tri_a.create_triangles(list_a, color=WHITE, scale=1, plot_depth=0).next_to(tri_m, RIGHT, buff=0.6)
        tri_n.create_triangles(list_n, color=WHITE, scale=1, plot_depth=0).next_to(tri_a, RIGHT, buff=0.6)
        tri_i.create_triangles(list_i, color=WHITE, scale=1, plot_depth=0).next_to(tri_n, RIGHT, buff=0.6)
        tri_m2 = Triangles(X, Y, O).create_triangles(list_m2, color=WHITE, scale=1, plot_depth=0).next_to(tri_i, RIGHT, buff=0.6)
        manim = VGroup(tri_m, tri_a, tri_n, tri_i, tri_m2).set_width(12).move_to(ORIGIN)
        self.add(manim)

        self.wait()

class Test_Plot_by_tri_02(Scene):

    def construct(self):

        r = 0.6
        theta = ValueTracker(0)
        X, Y, O = r * complex_to_R3(np.exp(1j * (PI/6 - theta.get_value()))),\
                  r * complex_to_R3(np.exp(1j * (PI/2 - 0 * theta.get_value()))), \
                  ORIGIN

        tri = Triangles(X, Y, O)

        # tri.create_triangles_by_move('Y' * 11 + 'yX' * 4, start=[-3, -5], color=BLUE_B)
        # tri.create_triangles_by_move('Xy' * 5 + 'X' + 'xy' * 4, start=[-3, 7], color=BLUE_D)
        # tri.create_triangles_by_move('y' * 8 + 'X' * 11, start=[-2, 2], color=BLUE_E)
        def update_tri(t):
            X, Y, O = r * complex_to_R3(np.exp(1j * (PI/6 - theta.get_value()))),\
                  r * complex_to_R3(np.exp(1j * (PI/2 - 0 * theta.get_value()))), \
                  ORIGIN
            t_new = Triangles(X, Y, O)
            t_new.create_triangles_by_move('Y' * 15 + 'yX' * 6, start=[-3, -5], color=BLUE_B)
            t_new.create_triangles_by_move('Xy' * 7 + 'X' + 'xy' * 6, start=[-3, 11], color=BLUE_D)
            t_new.create_triangles_by_move('y' * 12 + 'X' * 15, start=[-2, 6], color=BLUE_E)
            t.become(t_new)
        tri.add_updater(update_tri)


        self.add(tri)
        self.wait()
        # self.play(theta.set_value, PI/6, run_time=4)
        # self.wait()


class CGNB(Scene):

    def construct(self):

        l = 0.4
        X, Y, O = l/np.sqrt(3) * complex_to_R3(np.exp(1j * 0)) + RIGHT * 0.15 * l, \
                  l/np.sqrt(3) * complex_to_R3(np.exp(2j * PI/3)), \
                  l/np.sqrt(3) * complex_to_R3(np.exp(-2j * PI/3))

        tri_c = Triangles(X, Y, O)
        tri_c.create_triangles_by_move("xyxYxYYYYYYXYXyX", start=[1, -4]).center()
        tri_g = Triangles(X, Y, O)
        tri_g.create_triangles_by_move("XyyxyxYxYYYYYYXYXyX", start=[0, -1]).center()
        tri_n = Triangles(X, Y, O)
        tri_n.create_triangles_by_move("YYYYYYXyXyXYYyyyyyy", start=[-2, -3], color=WHITE).center()
        tri_b = Triangles(X, Y, O)
        tri_b.create_triangles_by_move("XyXyyxyxYxYYYYYYXYXyXyyx", start=[-1, 1], color=WHITE).center()

        cgnb = VGroup(tri_c, tri_g, tri_n, tri_b).arrange(RIGHT, buff=0.6)
        self.add(cgnb)


class Cigar666(Scene):

    def construct(self):
        
        l = 0.4
        X, Y, O = l/np.sqrt(3) * complex_to_R3(np.exp(1j * 0)) + RIGHT * 0.15 * l, \
                  l/np.sqrt(3) * complex_to_R3(np.exp(2j * PI/3)), \
                  l/np.sqrt(3) * complex_to_R3(np.exp(-2j * PI/3))

        tri_c = Triangles(X, Y, O)
        tri_c.create_triangles_by_move("xyxYxYYYYYYXYXyX", start=[1, -4]).center()

        tri_i = Triangles(X, Y, O)
        tri_i.create_triangles_by_move("Y" * 8 + "X" + "y" * 8, start=[-1, -3]).center()

        tri_g = Triangles(X, Y, O)
        tri_g.create_triangles_by_move("XyyxyxYxYYYYYYXYXyX", start=[0, -1]).center()

        tri_a = Triangles(X, Y, O)
        list_a = tri_a.create_list_by_move('Y' * 6 + 'XYXyX' + 'y' * 6, start=[-2, -3]) +\
                 tri_a.create_list_by_move('yXY', start=[-1, -2])
        tri_a.create_triangles(list_a).center()

        tri_r = Triangles(X, Y, O)
        tri_r.create_triangles_by_move("U"*6+"RURDRDDLDLRDRDD", start=[-2, -1]).center()

        tri_6 = Triangles(X, Y, O)
        tri_6.create_triangles_by_move("LULDL"+"D"*6+"RDRURUULULD", start=[1, 2], color=WHITE).center()

        cg666 = VGroup(tri_c, tri_i, tri_g, tri_a, tri_r, tri_6, tri_6.copy(), tri_6.copy()).arrange(RIGHT, buff=0.6).set_width(12)
        self.add(cg666)

