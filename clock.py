import time
import simpleaudio as sa

class Clock:
    def __init__(self):
        pass

    def set_timer(self, t):
        self._timer(t)

    def _play_beep(self):
        wave_obj = sa.WaveObject.from_wave_file("src/beep_my.wav")
        play_obj = wave_obj.play()
        #play_obj.wait_done()
        time.sleep(1)

    def _timer(self, t):
        while t:
            mins, secs = divmod(t, 60)
            display = '{:2d}:{:2d}'.format(mins, secs)
            print(display, end='\r')
            time.sleep(1)
            t -= 1
        print("finished!")
        self._play_beep()