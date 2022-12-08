import random, os
# from enums import *
from .enums import *
import easy_pil

class Game:
    """
    # Game
    2048 game!
    
    ## example
    [@see cmd2048](https://github.com/objectiveTM/play2048/tree/main/examples/cmd2048.py)
    """
    def __init__(self, spown = lambda :(4 if random.randint(0, 10) == 0 else 2)) -> None:
        self.arr = [[0 for i in range(4)] for i in range(4)]
        self.point = 0
        self.spown = spown
        w = 0

        try:
            pos = self._random()
            self.arr[pos[0]][pos[1]] = self.spown()
        except:pass
    
    def move(self , key:move, _debug = False):
        if key == move.UP:
            pos = {'x': 0, 'y': 0}
            where = [0 for i in range(4)]
            before = False
            for i in self.arr:
                pos['x'] = 0
                for j in i:
                    if self.arr[pos['y']][pos['x']] != 0:
                        if before:
                            save = self.arr[pos['y']][pos['x']]
                            self.arr[pos['y']][pos['x']] = 0
                            w = 0
                            
                            if self.arr[where[pos['x']]-1][pos['x']] == save and not _debug and where[pos['x']]-1 != -1: 
                                save *= 2
                                self.point += save
                                w = 1
                                ...

                            self.arr[where[pos['x']]-w][pos['x']] = save
                        where[pos['x']] += 1
                        
                    pos['x'] += 1
                before = True
                pos['y'] += 1
                
                    
        elif key == move.DOWN:
            pos = {'x': 0, 'y': 3}
            where = [3 for i in range(4)]
            before = False
            for i in self.arr[::-1]:
                pos['x'] = 0
                for j in i:
                    if self.arr[pos['y']][pos['x']] != 0:
                        if before:
                            save = self.arr[pos['y']][pos['x']]
                            self.arr[pos['y']][pos['x']] = 0
                            w = 0
                            try:
                                if self.arr[where[pos['x']]+1][pos['x']] == save and not _debug: 
                                    save *= 2
                                    self.point += save
                                    w = 1
                            except: ...
                            self.arr[where[pos['x']]+w][pos['x']] = save
                        where[pos['x']] -= 1
                        
                    pos['x'] += 1
                before = True
                pos['y'] -= 1
            
        elif key == move.LEFT:
            
            
            pos = {'x': 0, 'y': 0}
            where = [0 for i in range(4)]
            before = False
            for i in self.arr:
                pos['y'] = 0
                for j in i:
                    if self.arr[pos['y']][pos['x']] != 0:
                        if before:
                            save = self.arr[pos['y']][pos['x']]
                            self.arr[pos['y']][pos['x']] = 0
                            w = 0
                            try:
                                if self.arr[pos['y']][where[pos['y']]-1] == save and not _debug and where[pos['y']]-1 != -1: 
                                    save *= 2
                                    self.point += save
                                    w = 1
                            except: ...
                            self.arr[pos['y']][where[pos['y']]-w] = save
                        where[pos['y']] += 1
                    pos['y'] += 1
                before = True
                pos['x'] += 1
                    
        elif key == move.RIGHT:
            pos = {'x': 3, 'y': 0}
            where = [3 for i in range(4)]
            before = False
            for i in self.arr:
                pos['y'] = 0
                for j in i:
                    if self.arr[pos['y']][pos['x']] != 0:
                        if before:
                            save = self.arr[pos['y']][pos['x']]
                            self.arr[pos['y']][pos['x']] = 0
                            w = 0
                            try:
                                if self.arr[pos['y']][where[pos['y']]+1] == save and not _debug: 
                                    save *= 2
                                    self.point += save
                                    w = 1
                            except: ...
                            
                            self.arr[pos['y']][where[pos['y']]+w] = save
                        where[pos['y']] -= 1
                    pos['y'] += 1
                before = True
                pos['x'] -= 1
                
                
                    
        if not _debug:
            self.move(key, True)
            try:
                pos = self._random()
                self.arr[pos[0]][pos[1]] = self.spown()
            except:pass
        
    def _random(self) -> tuple[int]: 
        # return 0
        pos = (random.randint(0, 3), random.randint(0, 3))
        if self.arr[pos[0]][pos[1]] != 0:
            return self._random()
        else:
            return pos
    
    def encodingText(self) -> str:
        re = ""
        for i in self.arr:
            for j in i:
                re += f"{j} "
            re += "\n"
        
        return re
    
    def encodingImage(self, custom: Custom = customs.ORIGINAL.value) -> easy_pil.Editor:
        size = 500
        padding = 10
        blockSize = int((size - padding*5)/4)
        pos = [0, 0]
        img = easy_pil.Editor(easy_pil.Canvas(color = custom.bg, size = (size, size)))
        for i in self.arr:
            pos[0] = 0
            pos[1] += padding
            for j in i:
                pos[0] += padding
                try: color = custom.__getattribute__(f"_{j}")
                except: color = custom.none
                cnv = easy_pil.Editor(easy_pil.Canvas(color = color, size = (blockSize, blockSize)))
                if j != 0:
                    ln = len(str(j))-1
                    
                    fsize = blockSize-10
                    tsize = 3
                    
                    if ln == 1:
                        fsize = blockSize-20
                        tsize = 7
                        
                    if ln == 2:
                        fsize = blockSize-45
                        tsize = 7
                    
                    if ln == 3:
                        fsize = blockSize-70
                        tsize = 5
                    
                    if ln == 4:
                        fsize = blockSize-80
                        tsize = 1
                        
                    
                    font = easy_pil.Font.poppins(size = fsize)
                    top = 15 + ln*10 - (8 if ln != 0 else 0)
                    try:fontColor = custom.__getattribute__(f"font_{j}")
                    except:fontColor = custom.font
                    cnv.text(position = (blockSize/2, top+tsize), text = str(j), color = fontColor, font = font, align = "center")
                img.paste(cnv, position=(pos[0], pos[1]))
                pos[0] += blockSize
            pos[1] += blockSize
            
        
        return img
        
        
    
    
            
        
if __name__ == "__main__":
    os.system("cls")
    
    g = Game()
    g.encodingImage().show()
    
    print(f"point: {g.point}")
    print(g.encodingText())
    while True:
        def asdf():
            global m
            
            inp = input("where to move? wasd: ")
            if inp.lower() == "w": m = move.UP
            elif inp.lower() == "s": m = move.DOWN
            elif inp.lower() == "a": m = move.LEFT
            elif inp.lower() == "d": m = move.RIGHT
            else:
                print("Please re-enter!")
                asdf()
                
        asdf()
        os.system("cls")
        print(f"point: {g.point}")
        g.move(m)
        print("\n")
        print(g.encodingText())
        
        
    
    print(g.encodingText())
