
score=float(input("Enter the Score: "))
Stop=str(input("Enter Stop to Terminate code:"))
if Stop=="Stop":
    if score >=0.9:
        print("A")
    elif score >=0.8:
        print("B")
    elif score >=0.7:
        print("C")
    elif score >=0.6:
        print("D")
    elif score <0.6:
        print("F")
    print("Bad Mark")
else:
    print("Stopped")
    