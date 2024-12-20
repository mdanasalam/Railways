class Train:
    def __init__(self, trainname, idnumber, platformnumber):
        self.trainname = trainname
        self.idnumber = idnumber
        self.platformnumber = platformnumber

    def show(self):
        # Correctly use instance attributes to print the message
        print(f"The train {self.trainname}, Id no.{self.idnumber} is coming on platform no.{self.platformnumber}")

# Create an object of the Train class
train1 = Train("Rajdhani Express", 4527, 4)

# Call the show method to print the information
train1.show()