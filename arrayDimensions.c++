#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <iostream>

int** Reshape(int* in, int n, int m) {
	int** ret = new int*[n];
	for (int i = 0; i < n; i++) {
		ret[i] = new int[m];
		for (int j = 0; j < m; j++) {
			ret[i][j] = in[i*m + j];
			std::cout << ret[i][j] << " ";
		}
	}
	return ret;
} 

int main() {
    int cargas[20];
    srand(time(NULL));
    int i;

    for (i = 0; i < 20; i++) 
    {
        cargas[i] = (rand() % 5) + 1;
    }
	int** array = Reshape(cargas, 4, 5);
	std::cout << std::endl;

    for (i = 0; i < 20; i++)
        printf("%d ", cargas[i]);
}
