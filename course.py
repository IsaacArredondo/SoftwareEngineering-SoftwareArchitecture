from professor import Professor
from aifc import Error

class Course:
    def __init__(self, name, code, min_, max_, professor):
        self.name = name
        self.code = code
        self.max = max_
        self.min = min_
        self.professors = []

        if isinstance(professor, Professor):
            self.professors.append(professor)
        elif isinstance(professor, list):
            for entry in professor:
                if not isinstance(entry, Professor):
                    raise Error("Invalid professor...")

            self.professors = professor
        else:
            raise Error("Invalid professor...")