# Importing module from another module
from Module1 import show       

# Importing module/script from another packages
from MyMainPackage import some_main_script

# Importing module/script from packages and their subpackages
from MyMainPackage.SubPackage import Subscript

show()
some_main_script.main_report()
Subscript.sub_report()
