#include <thread> 
#include <chrono>
#include <atomic>
#include <iostream>
#include <iomanip>

unsigned maxThreads = 1; //std::thread::hardware_concurrency();
unsigned long long big = 0;

unsigned long long biggestOddFactor(unsigned long long n);
unsigned long long smart(unsigned long long min, unsigned long long max);
unsigned long long evensOnly(unsigned long long min, unsigned long long max);
unsigned long long oddsOnly(unsigned long long min, unsigned long long max);

int main() {
	unsigned long long n = 20000000000;
	unsigned long long block = n / maxThreads;
	auto start = std::chrono::high_resolution_clock::now();
/*	for (unsigned long long ii = 1; ii <= n; ii ++) {
		big += biggestOddFactor(ii);
		//std::cout << '\r' << (ii * 100) / n << std::flush;
	} 

  	std::thread threads[maxThreads];
	for (int ii = 0; ii < maxThreads - 1; ii ++) {
		threads[ii] = std::thread(smart, block * ii, block * (ii + 1));
	}
	threads[maxThreads - 1] = std::thread(smart, block * (maxThreads - 1), n);
	for (int ii = 0; ii < maxThreads; ii ++) {
		threads[ii].join();
	}
*/
	big = smart(1, n);
	std::cout << big << std::endl;
	auto elapsed = std::chrono::duration_cast<std::chrono::microseconds>(std::chrono::high_resolution_clock::now() - start).count();
	std::cout << elapsed << " microseconds" << std::endl;
}

unsigned long long biggestOddFactor(unsigned long long n) {
	while(n%2 == 0)
		n /= 2;
	return n;
}

unsigned long long smart(unsigned long long min, unsigned long long max) {
	if (min == max)
		return biggestOddFactor(min);

	return oddsOnly(min, max) + evensOnly(min, max);
}

unsigned long long evensOnly(unsigned long long min, unsigned long long max) {
	unsigned long long ret = 0;
	if ((min % 2) == 0)
		++min;
	if ((max % 2) == 0)
		--max;
	if (max < min)
		return 0;
	if (max == min)
		return biggestOddFactor (max);
	return oddsOnly (min/2, max/2) + evensOnly (min/2, max/2);
}

unsigned long long oddsOnly(unsigned long long min, unsigned long long max) {
	unsigned long long ret = 0;
	if ((min % 2) != 0)
		++min;
	if ((max % 2) != 0)
		--max;
	if (min > max)
		return 0;
	if (min == max)
		return min;
	++max;
	return (max*max - min*min)/4;
}
