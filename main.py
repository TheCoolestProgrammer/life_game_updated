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

objects = []

normal_picture_size = 500

rotate_angle = 90
angle_coof_sin = screen_height//2
angle_coof_cos = screen_width//2
# points=[]
# glaider gun
points = [(-14.0, -1.0), (-13.0, -1.0), (-13.0, -2.0), (-14.0, -2.0), (-4.0, -1.0), (-4.0, -2.0), (-4.0, -3.0), (-3.0, 0.0), (-3.0, -4.0), (-1.0, -5.0), (-2.0, -5.0), (-2.0, 1.0), (-1.0, 1.0), (0.0, -2.0), (1.0, 0.0), (1.0, -4.0), (2.0, -1.0), (2.0, -2.0), (2.0, -3.0), (3.0, -2.0), (6.0, -1.0), (7.0, -1.0), (7.0, 0.0), (6.0, 0.0), (6.0, 1.0), (7.0, 1.0), (8.0, -2.0), (8.0, 2.0), (10.0, 2.0), (10.0, 3.0), (10.0, -2.0), (10.0, -3.0), (20.0, 0.0), (20.0, 1.0), (21.0, 1.0), (21.0, 0.0)]
game_running=False
frames=0
frames_for_wait=1

def coordinates_changer(x,y):
    # в координаты поля
    global camera_center_y, camera_center_x
    # if x >= camera_center_y:
    new_x = camera_center_x+((x-screen_width//2)/scale)
    # else:
    #     new_x =camera_center_x-((screen_width//2 - x))
    # if y >= camera_center_y:
    new_y = camera_center_y-((y-screen_height//2)/scale)
    # # else:
    #     new_y =((screen_height//2 - y))- camera_center_y
    return(new_x,new_y)

def coordinates_chaneg_in_pygame(x,y):
    global camera_center_y, camera_center_x
    # x= x*scale
    # y = y*scale
    distance_x =x- camera_center_x
    distance_y =y- camera_center_y
    distance_x *=scale
    distance_y*=scale
    # zero_point_x = camera_center_x-screen_width//2
    # zero_point_y = camera_center_y-screen_height//2
    new_x = (screen_width//2 + distance_x)
    new_y = (screen_height//2 - distance_y)
    return(new_x,new_y)
def angle_correct_for_pygame(x,y,angle):
    global angle_coof_sin,angle_coof_cos
    a = math.radians(angle)
    b = math.cos(a)
    c = b*angle_coof_sin
    return(x+c,y+math.sin(math.radians(angle))*angle_coof_cos)
class Object():
    def __init__(self, x,y):
        self.x,self.y = coordinates_changer(x,y)
        # self.x_for_draw,self.y_for_draw = x,y
        self.image= pygame.image.load("planet.png")
        self.image = pygame.transform.scale(self.image,(normal_picture_size/scale,normal_picture_size/scale))

def scaling():
    global scale, objects, func_coords
    for object in objects:
        object.image = pygame.image.load("planet.png")
        object.image = pygame.transform.scale(object.image, (normal_picture_size *(scale/100), normal_picture_size *(scale/100)))
    func_coords = create_func()
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
        # print(x,y)
        if screen_width >x >0 and screen_height>y>0:

            pygame.draw.rect(screen, (255,255,255),(x,y,width,height))
def events_check():
    global process_running, scale, scale_value, objects,camera_center_x,camera_center_y,width_coof,height_coof,game_running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            process_running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                process_running = False
            elif event.key == pygame.K_1:
                # if scale >= scale_value and scale_value < 1:
                #     scale_value = scale_value * 10
                scale +=scale_value
                # if scale > 1.1:
                #     scale = round(scale)
                scale=round(scale,2)

                # scale = round(scale, 2)
                scaling()
            elif event.key == pygame.K_2:
                # if scale <= scale_value:
                #     scale_value = scale_value / 10
                if scale - scale_value >= scale_value:

                    scale -=scale_value
                    scale=round(scale,2)
                # if scale > 1.1:
                #     scale = round(scale)

                # scale = round(scale,2)
                scaling()
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
    # print(pos)
    # pos = pygame.mouse.get_pos()
    if keys[0]:

        camera_center_x-=(camera_center_x-pos[0])/2
        camera_center_y-=(camera_center_y-pos[1])/2
        # if pos[0]<screen_width//2:
        #     camera_center_x+=speed
        # else:
        #     camera_center_x-=speed

        scaling()

    if keys2[pygame.K_1]:
        # if scale >= scale_value and scale_value < 1:
        #     scale_value = scale_value* 10
        scale += scale_value
        scale = round(scale,2)

        # if scale >1.1:
        #     scale = round(scale)
        scaling()
    if keys2[pygame.K_2]:
        # if scale <= scale_value:
        #     scale_value = scale_value /10
        if scale - scale_value >= scale_value:
            scale -= scale_value
            scale = round(scale,2)

        # if scale > 1.1:
        #     scale = round(scale)
        # scale = round(scale, 2)
        scaling()
def test_camera_draw():
    global rotate_angle
    font = pygame.font.SysFont("Times New Roman", int(scale)*2)

    # for x in range(0,screen_width):
    #     if round(coordinates_changer(x,0)[0],2) % 5 ==0:
    #         pygame.draw.line(screen, (0, 255, 0), (x, 0), (x, screen_height), 1)
    #         surface = font.render(str(round(coordinates_changer(x, 0)[0],2) ), False, (255, 255, 255))
    #         screen.blit(surface, (x, 0))
    # for y in range(0,screen_height):
    #     if round(coordinates_changer(0,y)[1],2) % 5 ==0:
    #         pygame.draw.line(screen,(0,255,0),(0,y),(screen_width,y),1)
    #         surface = font.render(str(round(-coordinates_changer(0,y)[1],2)), False, (255, 255, 255))
    #         screen.blit(surface, (0,y))

    # |____________________for rotating_______________________|

    x =camera_center_x-(camera_center_x%5)
    y =camera_center_y-(camera_center_y%5)
    field_color=(0,150,0)
    # counter=x
    # angle =rotate_angle
    # while counter<=coordinates_changer(screen_width,0)[0]:
    #     pos = coordinates_chaneg_in_pygame(counter,0)[0]
    #     x1= angle_correct_for_pygame(pos,0,angle)[0]
    #     x2= angle_correct_for_pygame(pos,0,180+angle)[0]
    #
    #     pygame.draw.line(screen,field_color,(x1,0),
    #                      (x2,screen_height),2)
    #     surface = font.render(str(counter), False, (255, 255, 255))
    #     screen.blit(surface, (pos,0))
    #     counter+= 5
    # counter = x
    # angle = rotate_angle
    # if angle%360>180:
    #     angle=-angle
    # while counter >= coordinates_changer(0, 0)[0]:
    #     pos = coordinates_chaneg_in_pygame(counter, 0)[0]
    #     x1 = angle_correct_for_pygame(pos, 0, angle)[0]
    #     x2 = angle_correct_for_pygame(pos, 0, 180 + angle)[0]
    #
    #     pygame.draw.line(screen, field_color, (x1, 0),
    #                      (x2, screen_height), 2)
    #     surface = font.render(str(counter), False, (255, 255, 255))
    #     screen.blit(surface, (pos, 0))
    #     counter -= 5
    # counter=y
    # while counter<=coordinates_changer(screen_width,0)[0]:
    #     pos = coordinates_chaneg_in_pygame(0,counter)[1]
    #     y1= angle_correct_for_pygame(0,pos,270+angle)[1]
    #     y2= angle_correct_for_pygame(0,pos,90+angle)[1]
    #     pygame.draw.line(screen,field_color,(0,y1),
    #                      (screen_width,y2),2)
    #     surface = font.render(str(counter), False, (255, 255, 255))
    #     screen.blit(surface, (pos,0))
    #     counter+= 5
    # counter = y
    # while counter >= coordinates_changer(0, screen_height)[1]:
    #     pos = coordinates_chaneg_in_pygame(0, counter)[1]
    #     y1 = angle_correct_for_pygame(0, pos, 270 + angle)[1]
    #     y2 = angle_correct_for_pygame(0, pos, 90 + angle)[1]
    #     pygame.draw.line(screen, field_color, (0, y1),
    #                      (screen_width, y2), 2)
    #     surface = font.render(str(counter), False, (255, 255, 255))
    #     screen.blit(surface, (pos, 0))
    #     counter -= 5


    zero_x = round(coordinates_chaneg_in_pygame(0,0)[0],1)
    zero_y = round(coordinates_chaneg_in_pygame(0,0)[1],1)
    # print(zero_x)
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
    #

def create_func():
    func_coords=[]
    x=0
    way = 1
    # for sinusoida

    frequency=10
    high_coof = 10

    # for line func

    k = 1
    b=0
    # while coordinates_changer(x,0)[0] <= coordinates_changer(screen_width,0)[0]:
    #     x2 = coordinates_changer(x,0)[0]
    #     # sinusoida
    #     # y = math.cos(frequency*math.radians(x2))*high_coof
    #
    #     #parabola
    #     # y = x2**2
    #
    #     # line func
    #     # y = k*x2+b
    #
    #     # hyperbola
    #     if x2+2 !=0:
    #         y = 1/(2+x2)+5
    #
    #     # something
    #     # if x2 !=0 and -100<x2<1000:
    #         # y = 5*x2-x2**2+1/x2
    #         # y = math.sin((1/x2))**x2
    #
    #
    #         func_coords.append((x2,y))
    #     x+=way
    x = coordinates_changer(0,0)[0]
    x_end=coordinates_changer(screen_width,0)[0]
    while x<x_end:
        y = x**2
        func_coords.append((x, y))
        x+=1/scale
    return func_coords
def draw_func():
    global func_coords
    rotate_angle=0
    for i in range(1,len(func_coords)):
        scaled_cords= coordinates_chaneg_in_pygame(func_coords[i-1][0],func_coords[i-1][1])
        scaled_cords2= coordinates_chaneg_in_pygame(func_coords[i][0],func_coords[i][1])
        if type(scaled_cords[0])==float and type(scaled_cords[1])==float and type(scaled_cords2[0])== float and type(scaled_cords2[1])== float:
            pygame.draw.line(screen,(255,0,0),(scaled_cords[0],scaled_cords[1]),(scaled_cords2[0],scaled_cords2[1]),5)
            # pos1 = angle_correct_for_pygame(scaled_cords[0], scaled_cords[1], rotate_angle)
            # pos2 = angle_correct_for_pygame(scaled_cords2[0], scaled_cords2[1], rotate_angle + 180)
            # pygame.draw.line(screen,(255,0,0),(pos1[0],pos1[1]),(pos2[0],pos2[1]),5)
            # func_coords[i][0] = pos2[0]
            # func_coords[i][1] = pos2[1]

def draw_image():
    # a =  my_image.size(0)
    begin_point_x = coordinates_chaneg_in_pygame(-my_image.size[0]//2,0)[0]
    begin_point_y = coordinates_chaneg_in_pygame(0,my_image.size[1]//2)[1]
    res = coordinates_chaneg_in_pygame(1,1)
    res2 = coordinates_chaneg_in_pygame(0,0)
    len_x = res[0]-res2[0]
    len_y = res2[1]-res[1]
    len_x = round(len_x+width_coof*scale)
    y = height_coof*scale
    len_y = round(len_y+y)
    for x in range(len(my_pixels_array[0])):
        for y in range(len(my_pixels_array)):
            # a=coordinates_chaneg_in_pygame(begin_point_x + x, 0)[0]
            # b=coordinates_chaneg_in_pygame(0, begin_point_y + y)[1]
            # x=begin_point_x+x*len_x
            xx= begin_point_x+x*len_x
            yy=y*len_y
            yy = begin_point_y+yy
            pygame.draw.rect(screen,(my_pixels_array[y][x]),(xx,
                                                         yy,
                                                         len_x,len_y))
def drawing():
    screen.fill((0, 0, 0))
    draw_cells()
    test_camera_draw()
    # draw_func()
    # draw_image()
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
        # print(points)
        # print(scale)
        # rotate_angle+=1
        # print(rotate_angle)


if __name__ == '__main__':
    func_coords = create_func()
    width_coof=0
    height_coof=0

    # from PIL import Image
    # my_image = Image.open("valakas.jpg")
    # image_pixels = my_image.load()
    # my_pixels_array = []
    # for y in range(my_image.size[1]):
    #
    #     a = []
    #     for x in range(my_image.size[0]):
    #         a.append(image_pixels[x,y])
    #     my_pixels_array.append(a)


    mainloop()