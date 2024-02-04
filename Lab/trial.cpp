// Purpose: To test the swap function with and without the & operator
#include <iostream>
using namespace std;
void swap(int& first, int& second)
{
	int temp = first;
	first = second;
	second = temp;
    cout << "withing & swap function\n" << first << " " << second << "\n";
}

void swapValues(int first, int second)
{
    int temp = first;
    first = second;
    second = temp;
    cout << "without & swap function\n" << first << " " << second << "\n";
}

// Driver function
int main()
{
	// Variables declared
	int a = 2, b = 3;

	cout << "Swap with &\n";
	swap(a, b);
	cout << a << " " << b << "\n";

	cout << "Swap without &\n";
    swapValues(a, b);
    cout << a << " " << b;
	return 0;
}
