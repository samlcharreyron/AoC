CPPFLAGS=--std=c++17 -g

bin/main: main.cpp
	mkdir -p bin
	c++ ${CPPFLAGS} -o bin/main main.cpp


all: bin/main

clean: 
	rm -rf bin

run:
	@$(MAKE) && ./bin/main
