
def main():
    h1 = int(input('Type an angle between 0 and 360: '))
    h2 = int(input('Type an angle between 0 and 360: '))
    get_angle(h1, h2)


def get_angle(h1, h2):
    if h1 - h2 < 0:
        angle_1 = abs(h1 - h2)
        print(f"now turn: {angle_1} degrees")
        if h1 < h2 and h2 < angle_1:
            print('turn left')
        else:
            print('turn right')
    else:
        angle_1 = h1 - h2
        print(f'turn {angle_1} degrees')
        if angle_1 < 180:
            print('left turn')
        else:
            print('right turn')

    return


def triangle(angle):
    if angle >= 0 and angle < 90:
        print("This is an acute angle")
    elif angle == 90:
        print("This is a right angle")
    elif angle >= 90 and angle < 180:
        print("This is an obtuse angle")
    elif angle == 180:
        print("This is a straight line")
    elif angle > 180 and angle <= 360:
        print("This is a reflex angle")
    else:
        print("Try again with a value between 0 and 360 degrees")

if __name__ == '__main__':
    main()
