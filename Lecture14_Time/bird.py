import game_world
import game_framework
from pico2d import get_time, load_image, load_font, clamp
import random

PIXEL_PER_METER = (10.0 / 0.3) # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0 # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0/TIME_PER_ACTION
FRAMES_PER_ACTION = 8

FRAMES_PER_ACTION = FRAMES_PER_ACTION * ACTION_PER_TIME

class Bird:
    def __init__(self):
        self.x, self.y = 400, 500
        self.frame = random.randint(0, 13)
        self.action = self.frame // 5
        self.face_dir = 1
        self.dir = 1
        self.image = load_image('bird_animation.png')

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 13
        self.action = int(self.frame) // 5
        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
        if self.dir == 1 and self.x >=1508:
            self.dir = -1
        elif self.dir == -1 and self.x <= 92:
            self.dir = 1
        pass
    def draw(self):
        if self.dir == 1:
            self.image.clip_draw(int(self.frame % 3) * 184, 340-(self.action * 167), 183, 167, self.x, self.y)
        elif self.dir == -1:
            self.image.clip_composite_draw(int(self.frame % 3) * 184, 340-(self.action * 167), 183, 167, 0, 'h', self.x, self.y, 184, 170)

    def set_position(self, _x, _y):
        self.x = _x
        self.y = _y
