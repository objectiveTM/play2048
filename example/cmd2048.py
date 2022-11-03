from play2048 import *
os.system("cls")

g = Game()

print(f"point: {g.point}")
print(g.encodingText())
while True:
    def asdf():
        global m
        
        inp = input("where to move? WASD: ")
        if inp.lower() == "w": m = move.UP
        elif inp.lower() == "s": m = move.DOWN
        elif inp.lower() == "a": m = move.LEFT
        elif inp.lower() == "d": m = move.RIGHT
        else:
            print("Please re-enter!")
            asdf()
            
    asdf()
    os.system("cls")
    print(f"point: {g.point}\n")
    g.move(m)
    print("\n")
    print(g.encodingText())
