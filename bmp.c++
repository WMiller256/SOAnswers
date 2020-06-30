#include <iostream>
#include <fstream>
#include <bitset>
#include <iomanip>
#include <typeinfo>

using namespace std;

void readBMP(char* filename)
{
  int i;
  std::ifstream is(filename, std::ifstream::binary);
  is.seekg(0, is.end);
  i = is.tellg();
  std::cout << "{i}: " << i << std::endl;
  is.seekg(0);
  unsigned char *info = new unsigned char[i];
  is.read((char *)info,i);

  // Populate 18-21 with a recognizable pattern for demonstration
  std::bitset<8> bitset (std::string("10011010"));
  unsigned long bits = bitset.to_ulong();
  for (int ii = 18; ii < 22; ii ++) {
  		info[ii] = static_cast<unsigned char>(bits);
  }

  std::cout << "info[18]                    -> 1 byte  " << std::bitset<32>(info[18]) << std::endl;
  std::cout << "*(unsigned short*)&info[18] -> 2 bytes " << std::bitset<32>(*(unsigned short*)&info[18]) << std::endl;
  std::cout << "*(int)&info[18]             -> 4 bytes " << std::bitset<32>(*(int*)&info[18]) << std::endl;

  exit(0);
}

int main() {
    readBMP("./test.bmp");
    return 0;
}
