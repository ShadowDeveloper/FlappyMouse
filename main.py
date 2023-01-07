import keyboard
import pyautogui
startingYVel = -5
startingXVel = 2
yVel = startingYVel
xVel = startingXVel
terminalVel = 10
yChange = 0.5
jumpHeight = 10
jumpKey = input("What key should make you jump(all caps)")

toggleKey = input("What key should be the toggle key? (All caps)")
checksPressed = 0
togglePressed = 0
isToggled = False
screenX, screenY = pyautogui.size()
def tryJump():
    global yVel
    global checksPressed

    if keyboard.is_pressed(jumpKey):
        if checksPressed == 0:
            yVel -= jumpHeight
        checksPressed += 1
    else:
        checksPressed = 0



while True:
    if keyboard.is_pressed(toggleKey):
        if togglePressed == 0:
            isToggled = not isToggled
        togglePressed += 1
    else:
        togglePressed = 0
    if isToggled:
        pyautogui.moveRel(xVel, yVel)
        if yVel < terminalVel:
            yVel += yChange
        tryJump()
        mouseX, mouseY = pyautogui.position()
        if mouseX <= 0 or mouseX >= screenX:
            pyautogui.moveTo(screenX/2, mouseY)
        if mouseY <= 0:
            yVel = terminalVel/10
        if mouseY >= screenY-1:
            pyautogui.moveTo(screenX / 4, screenY / 2)
            yVel = startingYVel
