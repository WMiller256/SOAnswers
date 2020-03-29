#include <fstream>
#include <string>
#include <iostream>


int main(int argn, char** argv) {
	std::ifstream str2;
	str2.open ("test.data", std::ifstream::in);

	int nbline = 3;
	int nbcolumn = 4;
	int x = 0;

	std::istreambuf_iterator<char> istart (str2);
	std::istreambuf_iterator<char> iend ;

	std::ifstream* streams = new std::ifstream[nbline];
	for (int ii = 0; ii < nbline; ii++) {
		streams[ii].open("test.data", std::ifstream::in);
	}
	std::istreambuf_iterator<char>* iarray = new std::istreambuf_iterator<char>[nbline];
	for (int ii = 0; ii < nbline; ii ++) {
		iarray[ii] = std::istreambuf_iterator<char> (streams[ii]);
	}

	int idx = 0;
	while (istart != iend) {
		if (x % nbcolumn == 0) {
			std::advance(iarray[x/nbcolumn], (nbcolumn+1)*idx);
			idx++;
		}
		x++;
		istart++;
	}

	for (int ii = 0; ii < nbcolumn; ii ++) {
		for (int jj = 0; jj < nbline; jj ++) {
			std::cout << *iarray[jj]++ << "\t";
		}
		std::cout << std::endl;
	}
}
