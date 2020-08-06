from manimlib.imports import *

'''
这个文件中的代码是manim交流群的群友提供的，实际上是由@Elteoremadebeethoven(https://github.com/Elteoremadebeethoven)编写的
from @Elteoremadebeethoven(https://github.com/Elteoremadebeethoven)
'''

def return_random_from_word(word):
    """
    This function receives a TextMobject, 
    obtains its length: 
        len(TextMobject("Some text"))
    and returns a random list, example:

    INPUT: word = TextMobjecT("Hello")
    length = len(word) # 4
    rango = list(range(length)) # [0,1,2,3]

    OUTPUT: [3,0,2,1] # Random list
    """
    rango = list(range(len(word)))
    random.shuffle(rango)
    return rango

def return_random_direction(word):
    """
    This function returns a list of random UP or DOWN:
    [UP,UP,DOWN,UP,DOWN,DOWN,...]
    """
    return [random.choice([UP,DOWN]) for _ in range(len(word))]

def get_random_coord(r_x,r_y,step_x,step_y):
    """
    Given two ranges (a, b) and (c, d), this function returns an 
    intermediate array (x, y) such that "x" belongs to (a, c) 
    and "y" belongs to (b, d).
    """
    range_x = list(range(r_x[0],r_x[1],step_x))
    range_y = list(range(r_y[0],r_y[1],step_y))
    select_x = random.choice(range_x)
    select_y = random.choice(range_y)
    return np.array([select_x,select_y,0])

def return_random_coords(word,r_x,r_y,step_x,step_y):
    """
    This function returns a random coordinate array, 
    given the length of a TextMobject
    """
    rango = range(len(word))
    return [word.get_center() + get_random_coord(r_x,r_y,step_x,step_y) for _ in rango]


class WriteRandom(LaggedStart):
    CONFIG = {
        "lag_ratio":0.1,
        "run_time":2.5,
        "anim_kwargs":{},
        "anim_type":Write
    }
    def __init__(self,text,**kwargs):
        digest_config(self, kwargs)
        super().__init__(*[
            self.anim_type(text[i],**self.anim_kwargs)
            for i in return_random_from_word(text)
        ])

class UnWriteRandom(WriteRandom):
    CONFIG = {
        "anim_kwargs": {
            "rate_func": lambda t: smooth(1-t)
        },
        "remover": True,
    }

class FadeInRandom(WriteRandom):
    CONFIG = {
        "anim_type": FadeIn
    }

class FadeOutRandom(WriteRandom):
    CONFIG = {
        "anim_type": FadeOut
    }

class GrowRandom(WriteRandom):
    CONFIG = {
        "anim_type": GrowFromCenter
    }

class UnGrowRandom(GrowRandom):
    CONFIG = {
        "anim_kwargs": {
            "rate_func": lambda t: smooth(1-t),
        },
        "remover": True,
    }

class FadeInFromRandom(LaggedStart):
    CONFIG = {
        "lag_ratio":0.08,
        "anim_type":FadeInFrom,
        "anim_kwargs":{}
    }
    def __init__(self,text,**kwargs):
        digest_config(self, kwargs)
        super().__init__(*[
            self.anim_type(text[i],d,**self.anim_kwargs)
            for i,d in zip(return_random_from_word(text),return_random_direction(text))
        ])

class FadeOutFromRandom(FadeInFromRandom):
    CONFIG = {
        "anim_type":FadeOutAndShiftDown
    }

class GrowFromRandom(LaggedStart):
    CONFIG = {
        "lag_ratio":0.2,
        "anim_kwargs":{}
    }
    def __init__(self,text,r_x=[-2,3],r_y=[-2,3],step_x=1,step_y=1,**kwargs):
        digest_config(self, kwargs)
        super().__init__(*[
            GrowFromPoint(text[i],d,**self.anim_kwargs)
            for i,d in zip(return_random_from_word(text),return_random_coords(text,r_x,r_y,step_x,step_y))
        ])

class UnGrowFromRandom(GrowFromRandom):
    CONFIG = {
        "anim_kwargs": {
            "rate_func": lambda t: smooth(1-t)
        },
        "remover": True
    }
