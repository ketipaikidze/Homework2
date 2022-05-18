# დავალება 1

class MyList:
    def __init__(self, data=[]):
        self.data = data

    def __add__(self, other):
        new_list = self.data + other
        return new_list

    def __mul__(self, other):
        new_list = self.data * other
        return new_list

    def __str__(self):
        return f"{self.data}"


l1 = MyList([1, 3, 7])
l2 = MyList([4, 6, 8])


# დავალება 2

class TestPaper:
    def __init__(self, subject, mark_scheme, pass_mark, **kwargs):
        super.__init__(**kwargs)
        self.subject = subject
        self.mark_scheme = mark_scheme
        self.pass_mark = pass_mark

class Student(TestPaper):
    def __init__(self, tests_taken='no tests taken', ** kwargs):
        self.tests_taken = tests_taken
        super.__init__(**kwargs)

    def take_test(self,): pass

    # ეს ვერ გავიგე!!!





