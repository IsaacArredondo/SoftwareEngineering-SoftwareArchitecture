from professor import Professor
from enroll import Enroll
from aifc import Error

class Course:
    def __init__(self, name, code, min_, max_, professor):
        self.name = name
        self.code = code
        self.max = max_
        self.min = min_
        self.professors = []
        self.enrollments = []

        if isinstance(professor, Professor):
            self.professors.append(professor)
        elif isinstance(professor, list):
            for entry in professor:
                if not isinstance(entry, Professor):
                    raise Error("Invalid professor...")

            self.professors = professor
        else:
            raise Error("Invalid professor...")

    def add_professor(self, professor):
        if not isinstance(professor, Professor):
            raise Error("Invalid proffesor...")

        self.professors.append(professor)

    def add_enrollment(self, enroll):
        if not isinstance(enroll, Enroll):
            raise Error("Invalid Enroll...")

        if len(enrollments) == self.max:
            raise Error("Cannot enroll, course if full...")

        self.enrollments.append(enroll)

    def is_cancelled(self):
        return len(self.enrollments) < self.min
