#include <iostream>
#include <string>

int main() {
	std::string ans;
	std::string inter;
	std::cout << "Input: " << std::flush;
	while (std::cin.peek() != '\n') {
		std::cin >> inter;
		ans += inter+" ";
	}
	std::cout << ans << std::endl;
}
