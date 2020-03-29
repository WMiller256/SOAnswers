#include <iostream>
#include <atomic>
#include <mutex>
#include <chrono>
#include <thread>

void threadFunction(double* d);

double mtime = 0;
double end = 10000;

std::mutex mtx;

int main() {
	auto start = std::chrono::high_resolution_clock::now();
	double* d = new double(0);
	std::thread thread(threadFunction, d);
	std::thread two(threadFunction, d);
	while (true) {
		if (*d == end) {
			break;
		}
	}
	thread.join();
	two.join();
	int t = std::chrono::duration_cast<std::chrono::microseconds>(std::chrono::high_resolution_clock::now() - start).count();
	std::cout << mtime << std::endl;
	std::cout << t << std::endl;
}	
	
	
void threadFunction(double* d){
	while (*d < end) {
		auto start = std::chrono::high_resolution_clock::now();
		mtx.lock();
		*d += 1;
		mtx.unlock();
		mtime += std::chrono::duration_cast<std::chrono::microseconds>(std::chrono::high_resolution_clock::now() - start).count();
	}
}
