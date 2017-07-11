/*  A C++ program to find the smallest positive value that cannot be
 * represented as sum of subsets of a given sorted array
*/ 

#include <iostream>
using namespace std;
 
// Returns the smallest number that cannot be represented as sum
// of subset of elements from set represented by sorted array arr[0..n-1]
int findSmallest(int arr[], int n)
{
   int res = 1; // Initialize result
 
   // Traverse the array and increment 'res' if arr[i] is
   // smaller than or equal to 'res'.
   for (int i = 0; i < n && arr[i] <= res; i++)
       res = res + arr[i];
 
   return res;
}
 
int main()
{
   int arr1[] = {1, 3, 6, 10, 11, 15};
   int n1 = sizeof(arr1)/sizeof(arr1[0]);
   cout << findSmallest(arr1, n1) << endl;
 
 
   int arr2[] = {1, 1, 1, 1};
   int n2 = sizeof(arr2)/sizeof(arr2[0]);
   cout << findSmallest(arr2, n2) << endl;
 
   return 0;
}
