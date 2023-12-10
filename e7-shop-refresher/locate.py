import pyautogui
import time

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
pyautogui.moveTo(1700, 900)
pyautogui.mouseDown(button="left")
pyautogui.dragTo(1700, 200, duration=0.5)

