.PHONY: build clean

LAB = lab6

GFLAGS  = -std=c++11 -ansi -pedantic -Wall -lm

build: *.cpp  #$(OBJECTS)
	c++ t6.cpp $(GFLAGS) -o $(LAB) libshortest_path_cpp.a libshortest_path_c.a

clean:
	rm -f *.o $(LAB)