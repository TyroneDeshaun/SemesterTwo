class Pyramid:
    pw = int(input("Please enter the width of a pyramid."))
    ph = int(input("Enter the height of the pyramid."))
    pl = int(input("Enter the length of the pyramid."))
    pvolume = int((pw * ph * pl) / 3)
    psa = int((pw*ph/2) + (pw*pl))
    print("Your volume was " + str(pvolume))
    print("Your surface area was " + str(psa))
