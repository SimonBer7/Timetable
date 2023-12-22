class Lesson:
    """
    The Leason class represents a lesson or class in a timetable.

    Attributes:
    - id (int): The unique identifier for the lesson.
    - name (str): The name or code of the lesson.
    - teacher (str): The name of the teacher or lecturer for the lesson.
    - class_name (str): The class or room where the lesson takes place.
    - floor_number (int): The floor number where the lesson takes place.
    - type (str): The type or category of the lesson (e.g., lecture, exercise).

    Methods:
    - __init__(id, name, teacher, class_name, floor_number, type): Initializes a new instance of the Leason class.
    - __str__(): Returns a string representation of the Leason object.
    - basic_print(): Returns a basic string representation of the lesson for printing.
    """

    def __init__(self, id, name, teacher, class_name, floor_number, type):
        """
        Initializes a new instance of the Leason class.

        Parameters:
        - id (int): The unique identifier for the lesson.
        - name (str): The name or code of the lesson.
        - teacher (str): The name of the teacher or lecturer for the lesson.
        - class_name (str): The class or room where the lesson takes place.
        - floor_number (int): The floor number where the lesson takes place.
        - type (str): The type or category of the lesson (e.g., lecture, exercise).
        """
        self.id = id
        self.name = name
        self.teacher = teacher
        self.class_name = class_name
        self.floor_number = floor_number
        self.type = type

    def __str__(self):
        """
        Returns a string representation of the Leason object.
        """
        print_str = str(self.id) + ".) " + str(self.name) + ", " + str(self.teacher) + ", class: " + str(
            self.class_name) + ", floor: " + str(self.floor_number) + ", type: " + str(self.type)
        return print_str

    def basic_print(self):
        """
        Returns a basic string representation of the lesson for printing.
        """
        return self.name