from manimlib.imports import *
import numpy.linalg as lg

# interpolation functions #
get_st = lambda p, xy=[DL, UR]: [(p[0]-xy[0][0])/(xy[1][0]-xy[0][0])*2 - 1,
                                 (p[1]-xy[0][1])/(xy[1][1]-xy[0][1])*2 - 1]

N_RECT4 = lambda s, t: 1/4 * np.array([(1-s)*(1-t),
                                       (1+s)*(1-t),
                                       (1+s)*(1+t),
                                       (1-s)*(1+t)])

interpolate_RECT4_scalar = lambda st, x: sum(N_RECT4(*st)*np.array(x)) # x[i] is a float
interpolate_RECT4_vector = lambda st, x_vector: np.array([sum(N_RECT4(*st)*np.array(x_vector)[:,i]) for i in range(len(x_vector[0]))])

## interpolation functions / shape functions ##
# 2d elements #
get_xy_array = lambda x, y: np.array([1,
                                      x, y,
                                      x*y, x*x, y*y,
                                      x*x*y, x*y*y, x*x*y*y]) # x**3 和 y**3 不要了，因为只需要搞到平面八(最多九)节点单元

get_xy_TRIA3 = lambda x, y: get_xy_array(x, y)[0:3]
get_xy_QUAD4 = lambda x, y: get_xy_array(x, y)[0:4]
get_xy_TRIA6 = lambda x, y: get_xy_array(x, y)[0:6]
get_xy_QUAD8 = lambda x, y: get_xy_array(x, y)[0:8]
get_xy_QUAD9 = lambda x, y: get_xy_array(x, y)[0:9]

N_QUAD3 = lambda x, y, xy3: np.dot(get_xy_QUAD3(x, y), lg.inv(np.array([get_xy_QUAD3(*xy3[i][0:2]) for i in range(3)])))
N_QUAD4 = lambda x, y, xy4: np.dot(get_xy_QUAD4(x, y), lg.inv(np.array([get_xy_QUAD4(*xy4[i][0:2]) for i in range(4)])))
N_QUAD6 = lambda x, y, xy6: np.dot(get_xy_QUAD6(x, y), lg.inv(np.array([get_xy_QUAD6(*xy6[i][0:2]) for i in range(6)])))
N_QUAD8 = lambda x, y, xy8: np.dot(get_xy_QUAD8(x, y), lg.inv(np.array([get_xy_QUAD8(*xy8[i][0:2]) for i in range(8)])))
N_QUAD9 = lambda x, y, xy9: np.dot(get_xy_QUAD9(x, y), lg.inv(np.array([get_xy_QUAD9(*xy9[i][0:2]) for i in range(9)])))

interpolate_QUAD3_scalar = lambda xy, xy3, u: sum(N_QUAD3(xy[0], xy[1], xy3) * np.array(u)) # u[i] is a float
interpolate_QUAD4_scalar = lambda xy, xy4, u: sum(N_QUAD4(xy[0], xy[1], xy4) * np.array(u)) # u[i] is a float
interpolate_QUAD6_scalar = lambda xy, xy6, u: sum(N_QUAD6(xy[0], xy[1], xy6) * np.array(u)) # u[i] is a float
interpolate_QUAD8_scalar = lambda xy, xy8, u: sum(N_QUAD8(xy[0], xy[1], xy8) * np.array(u)) # u[i] is a float
interpolate_QUAD9_scalar = lambda xy, xy9, u: sum(N_QUAD9(xy[0], xy[1], xy9) * np.array(u)) # u[i] is a float

