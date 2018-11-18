CXX= g++

CC= gcc

SRCS:= first.c

INC= -I ./ \
	 -I	/usr/include/python3.6m/

OBJS:=	$(patsubst %.c, %.o, $(SRCS))

DEPS:= $(OBJS:.o=.d)

.SUFFIXES: .o .c

TARGET= VINH
all:$(TARGET)

$(TARGET): $(OBJS)
	$(CXX) -o $@  -g  $^ -lpython3.6m

#%.o: %.c
#	$(CC) $(INC)  -c -g  $< -o  $@ 

%.o: %.cpp
	$(CXX) $(INC) -std=c++11  -c -g  $< -o  $@

clean:
	rm VINH
	rm *.o