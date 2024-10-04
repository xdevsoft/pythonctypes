# Python Foreign Function Library
Using "ctypes" in Python

What if we have an existing DLL and shared objects or libraries written and exposes function and methods using FFI.

A foreign function interface (FFI) is a mechanism by which a program written in one programming language can call routines or make use of services written or compiled in another one. An FFI is often used in contexts where calls are made into a binary dynamic-link library.

Just sharing my experience and adventure while I'm exploring and building it.

# Additional readings

    FFI - https://en.wikipedia.org/wiki/Foreign_function_interface
    ctypes - https://docs.python.org/3/library/ctypes.html
    Nim - https://nim-lang.org/
    Zig - https://ziglang.org/

# How to compile

```
Compile the C code
gcc -shared -fPIC -o libcsample.so libcsample.c

Compile the Nim code
nim c --out:libnimsample.so --app:lib libnimsample.nim

Compile the Zig code
zig build-lib -dynamic libzigsample.zig -femit-bin=libzigsample.so
```


# Requirements

* Python 3

# My Current Setup

 - Development/Client Laptop
	 - Linux / Python 3.10.12
	 - Mac / Python 3.12.2

# Youtube Video
https://www.youtube.com/watch?v=T67t9zD2oGE

# What's next?

 - C/++ Fuction Pointer 
 - Execute or Call Python method inside the DLL or shared objects
 - Explore other FFI libraries for Python
 - Write DLL's and shared objects in other lnaguages other than C/++

