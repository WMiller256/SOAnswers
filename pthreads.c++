#include <iostream>
#include <chrono>
#include <cstring>
#include <string>
#include <pthread.h>
using namespace std;
using namespace std::chrono;

struct Thread_arg{ // struct to hold the arguments
    int a; // index of which element for runtime
    char *b; // name of the program to run
};

double runtime[20]; // store all 20 runtime

pthread_mutex_t mutex1 = PTHREAD_MUTEX_INITIALIZER;

void* run_program(void *input){
    auto *arg = (Thread_arg *) input;

    high_resolution_clock::time_point t1 = high_resolution_clock::now();
    system(arg->b);
    high_resolution_clock::time_point t2 = high_resolution_clock::now();

    auto duration = duration_cast<microseconds>( t2 - t1 ).count();
    runtime[arg->a] = duration;

    pthread_mutex_lock(&mutex1);
    std::cout << " Runtime: "+std::to_string(duration)+"\u00B5s\n";
    pthread_mutex_unlock(&mutex1);

    return nullptr;
}

int main(int argc, char** argv){
    if(argc != 2){
        if(argc > 2){
            cout << "Too many arguments, you only need 1" << endl;
        }else if(argc < 2){
            cout << "You need 1 argument" << endl;
        }
        exit(410);
    }

    // format name of the program
    string program = "./";
    program += argv[1];

    int n = (int) program.length();

    char char_array[n+1];

    strcpy(char_array, program.c_str());

    // start testing, get average of 20 test
    pthread_t threads[20]; // create threads

    for(int i = 0; i < 20; i++){
        struct Thread_arg *arg = (struct Thread_arg *)malloc(sizeof(struct Thread_arg)); // arguments in struct
        arg->b = char_array; // load struct
        arg->a = i;
        pthread_create(&threads[i], nullptr, run_program, (void *)arg); // launch thread
    }

    // join threads
    for (auto &thread : threads){
        pthread_join(thread, nullptr);
    }

    // calculate average
    double total_time = 0;
    for (double &i : runtime){
        total_time += i;
    }
    double runtime_ave = total_time/20; 

    cout << "************************************************************" << endl;
    cout <<"||| " << "Average runtime for program " << program << " is: " << runtime_ave << "\u00B5s" << " |||" << endl;
    cout << "************************************************************" << endl;
}
