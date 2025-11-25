import pygame
import random 
import math

pygame.init()
keith_face = ""
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
keith_right = pygame.transform.scale(pygame.image.load("Keith_right.jpg"), (100, 100))
keith_left = pygame.transform.flip(keith_right, True, False)

cookie = pygame.transform.scale(pygame.image.load("Cookie.png"), (45, 45))
half_cookie = pygame.transform.scale(pygame.image.load("Half_Cookie.png"), (45, 45))


cookies = []
num_cookies = 100
for i in range(num_cookies):
    cookie_data = {
        "x": 0.0,
        "y": 0.0,
        "vx": 0.0,
        "vy": 0.0,
        "spawned": False,
        "eaten": 2,
    }
    cookies.append(cookie_data)
cookie_spawn_event = pygame.USEREVENT + 1
pygame.time.set_timer(cookie_spawn_event, 6000)

i = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == cookie_spawn_event:
            if cookies[i]["spawned"] == False:
                x_start = random.randint(1, 1279)
                y_start = random.randint(1, 719)
                cookies[i]["x"] = x_start
                cookies[i]["y"] = y_start
                cookies[i]["spawned"] = True
                i += 1
                break

    screen.fill("purple")

    if keith_face == "left":
        screen.blit(keith_left, (player_pos))
    elif keith_face == "right":
        screen.blit(keith_right, (player_pos))
    else:
        screen.blit(keith_right, (player_pos))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
        keith_face = "up"
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
        keith_face = "left"
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
        keith_face = "down"
    if keys[pygame.K_d]: 
        player_pos.x += 300 * dt
        keith_face = "right"



    for cookie_data in cookies:
        if cookie_data["spawned"] and cookie_data["eaten"] != 0:
            if cookie_data["eaten"] == 2:
                screen.blit(cookie, (cookie_data["x"], cookie_data["y"]))
            elif cookie_data["eaten"] == 1:
                screen.blit(half_cookie, (cookie_data["x"], cookie_data["y"]))
            if cookie_data["vx"] == 0 and cookie_data["vy"] == 0:
                cookie_data["vx"] = random.randint(1, 100) * math.cos(math.radians(random.randint(0, 360)))
                cookie_data["vy"] = random.randint(1, 100) * math.sin(math.radians(random.randint(0, 360)))
            if cookie_data["vx"] != 0 and cookie_data["vy"] != 0:
                cookie_data["x"] += cookie_data["vx"] * dt
                cookie_data["y"] += cookie_data["vy"] * dt
            if cookie_data["x"] >= 1280 or cookie_data["x"] <= 0:
                cookie_data["vx"] *= -1
            if cookie_data["y"] >= 720 or cookie_data["y"] <= 0:
                cookie_data["vy"] *= -1

            if abs(cookie_data["x"] - player_pos.x) <= 50 and abs(cookie_data["y"] - player_pos.y) <= 50:
                if "overlap_time" not in cookie_data:
                    cookie_data["overlap_time"] = 0
                cookie_data["overlap_time"] += dt
                if cookie_data["eaten"] == 2 and cookie_data["overlap_time"] > .5:
                    cookie_data["eaten"] = 1
                    cookie_data["overlap_time"] = 0
                elif cookie_data["eaten"] == 1 and cookie_data["overlap_time"] > .5:
                    cookie_data["eaten"] = 0
                    cookie_data["overlap_time"] = 0
            else:
                cookie_data["overlap_time"] = 0
        

            


    pygame.display.flip()

    dt = clock.tick(60) / 1000

    
pygame.quit
        

            


pygame.display.flip()

dt = clock.tick(60) / 1000

    
pygame.quit