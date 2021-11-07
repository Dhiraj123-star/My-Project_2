#include <iostream>
#include<map>
#include<utility>


using namespace std;

int main(int argc, char const *argv[])
{

    //map example in c++

    map<int,string>prog_name;
    //assignment using index notation

    prog_name[1]="Python";

    prog_name[2]="Java";

    prog_name[3]="JavaScript";

    prog_name[4]="C";

    prog_name[5]="C++";

    cout<<"Prog_name[4]: "<<prog_name[4]<<endl;

    cout<<"natural order"<<endl;

    for(map<int,string>::iterator itr=prog_name.begin(); itr!=prog_name.end(); ++itr ){
        cout<<(*itr).first<<":"<<(*itr).second<<endl;
    }
    
    cout<<endl<<"Reverse order"<<endl;

    for(map<int,string>::reverse_iterator itr=prog_name.rbegin();itr!=prog_name.rend();++itr ){

        cout<<(*itr).first<<":"<<(*itr).second<<endl;

    }


    
    return 0;
}
