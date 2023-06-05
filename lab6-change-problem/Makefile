.PHONY: build clean

LAB = lab6

GFLAGS  = -std=c++11 -pedantic -Wall -lm

build: *.cpp  #$(OBJECTS)
	c++ t6.cpp shortest_path.cpp shortest_path.hpp $(GFLAGS) -o $(LAB)

clean:
	rm -f *.o $(LAB)