interpolate_QUAD3_vector = lambda xy, xy3, u: np.array([sum(N_QUAD3(xy[0], xy[1], xy3) * np.array(u)[:,i]) for i in range(len(u[0]))])
interpolate_QUAD4_vector = lambda xy, xy4, u: np.array([sum(N_QUAD4(xy[0], xy[1], xy4) * np.array(u)[:,i]) for i in range(len(u[0]))])
interpolate_QUAD6_vector = lambda xy, xy6, u: np.array([sum(N_QUAD6(xy[0], xy[1], xy6) * np.array(u)[:,i]) for i in range(len(u[0]))])
interpolate_QUAD8_vector = lambda xy, xy8, u: np.array([sum(N_QUAD8(xy[0], xy[1], xy8) * np.array(u)[:,i]) for i in range(len(u[0]))])
interpolate_QUAD9_vector = lambda xy, xy9, u: np.array([sum(N_QUAD9(xy[0], xy[1], xy9) * np.array(u)[:,i]) for i in range(len(u[0]))])

# 1d elements #
# get_x_array = lambda x: np.array([1, x, x*x, x*x*x])
get_x_array = lambda x, n=2: np.array([x**i for i in range(n)])
N_ROD2 = lambda x, x2: np.dot(get_x_array(x, n=2), lg.inv(np.array([get_x_array(x2[i], n=2) for i in range(2)])))
interpolate_ROD2_scalar = lambda x, x2, u: sum(N_ROD2(x, x2) * np.array(u)) # u[i] is a float
# interpolate_ROD2_2D = lambda xy, xy2, u: np.array([interpolate_ROD2_scalar(xy[0], np.array(xy2)[:,0], np.array(u)[:,0]),
#                                                    interpolate_ROD2_scalar(xy[1], np.array(xy2)[:,1], np.array(u)[:,1]),
#                                                    0])

interpolate_ROD2_vector = lambda xy, xy2, u: np.array([sum(N_ROD2(xy[i%2], np.array(xy2)[:, i%2]) * np.array(u)[:, i]) for i in range(len(u[0]))])
# 和预计的效果不一样

# TODO

# 3d elements #
get_xyz_array = lambda x, y, z: np.array([1,
                                          x, y, z,
                                          x*y, x*z, y*z, x*y*z,
                                          x*x, y*y, z*z,
                                          x*x*y, x*x*z, x*y*y, x*z*z, y*y*z, y*z*z,
                                          x*x*y*y, x*x*y*z, x*x*z*z, x*y*y*z, x*y*z*z, y*y*z*z,
                                          x*x*y*y*z, x*x*y*z*z, x*y*y*z*z,
                                          x*x*y*y*z*z])
get_xyz_HEXA8 = lambda x, y, z: get_xyz_array(x, y, z)[0:8]
get_xyz_HEXA27 = lambda x, y, z: get_xyz_array(x, y, z)
N_HEXA8 = lambda x, y, z, xyz8: np.dot(get_xyz_HEXA8(x, y, z), lg.inv(np.array([get_xyz_HEXA8(*xyz8[i]) for i in range(8)])))
N_HEXA27 = lambda x, y, z, xyz27: np.dot(get_xyz_HEXA27(x, y, z), lg.inv(np.array([get_xyz_HEXA27(*xyz27[i]) for i in range(27)])))
interpolate_HEXA8_scalar = lambda xyz, xyz8, u: sum(N_HEXA8(xyz[0], xyz[1], xyz[2], xyz8) * np.array(u)) # u[i] is a float
interpolate_HEXA27_scalar = lambda xyz, xyz27, u: sum(N_HEXA27(xyz[0], xyz[1], xyz[2], xyz27) * np.array(u)) # u[i] is a float
interpolate_HEXA8_vector = lambda xyz, xyz8, u: np.array([sum(N_HEXA8(xyz[0], xyz[1], xyz[2], xyz8) * np.array(u)[:,i]) for i in range(len(u[0]))])
interpolate_HEXA27_vector = lambda xyz, xyz27, u: np.array([sum(N_HEXA27(xyz[0], xyz[1], xyz[2], xyz27) * np.array(u)[:,i]) for i in range(len(u[0]))])

# TODO HEXA27这种还是通过拉格朗日插值推出针对标准母单元的形函数表达式吧，不然每次变形都对27阶矩阵求逆有点蛋疼

