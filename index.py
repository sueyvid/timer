from clock import Clock

def main():
    c = Clock()
    seconds = True
    while seconds:
        seconds = int(input("Time in seconds (tap 0 to exit): "))
        c.set_timer(seconds)

if __name__ == "__main__":
    main()