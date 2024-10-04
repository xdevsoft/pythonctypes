import ctypes

# .so for Unix/Linux, .dll for Windows .dylib for Mac
lib = ctypes.CDLL('./liblibzigsample.so')

# Function definition return type and param types for add function/method
# lib.add.restype = ctypes.c_void_p
# lib.add.argtypes = [ctypes.c_void_p]

# Function definition return type and param types for add function/method
lib.add.restype = ctypes.c_int
lib.add.argtypes = [ctypes.c_int, ctypes.c_int]

# Function definition return type and param types for hello function/method
lib.hello.restype = ctypes.c_void_p
lib.hello.argtypes = [ctypes.c_char_p]

# No need to define function for foo, since its returning void and no required parameter
lib.foo()

# No casting required for python integer
print(lib.add(10, 20))

# But you can always do this as well
print(lib.add(ctypes.c_int(11), ctypes.c_int(22)))

# We need to cast the python string to ctypes
name = 'gilbert'.encode('utf-8')
lib.hello(ctypes.c_char_p(name))
