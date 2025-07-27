import time
import os
import play_audio as pa

class Clock:
    def __init__(self):
        pass

    def set_timer(self, t):
        self._timer(t)

    def _timer(self, t):
        while t:
            mins, secs = divmod(t, 60)
            self._print(mins, secs)
            time.sleep(1)
            t -= 1
        else:
            self._print(msg="Timer finished!")
            pa.play("src/beep_my.wav")
            os.system('cls' if os.name == 'nt' else 'clear')

    def _set_print(self, mins, secs):
        if secs < 10:
            display = 'Timer: {:2d}:0{:1d}'.format(mins, secs)
        elif mins < 10:
            display = 'Timer: 0{:1d}:{:2d}'.format(mins, secs)
        else:
            display = 'Timer: {:2d}:{:2d}'.format(mins, secs)
        if secs < 10 and mins < 10:
            display = 'Timer: 0{:1d}:0{:1d}'.format(mins, secs)

        return display
    
    def _print(self, mins=0, secs=0, msg=""):
        display = self._set_print(mins, secs)
        print(display, end='\r')
        if msg:
            print(msg)

    def _clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')