import sys, math

if len(sys.argv) != 3:
    print("Необходимо указать 2 аргумента коммандной строки\nВ качестве аргументов принимаются пути к файлам"
          "\nExample: python task2.py path_to_file1 path_to_file2")
    exit(1)

with open(sys.argv[1], 'r') as circleFile:
    values = circleFile.readlines()

circleXY = list(map(int, values[0].split(sep=' ')))
circleRadius = int(values[1])

pointsXY = []
with open(sys.argv[2], 'r') as pointsFile:
    while True:
        values = pointsFile.readline()
        if not values:
            break
        pointsXY.append(list(map(int, values.split(sep=' '))))


def calculate_point_pos(circle_xy, point_xy, radius):
    distance = math.sqrt((circle_xy[0] - point_xy[0]) ** 2 + (circle_xy[1] - point_xy[1]) ** 2)

    if distance == radius:
        return 0
    elif distance < radius:
        return 1
    else:
        return 2


for i in range(len(pointsXY)):
    print(calculate_point_pos(circleXY, pointsXY[i], circleRadius))
