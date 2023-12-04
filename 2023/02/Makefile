bin/main: main.hs
	mkdir -p bin
	ghc -outputdir bin -o bin/main main.hs

all: bin/main

clean: 
	rm -rf bin

run:
	@$(MAKE) && ./bin/main