N_1D3N = lambda s, a: np.array([s*(s-a)/2/a/a, -(s*s-a*a)/a/a, s*(s+a)/2/a/a])

## utils ##
def get_vertices_RECT9(p_DL, p_UR):

    # p7, p8, p9
    # p4, p5, p6
    # p1, p2, p3

    x_min, x_max = min(p_DL[0], p_UR[0]), max(p_DL[0], p_UR[0])
    y_min, y_max = min(p_DL[1], p_UR[1]), max(p_DL[1], p_UR[1])

    xy = np.meshgrid(*[np.array([x_min, (x_min+x_max)/2, x_max]), np.array([y_min, (y_min+y_max)/2, y_max])])
    x, y, z = xy[0].flatten(), xy[1].flatten(), np.zeros(9)
    p = np.array([x, y, z]).T
    return p

def get_vertices_CIRCLE9(p_DL, p_UR):
    center = (p_DL + p_UR)/2
    a, b = abs(p_DL[0]-p_UR[0]), abs(p_DL[1]-p_UR[1])
    p = np.array(([center + complex_to_R3(np.exp(1j * i * TAU/8)) * np.array([a, b, 0])/2 for i in range(8)]+[center]))
    return p

def get_vertices_CUBE27(p_DLI, p_URO):

    x_min, x_max = min(p_DLI[0], p_URO[0]), max(p_DLI[0], p_URO[0])
    y_min, y_max = min(p_DLI[1], p_URO[1]), max(p_DLI[1], p_URO[1])
    z_min, z_max = min(p_DLI[2], p_URO[2]), max(p_DLI[2], p_URO[2])
    xyz = np.meshgrid(*[np.array([x_min, (x_min+x_max)/2, x_max]), np.array([y_min, (y_min+y_max)/2, x_max]), np.array([z_min, (z_min+z_max)/2, z_max])])
    x, y, z = xyz[0].flatten(), xyz[1].flatten(), xyz[2].flatten()
    p = np.array([x, y, z]).T

    return p

def get_vertices_from_circle(c, num=8):
    return [c.point_from_proportion(1/num * i) for i in range(num)]

def get_vertices_on_rect_by_circle(c, num=8):
    n5 = c.get_center()
    n6, n8, n4, n2 = c.point_from_proportion(0.0), c.point_from_proportion(0.25), \
                     c.point_from_proportion(0.5), c.point_from_proportion(0.75)
    n1 = n2 + n4 - n5
    n3 = n2 + n6 - n5
    n9 = n6 + n8 - n5
    n7 = n8 + n4 - n5
    return [n1, n2, n3, n4, n5, n6, n7, n8, n9]

    return [c.point_from_proportion(1/num * i) for i in range(num)]

def get_vertices_TUBE27(c_top, c_middle, c_bottom):

    p_list_1 = get_vertices_from_circle(c_top) + [c_top.get_center()]
    p_list_2 = get_vertices_from_circle(c_middle) + [c_top.get_center()]
    p_list_3 = get_vertices_from_circle(c_bottom) + [c_top.get_center()]

    return p_list_1 + p_list_2 + p_list_3


projection_ = lambda p, theta=PI/4: np.array([p[0]+np.sin(theta)*p[1], p[1]*np.cos(theta)+p[2], 0])
matrix_A = lambda theta=PI/4: np.array([[1,0,0], [np.sin(theta), np.cos(theta), 0], [0, 1, 0]])
projection = lambda p, theta=PI/4: np.dot(p, matrix_A(theta=theta))

