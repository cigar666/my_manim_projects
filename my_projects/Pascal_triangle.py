from manimlib.imports import *
# from scipy.special import comb

def factor_num(n, m):
    # n = s * m ** t, to get maximum t
    num = 0
    while n % m == 0:
        n = int(n/m)
        num += 1
    return num

def get_prime_factor(n):

    prime_factor = {}
    while n>1:
        for i in range(2, n+1):
            if n%i==0:
                n=int(n/i)

                if i in prime_factor.keys():
                    prime_factor[i] += 1
                else:
                    prime_factor[i] = 1

                break

    return prime_factor

def factorial_factor_num_(n, m):
    # (n!) = s * m ** t, to get maximum t
    # here m mast be prime number
    num = 0
    for i in range(1, n+1):
        num += factor_num(i, m)
    return num

def comb_factor_num_(n, k, m):
    # comb(n, k) = s * m ** t, to get maximum t
    # here m mast be prime number
    return factorial_factor_num_(n, m) - factorial_factor_num_(k, m) - factorial_factor_num_(n-k, m)

def factorial_factor_num(n, m):
    # (n!) = sum(p_i ^ k_i)
    # m = sum(pm_i ^ km_i)
    # so (n!) = s * sum(pm_i ^ t_i)
    # to get the dict with key of pm_i and value of t_i
    prime_factor = get_prime_factor(m)
    prime_f_02 = {}
    for key in prime_factor:
        prime_f_02[key] = factorial_factor_num_(n, key)
    return prime_f_02
    # return min([int(prime_f_02[key]/prime_factor[key]) for key in prime_factor])

def comb_factor_num(n, k, m):
    # comb(n, k) = s * m ** t, to get maximum t
    prime_factor = get_prime_factor(m)
    p_01 = factorial_factor_num(n, m)
    p_02 = factorial_factor_num(k, m)
    p_03 = factorial_factor_num(n-k, m)
    p = {}
    for key in p_01:
        p[key] = p_01[key] - p_02[key] - p_03[key]
    return min([int(p[key]/prime_factor[key]) for key in prime_factor])

# print(get_prime_factor(666))
# print(factorial_factor_num(100, 10))
# print(comb_factor_num(10, 4, 35))


class Pascal_Triangle_by_Dot(Scene):

    CONFIG = {
        'camera_config':{
            'background_color': WHITE,
        },
        'dot_radius': 0.025,
        'gap': 0.001,
        'dot_color': [BLUE_B, ORANGE],
        'layer_num': 160,
        'height_of_all': None,
    }

    def setup(self):

        r = self.dot_radius
        g = self.gap
        l = g + r * 2
        h = l * np.cos(PI/6)
        dot = Dot(radius=self.dot_radius, color=self.dot_color[0])

        self.dots = VGroup()
        for i in range(self.layer_num):
            dots_i = VGroup(*[dot.copy() for j in range(i+1)]).arrange(RIGHT * (g + 1e-5), buff=1)
            self.dots.add(dots_i)
        self.dots.arrange(DOWN * h, buff=(h - r * 2)/h)
        if not self.height_of_all == None:
            self.dots.set_height(self.height_of_all)

    def set_color_to_dots(self, n=2, color=None):

        if color == None:
            color = self.dot_color[1]

        for i in range(self.layer_num):
            for j in range(i+1):
                # if comb(i, j) % n == 0:
                #     self.dots[i][j].set_color(color)
                if comb_factor_num(i, j, n) > 0:
                    self.dots[i][j].set_color(color)
        return self.dots

    def get_colored_dots_copy(self, n=2, color=None):
        dots = self.dots.copy()
        if color == None:
            color = self.dot_color[1]

        for i in range(self.layer_num):
            for j in range(i+1):

                if comb_factor_num(i, j, n) > 0:
                    dots[i][j].set_color(color)
        return dots

    def construct(self):

        self.add(self.dots)
        self.wait()
        self.set_color_to_dots(n=15)
        self.wait(4)

class Increace_n(Pascal_Triangle_by_Dot):

    CONFIG = {
        'camera_config':{
            'background_color': WHITE,
        },
        'dot_radius': 0.025,
        'gap': 0.001,
        'dot_color': [BLUE_B, ORANGE],
        'layer_num': 256,
        'height_of_all': 6.5,
        'iter_num': 32,
    }

    def construct(self):

        dots_old = self.dots.copy()
        self.add(dots_old)
        num=self.iter_num
        colors = color_gradient([ORANGE, RED, PINK], num)
        dots_list =[dots_old, dots_old]
        t = 2.4
        text = Text('对杨辉三角中所有能\n被n=%d整除的点染色' % 2, font='思源黑体 Bold', color=BLACK).set_height(0.8).to_corner(UR * 1.2)
        text.set_color_by_t2c({'染色': colors[0], 'n=%d' % 2: GREEN})
        text_list = [text, text]
        self.play(Write(text), run_time=1.8)
        for i in range(2, num+1):

            dots_new = self.get_colored_dots_copy(n=i, color=colors[i-1])
            dots_list.append(dots_new)
            dots_list.remove(dots_list[0])

            self.play(ReplacementTransform(dots_list[0], dots_list[1]),
                      ReplacementTransform(text_list[0], text_list[1]),
                      run_time=t * 0.4)
            self.wait(t + 1.2 - 0.25 * (i-1) if i < 5 else t + 0.15)

            text_new = Text('对杨辉三角中所有能\n被n=%d整除的点染色' % (i+1), font='思源黑体 Bold', color=BLACK).set_height(0.8).to_corner(UR * 1.2)
            text_new.set_color_by_t2c({'染色': colors[i], 'n=%d' % (i+1): GREEN})
            text_list.append(text_new)
            text_list.remove(text_list[0])

        self.wait(4)

class Increace_n_02(Increace_n):

    CONFIG = {
        'camera_config':{
            'background_color': WHITE,
        },
        'dot_radius': 0.025,
        'gap': 0.001,
        'dot_color': [BLUE_B, ORANGE],
        'layer_num': 180,
        'height_of_all': 6.5,
        'iter_num': 25,
    }

class Picture(Pascal_Triangle_by_Dot):

    CONFIG = {
        'camera_config':{
            'background_color': WHITE,
        },
        'dot_radius': 0.025,
        'gap': 0.001,
        'dot_color': [BLUE_B, average_color(RED, PINK)],
        'layer_num': 256,
        'height_of_all': 6.6,
        'n': 24,
    }

    def construct(self):

        self.add(self.dots)
        self.wait()
        self.set_color_to_dots(n=self.n)
        self.wait(4)
