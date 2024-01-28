#include <iostream>
#include <list>
#include <vector>

/*
Mark Victor Kithinji
SCT212-0105/2022
Task 1
Approach: 
    Summation: create int to store the store sum (init at 0), loop adding i to the var
    maximum: largest be index 0, check if theres higher and replace
*/

class operations {
public:
    int summation(const std::vector<int>& input) {
        int response = 0;
        for (const auto& element : input) {
            response += element;
        }
        return response;
    }
    int maximum(const std::vector<int>& input) {
        if (input.empty()) {
            std::cerr << "Error: Array is empty." << std::endl;
            return -1; // Return a special value indicating an error
        }
        int largest = input[0];

        for (size_t i = 1; i < input.size(); ++i) {
            if (input[i] > largest) {
                largest = input[i];
            }
        }

    return largest;
    }
};

int main() {
    std::list<int> myInputList = { 1, 2, 3, 4, 5 };
    operations myOperation;
    std::vector<int> arr; //trying to ensure the size of array will be determined dynamically

    std::cout << "Enter length of array: ";
    int arrLen;
    std::cin >> arrLen;

    for (int i = 0; i < arrLen; i++) {
        int num;
        std::cout << "Enter number at index " << i << ": ";
        std::cin >> num;
        arr.push_back(num);
    }

    int sum = myOperation.summation(arr);
    int max = myOperation.maximum(arr);
    std::cout << "Sum of elements: " << sum << "Largest number: "<< max << std::endl;

    return 0;
}
