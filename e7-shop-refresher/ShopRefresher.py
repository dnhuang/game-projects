import pyautogui
import time
import random

# helper methods
def scan_cov_or_mystic(item):
    def scan_cov():
        try:
            # do dark version first, then light version
            # dark version
            cov_location = pyautogui.locateCenterOnScreen("images/cov_and_price_dark_img.png",
                                                          grayscale=True, confidence=0.95)
            mouse_location = cov_location.x + 470, cov_location.y + 15 # this is a tuple, can be indexed into
            offset_location = randomize_coordinate(mouse_location)
            return offset_location
        except:
            pass

        try:
            # light version
            cov_location = pyautogui.locateCenterOnScreen("images/cov_and_price_light_img.png",
                                                          grayscale=True, confidence=0.95)
            mouse_location = cov_location.x + 470, cov_location.y + 15
            offset_location = randomize_coordinate(mouse_location)
            return offset_location
        except:
            return 0
            
    def scan_mystic():
        #### NEED TO ADD LIGHT VERSION ####
        try:
            mystic_location = pyautogui.locateCenterOnScreen("images/mystic_and_price_dark_img.png",
                                                             grayscale=True, confidence=0.95)
            mouse_location = mystic_location.x + 470, mystic_location.y + 15
            offset_location = randomize_coordinate(mouse_location)
            return offset_location
        except:
            pass
        
        try:
            # light version
            mystic_location = pyautogui.locateCenterOnScreen("images/mystic_and_price_light_img.png",
                                                             grayscale=True, confidence=0.95)
            mouse_location = mystic_location.x + 470, mystic_location.y + 15
            offset_location = randomize_coordinate(mouse_location)
            return offset_location
        except:
            return 0
            
    # begin function
    if item=="cov":
        return scan_cov()
    else:
        return scan_mystic()

def buy(coord, item):
    def confirm_cov():
        cov_confirm_button = pyautogui.locateCenterOnScreen("images/cov_buy_button.png",
                                                            grayscale=True, confidence=0.95)
        offset_cov_confirm_button = randomize_coordinate((cov_confirm_button.x, cov_confirm_button.y))
        return offset_cov_confirm_button
    
    def confirm_mystic():
        mystic_confirm_button = pyautogui.locateCenterOnScreen("images/mystic_buy_button.png",
                                                            grayscale=True, confidence=0.95)
        offset_mystic_confirm_button = randomize_coordinate((mystic_confirm_button.x, mystic_confirm_button.y))
        return offset_mystic_confirm_button
    
    # begin function
    pyautogui.moveTo(coord) # move to determined coord from scan_cov_and_mystic()
    pyautogui.click() # press buy button
    time.sleep(1)

    # need to confirm depending on type of item
    if item=="cov": # use images for cov
        confirm_button = confirm_cov()
    else: # use images for mystic
        confirm_button = confirm_mystic()
    
    # confirm button coord found, need to move and press
    pyautogui.moveTo(confirm_button)
    pyautogui.click() # this buys the item we good to scan again
    time.sleep(1)

def refresh():
    # press refresh button
    refresh_button = pyautogui.locateCenterOnScreen("images/refresh_button.png",
                                                    grayscale=True, confidence=0.95)
    offset_refresh_button = randomize_coordinate((refresh_button.x, refresh_button.y))
    pyautogui.moveTo(offset_refresh_button)
    pyautogui.click()
    time.sleep(1)

    # press confirm refresh button
    refresh_confirm_button = pyautogui.locateCenterOnScreen("images/refresh_confirm_button.png",
                                                            grayscale=True, confidence=0.95)
    offset_refresh_confirm_button = randomize_coordinate((refresh_confirm_button.x, refresh_confirm_button.y))
    pyautogui.moveTo(offset_refresh_confirm_button)
    pyautogui.click()

# helper function to drag down to scan for more cov/mystic
def drag_down():
    start_coord = randomize_coordinate((1700, 900))
    pyautogui.moveTo(start_coord)
    pyautogui.mouseDown(button="left")
    pyautogui.dragTo(start_coord[0], start_coord[1]-700, duration=0.5)

def randomize_coordinate(coord):
    x = coord[0] + random.randrange(-100, 101)
    y = coord[1] + random.randrange(-5, 6)
    return (x, y)
    

### BEGIN OPERATION
while True:
    try:
        def scan_and_buy():
            num_bought = 0
            # scan - scan cov, then scan mystic
            scan_coord = scan_cov_or_mystic("cov")
            if scan_coord: # covenant bookmark found
                buy(scan_coord, "cov")
                num_bought += 1

            # scan for mystic
            scan_coord = scan_cov_or_mystic("mystic") # if nothing found, false is returned, resseting the results from cov
            if scan_coord:
                buy(scan_coord, "mystic")
                num_bought += 1

            # return if we bought things
            return num_bought

        # begin funciotn
        num_bought = scan_and_buy()
        if num_bought < 2: # look for more covs/mystics
            drag_down()
            scan_and_buy()

        print("shop exhausted, waiting to refresh")
        refresh()
        time.sleep(1.5) # NEEDED otherwise will miss
    except KeyboardInterrupt:
        break
    except:
        pass
    