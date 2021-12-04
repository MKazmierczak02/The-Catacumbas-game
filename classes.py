class car:
    status = False

    def __init__(self, name):
        self.name = name

    def SetColor(self, color):
        self.color = color

    def SetSpeed(self, speed):
        self.speed = int(speed)

    def SetWheelsInch(self, inch):
        self.wheels = inch

    def Start(self):
        car.status = True

    def Stop(self):
        car.status = False


def menu():
    print("Tap enter to start")
    print("↑ ▉ Drive up ↓ ▉ Drive down ← ▉ Drive left → ▉ Drive right")


EmptyMap = [['▉', '▉''▉', '▉''▉', '▉', '▉', '▉', '▉'], ['▉', '▉', '▉', '▉', '▉', ' ', ' ', ' ', '▉'], [
    '▉', '▉', '▉', '▉', ' ', ' ', '▉', ' ', '▉'], ['▉', '▉', ' ', ' ', ' ', '▉', '▉', ' ', '▉'], ['⚑', ' ', ' ', '▉''▉', '▉', '▉', ' ', '▉'], ['▉', '▉', '▉', '▉', '▉', '▉', '▉', ' ', '▉']]

# ⚑▉

for x in EmptyMap:
    for i in x:
        print(i, end="")
    print()
