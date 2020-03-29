#include <iostream>
#include <thread>
#include <string>
#include <sstream>
#include <vector>
#include <chrono>
#include <mutex>
#include <atomic>
using namespace std;
vector<int> inputs;

std::atomic<int> timer;
std::atomic<int> lifeTime;

void thread_function()
{
    std::cout<<"[Monitor] Total cells: "<< lifeTime-- << " [ " << ++timer <<" s ] " << std::endl;
}
int main()
{
	timer = 0;
	lifeTime = 8;
    cout<<"[Main] Please input a list of gene seeds: "<<endl;
    int value;
    string line;
    getline(cin, line);
    istringstream iss(line);
    while(iss >> value){

       inputs.push_back(value);
    }


    cout<<"[Monitor] Started [ 0 s ]"<<endl;
    std::thread threads[inputs.size()];
    for (int unsigned i = 0; i < inputs.size(); i++) {
        threads[i] = std::thread(thread_function);
    }
    for (int unsigned i = 0; i < inputs.size(); i++) {
        threads[i].join();
    }

    return 0;
}
