
import pygame
import sys
from button import Button
from pygame import mixer
from fighter import Fighter
from moviepy.editor import VideoFileClip

pygame.init()


# Define the backgrounds for each field
FIELD_1_BG = pygame.image.load("assets/images/background/mk3-stage-soul-chamber00.jpg")
FIELD_2_BG = pygame.image.load("assets/images/background/background2.jpg")
FIELD_3_BG = pygame.image.load("assets/images/background/background3.jpg")

CURRENT_BACKGROUND = FIELD_2_BG



pygame.mixer.music.load("assets/audio/menu_music.mp3")
pygame.mixer.music.set_volume(0.5)


SCREEN = pygame.display.set_mode((1600, 900))
pygame.display.set_caption("Warrior's Wrath")

BG = pygame.image.load("assets/l6Xgvsw.jpg")



def fade_transition(screen, duration=400):
    fade_surface = pygame.Surface((screen.get_width(), screen.get_height()))
    fade_surface.fill((0, 0, 0))
    for alpha in range(0, 255, 5):
        fade_surface.set_alpha(alpha)
        screen.blit(fade_surface, (0, 0))
        pygame.display.flip()
        pygame.time.delay(duration // 70)  # Adjust the delay for the desired transition speed


def get_font(size):
    return pygame.font.Font("assets/ChrustyRock-ORLA.ttf", size)

def load_main_menu_music():
    pygame.mixer.music.load("assets/audio/menu_music.mp3")
    pygame.mixer.music.set_volume(0.5)

def play_main_menu_music():
    pygame.mixer.music.play(-1)  # -1 makes the music loop indefinitely

def stop_main_menu_music():
    pygame.mixer.music.stop()

def play_intro_video():
    intro_video_path = "assets/gameintro1111.mp4"  # Replace with the actual path to your video
    intro_clip = VideoFileClip(intro_video_path)
    intro_clip.preview(fps=60, audio_fps=22050, audio_buffersize=3000, audio_nbytes=2, audio=True, fullscreen=True)

def play_main_menu():
    fade_transition(SCREEN)
    load_main_menu_music()
    play_main_menu_music()
    main_menu()

def play():
    choose_fighter()

def display_selected_fighters(selected_fighter_1, selected_fighter_2):
    SELECTED_FIGHTER_FONT = pygame.font.Font("assets/fonts/turok.ttf", 40)

    # Display selected fighter for Player 1
    if selected_fighter_1 is not None:
        fighter_1_text = SELECTED_FIGHTER_FONT.render("Player 1: " + selected_fighter_1, True, (255, 255, 255))
        fighter_1_rect = fighter_1_text.get_rect(center=(800, 100))
        SCREEN.blit(fighter_1_text, fighter_1_rect)

    # Display selected fighter for Player 2
    if selected_fighter_2 is not None:
        fighter_2_text = SELECTED_FIGHTER_FONT.render("Player 2: " + selected_fighter_2, True, (255, 255, 0))
        fighter_2_rect = fighter_2_text.get_rect(center=(640, 100))
        SCREEN.blit(fighter_2_text, fighter_2_rect)

    pygame.display.update()
def choose_fighter():
    selected_fighter_1 = None
    selected_fighter_2 = None

    while selected_fighter_1 is None or selected_fighter_2 is None:
        FIGHTER_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        FIGHTER_TEXT = get_font(45).render("Choose Your Fighters!", True, "White")
        FIGHTER_RECT = FIGHTER_TEXT.get_rect(center=(800, 160))
        SCREEN.blit(FIGHTER_TEXT, FIGHTER_RECT)

        WARRIOR_BUTTON = Button(image=pygame.image.load("assets/images/warrior/warrioricon.png"), pos=(300, 300),
                                text_input="warrior", font=get_font(75), base_color="#d7fcd4",
                                hovering_color="White")
        Samurai_BUTTON = Button(image=pygame.image.load("assets/images/Samurai/samuraiIcon.png"), pos=(1350, 300),
                               text_input="Samurai", font=get_font(75), base_color="#d7fcd4",
                               hovering_color="White")

        WomenHunter_BUTTON = Button(image=pygame.image.load("assets/images/womenhunter/womenhuntericon.png"), pos=(300, 700),
                                text_input="WomenHunter", font=get_font(50), base_color="#d7fcd4",
                                hovering_color="White")

        SUBZERO_BUTTON = Button(image=pygame.image.load("assets/images/sub-ZERO/newSUB-zero-icon.png"), pos=(1350, 700),
                                 text_input="Sub-zero", font=get_font(75), base_color="#d7fcd4", hovering_color="White")



        BACK_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(800, 800),
                             text_input="Back", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        for button in [WARRIOR_BUTTON, Samurai_BUTTON, BACK_BUTTON  ,WomenHunter_BUTTON,SUBZERO_BUTTON]:
            button.changeColor(FIGHTER_MOUSE_POS)
            button.update(SCREEN)

        display_selected_fighters(selected_fighter_1, selected_fighter_2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if WARRIOR_BUTTON.checkForInput(FIGHTER_MOUSE_POS):
                    if selected_fighter_1 is None:
                        selected_fighter_1 = "warrior"
                    elif selected_fighter_2 is None:
                        selected_fighter_2 = "warrior"
                elif Samurai_BUTTON.checkForInput(FIGHTER_MOUSE_POS):
                    if selected_fighter_1 is None:
                        selected_fighter_1 = "Samurai"
                    elif selected_fighter_2 is None:
                        selected_fighter_2 = "Samurai"
                elif WomenHunter_BUTTON.checkForInput(FIGHTER_MOUSE_POS):
                    if selected_fighter_1 is None:
                        selected_fighter_1 = "WomenHunter"
                    elif selected_fighter_2 is None:
                        selected_fighter_2 = "WomenHunter"
                elif SUBZERO_BUTTON.checkForInput(FIGHTER_MOUSE_POS):
                    if selected_fighter_1 is None:
                        selected_fighter_1 = "Sub-zero"
                    elif selected_fighter_2 is None:
                        selected_fighter_2 = "Sub-zero"
                elif BACK_BUTTON.checkForInput(FIGHTER_MOUSE_POS):
                    fade_transition(SCREEN)

                    choose_field_menu()

        if selected_fighter_1 is not None and selected_fighter_2 is not None:
            stop_main_menu_music()
            fade_transition(SCREEN)
            play_with_fighters(selected_fighter_1, selected_fighter_2)


# Define the pause menu text and font
pause_text_font = get_font(100)
pause_text = pause_text_font.render("Game Paused", True, (255, 0, 0))
pause_text_rect = pause_text.get_rect(center=(SCREEN.get_width() // 2, SCREEN.get_height() // 2))

# Create a surface for the pause menu
pause_menu_surface = pygame.Surface((SCREEN.get_width(), SCREEN.get_height()), pygame.SRCALPHA)
pause_menu_surface.fill((0, 0, 0, 128))  # Transparent black background

# Variable to keep track of the game's pause state
is_paused = False

# Global variable to track the pause state of the music
is_music_paused = False

def play_with_fighters(selected_fighter_1, selected_fighter_2):
    global is_paused, is_music_paused  # Declare variables as global

    is_paused = False  # Variable to keep track of the game's pause state
    pause_menu_surface = pygame.Surface((SCREEN.get_width(), SCREEN.get_height()), pygame.SRCALPHA)
    pause_menu_surface.fill((0, 0, 0, 128))  # Transparent black background
    pygame.init()

    while True:


        # create game window
        SCREEN_WIDTH = 1600
        SCREEN_HEIGHT = 900

        # define timer variables
        timer_font = pygame.font.Font("assets/fonts/turok.ttf", 50)
        timer_value = 30  # initial timer value in seconds
        timer_cooldown = 1000  # timer cooldown in milliseconds
        timer_last_update = pygame.time.get_ticks()
        round_over_delay = 3000

        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Warrior's Wrath")

        # set framerate
        clock = pygame.time.Clock()
        FPS = 60

        # define colours
        RED = (255, 0, 0)
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)

        # define game variables
        intro_count = 0
        last_count_update = pygame.time.get_ticks()
        score = [0, 0]  # player scores. [P1, P2]
        round_over = False
        #ROUND_OVER_COOLDOWN = 2000

        # define fighter variables
        WARRIOR_SIZE = 250
        WARRIOR_SCALE = 3
        WARRIOR_OFFSET = [112, 100]
        WARRIOR_DATA = [WARRIOR_SIZE, WARRIOR_SCALE, WARRIOR_OFFSET]

        Samurai_SIZE = 250
        Samurai_SCALE = 3
        Samurai_OFFSET = [112, 100]
        Samurai_DATA = [Samurai_SIZE, Samurai_SCALE, Samurai_OFFSET]

        subzero_SIZE = 250
        subzero_SCALE = 1.75
        subzero_OFFSET = [112, 50]
        subzero_DATA = [subzero_SIZE, subzero_SCALE, subzero_OFFSET]

        WomenHunter_SIZE = 250
        WomenHunter_SCALE = 3
        WomenHunter_OFFSET = [112, 95]
        WomenHunter_DATA = [WomenHunter_SIZE, WomenHunter_SCALE, WomenHunter_OFFSET]

        #HUNTRESS_SIZE = 162
        #HUNTRESS_SCALE = 4
        #HUNTRESS_OFFSET = [112, 59]
        #HUNTRESS_DATA = [HUNTRESS_SIZE, HUNTRESS_SCALE, HUNTRESS_OFFSET]

        # load music and sounds
        pygame.mixer.music.load("assets/audio/game_music.mp3")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1, 0.0, 5000)

        sword_fx = pygame.mixer.Sound("assets/audio/sword.wav") #for warrior
        sword_fx.set_volume(0.5)
        magic_fx = pygame.mixer.Sound("assets/images/Samurai/samurai-sword.mp3")
        magic_fx.set_volume(0.75)
        spear_fx = pygame.mixer.Sound("assets/images/womenhunter/heavy-spear-hammer-large-[AudioTrimmer.com].wav")
        spear_fx.set_volume(0.75)
        punch_fx = pygame.mixer.Sound("assets/images/sub-ZERO/punch-sound-effects-28649-[AudioTrimmer.com].mp3")
        punch_fx.set_volume(0.75)

        victory_sound = pygame.mixer.Sound("assets/audio/victory sound.mp3")
        victory_sound.set_volume(0.5)
        # load background image


        # load spritesheets
        warrior_sheet = pygame.image.load("assets/images/warrior/Sprites/warriorNEW.png").convert_alpha()
        Samurai_sheet = pygame.image.load("assets/images/Samurai/Sprites/Samurai.png").convert_alpha()
        subzero_sheet = pygame.image.load("assets/images/sub-ZERO/FINALSUBZERO.png").convert_alpha()
        WomenHunter_sheet = pygame.image.load("assets/images/Samurai/Sprites/hunter.png").convert_alpha()
        #Huntress_sheet = pygame.image.load("assets/images/Huntress/Sprites/Character/Huntressv4.png").convert_alpha()

        # load vicory image
        victory_img = pygame.image.load("assets/images/icons/victory.png").convert_alpha()

        # define number of steps in each animation
        WARRIOR_ANIMATION_STEPS = [4, 8, 2, 4, 4, 3, 7]
        Samurai_ANIMATION_STEPS = [8, 6, 2, 4, 4, 3, 8]
        subzero_ANIMATION_STEPS = [8, 8, 4, 6, 8, 3, 8]
        WomenHunter_ANIMATION_STEPS = [8, 8, 2, 5, 5, 3, 8]
        #Huntress_ANIMATION_STEPS = [10, 8 ,1, 6, 6, 3, 10]

        # define font
        count_font = pygame.font.Font("assets/fonts/turok.ttf", 80)
        score_font = pygame.font.Font("assets/fonts/turok.ttf", 30)

        # function for drawing text
        def draw_text(text, font, text_col, x, y):
            img = font.render(text, True, text_col)
            screen.blit(img, (x, y))

        # function for drawing background
        def draw_bg():
            scaled_bg = pygame.transform.scale(CURRENT_BACKGROUND, (SCREEN_WIDTH, SCREEN_HEIGHT))
            screen.blit(scaled_bg, (0, 0))

        # function for drawing fighter health bars
        def draw_health_bar(health, x, y):
            ratio = health / 100
            pygame.draw.rect(screen, WHITE, (x - 2, y - 2, 404, 34))
            pygame.draw.rect(screen, BLACK, (x, y, 400, 30))
            pygame.draw.rect(screen, RED, (x, y, 400 * ratio, 30))

        # create two instances of fighters
        fighter_1 = Fighter(1, 200, 700, False, WARRIOR_DATA, warrior_sheet, WARRIOR_ANIMATION_STEPS, sword_fx) \
            if selected_fighter_1 == "warrior" else Fighter(1, 200, 700, False, Samurai_DATA, Samurai_sheet,
                                                            Samurai_ANIMATION_STEPS, magic_fx) \
            if selected_fighter_1 == "Samurai" else Fighter(1, 200, 700, False, WomenHunter_DATA, WomenHunter_sheet,
                                                            WomenHunter_ANIMATION_STEPS, spear_fx) \
            if selected_fighter_1 == "WomenHunter" else Fighter(1, 200, 700, False, subzero_DATA, subzero_sheet,
                                                                subzero_ANIMATION_STEPS, punch_fx)

        fighter_2 = Fighter(2, 1400, 700, True, WARRIOR_DATA, warrior_sheet, WARRIOR_ANIMATION_STEPS, sword_fx) \
            if selected_fighter_2 == "warrior" else Fighter(2, 1400, 700, True, Samurai_DATA, Samurai_sheet,
                                                            Samurai_ANIMATION_STEPS, magic_fx) \
            if selected_fighter_2 == "Samurai" else Fighter(2, 1400, 700, True, WomenHunter_DATA, WomenHunter_sheet,
                                                            WomenHunter_ANIMATION_STEPS, spear_fx) \
            if selected_fighter_2 == "WomenHunter" else Fighter(2, 1400, 700, True, subzero_DATA, subzero_sheet,
                                                                subzero_ANIMATION_STEPS, punch_fx)

        # create a Back button
        BACK_TO_MENU_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(800, 50),
                                     text_input="Back to Menu", font=get_font(30), base_color="#d7fcd4",
                                     hovering_color="White")
        # game loop
        run = True
        while True:

            clock.tick(FPS)

            # draw background
            draw_bg()

            # show player stats
            draw_health_bar(fighter_1.health, 50, 30)
            draw_health_bar(fighter_2.health, 1140, 30)
            draw_text("P1: " + str(score[0]), score_font, RED, 50, 60)
            draw_text("P2: " + str(score[1]), score_font, RED, 1090, 60)

            # draw the "Back to Menu" button
            BACK_TO_MENU_BUTTON.changeColor(pygame.mouse.get_pos())
            BACK_TO_MENU_BUTTON.update(screen)

            # display countdown timer
            draw_text(str(timer_value), timer_font, RED, 800,100)

            # update countdown
            current_time = pygame.time.get_ticks()

            if not is_paused:  # Only update timer and fighters if the game is not paused
                if not round_over and timer_value > 0:
                    if current_time - timer_last_update >= timer_cooldown:
                        timer_value -= 1
                        timer_last_update = current_time

                if timer_value <= 0:
                    if not round_over:
                        round_over = True
                        round_over_start_time = pygame.time.get_ticks()
                        if fighter_1.health < fighter_2.health:
                            fighter_1.health = 0
                        else:
                            fighter_2.health = 0

                if round_over:
                    if current_time - round_over_start_time >= round_over_delay:
                        round_over = False
                        intro_count = 3

                        choose_fighter()




            # draw fighters
            fighter_2.draw(SCREEN)
            fighter_1.draw(screen)

            # check for player defeat
            if not round_over:
                if not fighter_1.alive:
                    score[1] += 1
                    round_over = True
                    round_over_start_time = pygame.time.get_ticks()
                elif not fighter_2.alive:
                    score[0] += 1
                    round_over = True
                    round_over_start_time = pygame.time.get_ticks()
            else:
                if not victory_sound.play(0, 3000):
                        # display victory image
                        screen.blit(victory_img, (650, 150))

            # event handler
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        is_paused = not is_paused
                        if is_paused:
                            pygame.mixer.music.pause()
                            is_music_paused = True

                        else:
                            pygame.mixer.music.unpause()
                            is_music_paused = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if BACK_TO_MENU_BUTTON.checkForInput(pygame.mouse.get_pos()):
                        play_main_menu_music()
                        fade_transition(SCREEN)
                        choose_fighter()

            if is_paused:
                # Draw the pause menu
                SCREEN.blit(pause_menu_surface, (0, 0))
                SCREEN.blit(pause_text, pause_text_rect)
            else:
                if intro_count <= 0:
                    # move fighters
                    fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_2, round_over)
                    fighter_2.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_1, round_over)
                else:
                    # display count timer
                    draw_text(str(intro_count), count_font, RED, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3)
                    # update count timer
                    if (pygame.time.get_ticks() - last_count_update) >= 1000:
                        intro_count -= 1
                        last_count_update = pygame.time.get_ticks()

                # update fighters
                fighter_1.update()
                fighter_2.update()


            # update display
            pygame.display.update()

        # exit pygame
        pygame.quit()


