LINK_TARGET = bin/compiler_program
CC = g++

CPPFLAGS += -std=c++17 -W -Wall -g #-Wno-unused-parameter
CPPFLAGS += -I include -I src #if not work add -I src/implementations

#CPPALLTEST = ast_declaration.cpp ast_expressions.cpp ast_functions.cpp ast_operators.cpp ast_primitives.cpp ast_specifiers.cpp ast_statement.cpp compiler.cpp

HPPFILES = $(wildcard include/*.hpp) 
CPPFILES = $(wildcard src/implementations/*.cpp) $(wildcard src/*.cpp)
OBJS = $(patsubst %.cpp,%.o,$(CPPFILES))

bin/compiler : $(LINK_TARGET)

all : $(LINK_TARGET)

$(LINK_TARGET) : src/lexer.yy.o src/parser.tab.o $(OBJS) 
	$(CC) $(CPPFLAGS) $^ -o $@

src/%.o: src/%.cpp $(HPPFILES)
	$(CC) $(CPPFLAGS) -c -o $@ $<

src/lexer.yy.cpp : src/lexer.flex src/parser.tab.hpp
	flex -o src/lexer.yy.cpp src/lexer.flex

src/parser.tab.cpp src/parser.tab.hpp: src/parser.y
	yacc -v -d src/parser.y -o src/parser.tab.cpp
	mkdir -p bin;

#makeobj:
#	$(CC) $(CPPFLAGS) src/$(CPPALLTEST) -o bin/testout

lexer: src/lexer.yy.cpp

parser: src/parser.tab.cpp src/parser.tab.hpp

bin/compiler: #src/compiler.output
	
	
.PHONY: clean
clean :
	rm -f src/*.tab.hpp
	rm -f src/*.tab.cpp
	rm -f src/*.yy.cpp
	rm -f src/*.output
	rm -f src/*.o
	rm -f src/implementations/*.o
	
