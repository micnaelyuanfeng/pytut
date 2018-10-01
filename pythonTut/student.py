class student(object):
    school        = 'AMD'

    def __init__(self):
        self.__name   = None
        self.__grade  = None
        self.__gender = None
        self.__birth_year = None
        self.__birth_date = None
        self.__list   = ()

    def set_info(self, name, gender, grade):
        self.__name   = name
        self.__gender = gender
        self.__grade  = grade
    
    @property
    def birthday(self) -> str:
        birthday = self.__birth_year + ' ' + self.__birth_date

        return birthday
    
    @birthday.setter
    def birthday(self, year, date):
        self.__birth_year = year
        self.__birth_date = date

    def print_school_info(self):
        print('%s' % self.school)

    def print_info(self):
        print('%s : %s : %s : %s' % (self.__name, self.__grade, self.__gender, self.school))


class highSchoolStudent(student):
    def __init__(self):
        self.__course = None
        self.__list   = ()
    
    def set_info(self, course):
        self.__course = course

    def print_school_info(self):
        print('%s' % self.school)