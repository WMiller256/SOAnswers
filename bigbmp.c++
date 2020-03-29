#include <iostream>
#include <fstream>

int main() {
	int r = 10000;
	int c = 10000;
	std::ifstream f = std::ifstream("./test.bmp", std::ios::binary | std::ios::in);
	unsigned char * in = new unsigned char[r * c];
	f.read((char*) in, r * c);
	f.close();
	unsigned char * dat = new unsigned char[r*c*10];
	for (int mm = 0; mm < 10; mm ++) {
		for (int ii = 0; ii < r; ii ++) {
			for (int jj = 0; jj < c; jj ++) {
				dat[mm * r * c + ii * c + jj] = in[ii * c + jj];
			}
		}
	}

	std::ofstream of = std::ofstream("big.bmp", std::ios::binary | std::ios::out);
	of.write(reinterpret_cast<char*>(dat), r*c*10);
	of.close();
	return 0;
}
