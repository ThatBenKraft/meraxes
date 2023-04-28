"""
Runs complete Meraxes Final Project actions. Will access airtable data and 
begin processing if transport robot is docked.
"""

import time

import RPi.GPIO as GPIO

import chopper
import new_airtable
from create_3 import publishers

motors = publishers.MotorPublisher()

CLOCK_SPEED = 2


def main():

    try:

        time.sleep(3)

        # Defines utility variables
        emergency_stop = False

        previous_banana_docked = False
        previous_transport_docked = False

        # Loops until stop:
        while not emergency_stop:

            # Acquires valeus from airtable
            banana_docked = bool(new_airtable.docked2(6))
            transport_docked = bool(new_airtable.docked2(5))

            print(
                f"Banana docked: {banana_docked}\nTransport docked: {transport_docked}"
            )

            # If the banana robot leaves its dock:
            if banana_docked < previous_banana_docked:
                # Moves robot to processing position
                move_to_process(direction=-1)

                time.sleep(5)

            # If the transport arrives at its dock
            if transport_docked > previous_transport_docked:

                time.sleep(1)

                chopper.main()

                time.sleep(3)

                move_to_process(direction=1)

                time.sleep(5)

            # Updates utility functions
            previous_banana_docked = banana_docked
            previous_transport_docked = transport_docked

        time.sleep(CLOCK_SPEED)

    except KeyboardInterrupt:

        GPIO.cleanup()  # type:ignore

    GPIO.cleanup()  # type:ignore


def move_to_process(direction: int = 1):
    """
    Moves robot to or from processing position."""

    if direction not in (-1, 1):
        raise ValueError("Choose either 1 or -1.")

    motors.turn_degrees(-45)

    time.sleep(1)

    motors.move_distance(3 * direction)

    time.sleep(1)

    motors.turn_degrees(45)


if __name__ == "__main__":
    main()
