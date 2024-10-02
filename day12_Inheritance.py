class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):

    # Class Constructor
    #
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName: str, lastName: str, idNumber: int, scores: list[int]):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self) -> str:
        average_score = sum(self.scores) / len(self.scores)
        assert 0 <= average_score <= 100, "Average out of bounds, should be 0 <= avg(scores) <= 100."

        match average_score:
            case avg if 90 <= avg <= 100:
                return 'O'
            case avg if 80 <= avg < 90:
                return 'E'
            case avg if 70 <= avg < 80:
                return 'A'
            case avg if 55 <= avg < 70:
                return 'P'
            case avg if 40 <= avg < 55:
                return 'D'
            case avg if avg < 40:
                return 'T'


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = int(line[2])
numScores = int(input())  # not needed for Python
scores = list(map(int, input().split()))
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