class Node(VGroup):

    CONFIG = {
        'color': BLUE_D,
        'radius': 0.1,
        'stroke_width': 2.5,
        'ds': 1e-3,
    }

    def __init__(self, pos=ORIGIN, **kwargs):
        VGroup.__init__(self, **kwargs)
        self.pos = pos
        self.node = Circle(arc_center=pos, stroke_color=self.color, stroke_width=self.stroke_width, radius=self.radius, fill_color=WHITE, fill_opacity=1)
        self.add(self.node)

    def active_on(self):
        return self.node.set_fill(BLUE_D, 1).set_height(self.radius * 2.)

    def active_off(self):
        return self.node.set_fill(WHITE, 1).set_height(self.radius*2)

    def change_style(self, node):
        pos_old = self.pos
        self.pos = node.get_center()
        if get_norm(self.pos - pos_old) > self.ds:
            self.active_on()
        else:
            self.active_off()

    def active_if_moved(self):
        self.node.add_updater(self.change_style)


class Small_Node(Node):
     CONFIG = {
         'color': BLUE_D,
         'radius': 0.05,
         'stroke_width': 2.4,
     }


class Nodes(VGroup):

    def __init__(self, pos=ORIGIN, **kwargs):
        VGroup.__init__(self, **kwargs)

    def select_nodes_by_range(self, range):
        pass

    def create_subgroup(self):
        pass

    def set_constraint(self):
        pass

    # TODO 将一堆节点（不一定是一个DeformableVMobject中的节点）放进Nodes中进行统一管理，可按条件选择节点、添加约束、控制节点位移等

# 先写个能用的函数放这儿，之后改写成Nodes的类方法
def put_nodes_on_curve(nodes_list, curve, start_alpha=0, end_alpha=1, reverse=False):
    # make sure that len(nodes_list) > 1

    x_list = [n.get_center()[0] for n in nodes_list]
    if reverse:
        # alpha_list = [start_alpha + (x_list[i] - x_list[-1])/(x_list[0] - x_list[-1]) * (end_alpha - start_alpha) for i in range(len(nodes_list))]
        start_alpha, end_alpha = 1-end_alpha, 1-start_alpha
        alpha_list = [start_alpha + (x_list[i] - x_list[-1])/(x_list[0] - x_list[-1]) * (end_alpha - start_alpha) for i in range(len(nodes_list))]
    else:
        alpha_list = [start_alpha + (x_list[i] - x_list[0])/(x_list[-1] - x_list[0]) * (end_alpha - start_alpha) for i in range(len(nodes_list))]
    for n, alpha in zip(nodes_list, alpha_list):
        n.move_to(curve.point_from_proportion(alpha))

