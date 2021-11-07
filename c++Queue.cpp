//queue implementation in cpp

#include<iostream>
#include<queue>
using namespace std;

void showmyqueue(queue<int>myqueue){
    queue <int> myqueue1 = myqueue;

    while (!myqueue1.empty())
    {
        cout<<"\t"<<myqueue1.front();
        myqueue1.pop();
    }
    cout<<endl;
    
}
int main(int argc, char const *argv[])
{
    queue <int > mynum;

    mynum.push(100);
    mynum.push(90);
    mynum.push(1000);
    mynum.push(89);

    cout<<"The queue mynum is: "<<endl;

    showmyqueue(mynum);

    cout<<"The size of the queue is: "<<mynum.size()<<endl;

    cout<<"The front of the queue is: "<<mynum.front()<<endl;

    cout<<"The back of the queue is: "<<mynum.back()<<endl;

    mynum.pop(); // it removes the last element from the queue 

    cout<<"After the pop method: "<<endl;

    showmyqueue(mynum);

    
    return 0;
}
