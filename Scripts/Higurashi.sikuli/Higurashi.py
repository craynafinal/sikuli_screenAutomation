Settings.MoveMouseDelay = 0
running = True
count = 0
scr1 = Screen(1)

def runHotkey(event):
    global running
    running = False

Env.addHotkey(Key.F1, KeyModifier.ALT, runHotkey)

while(running):
    if ((exists("1507485878000.png", .5) or (exists("1509668195740.png", .5))) and scr1.exists(Pattern("1507491127022.png").exact(), .5)):
        #If tip window shows up, wait
        wait(3)
        #Finding element in second screen
        scr1.doubleClick("1507486006667.png")
        type(Key.F7)
        
        exit()
    elif (exists(Pattern("1507484956784.png").similar(0.50), .5) or exists(Pattern("1507485545706.png").similar(0.55), .5) or exists("1507484935580.png") or count == 10):
        #Regular sequence
        wait(1.5 *  count + 1)
        type(Key.ENTER)
        count = 0
    else:
        count += 1
    wait(1)
        
        
        
        