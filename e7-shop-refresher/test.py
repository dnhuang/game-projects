import pyautogui

coord = pyautogui.locateCenterOnScreen("images/edit_button.png",
                                       grayscale=True, confidence=0.5)
offset_coord = coord.x + 10, coord.y+10
print(offset_coord)
print(type(offset_coord))
print(offset_coord[1])