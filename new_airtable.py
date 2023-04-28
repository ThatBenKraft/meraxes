"""
WRITTEN BY DARYA CLARK
"""

################################
# THINGS EVERYONE NEEDS #
import time

import requests

# # step to index
Smoothie1Dict = {1: 0, 2: 5, 3: 1, 4: 6, 5: 9, 6: 3, 7: 10, 8: 2, 9: 4, 10: 7}

Smoothie2Dict = {1: 9, 2: 3, 3: 1, 4: 7, 5: 6, 6: 8, 7: 5, 8: 0, 9: 2, 10: 4}

# this is information for pushing data to the airtable
AIRTABLE_API_KEY = "keyKf7fEzdNw4S7qi"
AIRTABLE_BASE_ID = "appxFSx1vodDWljqe"
SMOOTHIE1 = "Smoothie1Tasks"
SMOOTHIE2 = "Smoothie2Tasks"

# pulling info for Smoothie 1
URLSmoothie1 = f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{SMOOTHIE1}?api_key={AIRTABLE_API_KEY}"

# pulling info for Smoothie 2
URLSmoothie2 = f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{SMOOTHIE2}?api_key={AIRTABLE_API_KEY}"

# updating current order info
currID = "recBNdKxX9ccyOdSf"
currEndpoint = f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/Current_Order/{currID}"

# pull current order info
currURL = f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/Current_Order?api_key={AIRTABLE_API_KEY}"


# python request headers
headers = {
    "Authorization": f"Bearer {AIRTABLE_API_KEY}",
    "Content-Type": "application/json",
}

#####################################
# take info as needed

# specified endpoint depending on team
# information for being able to publish to airtable

###### ICE / BLUEB / MILK / LEMONADE ######

# smoothie 1 and 2
iceS1ID = "recf3pP4j1RPFlQhj"
iceS1Endpoint = f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{SMOOTHIE1}/{iceS1ID}"
iceS2ID = "recIvY5XrPpN0U6Ic"
iceS2Endpoint = f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{SMOOTHIE2}/{iceS2ID}"

# smoothie 1
lemonadeID = "rec9I4VI8dVhE2bQ3"
lemonadeEndpoint = (
    f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{SMOOTHIE1}/{lemonadeID}"
)

# smoothie 2
milkID = "recCaDbBg1tfZBrhW"
milkEndpoint = f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{SMOOTHIE2}/{milkID}"

# smoothie 1
bluebID = "recgdygMg21uApHgQ"
bluebEndpoint = f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{SMOOTHIE1}/{bluebID}"

##### STRAWBERRY AND BANANA #####

# smoothie 1 and 2
strawberryS1ID = "recrQSMlTC3rVhQVM"
strawberryS1Endpoint = (
    f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{SMOOTHIE1}/{strawberryS1ID}"
)
strawberryS2ID = "recgPvp8ooDJ7hIHR"
strawberryS2Endpoint = (
    f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{SMOOTHIE2}/{strawberryS2ID}"
)

# smoothie 2
bananaID = "recg6PhVTnypcWleC"
bananaEndpoint = (
    f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{SMOOTHIE2}/{bananaID}"
)

#### STRAWBERRY AND BANANA AND PROCESSING ####

# smoothie 1 and 2
dropOffProcessingS1ID = "recK4TPYcr89XiKRJ"
dropOffProcessingS1Endpoint = f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{SMOOTHIE1}/{dropOffProcessingS1ID}"
dropOffProcessingS2ID = "reckso7rzDIYQFz3W"
dropOffProcessingS2Endpoint = f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{SMOOTHIE2}/{dropOffProcessingS2ID}"

##### PROCESSING ######

# smoothie 1 and 2
pickUpProcessingS1ID = "recm0NkjJTLlbpVyx"
pickUpProcessingS1Endpoint = (
    f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{SMOOTHIE1}/{pickUpProcessingS1ID}"
)
pickUpProcessingS2ID = "recPsmAcRHjjwYbZq"
pickUpProcessingS2Endpoint = f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{SMOOTHIE2}/{dropOffProcessingS2ID}"

