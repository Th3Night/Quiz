#include <iostream>
#include <fstream>
#include <string>
#include <cmath>

using namespace std;

string symbol(int x){
    string symbols[10] = {"_####_\n"
                          "#____#\n"
                          "#____#\n"
                          "#____#\n"
                          "#____#\n"
                          "_####_", "_#_\n"
                                    "_#_\n"
                                    "_#_\n"
                                    "_#_\n"
                                    "_#_\n"
                                    "_#_", "__##__\n"
                                           "_#__#_\n"
                                           "_#__#_\n"
                                           "___#__\n"
                                           "__#___\n"
                                           "_####_", "__####_\n"
                                                     "_#____#\n"
                                                     "__###__\n"
                                                     "______#\n"
                                                     "_#____#\n"
                                                     "__####_", "_#__#_\n"
                                                                "_#__#_\n"
                                                                "_####_\n"
                                                                "____#_\n"
                                                                "____#_\n"
                                                                "____#_", "_#####\n"
                                                                          "_#____\n"
                                                                          "_#_##_\n"
                                                                          "_____#\n"
                                                                          "_____#\n"
                                                                          "_####_", "__###_\n"
                                                                                    "_#___#\n"
                                                                                    "_#_#__\n"
                                                                                    "_#___#\n"
                                                                                    "_#___#\n"
                                                                                    "___##_", "_#####\n"
                                                                                              "____#_\n"
                                                                                              "___#__\n"
                                                                                              "__#___\n"
                                                                                              "_#____\n"
                                                                                              "_#____", "__##__\n"
                                                                                                        "_#__#_\n"
                                                                                                        "__##__\n"
                                                                                                        "#____#\n"
                                                                                                        "#____#\n"
                                                                                                        "_####_", "__###_\n"
                                                                                                                  "_#__#_\n"
                                                                                                                  "__###_\n"
                                                                                                                  "____#_\n"
                                                                                                                  "____#_\n"
                                                                                                                  "_###__"};
    return symbols[x];
}



int main(){
    int x ;
    cin >> x;
    cout << symbol(x);
}
