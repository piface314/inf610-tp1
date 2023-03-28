TARGET := inf610-tp1
CC := g++
CCFLAGS := -O2 -Wall -g -std=c++17
LDFLAGS := -Wall -lpthread -lm -ldl -lz -lncurses -rdynamic

.PHONY: all clean

all: obj bin bin/$(TARGET)

obj:
	mkdir -p obj

bin:
	mkdir -p bin

bin/$(TARGET): obj/fft.o obj/main.o obj/dijkstra.o
	$(CC) -o bin/$(TARGET) obj/* $(LDFLAGS)

obj/main.o: src/main.cpp src/fft.hpp src/dijkstra.hpp
	$(CC) -c $(CCFLAGS) src/main.cpp -o obj/main.o

obj/fft.o: src/fft.hpp src/fft.cpp
	$(CC) -c $(CCFLAGS) src/fft.cpp -o obj/fft.o

obj/dijkstra.o: src/dijkstra.hpp src/dijkstra.cpp
	$(CC) -c $(CCFLAGS) src/dijkstra.cpp -o obj/dijkstra.o

clean:
	rm -vf obj/* bin/*
