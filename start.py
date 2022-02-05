import random

def main() :
    # print("how do you do?\n")

    f = open("image0.ppm", "w")
    f.write("P3\n500 500\n")
    for i in range(500):
        for j in range(500):
            r = random.randint(0,256)
            g = random.randint(0,256)
            b = random.randint(0,256)
            # r = 100
            # g = 200
            # b = 150
            f.write(str(r) + " " + str(g) + " " + str(b) + " ")
        f.write("\n")
    f.close()

main()