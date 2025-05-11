from type.node import *
from type.line import *
from type.touching import *
from tool.database import *
from tool.color import *
from tool.doing import *
from tool.id import *
from tool.xyconverter import *
from tool.filewindow import *
from tool.image.icon import *
from tool.image.png import *
from file.json import *
from file.zip import *
from ui.toollist import *
from ui.event import *
from ui.drawscreen import *
from ui.drawui import *
import pygame
import time

def main():
    try:
        window_settings = read_json('setting/window.json')
        height = window_settings["height"]
        width = window_settings["width"]
        title = window_settings["title"]
        # data_images = window_settings["images"]
    except:
        raise JsonFileError("window.json解析失败")

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption(title)
    pygame.display.set_icon(load_icon('SLCMP.png'))
    pygame.key.stop_text_input()
    clock = pygame.time.Clock()
    strat_time = time.time()
    fps_sum = 0 

    init_toollist()
    init_event()
    init_database(window_settings)
    init_doing()
    init_draw()
    init_filewindow()


    running = True
    while running:
        clock.tick(20)
        # fps = fps_sum / (time.time() - strat_time)
        # fps_sum += 1
        # print("fps:", fps)
        # if fps_sum >= 1000:
        #     fps_sum = 0
        #     strat_time = time.time()

        handle_event(screen)

        screen.fill(hex_to_rgb(getbgcolor()))
        drawalllines(screen)
        drawguideline(screen)
        drawallnodes(screen)
        puttoollist(screen)
        
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
