#include <atomic>
#include <iostream>
#include <thread>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <pthread.h>

void threadFunction(int id);

std::atomic<unsigned long> now;
unsigned long end = 10000000;
cpu_set_t cpuset;

int main() {
	int nthreads = 2;
	now = 0;
	
	CPU_ZERO(&cpuset);
	
	std::thread threads[nthreads];
	for (int ii = 0; ii < nthreads; ii ++) {
		CPU_SET(ii, &cpuset);	
		threads[ii] = std::thread(threadFunction, ii);
	}
	
	while (now < end) {
		now ++;
	}
	
	for (int ii = 0; ii < nthreads; ii ++) {
		threads[ii].join();
	}
}

void threadFunction(int id) {
	int arbitrary;
	unsigned long count = 0;
	pthread_t self = pthread_self();
	cpu_set_t selfset;
	CPU_ZERO(&selfset);
	CPU_SET(id, &selfset);
	pthread_setaffinity_np(self, sizeof(cpu_set_t), &selfset); 
	while (now < end) {
		//do a calculation
		arbitrary = (1*2 + 3*4)*1000;
		count++;
	}
	int cpu_id;
	for (int j = 0; j < CPU_SETSIZE; j++)
		if (CPU_ISSET(j, &selfset))
			cpu_id = j;
	
	std::cout << "Thread "+std::to_string(id)+" on core "+std::to_string(cpu_id)+" - "+std::to_string(count)+"\n";
}
