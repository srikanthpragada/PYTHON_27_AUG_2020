import sys

sys.path.insert(0,r'c:\classroom\aug27\demo\mylib')
print(sys.path)  # Module search path


import number_funs as nf
#from number_funs import iseven

print("In module test")
print(nf.iseven(10))