#### BLENDING #####

# smoothie 1 and 2
blender1S1ID = "recFOJQgatzvw5sTN"
blender1S1Endpoint = (
    f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{SMOOTHIE1}/{blender1S1ID}"
)
blender2S2ID = "recFOJQgatzvw5sTN"
blender2S2Endpoint = (
    f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{SMOOTHIE2}/{blender2S2ID}"
)

# individual for each blender
clean1ID = "recaeyVAbjQ826om0"
clean1Endpoint = (
    f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{SMOOTHIE1}/{clean1ID}"
)
clean2ID = "recDG7btj7o6nFENT"
clean2Endpoint = (
    f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{SMOOTHIE2}/{clean2ID}"
)

#### TRANSPORT ######

# smoothie 1 and 2
pickUpCupS1ID = "rec2oMFRbIcSoNrvC"
pickupCupS1Endpoint = (
    f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{SMOOTHIE1}/{pickUpCupS1ID}"
)
pickUpCupS2ID = "recvQlVKjwKQJmHWv"
pickupCupS2Endpoint = (
    f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{SMOOTHIE2}/{pickUpCupS2ID}"
)

# smoothie 1 and 2
deliveryS1ID = "rech2uiOultJVpfjH"
deliveryS1Endpoint = (
    f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{SMOOTHIE1}/{deliveryS1ID}"
)
deliveryS2ID = "recKu3yHC91HgYvKA"
deliveryS2Endpoint = (
    f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{SMOOTHIE2}/{deliveryS2ID}"
)

###################################
# FUNCTIONS for everyone


def _get_fields(url: str, index: int) -> dict:
    """
    Gets data from url in airtable.
    """
    response = requests.get(url).json()
    # Return all fields at index in records
    return response["records"][index]["fields"]


def smoothieType() -> int:
    return _get_fields(currURL, 0)["Smoothie Type"]


def taskFinished1(index: int) -> int:
    return _get_fields(URLSmoothie1, index)["Task Finished"]


def docked1(index: int) -> int:
    return _get_fields(URLSmoothie1, index)["Robot Docked"]


def ready1(index: int) -> int:
    return _get_fields(URLSmoothie1, index)["Ready for Robot"]


def taskFinished2(index: int) -> int:
    return _get_fields(URLSmoothie2, index)["Task Finished"]


def docked2(index: int) -> int:
    return _get_fields(URLSmoothie2, index)["Robot Docked"]


def ready2(index: int) -> int:
    return _get_fields(URLSmoothie2, index)["Ready for Robot"]


#############################

##### INDIVIDUAL TEAMS FUNCTIONS ######
# In theory, each of these functions would go in a while loop of sorts. Then,
# the airtable would be constantly checked


