#include <iostream>
using namespace std;

int main()
{
  const double PI = 3.141592;

  double radius;
  double perimeter;
  double area;

  cout << "원의 반지름 입력: ";
  cin >> radius;

  perimeter = 2 * PI * radius;
  area = PI * PI * radius;

  cout << "반지름: " << radius << endl;
  cout << "둘레: " << perimeter << endl;
  cout << "면적: " << area;
  return 0;


}