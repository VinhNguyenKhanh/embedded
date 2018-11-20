CXX= g++

CC= gcc

SRCS:= first.cpp

INC= -I ./ \
	 -I	/usr/include/python2.7/

OBJS:=	$(patsubst %.cpp, %.o, $(SRCS))

DEPS:= $(OBJS:.o=.d)

.SUFFIXES: .o .cpp

TARGET= VINH
all:$(TARGET)

$(TARGET): $(OBJS)
	$(CXX) -o $@  -g  $^ -lpython2.7

#%.o: %.c
#	$(CC) $(INC)  -c -g  $< -o  $@ 

%.o: %.cpp
	$(CXX) $(INC) -std=c++11  -c -g  $< -o  $@

clean:
	rm VINH
	rm *.o