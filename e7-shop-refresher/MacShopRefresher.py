import pyautogui
import time
import random
### pyautogui.moveTo((coord.x + 1490)/2, coord.y/2+30) ###

# Takes in a String item, if "covs", function scans screen for covenant bookmarks and
# returns its offset coordinates, otherwise scans screen for mystic bookmarks and
# returns its offset coordinates. If neither covenants or mystics are found, an integer
# of 0 is returned.

### REASON WHY COORDS NEED TO BE DIVIDED BY 2:
### https://stackoverflow.com/questions/43606520/pyautogui-locate-command-returning-incorrect-coordinates-for-image-recognition

def scan(item):
    def get_buy_coord(item):
        try:
            item_location = pyautogui.locateCenterOnScreen("mac/" + item + ".png",
                                                          grayscale=True, confidence=0.95)
            buy_location = (item_location.x+1490)/2, item_location.y/2+30 # this is a tuple, can be indexed into
            offset_buy_location = randomize_coordinate(buy_location)
            return offset_buy_location
        except:
            return 0
        
    # begin function
    return get_buy_coord(item)

def buy(buy_coord, item):
    def get_confim_coord(item):
        confirm_button = pyautogui.locateCenterOnScreen("mac/" + item + "_confirm.png",
                                                            grayscale=True, confidence=0.95)
        offset_confirm_button = randomize_coordinate((confirm_button.x/2, confirm_button.y/2))
        return offset_confirm_button    

    # begin function
    ### PRESSING THE FIRST BUY BUTTON ###
    pyautogui.moveTo(buy_coord) # move to determined coord from scan()
    pyautogui.click() # press buy button
    time.sleep(0.5)

    ### PRESSING THE CONFIRM BUY BUTTON ###
    confirm_button = get_confim_coord(item)
    
    # confirm button coord found, need to move and press
    pyautogui.moveTo(confirm_button)
    pyautogui.click() # this buys the item we good to scan again
    time.sleep(0.5)

def scan_and_buy(cov_bought, mystic_bought):
    # scan - scan cov, then scan mystic
    if not cov_bought:
        scan_coord = scan("cov")
        if scan_coord: # covenant bookmark found
            buy(scan_coord, "cov")
            cov_bought = True

    # scan for mystic
    if not mystic_bought:
        scan_coord = scan("mystic") # if nothing found, false is returned, resseting the results from cov
        if scan_coord:
            buy(scan_coord, "mystic")
            mystic_bought = True
    return (cov_bought, mystic_bought)

def refresh():
    # press refresh button
    refresh_button = pyautogui.locateCenterOnScreen("mac/refresh.png",
                                                    grayscale=True, confidence=0.95)
    offset_refresh_button = randomize_coordinate((refresh_button.x/2, refresh_button.y/2))
    pyautogui.moveTo(offset_refresh_button)
    pyautogui.click()
    time.sleep(0.5)

    # press confirm refresh button
    refresh_confirm_button = pyautogui.locateCenterOnScreen("mac/refresh_confirm.png",
                                                            grayscale=True, confidence=0.95)
    offset_refresh_confirm_button = randomize_coordinate((refresh_confirm_button.x/2, refresh_confirm_button.y/2))
    pyautogui.moveTo(offset_refresh_confirm_button)
    pyautogui.click()

# helper function to drag down to scan for more cov/mystic
def drag_down():
    start_coord = randomize_coordinate((1200, 800))
    pyautogui.moveTo(start_coord)
    pyautogui.mouseDown(button="left")
    pyautogui.dragTo(start_coord[0], start_coord[1]-400, button='left', duration=0.5)

def randomize_coordinate(coord):
    x = coord[0] + random.randrange(-100, 101)
    y = coord[1] + random.randrange(-10, 11)
    return (x, y)
    

### BEGIN OPERATION

cov_bought = False
mystic_bought = False
while True:
    try:
        # begin function
        results = scan_and_buy(cov_bought, mystic_bought)
        cov_bought = results[0]
        mystic_bought = results[1]
        if not cov_bought or not mystic_bought:
            drag_down()
            results = scan_and_buy(cov_bought, mystic_bought)
        
        cov_bought = False
        mystic_bought = False
        refresh()
        time.sleep(0.5) # NEEDED otherwise will miss
    except KeyboardInterrupt:
        break
    except:
        pass
    