##
class DeformableVMobject(VGroup):

    CONFIG = {
        'interp_func_config':{
            'ROD':   interpolate_ROD2_vector,
            'ROD2':  interpolate_ROD2_vector,
            'RECT':  interpolate_RECT4_vector,
            'RECT4': interpolate_RECT4_vector,
            'TRIA':  interpolate_QUAD3_vector,
            'TRIA3': interpolate_QUAD3_vector,
            'TRIA6': interpolate_QUAD6_vector,
            'QUAD':  interpolate_QUAD4_vector,
            'QUAD4': interpolate_QUAD4_vector,
            'QUAD8': interpolate_QUAD8_vector,
            'QUAD9': interpolate_QUAD9_vector,
            'HEXA':  interpolate_HEXA8_vector,
            'HEXA8': interpolate_HEXA8_vector,
            'HEXA27': interpolate_HEXA27_vector,
        },
        'node': Node(),
    }

    def __init__(self, *mobs, elem_range=[DL, UR], type='RECT4', **kwargs):

        VGroup.__init__(self, **kwargs)
        self.elem_range = elem_range
        self.origin_mobs = VGroup(*mobs)
        self.mobs = self.origin_mobs.copy()
        self.add(self.mobs)
        self.type = type if type in self.interp_func_config.keys() else 'RECT4'
        if 'RECT' in self.type:
            node_pos= elem_range[0], RIGHT * elem_range[1][0] + UP * elem_range[0][1], elem_range[1], RIGHT * elem_range[0][0] + UP * elem_range[1][1]
            self.nodes = VGroup(*[self.node.copy().move_to(pos) for pos in node_pos])
        else:
            node_pos = elem_range
            self.nodes = VGroup(*[self.node.copy().move_to(pos) for pos in node_pos])
        # self.interpolate_func = self.get_interpolate_func_RECT4() if ('RECT' in self.type) else self.get_interpolate_func_QUAD()
        if 'RECT' in self.type:
            self.interpolate_func = self.get_interpolate_func_RECT4()
        elif 'HEXA' in self.type:
            self.interpolate_func = self.get_interpolate_func_HEXA()
        else:
            self.interpolate_func = self.get_interpolate_func_QUAD()

    def get_interpolate_func_RECT4(self):
        return lambda p: interpolate_RECT4_vector(get_st((p[0], p[1]), xy=self.elem_range), x_vector=[n.get_center() for n in self.nodes])

    def get_interpolate_func_QUAD(self):
        return lambda p: self.interp_func_config[self.type]((p[0], p[1]), self.elem_range, u=[n.get_center() for n in self.nodes])

    def get_interpolate_func_HEXA(self):
        return lambda p: self.interp_func_config[self.type]((p[0], p[1], p[2]), self.elem_range, u=[n.get_center() for n in self.nodes])

    def get_result(self):
        return self.origin_mobs.copy().apply_function(self.interpolate_func)

    def update_interpolate_func(self):
        # self.interpolate_func = self.get_interpolate_func_RECT4() if (self.type == 'RECT4' or self.type == 'RECT') else self.get_interpolate_func_QUAD()
        if 'RECT' in self.type:
            self.interpolate_func = self.get_interpolate_func_RECT4()
        elif 'HEXA' in self.type:
            self.interpolate_func = self.get_interpolate_func_HEXA()
        else:
            self.interpolate_func = self.get_interpolate_func_QUAD()
        return self

    def update_by_interpolation(self):
        self.update_interpolate_func()
        self.mobs.become(self.get_result())
        return self

    def get_nodes(self):
        return self.nodes

    def always_update(self):
        self.mobs.add_updater(lambda mobs: mobs.become(self.get_result()))
        return self

    def stop_update(self):
        # self.update_by_interpolation()
        self.mobs.become(self.get_result())
        self.mobs.clear_updaters()
        # self.mobs.suspend_updating()
        return self

    def add_grid(self):
        pass

    def reset_nodes_and_type(self):
        pass

    def updata_range_by_nodes(self):
        self.elem_range = [n.get_center() for n in self.nodes]
        return self


class Dmob_RECT4(DeformableVMobject):

    def __init__(self, *mobs, side_offset=0, **kwargs):

        v4, v3, v2, v1 = SurroundingRectangle(VGroup(*mobs), buff=0).get_vertices()
        v1 += side_offset * DL
        v3 += side_offset * UR

        DeformableVMobject.__init__(self, *mobs, elem_range=[v1, v3], type='RECT', **kwargs)
        self.nodes_corner = VGroup(self.nodes[0], self.nodes[1], self.nodes[2], self.nodes[3])
        self.nodes_left = VGroup(self.nodes[0], self.nodes[3])
        self.nodes_right = VGroup(self.nodes[1], self.nodes[2])
        self.nodes_up = VGroup(self.nodes[2], self.nodes[3])
        self.nodes_down = VGroup(self.nodes[0], self.nodes[1])


class Dmob_RECT9(DeformableVMobject):

    def __init__(self, *mobs, side_offset=0, **kwargs):

        v4, v3, v2, v1 = SurroundingRectangle(VGroup(*mobs), buff=0).get_vertices()
        v1 += side_offset * DL
        v3 += side_offset * UR
        p = get_vertices_RECT9(v1, v3)
        DeformableVMobject.__init__(self, *mobs, elem_range=p, type='QUAD9', **kwargs)
        self.nodes_corner = VGroup(self.nodes[0], self.nodes[2], self.nodes[8], self.nodes[6])
        self.nodes_left = VGroup(self.nodes[0], self.nodes[3], self.nodes[6])
        self.nodes_right = VGroup(self.nodes[2], self.nodes[5], self.nodes[8])
        self.nodes_up = VGroup(self.nodes[6], self.nodes[7], self.nodes[8])
        self.nodes_down = VGroup(self.nodes[0], self.nodes[1], self.nodes[2])
        self.node_center = self.nodes[4]


