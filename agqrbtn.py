#!/usr/bin/env python3
import subprocess
from aiy.board import Board, Led

def main():
    # init
    play = False

    # main loop
    print('LED is ON while button is pressed (Ctrl-C for exit).')
    with Board() as board:
        while True:
            board.button.wait_for_press()
            board.button.wait_for_release()

            if play == False:
                subprocess.run(['sudo','systemctl','start','agqrplay'])
                board.led.state = Led.ON
                play = True
            else:
                subprocess.run(['sudo','systemctl','stop','agqrplay'])
                board.led.state = Led.OFF
                play = False

if __name__ == '__main__':
    main()
