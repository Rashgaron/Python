#include<iostream>
using namespace std;

int fib(int i);



int main(int argc, char** argv)
{
	int i = atoi(argv[1]);
	cout<<fib(i)<<endl;

}

int fib(int i)
{
	if( i == 0 or i == 1)
		return i;
	return fib(i -2) + fib(i-1);


}
