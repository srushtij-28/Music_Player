import pygame
import sys

def main():
    pygame.init()
    
    # Set window size and title
    screen = pygame.display.set_mode((550, 600))
    pygame.display.set_caption("Music Player")

    # Load disc image
    disc_image = pygame.image.load("dvd.png").convert_alpha()
    disc_rect = disc_image.get_rect(center=(300, 300))  # Center of screen

    # Load and play music
    pygame.mixer.pre_init(48000, -16, 2, 512)
    pygame.mixer.init()

    # 🔴 KEEP YOUR PATH STYLE (just fix slashes if needed)
    pygame.mixer.music.load(r"song.mp3")
    pygame.mixer.music.play()

    # Clock for controlling frame rate
    clock = pygame.time.Clock()
    angle = 0

    paused = False  # ✅ NEW

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # ✅ NEW CONTROLS
            if event.type == pygame.KEYDOWN:

                # PAUSE / RESUME
                if event.key == pygame.K_SPACE:
                    if paused:
                        pygame.mixer.music.unpause()
                        paused = False
                    else:
                        pygame.mixer.music.pause()
                        paused = True

                # STOP
                if event.key == pygame.K_s:
                    pygame.mixer.music.stop()
                    paused = True

                # EXIT
                if event.key == pygame.K_ESCAPE:
                    running = False

        # Rotate the disc ONLY if music is playing
        if pygame.mixer.music.get_busy() and not paused:
            angle += 1
            if angle >= 360:
                angle = 0

        # Clear screen
        screen.fill((30, 30, 30))

        # Rotate image and draw
        rotated_disc = pygame.transform.rotate(disc_image, angle)
        rotated_rect = rotated_disc.get_rect(center=disc_rect.center)
        screen.blit(rotated_disc, rotated_rect)

        pygame.display.flip()
        clock.tick(60)

        # Stop program when music ends
        if not pygame.mixer.music.get_busy() and not paused:
            running = False

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
