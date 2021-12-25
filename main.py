import pygame
import sys

# initialize the pygame

pygame.init()
clock = pygame.time.Clock()
# creating screen
screen = pygame.display.set_mode((800, 600))
base_font = pygame.font.Font(None, 32)
user_text = ''
user_text2 = ''
user_text3 = ''
# creating rectangle1
input_rect = pygame.Rect(680, 10, 100, 32)
color_active = pygame.Color('lightskyblue3')
color_passive = pygame.Color('gray15')
color = color_passive
active = False

# creating rectangle2
input_rect2 = pygame.Rect(680, 60, 100, 32)
color_active2 = pygame.Color('lightskyblue3')
color_passive2 = pygame.Color('gray15')
color2 = color_passive2
active2 = False

# creating rectangle3
input_rect3 = pygame.Rect(680, 110, 100, 32)
color_active3 = pygame.Color('lightskyblue3')
color_passive3 = pygame.Color('gray15')
color3 = color_passive3
active3 = False

# background
background = pygame.image.load('ϴ.png')

# title and icon
pygame.display.set_caption("Physics Simulator")
icon = pygame.image.load('gravity-3.png')
pygame.display.set_icon(icon)

# game loop
running = True
while running:
    # rgb- red ,green ,blue
    screen.fill((0, 0, 0))
    # background
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = True

            else:
                active = False

        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode

        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect2.collidepoint(event.pos):
                active2 = True
            else:
                active2 = False

        if event.type == pygame.KEYDOWN:
            if active2:
                if event.key == pygame.K_BACKSPACE:
                    user_text2 = user_text2[:-1]
                else:
                    user_text2 += event.unicode

        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect3.collidepoint(event.pos):
                active3 = True
            else:
                active3 = False

        if event.type == pygame.KEYDOWN:
            if active3:
                if event.key == pygame.K_BACKSPACE:
                    user_text3 = user_text3[:-1]
                else:
                    user_text3 += event.unicode

    if active:
        color = color_active
    else:
        color = color_passive

    if active2:
        color2 = color_active2
    else:
        color2 = color_passive2

    if active3:
        color3 = color_active3
    else:
        color3 = color_passive3

    pygame.draw.rect(screen, color, input_rect, 2)
    pygame.draw.rect(screen, color, input_rect2, 2)
    pygame.draw.rect(screen, color, input_rect3, 2)

    text_surface = base_font.render(user_text, True, (0, 0, 0))
    text_surface2 = base_font.render(user_text2, True, (0, 0, 0))
    text_surface3 = base_font.render(user_text3, True, (0, 0, 0))

    # linking input text to rectangle and printing and making it look good
    screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
    screen.blit(text_surface2, (input_rect2.x + 5, input_rect2.y + 5))
    screen.blit(text_surface3, (input_rect3.x + 5, input_rect3.y + 5))
    #     limiting the no.of characters input and stopping the text from leaving box.
    input_rect.w = max(100, text_surface.get_width() + 10)
    input_rect2.w = max(100, text_surface2.get_width() + 10)
    input_rect3.w = max(100, text_surface3.get_width() + 10)
    # headings
    mass_heading = base_font.render('mass:', True, (0, 0, 0))
    screen.blit(mass_heading, (610, 15))
    Angle_heading = base_font.render('angle:', True, (0, 0, 0))
    screen.blit(Angle_heading, (605, 65))
    Length_heading = base_font.render('length:', True, (0, 0, 0))
    screen.blit(Length_heading, (595, 115))
    #  updating screen
    pygame.display.update()

    clock.tick(60)
