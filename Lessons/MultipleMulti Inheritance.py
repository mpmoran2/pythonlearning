# Multiple Inheritance
# class A:
#     def a_method(self):
#         print("This is from class a method")
#
# class B:
#     def b_method(self):
#         print("This is from class b method")
#
# class C(A,B): # by doing this, class C inherits from both A & B
#     def c_method(self):
#         print("This is from class c method")
#
# c_object = C()
# c_object.a_method()
# c_object.b_method()
# c_object.c_method()

# Multi-Level Inheritance

class A:
    def a_method(self):
        print("This is from class a method")

class B(A): # class B inherits from A
    def b_method(self):
        print("This is from class b method")

class C(B): # so that when C inherits from B, it has access to A through B
    def c_method(self):
        print("This is from class c method")

c_object = C()
c_object.a_method()
c_object.b_method()
c_object.c_method()