import circle
import rectangle
import square
import triangle

count = 0
suc_count = 0
print("Running geometric lib test protocol")
print("Circle tests:")
count += 1
if circle.perimeter(5) == 31.41592653589793:
    print(f"\tTest%s.Perimeter: Successfully passed." % count)
    suc_count += 1
else:
    print("\tTest%s.Perimeter: Failed" % count)
count += 1
if circle.area(5) == 78.53981633974483:
    print("\tTest%s.Area: Successfully passed." % count)
    suc_count += 1
else:
    print("\tTest%s.Area: Failed")

print("Rectangle tests:")
count += 1
if rectangle.perimeter(4, 5) == 18:
    print("\tTest%s.Perimeter: Successfully passed." % count)
    suc_count += 1
else:
    print("\tTest%s.Perimeter: Failed" % count)
count += 1
if rectangle.area(4, 5) == 20:
    print("\tTest%s.Area: Successfully passed." % count)
    suc_count += 1
else:
    print("\tTest%s.Area: Failed" % count)

print("Square tests:")
count += 1
if square.perimeter(5) == 20:
    print("\tTest%s.Perimeter: Successfully passed." % count)
    suc_count += 1
else:
    print("\tTest%s.Perimeter: Failed" % count)
count += 1
if square.area(5) == 25:
    print("\tTest%s.Area: Successfully passed." % count)
    suc_count += 1
else:
    print("\tTest%s.Area: Failed" % count)

print("Triangle tests:")
count += 1
if triangle.perimeter(3, 4, 5) == 12:
    print("\tTest%s.Perimeter: Successfully passed." % count)
    suc_count += 1
else:
    print("\tTest%s.Perimeter: Failed" % count)
count += 1
if triangle.area(5, 4) == 10:
    print("\tTest%s.Area: Successfully passed." % count)
    suc_count += 1
else:
    print("\tTest%s.Area: Failed" % count)

print("\nSuccessfully passed %s of %s tests." % (count, suc_count))
