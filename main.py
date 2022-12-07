import pygame
import math
pygame.init()
clock = pygame.time.Clock()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width,screen_height))

scale = 10
scale_value = 0.1

camera_center_x = 0
camera_center_y = 0
process_running = True

# points=[]
# glaider gun
points = [(-14.0, -1.0), (-13.0, -1.0), (-13.0, -2.0), (-14.0, -2.0), (-4.0, -1.0), (-4.0, -2.0), (-4.0, -3.0), (-3.0, 0.0), (-3.0, -4.0), (-1.0, -5.0), (-2.0, -5.0), (-2.0, 1.0), (-1.0, 1.0), (0.0, -2.0), (1.0, 0.0), (1.0, -4.0), (2.0, -1.0), (2.0, -2.0), (2.0, -3.0), (3.0, -2.0), (6.0, -1.0), (7.0, -1.0), (7.0, 0.0), (6.0, 0.0), (6.0, 1.0), (7.0, 1.0), (8.0, -2.0), (8.0, 2.0), (10.0, 2.0), (10.0, 3.0), (10.0, -2.0), (10.0, -3.0), (20.0, 0.0), (20.0, 1.0), (21.0, 1.0), (21.0, 0.0)]
game_running=False
frames=0
frames_for_wait=1

def coordinates_changer(x,y):
    # в координаты поля
    global camera_center_y, camera_center_x
    new_x = camera_center_x+((x-screen_width//2)/scale)
    new_y = camera_center_y-((y-screen_height//2)/scale)
    return(new_x,new_y)

def coordinates_chaneg_in_pygame(x,y):
    global camera_center_y, camera_center_x
    distance_x =x- camera_center_x
    distance_y =y- camera_center_y
    distance_x *=scale
    distance_y*=scale
    new_x = (screen_width//2 + distance_x)
    new_y = (screen_height//2 - distance_y)
    return(new_x,new_y)

def get_field_cell(x,y):
    x = (coordinates_changer(x,0)[0])//5
    y = (coordinates_changer(0,y)[1])//5
    return (x,y)
def draw_cells():
    width1 = coordinates_chaneg_in_pygame(5, 0)[0]
    width2 = coordinates_chaneg_in_pygame(0, 0)[0]
    width = width1-width2
    height = width
    for pos in points:
        x = coordinates_chaneg_in_pygame(pos[0]*5,0)[0]
        y = coordinates_chaneg_in_pygame(0,(pos[1]+1)*5)[1]
        if screen_width >x >0 and screen_height>y>0:
            pygame.draw.rect(screen, (255,255,255),(x,y,width,height))
def events_check():
    global process_running, scale, scale_value, camera_center_x,camera_center_y,game_running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            process_running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                process_running = False
            elif event.key == pygame.K_1:
                scale +=scale_value
                scale=round(scale,2)

            elif event.key == pygame.K_2:
                if scale - scale_value >= scale_value:
                    scale -=scale_value
                    scale=round(scale,2)
            elif event.key == pygame.K_q:
                game_running= not game_running
                frames=0
        elif event.type== pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
                pos = pygame.mouse.get_pos()
                cell_pos = get_field_cell(pos[0],pos[1])
                if cell_pos in points:
                    points.remove(cell_pos)
                else:
                    points.append(cell_pos)
    keys = pygame.mouse.get_pressed()
    keys2= pygame.key.get_pressed()

    pos = coordinates_changer(*pygame.mouse.get_pos())
    if keys[0]:

        camera_center_x-=(camera_center_x-pos[0])/2
        camera_center_y-=(camera_center_y-pos[1])/2

    if keys2[pygame.K_1]:
        scale += scale_value
        scale = round(scale,2)
    if keys2[pygame.K_2]:
        if scale - scale_value >= scale_value:
            scale -= scale_value
            scale = round(scale,2)
def test_camera_draw():
    global rotate_angle
    font = pygame.font.SysFont("Times New Roman", int(scale)*2)
    x =camera_center_x-(camera_center_x%5)
    y =camera_center_y-(camera_center_y%5)
    field_color=(0,150,0)

    zero_x = round(coordinates_chaneg_in_pygame(0,0)[0],1)
    zero_y = round(coordinates_chaneg_in_pygame(0,0)[1],1)
    
    pygame.draw.line(screen,(0,0,255),(zero_x,0),(zero_x,screen_height),5)
    counter = x
    while counter >= coordinates_changer(0, 0)[0]:
        pos = coordinates_chaneg_in_pygame(counter, 0)[0]
        pygame.draw.line(screen, field_color, (pos, 0), (pos, screen_height), 2)
        surface = font.render(str(counter), False, (255, 255, 255))
        screen.blit(surface, (pos, 0))
        counter -= 5
    counter = x
    
    while counter <= coordinates_changer(screen_width,0)[0]:
        pos = coordinates_chaneg_in_pygame(counter,0)[0]
        pygame.draw.line(screen,field_color, (pos,0), (pos,screen_height), 2)
        surface = font.render(str(counter), False, (255, 255, 255))
        screen.blit(surface, (pos,0))
        counter += 5
    counter = y
    
    while counter <= coordinates_changer(0, 0)[1]:
        pos = coordinates_chaneg_in_pygame(0,counter)[1]
        pygame.draw.line(screen, field_color, (0,pos), (screen_width,pos), 2)
        surface = font.render(str(counter), False, (255, 255, 255))
        screen.blit(surface, (0,pos))
        counter += 5
    pygame.draw.line(screen,(0,0,255),(0,zero_y),(screen_width,zero_y),5)
    counter = y
    
    while counter >= coordinates_changer(0, screen_height)[1]:
        pos = coordinates_chaneg_in_pygame(0, counter)[1]
        pygame.draw.line(screen,field_color, (0, pos), (screen_width, pos), 2)
        surface = font.render(str(counter), False, (255, 255, 255))
        screen.blit(surface, (0,pos))
        counter -= 5

def drawing():
    screen.fill((0, 0, 0))
    draw_cells()
    test_camera_draw()
    pygame.display.update()
def game_way(points):
    new_points= []

    # looking for live
    for i in points:
        counter=0
        for x in range(-1,2):
            if (i[0]+x,i[1]+1) in points:
                counter+=1
            if (i[0] + x, i[1] - 1) in points:
                counter += 1
        if (i[0]-1, i[1]) in points:
            counter += 1
        if (i[0] +1, i[1]) in points:
            counter += 1
        if 1<counter<4:
            if i not in new_points:
                new_points.append(i)
    #looking for dead
    for i in points:

        for y1 in range(-1,2):
            for x1 in range(-1,2):
                if x1==0 and y1==0:
                    continue
                if (i[0]+x1,i[1]-y1) in points:
                    continue
                counter = 0
                for y2 in range(-1,2):
                    for x2 in range(-1,2):
                        if x2 == 0 and y2==0:
                            continue

                        if (i[0]+x1+x2,i[1]-y1-y2) in points:
                            counter+=1
                if counter ==3:
                    if (i[0]+x1,i[1]-y1) not in new_points:
                        new_points.append((i[0]+x1,i[1]-y1))
    return new_points

def mainloop():
    global height_coof,rotate_angle,frames,frames_for_wait,points
    while process_running:
        events_check()
        drawing()
        print(points)
        if game_running:
            frames+=1
            if frames==frames_for_wait:
                frames=0
                points = game_way(points)

        pygame.time.delay(20)


if __name__ == '__main__':

    mainloop()
