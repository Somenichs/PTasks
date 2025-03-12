import sys

if len(sys.argv) != 3:
    print("Необходимо указать 2 аргумента коммандной строки:\nВ качестве аргументов принимаются значения N и M"
          "\nГде N - длина массива, M - длина интервала \nExample: python task1.py 4 3")
    exit(1)
length = int(sys.argv[1])
circleArray = range(1, length + 1)

path = ''
maxSteps = int(sys.argv[2])
currentIndex = 0
currentStep = 0

while True:
    if currentStep == 0:
        path += str(circleArray[currentIndex])

    currentStep += 1

    if currentStep >= maxSteps:
        currentStep = 0
    else:
        currentIndex += 1

    if currentIndex >= len(circleArray):
        currentIndex = 0

    if currentStep == 0 and currentIndex == 0:
        break

print(path)
