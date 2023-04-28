"""
Example code for running airtable communication. This specific example is for
a simplified version of the BANANA CHOPPING ROBOT.
"""

import time

import airtable
import chopper


def main() -> None:
    """
    Runs main program code.
    """

    # *** CHANGE THIS ENTIRE FUNCTION TO FIT YOUR ROBOT ***

    # Defines needed variables
    emergency_stop = False
    previous_dock_state = False

    # Loops until emergency stop
    while not emergency_stop:
        # Gets specific value from airtable
        trasport_docked = airtable.get_status("Processing B", "Transport Present")

        # If banana transport has just LEFT:
        if trasport_docked < previous_dock_state:
            # Post to airtable that processing is beginning
            airtable.post_status("Processing B", "Robot Processing", True)
            # Execute main chopping action
            chopper.main()
            # Posts again to airtable to denote the completion of action
            airtable.post_status("Processing B", "Robot Processing", False)

        # Sets previous state for next iteration
        previous_dock_state = trasport_docked
        # Checks for emergency stop
        emergency_stop = chopper.button_pushed()
        # Sets loop speed
        time.sleep(1)


# Runs main code if file is run from console but NOT if included as library.
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
