from clock import Clock

def main():
    c = Clock()
    seconds = int(input("Time in seconds: "))
    c.set_timer(seconds)

if __name__ == "__main__":
    main()