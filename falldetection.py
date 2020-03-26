from adafruit_circuitplayground import cp

while True:
    if cp.shake(50):
        print("Hard shake Detected")
        cp.pixels.fill((255, 0, 0))
        cp.play_tone(440, 10.0)

