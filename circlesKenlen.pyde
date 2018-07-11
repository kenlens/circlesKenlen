def setup():
    size(500, 500)
    background(188, 143, 143)
    
def draw():
    size = random(10, 80)
    if mouseX < 250:
        fill(255, 0, 0)
    else:
        fill(0, 0, 255)
    ellipse(250, 100, size, size) # top middle circle
    ellipse(400, 100, size, size) # top right circle
    ellipse(100, 100, size, size) # top left circle
    stroke(255, 255, 255)
    
    if mouseX < 250 and mouseY > 250:
        fill(255, 182, 193)         # light pink color
    elif mouseX > 250 and mouseY > 250:
        fill( 25, 25, 112)        # navy blue color
    elif mouseX > 250 and mouseY < 250:
        fill(0, 0, 63)            # other navy blue color
        
        fill(222, 184, 135)
    ellipse(250, 250, size, size) # middle circle
    ellipse(100, 250, size, size) # middle left circle
    ellipse(400, 250, size, size) # middle right circle
    
    if mouseX < 250 :
        fill(205, 92, 92)
    else: 
        fill(0, 255, 197)
    ellipse(100, 400, size, size) # bottom left circle
    ellipse(250, 400, size, size) # bottom middle circle
    ellipse(400, 400, size, size) # bottom right circle
    stroke(255, 255, 255)
    
