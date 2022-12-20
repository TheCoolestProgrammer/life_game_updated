# _______________/============\____________________#

# original idea by https://github.com/MrPr0per

# _______________\============/____________________#

import pygame
import random

pygame.init()
clock = pygame.time.Clock()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
scale = 2
scale_value =0.1
def draw(s):
    for y in range(len(s)):
        for x in range(len(s[y])):
            if s[y][x] == "1":
                pygame.draw.rect(screen,(0,255,0),(x*scale,y*scale,scale,scale))

def game_way(field,base):

    new_field=""
    for i in range(len(field)):
        x="000"
        if i== 0:
            x = "0"+field[0:2]
        elif i == len(field)-1:
            x= field[-2:]+"0"
        else:
            x = field[i-1:i+2]
        new_field += base[x]
    return new_field
def create_field(x):
    rule = str(bin(x))[:1:-1]

    if len(rule)<8:
        rule = rule+ "0"*(8-len(rule))
    base={}
    for i in range(8):
        x = str(bin(i))[2:]
        if len(x)<3:
            x= "0"*(3-len(x))+x
        base[x] =rule[i]

    field=""
    for i in range(int(screen_width//scale)):
        if random.randint(1,10) >5:
            field+="1"
        else:
            field+="0"
    field=[field]
    for i in range(int(screen_height // scale)):
        field.append(game_way(field[-1],base))
    return base,field,field[0]

process_running=True

rule=82
base,field,seed=create_field(rule)
pygame.display.set_caption(f"rule: {rule} seed: {seed}")

while process_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            process_running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                process_running = False
            if event.key == pygame.K_s:
                file = open("saves.txt","a")
                file.write(f"rule: {rule}, seed: {seed}\n")
                file.close()
            if event.key == pygame.K_1:
                scale+=scale_value
            if event.key == pygame.K_2:
                if scale -scale_value >1:
                    scale -= scale_value

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if rule>=2:
                    rule-=1
                    pygame.display.set_caption(f"rule: {rule} seed: {seed}")
                    base, field,seed = create_field(rule)
            if event.button == 2:
                base, field,seed = create_field(rule)
                pygame.display.set_caption(f"rule: {rule} seed: {seed}")

            if event.button == 3:
                if rule <= 254:
                    rule += 1
                    base, field ,seed= create_field(rule)
                    pygame.display.set_caption(f"rule: {rule} seed: {seed}")

    screen.fill((0, 0, 0))
    draw(field)
    pygame.display.update()


