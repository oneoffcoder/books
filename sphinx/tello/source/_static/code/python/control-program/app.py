import tello
from ui import TelloUI


def main():
    drone = tello.Tello('', 8889)  
    vplayer = TelloUI(drone)
    vplayer.root.mainloop() 


if __name__ == "__main__":
    main()