def liqAndSmall():
    # check which smoothie
    smoothie = smoothieType()
    # smoothie 1 - ice and lemonade and blueberries
    if smoothie == 1:
        # need robot to be docked and ready for ice/lemonade
        if (ready1(5) == 1) and (docked1(5) == 1):
            data = {"fields": {"Ready for Robot": 0}}
            # briefly update airtable for Ready for Robot to be False so two robots are not in the same place
            r = requests.patch(iceS1Endpoint, json=data, headers=headers)
            r = requests.patch(lemonadeEndpoint, json=data, headers=headers)
            # INSERT function for ice / lemonade
            time.sleep(5)

            data = {"fields": {"Ready for Robot": 1, "Task Finished": 1}}

            r = requests.patch(iceS1Endpoint, json=data, headers=headers)
            r = requests.patch(lemonadeEndpoint, json=data, headers=headers)
        # need robot to be docked and ready for blueberries
        if ready1(6) == 1 and docked1(6) == 1:
            data = {"fields": {"Ready for Robot": 0}}
            # briefly update airtable for Ready for Robot to be False so two robots are not in the same place
            r = requests.patch(bluebEndpoint, json=data, headers=headers)
            # INSERT function for blueberries
            time.sleep(5)

            data = {"fields": {"Ready for Robot": 1, "Task Finished": 1}}

            r = requests.patch(bluebEndpoint, json=data, headers=headers)
    # smoothie 2 - ice and milk
    if smoothie == 2:
        # docked and ready for ice
        if (ready2(3) == 1) and (docked2(3) == 1):
            data = {"fields": {"Ready for Robot": 0}}
            # briefly update airtable for Ready for Robot to be False so two robots are not in the same place
            r = requests.patch(iceS2Endpoint, json=data, headers=headers)
            # INSERT function for ice
            time.sleep(5)

            data = {"fields": {"Ready for Robot": 1, "Task Finished": 1}}

            r = requests.patch(iceS2Endpoint, json=data, headers=headers)
        # need robot to be docked and ready for milk
        if (ready2(1) == 1) and (docked2(1) == 1):
            data = {"fields": {"Ready for Robot": 0}}
            # briefly update airtable for Ready for Robot to be False so two robots are not in the same place
            r = requests.patch(milkEndpoint, json=data, headers=headers)
            # INSERT function for ice / lemonade
            time.sleep(5)

            data = {"fields": {"Ready for Robot": 1, "Task Finished": 1}}

            r = requests.patch(milkEndpoint, json=data, headers=headers)


# STRAWBERRY AND BANANA / PROCESSING TEAMS
def strawbBanana():
    # clearing up some misleading terms, strawberry is meant to be used by
    # strawberry processing, same for banana. the drop off is for the fork team

    # get smoothie information
    smoothie = smoothieType()
    # strawberry no banana
    # STAWBERRY AND BANANA
    if smoothie == 1:
        # docked and ready for drop off
        if (ready1(6) == 1) and (docked1(6) == 1):
            data = {"fields": {"Ready for Robot": 0}}
            # briefly update airtable for Ready for Robot to be False so two robots are not in the same place
            r = requests.patch(dropOffProcessingS1Endpoint, json=data, headers=headers)
            # INSERT function for dropping off (strawberries only for this one)

            # set Strawberry docked to True as they are being dropped off
            data = {"fields": {"Robot Docked": 1}}
            r = requests.patch(strawberryS1Endpoint, json=data, headers=headers)

            time.sleep(5)
            # once finished
            data = {"fields": {"Ready for Robot": 1, "Task Finished": 1}}

            r = requests.patch(dropOffProcessingS1Endpoint, json=data, headers=headers)
        # For processing teams
        # only strawberries

        # if strawberries is docked (incoming strawberries) and pick up is ready
        if (docked1(9) == 1) and (docked1(8) == 1):
            data = {"fields": {"Ready for Robot": 0}}
            # briefly update airtable for Ready for Robot to be False so two robots are not in the same place
            r = requests.patch(strawberryS1Endpoint, json=data, headers=headers)
            # INSERT function for strawberry processing
            time.sleep(10)
            data = {"fields": {"Ready for Robot": 1, "Task Finished": 1}}

        r = requests.patch(strawberryS1Endpoint, json=data, headers=headers)
    # if smoothie 2, need both fruits
    if smoothie == 2:
        # docked and ready for robot to start picking up both strawberries and bananas
        if (ready2(5) == 1) and (docked2(5) == 1):
            data = {"fields": {"Ready for Robot": 0}}
            # briefly update airtable for Ready for Robot to be False so two robots are not in the same place
            r = requests.patch(pickUpProcessingS2Endpoint, json=data, headers=headers)
            # INSERT function for strawberry and banana pick up

            # set Drop Off Processing to True as strawberries and bananas are dropped off
            data = {"fields": {"Robot Docked": 1}}
            r = requests.patch(strawberryS2Endpoint, json=data, headers=headers)
            r = requests.patch(bananaEndpoint, json=data, headers=headers)

            time.sleep(5)
            # once finished
            data = {"fields": {"Ready for Robot": 1, "Task Finished": 1}}

            r = requests.patch(strawberryS2Endpoint, json=data, headers=headers)
            r = requests.patch(bananaEndpoint, json=data, headers=headers)
        # if strawberries is docked (incoming strawberries) and pick up is ready
        if (docked2(7) == 1) and (docked2(5) == 1):
            data = {"fields": {"Ready for Robot": 0}}
            # briefly update airtable for Ready for Robot to be False so two robots are not in the same place
            r = requests.patch(strawberryS2Endpoint, json=data, headers=headers)
            # INSERT function for strawberry processing
            time.sleep(10)
            data = {"fields": {"Ready for Robot": 1, "Task Finished": 1}}

            r = requests.patch(strawberryS2Endpoint, json=data, headers=headers)
        # same idea for bananas
        if docked2(5) == 1 and docked2(6) == 1:
            data = {"fields": {"Ready for Robot": 0}}

            r = requests.patch(bananaEndpoint, json=data, headers=headers)
            # INSERT function for banana processing
            time.sleep(10)
            data = {"fields": {"Ready for Robot": 1, "Task Finished": 1}}

            r = requests.patch(bananaEndpoint, json=data, headers=headers)


