from bmp import ReadBMP, WriteBMP

class ImageProcesser:
    def __init__(self, filename):
        self.pixelgrid = ReadBMP(filename)
        self.height = len(self.pixelgrid)
        self.width = len(self.pixelgrid[0])

    def save(self, newName):
        WriteBMP(self.pixelgrid, newName)

    def invert(self):
        for row in range(self.height):
            for col in range(self.width):
                self.pixelgrid[row][col] = [255 - value for value in self.pixelgrid[row][col]]

    def displayChannel(self, channel):
        for row in range(self.height):
            for col in range(self.width):
                if channel == 'r':
                    self.pixelgrid[row][col][1] = 0
                    self.pixelgrid[row][col][2] = 0
                elif channel == 'g':
                    self.pixelgrid[row][col][0] = 0
                    self.pixelgrid[row][col][2] = 0
                elif channel == 'b':
                    self.pixelgrid[row][col][0] = 0
                    self.pixelgrid[row][col][1] = 0

    def flip(self, axis):
        if axis == 'v':
            self.pixelgrid = self.pixelgrid[::-1]
        elif axis == 'h':
            self.pixelgrid = [row[::-1] for row in self.pixelgrid]

    def grayscale(self):
        for row in range(self.height):
            for col in range(self.width):
                gray = sum(self.pixelgrid[row][col]) // 3
                self.pixelgrid[row][col] = [gray, gray, gray]

    def brightness(self, operation):
        for row in range(self.height):
            for col in range(self.width):
                if operation == '+':
                    self.pixelgrid[row][col] = [min(value + 25, 255) for value in self.pixelgrid[row][col]]
                elif operation == '-':
                    self.pixelgrid[row][col] = [max(value - 25, 0) for value in self.pixelgrid[row][col]]

    def contrast(self):
        c = 45
        factor = 259 * (c + 255) / (255 * (259 - c))
        for row in range(self.height):
            for col in range(self.width):
                for i in range(3):
                    new_value = int(factor * (self.pixelgrid[row][col][i] - 128) + 128)
                    self.pixelgrid[row][col][i] = max(0, min(new_value, 255))

def main():
    filename = input("Enter filename containing source image (must be .bmp): ")
    image_processor = ImageProcesser(filename)

    while True:
        print("==============================")
        print("Python Basic Image Processer")
        print("==============================")
        print("a) Invert Colors")
        print("b) Flip Image")
        print("c) Display color channel")
        print("d) Convert to grayscale")
        print("e) Adjust brightness")
        print("f) Adjust contrast")
        print("s) SAVE current image")
        print("o) Open new image")
        print("q) Quit")
        print("==============================")
        choice = input("(a/b/c/d/e/f/s/o/q): ")

        if choice == 'a':
            image_processor.invert()
        elif choice == 'b':
            axis = input("Enter axis to flip (h for horizontal, v for vertical): ")
            image_processor.flip(axis)
        elif choice == 'c':
            channel = input("Enter channel to display (r/g/b): ")
            image_processor.displayChannel(channel)
        elif choice == 'd':
            image_processor.grayscale()
        elif choice == 'e':
            while True:
                operation = input("[+] increase brightness\n[-] decrease brightness\n[q] exit\n(+/-/q): ")
                if operation == '+':
                    image_processor.brightness('+')
                elif operation == '-':
                    image_processor.brightness('-')
                elif operation == 'q':
                    break
        elif choice == 'f':
            image_processor.contrast()
        elif choice == 's':
            new_filename = input("Enter name for edited picture (must have .bmp extension): ")
            image_processor.save(new_filename)
        elif choice == 'o':
            filename = input("Enter filename containing source image (must be .bmp): ")
            image_processor = ImageProcesser(filename)
        elif choice == 'q':
            break

if __name__ == "__main__":
    main()
