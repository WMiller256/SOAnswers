
#include <iostream>
#include <string>

class A {

public:
	A(std::string S = "");
	std::string s;
	
	void makeB(std::string S);
};

class B {

public:
	B(std::string S = "");
	std::string s;
	
	void makeA(std::string S);
};

