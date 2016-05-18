class Box:
    bw = int(input("Please enter the width of a box."))
    bh = int(input("Enter the height of the box."))
    bl = int(input("Enter the length of the box."))
    bvolume = int(bw*bh*bl)
    bsa = int((2*bl) * (2*bh) + (2*bw) * (2*bh))
    print("Your volume was " + str(bvolume))
    print("Your surface area was " + str(bsa))
