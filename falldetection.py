from adafruit_circuitplayground import cp

if cp.shake(100):
    print("Hard Shake Detected!")
    cp.pixels[9] = (255, 0, 0)
    cp.pixels[8] = (255, 0, 0)
    cp.pixels[7] = (255, 0, 0)
    cp.pixels[6] = (255, 0, 0)
    cp.pixels[5] = (255, 0, 0)
    cp.pixels[4] = (255, 0, 0)
    cp.pixels[3] = (255, 0, 0)
    cp.pixels[2] = (255, 0, 0)
    cp.pixels[1] = (255, 0, 0)
    cp.pixels[0] = (255, 0, 0)
    cp.play_tone(440, 10.0)

