import pyautogui
import time

# helper methods
def scan_cov_and_mystic(item):
    def scan_cov():
        try:
            cov_location = pyautogui.locateCenterOnScreen("images/cov_and_price_img.png",
                                                          grayscale=True, confidence=0.95)
            mouse_location = cov_location.x + 470, cov_location.y + 42
            return mouse_location
        except:
            return False
            
    def scan_mystic():
        try:
            mystic_location = pyautogui.locateCenterOnScreen("images/mystic_and_price_img.png",
                                                             grayscale=True, confidence=0.95)
            mouse_location = mystic_location.x + 470, mystic_location.y + 42
            return mouse_location
        except:
            return False
    if item=="cov":
        scan_cov()
    else:
        scan_mystic()

def buy(coord, item):
    def confirm_cov():
        cov_confirm_button = pyautogui.locateCenterOnScreen("images/cov_buy_button.png",
                                                            grayscale=True, confidence=0.95)
        return cov_confirm_button
    def confirm_mystic():
        mystic_confirm_button = pyautogui.locateCenterOnScreen("images/mystic_buy_button.png",
                                                            grayscale=True, confidence=0.95)
        return mystic_confirm_button
    
    pyautogui.moveTo(coord) # move to determined coord from scannin
    pyautogui.click() # press buy button

    # need to confirm depending on type of item
    if item=="cov": # use images for cov
        confirm_button = confirm_cov()
    else: # use images for mystic
        confirm_button = confirm_mystic()
    
    # confirm button coord found, need to move and press
    pyautogui.moveTo(confirm_button)
    pyautogui.click() # this buys the item we good to sca again

def refresh():
    # press refresh button
    refresh_button = pyautogui.locateCenterOnScreen("images/refresh_button.png",
                                                    grayscale=True, confidence=0.95)
    pyautogui.moveTo(refresh_button)
    pyautogui.click()

    # press confirm refresh button
    refresh_confirm_button = pyautogui.locateCenterOnScreen("images/refresh_confirm_button.png",
                                                            grayscale=True, confidence=0.95)
    pyautogui.moveTo(refresh_confirm_button)
    pyautogui.click()

# helper function to drag down to scan for more cov/mystic
def drag_down():
    pyautogui.moveTo(1700, 900)
    pyautogui.mouseDown(button="left")
    pyautogui.dragTo(1700, 200, duration=0.5)
    

### BEGIN OPERATION
while (True):
    def scan_and_buy():
        num_bought = 0
        # scan - scan cov, then scan mystic
        scan_coord = scan_cov_and_mystic("cov")
        if scan_coord: # covenant bookmark found
            buy(scan_coord, "cov")
            num_bought += 1

        # scan for mystic
        scan_coord = scan_cov_and_mystic("mystic") # if nothing found, false is returned, resseting the results from cov
        if scan_coord:
            buy(scan_coord, "mystic")
            num_bought += 1
        
        # return if we bought things
        return num_bought


    num_bought = scan_and_buy()
    if num_bought < 2: # look for more covs/mystics
        drag_down()
        scan_and_buy()

    print("shop exhausted, waiting to refresh")
    time.wait(5)
    refresh()
    
### FOR MYSTIC ###
#test_location = pyautogui.locateOnScreen("images/mystic_and_price_img.png",
                                         #grayscale=True, confidence=0.95)

#test_center_loc = pyautogui.center(test_location)
#print(test_center_loc)
# https://stackoverflow.com/questions/65873960/useing-pyautogui-how-to-append-a-value-to-the-coordinates-from-locatecenteronsc
# Point object is immutable, need to create a new one to offset
#button_offset = test_center_loc.x + 620, test_center_loc.y + 85
#print(button_offset)
#print(test_location)
#pyautogui.moveTo(button_offset)

#res = pyautogui.locateOnScreen("images/test_img.png")
#print(res)
#test_button = pyautogui.center(res)
#pyautogui.moveTo(test_button)

#refresh_location = pyautogui.locateOnScreen("images/refresh.png")
#print(refresh_location)


#test_location = pyautogui.locateOnScreen("images/test2.png")
#print(test_location)


### FOR MYSTIC ###
#test_location = pyautogui.locateOnScreen("images/mystic_and_price_img.png",
                                         #grayscale=True, confidence=0.95)

#test_center_loc = pyautogui.center(test_location)
#print(test_center_loc)
# https://stackoverflow.com/questions/65873960/useing-pyautogui-how-to-append-a-value-to-the-coordinates-from-locatecenteronsc
# Point object is immutable, need to create a new one to offset
#button_offset = test_center_loc.x + 620, test_center_loc.y + 85
#print(button_offset)
#print(test_location)
#pyautogui.moveTo(button_offset)

### FOR MYSTIC BUY BUTTON ###
#mystic_buy_button = pyautogui.locateOnScreen("images/mystic_buy_button.png",
 #                                              grayscale=True, confidence=0.95)
#center_mystic_buy_button = pyautogui.center(mystic_buy_button)
#print(center_mystic_buy_button)
#pyautogui.moveTo(center_mystic_buy_button)


### FOR REFRESH ###
#refresh_confirm_button = pyautogui.locateCenterOnScreen("images/refresh_confirm_button.png",
                                                        #grayscale=True,confidence=0.95)
#print(refresh_confirm_button)
#pyautogui.moveTo(refresh_confirm_button)

#refresh_button = pyautogui.locateCenterOnScreen("images/refresh_button.png",
                                                #grayscale=True, confidence=0.95)
#print(refresh_button)
#pyautogui.moveTo(refresh_button)

### FOR COV ###
#cov_location = pyautogui.locateCenterOnScreen("images/cov_and_price_img.png",
#                                                        grayscale=True,confidence=0.95)
#print(cov_location)
#pyautogui.moveTo(cov_location)

### COV CONFIRM ###
#cov_confim_button = pyautogui.locateCenterOnScreen("images/cov_buy_button.png",
#                                                   grayscale=True, confidence=0.95)
#print(cov_confim_button)
#pyautogui.moveTo(cov_confim_button)

### for keyboard D input
#pyautogui.moveTo(1700, 900)
#pyautogui.mouseDown(button="left")
#pyautogui.dragTo(1700, 200, duration=0.5)
