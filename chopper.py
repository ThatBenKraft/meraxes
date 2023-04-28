"""
WRITTEN BY PHILLIP ROOS
"""

from time import sleep

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

mode = GPIO.getmode()

# knife motor pins
KNIFE_A = (11, 12, 13, 15)  # Yellow Red Green Gray
KNIFE_B = (35, 36, 37, 38)  # Yellow Red Green Gray

# linear actuator motor
LEAD_SCREW = (29, 31, 33, 32)

# Motor section
GPIO.setup(KNIFE_A, GPIO.OUT)
GPIO.setup(KNIFE_B, GPIO.OUT)
GPIO.setup(LEAD_SCREW, GPIO.OUT)
STEP_NUMBER = 1000
INPUT_DELAY = 0.005
steps = int(STEP_NUMBER)


def main():
    """
    Runs full banana-knife process action.
    """

    try:
        knife_up()

        sleep(1)

        for _ in range(12):
            linear()
            sleep(1)
            single_chop()
            sleep(0.1)
            single_chop()
            sleep(0.1)
            single_chop()

        linear_retract()

        knife_down()

    except KeyboardInterrupt:

        knife_down()
        GPIO.cleanup()

    GPIO.cleanup()


def linear_retract():
    for _ in range(1227):
        # GPIO.output(motor_pins, (GPIO.LOW,GPIO.LOW,GPIO.LOW,GPIO.LOW))
        # GPIO.output(ledPin, GPIO.HIGH)
        GPIO.output(LEAD_SCREW, (GPIO.HIGH, GPIO.LOW, GPIO.HIGH, GPIO.LOW))
        sleep(INPUT_DELAY)
        GPIO.output(LEAD_SCREW, (GPIO.LOW, GPIO.HIGH, GPIO.HIGH, GPIO.LOW))
        sleep(INPUT_DELAY)
        GPIO.output(LEAD_SCREW, (GPIO.LOW, GPIO.HIGH, GPIO.LOW, GPIO.HIGH))
        sleep(INPUT_DELAY)
        GPIO.output(LEAD_SCREW, (GPIO.HIGH, GPIO.LOW, GPIO.LOW, GPIO.HIGH))


def linear():
    for _ in range(100):
        # GPIO.output(motor_pins, (GPIO.LOW,GPIO.LOW,GPIO.LOW,GPIO.LOW))
        # GPIO.output(ledPin, GPIO.HIGH)
        GPIO.output(LEAD_SCREW, (GPIO.HIGH, GPIO.LOW, GPIO.LOW, GPIO.HIGH))
        sleep(INPUT_DELAY)
        GPIO.output(LEAD_SCREW, (GPIO.LOW, GPIO.HIGH, GPIO.LOW, GPIO.HIGH))
        sleep(INPUT_DELAY)
        GPIO.output(LEAD_SCREW, (GPIO.LOW, GPIO.HIGH, GPIO.HIGH, GPIO.LOW))
        sleep(INPUT_DELAY)
        GPIO.output(LEAD_SCREW, (GPIO.HIGH, GPIO.LOW, GPIO.HIGH, GPIO.LOW))
        sleep(INPUT_DELAY)


def single_chop():

    knife_down()

    sleep(0.1)

    knife_up()


def knife_up() -> None:

    for _ in range(20):
        # GPIO.output(motor_pins, (GPIO.LOW,GPIO.LOW,GPIO.LOW,GPIO.LOW))
        # GPIO.output(ledPin, GPIO.HIGH)
        GPIO.output(KNIFE_A, (GPIO.HIGH, GPIO.LOW, GPIO.HIGH, GPIO.LOW))
        GPIO.output(KNIFE_B, (GPIO.HIGH, GPIO.LOW, GPIO.LOW, GPIO.HIGH))
        sleep(INPUT_DELAY)
        GPIO.output(KNIFE_B, (GPIO.LOW, GPIO.HIGH, GPIO.LOW, GPIO.HIGH))
        GPIO.output(KNIFE_A, (GPIO.LOW, GPIO.HIGH, GPIO.HIGH, GPIO.LOW))
        sleep(INPUT_DELAY)
        GPIO.output(KNIFE_B, (GPIO.LOW, GPIO.HIGH, GPIO.HIGH, GPIO.LOW))
        GPIO.output(KNIFE_A, (GPIO.LOW, GPIO.HIGH, GPIO.LOW, GPIO.HIGH))
        sleep(INPUT_DELAY)
        GPIO.output(KNIFE_B, (GPIO.HIGH, GPIO.LOW, GPIO.HIGH, GPIO.LOW))
        GPIO.output(KNIFE_A, (GPIO.HIGH, GPIO.LOW, GPIO.LOW, GPIO.HIGH))
        sleep(INPUT_DELAY)


def knife_down() -> None:

    for _ in range(11):
        # GPIO.output(motor_pins, (GPIO.LOW,GPIO.LOW,GPIO.LOW,GPIO.LOW))
        # GPIO.output(ledPin, GPIO.HIGH)
        GPIO.output(KNIFE_B, (GPIO.HIGH, GPIO.LOW, GPIO.HIGH, GPIO.LOW))
        GPIO.output(KNIFE_A, (GPIO.HIGH, GPIO.LOW, GPIO.LOW, GPIO.HIGH))
        sleep(INPUT_DELAY)
        GPIO.output(KNIFE_A, (GPIO.LOW, GPIO.HIGH, GPIO.LOW, GPIO.HIGH))
        GPIO.output(KNIFE_B, (GPIO.LOW, GPIO.HIGH, GPIO.HIGH, GPIO.LOW))
        sleep(INPUT_DELAY)
        GPIO.output(KNIFE_A, (GPIO.LOW, GPIO.HIGH, GPIO.HIGH, GPIO.LOW))
        GPIO.output(KNIFE_B, (GPIO.LOW, GPIO.HIGH, GPIO.LOW, GPIO.HIGH))
        sleep(INPUT_DELAY)
        GPIO.output(KNIFE_A, (GPIO.HIGH, GPIO.LOW, GPIO.HIGH, GPIO.LOW))
        GPIO.output(KNIFE_B, (GPIO.HIGH, GPIO.LOW, GPIO.LOW, GPIO.HIGH))
        sleep(INPUT_DELAY)


if __name__ == "__main__":
    main()
