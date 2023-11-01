from pico2d import *
import game_framework

import game_world
from grass import Grass
from boy import Boy
from bird import Bird

# boy = None

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            boy.handle_event(event)

def init():
    global grass
    global boy
    global bird

    running = True

    grass = Grass()
    game_world.add_object(grass, 0)

    boy = Boy()
    game_world.add_object(boy, 1)

    bird1 = Bird()
    bird1.x = 200
    bird1.y = 520
    game_world.add_object(bird1, 0)
    bird2 = Bird()
    bird2.x = 384
    bird2.y = 520
    game_world.add_object(bird2, 0)
    bird3 = Bird()
    bird3.x = 568
    bird3.y = 520
    game_world.add_object(bird3, 0)
    bird4 = Bird()
    bird4.x = 752
    bird4.y = 520
    game_world.add_object(bird4, 0)
    bird5 = Bird()
    bird5.x = 936
    bird5.y = 520
    game_world.add_object(bird5, 0)
    bird6 = Bird()
    bird6.x = 200
    bird6.y = 350
    game_world.add_object(bird6, 0)
    bird7 = Bird()
    bird7.x = 384
    bird7.y = 350
    game_world.add_object(bird7, 0)
    bird8 = Bird()
    bird8.x = 568
    bird8.y = 350
    game_world.add_object(bird8, 0)
    bird9 = Bird()
    bird9.x = 752
    bird9.y = 350
    game_world.add_object(bird9, 0)
    bird10 = Bird()
    bird10.x = 936
    bird10.y = 350
    game_world.add_object(bird10, 0)


def finish():
    game_world.clear()
    pass


def update():
    game_world.update()
    # delay(0.5)


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def pause():
    pass

def resume():
    pass

