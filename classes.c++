
#include "classes.h"

A::A(std::string S) {
	s = S;
}

void A::makeB(std::string S) {
	B b(S);
	std::cout << "B: "+b.s << std::endl;
}

B::B(std::string S) {
	s = S;
}

void B::makeA(std::string S) {
	A a(S);
	std::cout << "A: "+a.s << std::endl;
	a.makeB(S);
}
