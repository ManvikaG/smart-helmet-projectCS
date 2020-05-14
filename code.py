#!/usr/bin/python
# -*- coding: utf-8 -*-
from adafruit_circuitplayground.express import cpx
import time
import adafruit_irremote
import pulseio
import board

pulsein = pulseio.PulseIn(board.IR_RX, maxlen=120, idle_state=True)
decoder = adafruit_irremote.GenericDecode()

# Create a 'pulseio' output, to send infrared signals on the IR transmitter @ 38KHz

pwm = pulseio.PWMOut(board.IR_TX, frequency=38000, duty_cycle=2 ** 15)
pulseout = pulseio.PulseOut(pwm)

# Create an encoder that will take numbers and turn them into NEC IR pulses

encoder = adafruit_irremote.GenericTransmit(header=[9500, 4500],
        one=[550, 550], zero=[550, 1700], trail=0)

while True:
    if cpx.shake():
        print ('Shake detected!')
        count = 0
        while count < 4:
            cpx.pixels.fill((90, 90, 90))
            cpx.pixels.fill((0, 0, 0))
            cpx.play_tone(440, 1)
            time.sleep(1)

#          cpx.pixels[count]= (255,255,255)
#          cpx.pixels[count]= (0,0,0)

            count = count + 1
    if cpx.light > 5:
        cpx.pixels.fill((0, 0, 0))
    if cpx.light <= 4:
        cpx.pixels.fill((11, 11, 11))
    cpx.red_led = True
    encoder.transmit(pulseout, [255, 2, 255, 2])
    cpx.red_led = False

    # wait so the receiver can get the full message
    time.sleep(0.2)
    pulses = decoder.read_pulses(pulsein)
    try:
        # Attempt to convert received pulses into numbers
        received_code = decoder.decode_bits(pulses)
        print(received_code)
        if received_code == [129, 127, 129, 0]:
            print ('received ir')
            cpx.pixels.fill((255, 0, 0))
            cpx.play_tone(440, 2.0)
        if recieved_code not == [129, 127, 129, 0]:
            cpx.pixels.fill((50, 0, 75))
    except adafruit_irremote.IRNECRepeatException:
        # We got an unusual short code, probably a 'repeat' signal
        print("NEC repeat!")
        continue
    except adafruit_irremote.IRDecodeException:
     # Something got distorted or maybe its not an NEC-type remote?
        #print("Failed to decode: ")
        continue
