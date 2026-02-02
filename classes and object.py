class Student:
    # Constructor to initialize attributes
    def _init_(self, id, name, marks):
        self.id = id
        self.name = name
        self.marks = marks

    # Method to display attribute values
    def display(self):
        print("Student ID is :", self.id)
        print("Student Name is :", self.name)
        print("Student Marks is :", self.marks)

# Driver Code
obj = Student(101, "mohini", 82.5)  # Create object and pass attribute values
obj.display()  # Call the method using the object