# BLENDING TEAM
def blending():
    # get smoothie type
    smoothie = smoothieType()

    if smoothie == 1:
        # check if transport bot is docked
        if docked1(2):
            data = {"fields": {"Ready for Robot": 0}}
            # briefly update airtable for Ready for Robot to be False so two robots are not in the same place
            r = requests.patch(blender1S1Endpoint, json=data, headers=headers)

            # INSERT function for blending
            time.sleep(5)

            data = {"fields": {"Ready for Robot": 1, "Task Finished": 1}}

            r = requests.patch(blender1S1Endpoint, json=data, headers=headers)
    if smoothie == 2:
        # check if transport bot is docked
        if docked2(0):
            data = {"fields": {"Ready for Robot": 0}}
            # briefly update airtable for Ready for Robot to be False so two robots are not in the same place
            r = requests.patch(blender2S2Endpoint, json=data, headers=headers)

            # INSERT function for blending
            time.sleep(5)

            data = {"fields": {"Ready for Robot": 1, "Task Finished": 1}}

            r = requests.patch(blender2S2Endpoint, json=data, headers=headers)
    # if done blending, clean blade
    if taskFinished1(2) == 1:
        # INSERT function for cleaning
        time.sleep(5)

        data = {"fields": {"Ready for Robot": 1, "Task Finished": 1}}

        r = requests.patch(clean1Endpoint, json=data, headers=headers)
    if taskFinished1(0) == 1:
        # INSERT function for cleaning
        time.sleep(5)

        data = {"fields": {"Ready for Robot": 1, "Task Finished": 1}}

        r = requests.patch(clean2Endpoint, json=data, headers=headers)


def transport():
    # if a delivery is completed, use the following to indicate it in the airtable
    if smoothieType() == 1:
        data = {"fields": {"Task Finished": 1}}
        r = requests.patch(deliveryS1Endpoint, json=data, headers=headers)
    if smoothieType() == 2:
        data = {"fields": {"Task Finished": 1}}
        r = requests.patch(deliveryS2Endpoint, json=data, headers=headers)


# hello alex savic this is for you
def dock():
    # if you want to publish that you have docked:
    data = {"fields": {"Robot Docked": 1}}
    # where it says endpoint, put the specific section you are publishing to from above
    r = requests.patch(ENDPOINT, json=data, headers=headers)

    # if you want to publish that you have undocked:
    data = {"fields": {"Robot Docked": 0}}

    r = requests.patch(ENDPOINT, json=data, headers=headers)


def main():
    for i in range(10):
        print(i)
        print(data2["records"][i]["fields"]["Step"])
    return


if __name__ == "__main__":
    main()
