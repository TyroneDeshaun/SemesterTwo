print ("Welcome to shape maker! Let's find volume and surface area for a few shapes.")
print ("Three shapes currently available. Box, Sphere, and Pyramid.")
choice = str(input("Type which shape you want to do. (Caps matters!) "))
if choice == str("Box"):
    import box.py
elif choice == str("Sphere"):
    import Sphere.py
elif choice == str("Pyramid"):
    import Pyramid.py
else:
    print("Your input was not one of the three shapes.(Check caps!)")
    







    
