import pygame
import random
import time
import os
import sys

def play_random(filePath, duration):

    pygame.mixer.init()

    songNames = [
        entry for entry in os.listdir(filePath) 
            if os.path.isfile
                (
                    os.path.join(filePath, entry)
                )
            ]
    
    numFiles = len(songNames)
    # print("picking from ", numFiles, "songs!")

    random_num = random.randint(0, numFiles-1)
    pygame.mixer.music.load(f"{filePath}/{songNames[random_num]}")
    
    if not duration :
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.play()
        time.sleep(duration)
        pygame.mixer.music.stop()
    
    guess = input("Title?: ").lower().strip()

    if guess in songNames[random_num].lower().strip():
        print("Correct!")
        return 1
    else:
        print("wrong! the song was: ", songNames[random_num])
        return 0

def main():
    points = 0
    # print(len(sys.argv))
    if not len(sys.argv) == 4:
        print("Usage: python music.py <path to folder of MP3 files> <duration to play songs (in seconds)> <number of rounds>")
        sys.exit(1)
    else:
        sys.argv[1] = sys.argv[1].strip()
        sys.argv[2] = float(sys.argv[2].strip())
        sys.argv[3] = int(sys.argv[3].strip())
        # filePath = '/home/dumbhead/Desktop/test/MOBO/'
        for i in range(sys.argv[3]):
            if play_random(sys.argv[1], sys.argv[2]):
                points += 1
            else:
                pass
        print("you got a", str(points/sys.argv[3] * 100) + "%!")

if __name__ == "__main__":
    main()
