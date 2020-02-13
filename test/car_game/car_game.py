command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("the car already started")
        else:
            started = True
            print("car started...")
    elif command == "stop":
        if not started:
            print("the car already stopped")
        else:
            started = False
            print("car stopped...")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit
        """)
    elif command == "quit":
        break
    else:
        print("sorry I don't understand what you command ,please type the 'help' ")