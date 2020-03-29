#include <iostream>
#include <string.h>

int main() {
	char str[1024];
	std::cin.getline(str, 1024);
	std::cout << strlen(str) << std::endl;
}
