class Sphere:
    sr = int(input("Please enter the radius of the sphere."))
    svolume = int(((4/3)*(3.14)*(sr**3)))
    ssa = int((4*(3.14)*(sr**2)))
    print("Your volume was " + str(svolume))
    print("Your surface area was " + str(ssa))