def how_to_play():
    while True:
        how_to_play_MOUSE_POS = pygame.mouse.get_pos()

        how_to_play_TEXT = get_font(45).render("This is the how_to_play screen.", True, "Black")
        how_to_play_RECT = how_to_play_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(how_to_play_TEXT, how_to_play_RECT)



        # Load the "How to play" image
        how_to_play_image = pygame.image.load("assets/how-to-play00000.png")
        screen_rect = SCREEN.get_rect()
        image_rect = how_to_play_image.get_rect(center=(screen_rect.centerx, screen_rect.centery))
        SCREEN.blit(how_to_play_image, image_rect)

        how_to_play_BACK = Button(image=None, pos=(800, 850),
                              text_input="BACK", font=get_font(75), base_color="white", hovering_color="Green")

        how_to_play_BACK.changeColor(how_to_play_MOUSE_POS)
        how_to_play_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fade_transition(SCREEN)
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if how_to_play_BACK.checkForInput(how_to_play_MOUSE_POS):
                    fade_transition(SCREEN)
                    main_menu()

        pygame.display.update()


def main_menu():

    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(150).render("Warrior's Wrath", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(800, 150))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(800, 300),
                             text_input="Start", font=get_font(75), base_color="#d7fcd4", hovering_color="white")
        how_to_play_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(800, 450),
                                text_input="How to play", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(800, 600),
                             text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, how_to_play_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):

                    fade_transition(SCREEN)
                    # If the play button is pressed, display the "Choose Your Field" menu
                    choose_field_menu()
                if how_to_play_BUTTON.checkForInput(MENU_MOUSE_POS):
                    fade_transition(SCREEN)
                    how_to_play()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    fade_transition(SCREEN)
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
def choose_field_menu():
    global CURRENT_BACKGROUND
    while True:

        SCREEN.fill("black")

        CHOOSE_FIELD_MOUSE_POS = pygame.mouse.get_pos()

        CHOOSE_FIELD_TEXT = get_font(45).render("Choose Your Field", True, "White")
        CHOOSE_FIELD_RECT = CHOOSE_FIELD_TEXT.get_rect(center=(800, 260))
        SCREEN.blit(CHOOSE_FIELD_TEXT, CHOOSE_FIELD_RECT)

        FIELD_1_BUTTON = Button(image=pygame.image.load("assets/images/background/mk3-stage- icon.jpg"), pos=(290, 500),
                                text_input="soul-chamber", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        FIELD_2_BUTTON = Button(image=pygame.image.load("assets/images/background/background2 icon.jpg"), pos=(800, 500),
                                text_input="The Hood", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        FIELD_3_BUTTON = Button(image=pygame.image.load("assets/images/background/background3 icon.jpg"), pos=(1310, 500),
                                text_input="China-Town", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        BACK_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(800, 700),
                             text_input="Back", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        for button in [FIELD_1_BUTTON, FIELD_2_BUTTON, FIELD_3_BUTTON, BACK_BUTTON]:
            button.changeColor(CHOOSE_FIELD_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if FIELD_1_BUTTON.checkForInput(CHOOSE_FIELD_MOUSE_POS):
                    fade_transition(SCREEN)
                    CURRENT_BACKGROUND = FIELD_1_BG  # Set the current background to the chosen image path
                    choose_fighter()
                elif FIELD_2_BUTTON.checkForInput(CHOOSE_FIELD_MOUSE_POS):
                    fade_transition(SCREEN)
                    CURRENT_BACKGROUND = FIELD_2_BG  # Set the current background to the chosen image path
                    choose_fighter()
                elif FIELD_3_BUTTON.checkForInput(CHOOSE_FIELD_MOUSE_POS):
                    fade_transition(SCREEN)
                    CURRENT_BACKGROUND = FIELD_3_BG  # Set the current background to the chosen image path
                    choose_fighter()
                elif BACK_BUTTON.checkForInput(CHOOSE_FIELD_MOUSE_POS):
                    fade_transition(SCREEN)
                    main_menu()

        pygame.display.update()
play_intro_video()
play_main_menu()