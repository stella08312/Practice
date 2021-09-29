/*****************************************************
*점수를 입력하면 합격/불합격과 학점을 알 수 있는 프로그램*
******************************************************/

#include <iostream>
using namespace std;

int main()
{
  int score;
  char grade;

  cout << "0~100점 사이의 점수를 입력하세요: ";
  cin >> score;

  if(score >=70)
  {
    cout << "pass 입니다." << endl;
  }
  else
  {
    cout << "fail 입니다." <<endl;
  }

  if(score >=90)
  {
    grade = 'A';
  }
  else if(score >=80)
  {
    grade = 'B';
  }
  else if(score >=70)
  {
    grade = 'C';
  }
  else if(score >=60)
  {
    grade = 'D';
  }
  else
  {
    grade = 'F';
  }

  cout << "최종 학점 = " << grade;
  return 0;
}