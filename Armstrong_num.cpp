//armstrong number using c++

#include<iostream>

using namespace std;

int main(int argc, char const *argv[])
{
    int n,r,sum=0,temp;

    cout<<"Enter your number: "<<endl;
    cin>>n;

    temp=n;

    while(n>0){
        r=n%10;
        sum=sum+(r*r*r);

        n=n/10;
    }

    if(temp==sum){

        cout<<"Armstrong number"<<endl;

    }
    else{

        cout<<"Not Armstrong number"<<endl;
    }
    
    return 0;
}
