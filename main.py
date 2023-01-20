import pygame
import pyaudio
import audioop
import tomllib

with open("config.toml", "rb") as f:
    config = tomllib.load(f)

FPS = config["fps"]
WINDOW = config["window"]
BACKGROUND = config["background"]
RECOGNITION = config["recognition"]
DURATIONS = config["durations"]

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100

p = pyaudio.PyAudio()
stream = p.open(
    format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK
)


pygame.init()
display = pygame.display.set_mode(WINDOW)
pygame.display.set_caption("Pop")
clock = pygame.time.Clock()

images = []
n = 1
while True:
    try:
        image = pygame.image.load(f"images/{n}.png")
    except FileNotFoundError:
        break
    images.append(image)
    n += 1

frame = 0
timer = 0
sound = 0

running = True
while running:
    dt = clock.tick(FPS)
    display.fill(BACKGROUND)

    data = stream.read(CHUNK)
    sound = audioop.rms(data, 2)

    if sound >= RECOGNITION:
        timer += dt
        if timer >= DURATIONS[frame]:
            frame += 1
            if frame == len(images):
                frame = 0
            timer = 0
    else:
        frame = 0
        timer = 0

    image = images[frame]
    display.blit(image, (250 - (image.get_width() / 2), 250 - (image.get_height() / 2)))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()
