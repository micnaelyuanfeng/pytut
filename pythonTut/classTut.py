
from student import *

if __name__ == '__main__':
    stu1 = student()
    stu2 = highSchoolStudent()

    stu1.set_info('Allan', '10', 'Male')
    stu1.print_info()
    stu2.set_info('Physics')
    stu2.print_school_info()

    #print('%s' % stu1.birthday)
# member variables and functions can be added in the fly
# private cannot be inheritated
# public can be inheritated
# add element def __init__:
# __slot__ only take effect current class, not derived class
# instance or class dynamically add member var/functions
# instance.var_name  = value
# instance.func_name = MethodType(func_name, instance)
# class.func_name    = func_name which is different