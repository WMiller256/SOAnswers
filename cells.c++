#include <iostream>
#include <thread>
#include <atomic>
#include <vector>
#include <mutex>

class Cell {
public:
	Cell(int x, bool child = false) {
		lifetime = (0.1 + x % 8);
		n = x;
		is_child = child;
		alive = true;
		has_children = false;
	}
	int lifetime;
	int n;
	bool is_child;
	bool has_children;
	bool alive;
};

std::mutex mtx;

std::vector<Cell> cells;
std::vector<std::thread> threads;

std::atomic<int> t;
std::atomic<int> living;
std::atomic<int> check;

void thread_function(Cell cell) {
	int prev = t;
	while (living > 0) {
		while (prev == t) {
			if (living == 0) {
				return;
			}
		}
		prev = (int)t;
		if (!cell.has_children && !cell.is_child && t > cell.lifetime / 2.0) {
			cell.has_children = true;
			for (int ii = 0; ii < ((cell.n - cell.n % 8) / 8); ii ++) {
				living ++;
				Cell c(ii, true);
				c.lifetime = cell.lifetime + t;
				mtx.lock();
				threads.push_back(std::thread(thread_function, c));
				mtx.unlock();
			}
		}
		if (cell.alive && t >= cell.lifetime) {
			cell.alive = false;
			living --;
		}
		check --;
	}
}

int main(int argn, char** argv) {
	living = argn - 1;
	if (argn > 1) {
		for (int ii = 1; ii < argn; ii ++) {
			cells.push_back(Cell(atoi(argv[ii])));
			threads.push_back(std::thread(thread_function, cells[ii-1]));
		}
	}
	t = 0;

	while (living > 0) {
		std::cout << "Total Cells: "+std::to_string(living)+" [ "+std::to_string(t)+
			" s ]\n" << std::flush;
		check = threads.size();
		t ++;
		while (check > 0) {
			if (living == 0) break;
		}
	}
	std::cout << "Total Cells: "+std::to_string(living)+" [ "+std::to_string(t)+" s ]\n" << std::flush;

	for (int ii = 0; ii < threads.size(); ii ++) {
		threads[ii].join();
	}
	
	return 0;
}