class Dmob_HEXA27(DeformableVMobject):

    def __init__(self, *mobs, elem_range=[-np.ones(3), np.ones(3)], side_offset=0, **kwargs):
        v1, v2 = elem_range[0] + side_offset * (-np.ones(3)), elem_range[1] + side_offset * np.ones(3)
        p = get_vertices_CUBE27(v1, v2)
        DeformableVMobject.__init__(self, *mobs, elem_range=p, type='HEXA27', **kwargs)

        node_id = list(range(27))
        y_n = node_id[0:9]
        y_0 = node_id[9:18]
        y_p = node_id[18:27]
        x_n = [id for id in node_id if (id%9) in [0, 1, 2]]
        x_0 = [id for id in node_id if (id%9) in [3, 4, 5]]
        x_p = [id for id in node_id if (id%9) in [6, 7, 8]]
        z_n = [id for id in node_id if id%3 == 0]
        z_0 = [id for id in node_id if id%3 == 1]
        z_p = [id for id in node_id if id%3 == 2]
        self.nodes_yn = VGroup(*[self.nodes[id] for id in y_n])
        self.nodes_y0 = VGroup(*[self.nodes[id] for id in y_0])
        self.nodes_yp = VGroup(*[self.nodes[id] for id in y_p])
        self.nodes_xn = VGroup(*[self.nodes[id] for id in x_n])
        self.nodes_x0 = VGroup(*[self.nodes[id] for id in x_0])
        self.nodes_xp = VGroup(*[self.nodes[id] for id in x_p])
        self.nodes_zn = VGroup(*[self.nodes[id] for id in z_n])
        self.nodes_z0 = VGroup(*[self.nodes[id] for id in z_0])
        self.nodes_zp = VGroup(*[self.nodes[id] for id in z_p])


class Dmob_CIRCLE9(DeformableVMobject):

    def __init__(self, *mobs, side_offset=0, **kwargs):

        v4, v3, v2, v1 = SurroundingRectangle(VGroup(*mobs), buff=0).get_vertices()
        v1 += side_offset * DL
        v3 += side_offset * UR
        p = get_vertices_CIRCLE9(v1, v3)
        DeformableVMobject.__init__(self, *mobs, elem_range=p, type='QUAD9', **kwargs)
        self.nodes_around = self.nodes[0:8]
        self.node_center = self.nodes[-1]

    
class DeformableGroup(VGroup):

    def __init__(self, *dmobs, **kwargs):

        VGroup.__init__(self, *dmobs, **kwargs)

    def always_update(self):
        for dmob in self:
            dmob.always_update()
        return self

    def stop_update(self):
        for dmob in self:
            dmob.stop_update()
        return self

    # TODO 将一堆DeformableVMobject放进DeformableGroup里面，按照一定的条件和约束来选择控制节点变化，达到对整体的变形效果


