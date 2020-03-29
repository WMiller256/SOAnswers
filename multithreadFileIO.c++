
fstream outfile;
#pragma omp parallel for num_threads(8) schedule(static) private(it) shared(array)
for (it = 0; it < array.size(); ++it) 
{
            int _pre, _sub = 0, _end;
             if(---)
            {        
                    _pre = xyz;
                                    _end = abc;
                                    ostringstream strCounter;
                                    strCounter << _pre;
                                    string result = "file" + strCounter.str() + ".txt";
                    #pragma omp critical(outfile)
                                        {
                                        outfile.open(result.c_str(), std::ios_base::app);
                                        if (outfile.is_open()) 
                                            {
                                            for (int count = _sub; count < _end; count++) 
                                            {
                                                outfile << buffer[count];
                                            }
                                            outfile << "\n";
                                            outfile.close();
                                           } else cout << "Unable to open file";
                                        _sub = _abc;
                    }
            }
            else
            {
                    _pre = _xyz_;
                                    _end = _abc_;
                                    ostringstream strCounter;
                                    strCounter << _pre;
                                    string result = "file" + strCounter.str() + ".txt";
                    #pragma omp critical(outfile)
                                        {
                                        outfile.open(result.c_str(), std::ios_base::app);
                                        if (outfile.is_open()) 
                                            {
                                            for (int count = _sub; count < _end; count++) 
                                            {
                                                outfile << buffer[count];
                                            }
                                            outfile << "\n";
                                            outfile.close();
                                           } else cout << "Unable to open file";
                                        _sub = _abc;
                    }

            }

}
