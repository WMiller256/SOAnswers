#include <iostream>
#include <string>
#include <algorithm>

void showStudents() {
	
}
void addStudent(std::string name, std::string surname) {
	std::cout << name << " " << surname << std::endl;
}

void selectOption(){
	int choice = 0;
    std::string in = ""; 
	std::cout << "Choice: " << std::flush;
	std::cin >> in;
	if (std::all_of(in.begin(), in.end(), ::isdigit)) {
		choice = std::stoi(in);
	}
    std::string name, surname;
    switch(choice){
        case 1:
            showStudents();
            break;
        case 2:
            std::cout <<"Name: "; 
			std::cin >> name;
            std::cout <<"Surname: "; 
			std::cin >> surname;
            addStudent(name,surname);
            break;
        case 3:
            break;
        default:
            std::cout << "DOES NOT SUPPORT" << std::endl;
            return;
    }
}

int main(){
    while(true){
        selectOption();
		std::cout << std::flush;
    }
}