class DeformableTube(DeformableGroup):
    CONFIG = {
        'subtube_num': 3,
        'circle_config': {
            'stroke_width': 1.5,
            'stroke_color': BLUE_D,
            'fill_opacity': 0,
        },
        'tube_config': {
            'resolution': (18, 6),
            'checkerboard_colors': None,
            'stroke_color': GREY_E,
            'stroke_width': 2.,
            'fill_opacity': 1,
            'fill_color' :WHITE,
        },
        'angle': TAU,

    }

    def __init__(self, radius=0.5, start=IN * 3, end=OUT * 3, side_offset=0, **kwargs):
        # 此处radius先暂为固定值，后续工作中可将其变为列表或函数
        DeformableGroup.__init__(self, **kwargs)
        self.tube_radius = radius
        self.circle_radius = radius + side_offset

        n = self.subtube_num
        c_list = [(start + (end - start) * i / n / 2)  for i in range(n * 2 + 1)]
        self.control_circle = VGroup(*[Circle(arc_center=c, radius=self.circle_radius, **self.circle_config) for c in c_list])
        self.add(*[self.create_deformable_subtube(c1, c2, c3) for c1, c2, c3 in zip(self.control_circle[0:-2:2], self.control_circle[1:-1:2], self.control_circle[2::2])])


    # def create_deformable_subtube(self, c1, c2, c3, update_nodes=True):
    #     p = get_vertices_TUBE27(c1, c2, c3)
    #     subtube = ParametricSurface(lambda u, v: v * OUT + complex_to_R3(np.exp(1j * u)),
    #                                 u_min=0, u_max=TAU, v_min=-0.5, v_max=0.5, **self.tube_config)
    #     l = get_norm(c3.get_center() - c1.get_center())
    #     subtube.scale([self.tube_radius, self.tube_radius, l]) # .rotate() TODO: 根据朝向旋转合适的角度，这里先假设是x+朝向
    #     subtube.shift((c3.get_center() + c1.get_center())/2)
    #     d_tube = DeformableVMobject(subtube, elem_range=p, type='HEXA27')
    #
    #     if update_nodes:
    #         def update_subtube(tube):
    #             # p9 = get_vertices_from_circle(c1) + [c1.get_center()]
    #             # for p, n in zip(p9, tube.nodes[0:9]):
    #             #     n.move_to(p)
    #             self.move_nodes_onto_circles(tube.nodes[0:9],  c1)
    #             self.move_nodes_onto_circles(tube.nodes[9:18], c2)
    #             self.move_nodes_onto_circles(tube.nodes[18:],  c3)
    #
    #         d_tube.add_updater(update_subtube)
    #     return d_tube

    def create_deformable_subtube(self, c1, c2, c3, update_nodes=True):
        v1 = c1.get_center() + self.circle_radius * DL
        v2 = c3.get_center() + self.circle_radius * UR

        subtube = ParametricSurface(lambda u, v: v * OUT + complex_to_R3(np.exp(1j * u)),
                                    u_min=0, u_max=self.angle, v_min=-0.5, v_max=0.5, **self.tube_config)
        l = get_norm(c3.get_center() - c1.get_center())
        subtube.scale([self.tube_radius, self.tube_radius, l]) # .rotate() TODO: 根据朝向旋转合适的角度，这里先假设是x+朝向
        subtube.shift((c3.get_center() + c1.get_center())/2)
        d_tube = Dmob_HEXA27(subtube, elem_range=(v1, v2))

        # d_tube = DeformableVMobject(subtube, elem_range=get_vertices_CUBE27(v1, v2), type='HEXA27')

        if update_nodes:
            def update_subtube(tube):
                # p9 = get_vertices_from_circle(c1) + [c1.get_center()]
                # for p, n in zip(p9, tube.nodes[0:9]):
                #     n.move_to(p)
                self.move_nodes_by_circle(tube.nodes_zn,  c1)
                self.move_nodes_by_circle(tube.nodes_z0,  c2)
                self.move_nodes_by_circle(tube.nodes_zp,  c3)

            d_tube.add_updater(update_subtube)
        return d_tube

    def move_nodes_onto_circles(self, n9, circle):
        p9 = get_vertices_from_circle(circle) + [circle.get_center()]
        for p, n in zip(p9, n9):
            n.move_to(p)

    def move_nodes_by_circle(self, n9, circle):
        p9 = get_vertices_on_rect_by_circle(circle)
        for p, n in zip(p9, n9):
            n.move_to(p)

    def stop_update(self):
        # TODO 有点问题需要重写该方法
        # for dmob in self:
        #     dmob.remove_updater(dmob.updaters[0])
        return self
