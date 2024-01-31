#include<iostream>
#include<sstream>

struct Course
{
    std::string course_code;
    std::string course_name;
};

struct Grade 
{
    int mark;
    std::string the_grade() {
        if (mark && mark >= 0 && mark <= 100){
            if(mark < 40) return "E";
            else if(mark < 50) return "D";
            else if(mark < 60) return "C";
            else if(mark < 70) return "B";
            else return "A";
        } else{
            std::cout << "Marks value evaluted as invalid: value given (" << mark <<")";
        }
    }
    Grade(
        const int mark_
    ): mark(mark_){}
};

struct Student
{
    std::string registration_number;
    std::string name;
    int age;
    Grade grade;
    Course course;  

    // Default constructor
    Student() 
        : registration_number(""), name(""), age(0), grade(Grade{0}), course(Course{"", ""}) {}

    // I decided to use the constructor to initialize the strings adding limits
    Student(
        const std::string& registration_number_, 
        const std::string& name_, 
        const int& age_, 
        const Grade grade_,
        const Course course_
    )
    : 
    registration_number(registration_number_.substr(0, 20)),
    name(name_.substr(0, 50)),
    age(age_),
    grade(grade_),
    course(course_)
    {}

};


class StudentDetails
{
    bool gradesCalculated = false;
public:
    //default constructor
    StudentDetails() = default;
    int studentCount;

    StudentDetails(int studentCount_){
        std::cout << "Enter registration number of the students: ";
        const int studentCount = studentCount_;
        std::string regNum[studentCount];

        while(true){
            std::cout << "Student reg Number: (Type N to submit)" << std::endl;
            std::cin >> regNum[0];

        }

    }

    int viewStudentDetails(Student students[]){
      std::cout << "Student details: " << std::endl;
        for(int i = 0; i < studentCount; i++){
            std::cout << "Student " << i+1 << ": " << std::endl;
            std::cout << "Registration number: " << students[i].registration_number << std::endl;
            std::cout << "Name: " << students[i].name << std::endl;
            std::cout << "Age: " << students[i].age << std::endl;
            std::cout << "Grade: " << students[i].grade.the_grade() << std::endl;
            std::cout << "Course code: " << students[i].course.course_code << std::endl;
            std::cout << "Course name: " << students[i].course.course_name << std::endl;
        }
        return 0;  
    }
    int editDetails(Student students[]){

        if (gradesCalculated) std::cout << "Grades have already been calculated. You cannot edit student details." << std::endl;
        else std::cout << "Grades have not been calculated. You can edit student details." << std::endl;

        std::cout << "Enter registration number of student to edit: ";
        std::string regNum;
        std::cin >> regNum;
        for(int i = 0; i < studentCount; i++){
            if(students[i].registration_number == regNum){
                std::cout << "Enter new registration number, press N to skip: ";
                std::string newRegNum;
                std::cin >> newRegNum;
                if (toupper(newRegNum[0]) != 'N') students[i].registration_number = newRegNum;

                std::cout << "Enter new name, press N to skip: ";
                std::string newName;
                std::cin >> newName;
                if (toupper(newName[0]) != 'N') students[i].name = newName;

                std::cout << "Enter new age, press N to skip: ";
                int newAge;
                std::cin >> newAge;
                if (toupper(newAge) != 'N') students[i].age = newAge;

                std::cout << "Enter new mark, press N to skip: ";
                int newMark;
                std::cin >> newMark;
                if (toupper(newMark) != 'N') students[i].grade.mark = newMark;

                std::cout << "Enter new course code, press N to skip: ";
                std::string newCourseCode;
                std::cin >> newCourseCode;
                if (toupper(newCourseCode[0]) != 'N') students[i].course.course_code = newCourseCode;

                std::cout << "Enter new course name, press N to skip: ";
                std::string newCourseName;
                std::cin >> newCourseName;
                if (toupper(newCourseName[0]) != 'N') students[i].course.course_name = newCourseName;
                break;
            }
        }
        return 0;
    };

    int calculateGrades(Student students[]){
        std::cout << "Note: Once grades are calculated, grades cannot be edited. Continue? (y/n): ";
        std::string answer;
        std::cin >> answer;
        if(toupper(answer == "N"))  return 0;
        
        std::cout << "Calculating grades...";
        int total = 0;
        for(int i = 0; i < studentCount; i++){
            total += students[i].grade.mark;
            std::cout << "Grade: " << students[i].grade.the_grade() << std::endl;
            
        }
        std::cout << "Total grade: " << total << std::endl;
        std::cout << "Average grade: " << total/studentCount << std::endl;
        gradesCalculated = true;
        return 0;
    };
};



int main() {
    //todo: have an array storing previously inputed student details and print them out
    const int maxStudents = 40;
    Student students[maxStudents];
    int studentCount = 0;

    //!This array shall be used to ensure the user can see the details of the student that theyve just inputed
    //TODO: dont forget to implement this
    std::string curentStudent[10];

    do{
        std::string registration_number;
        std::string name;
        int age;
        int mark;
        std::string course_code;
        std::string course_name;

        std::cout << "Enter registration number: ";
        std::cin >> registration_number;
        std::cout << "Enter name: ";
        std::cin >> name;
        std::cout << "Enter age: ";
        std::cin >> age;
        std::cout << "Enter mark: ";
        std::cin >> mark;
        std::cout << "Enter course code: ";
        std::cin >> course_code;
        std::cout << "Enter course name: ";
        std::cin >> course_name;
// *126#
        Grade grade(mark);
        Course course{course_code, course_name};
        Student student(registration_number, name, age, grade, course);

        students[studentCount] = student;
        studentCount++;
        std::cout << "Student details: " << std::endl;

        std::cout << "Do you want to enter another student? (y/n): ";
        std::string answer;
        std::cin >> answer;
        if(answer == "n") {
            break;
        };
    } while(true && studentCount < maxStudents);
    std::string currentTaskInfo = "You've successfully entered " + std::to_string(studentCount) + " students.";
    do{
        std::cout << currentTaskInfo << std::endl;
        std::cout << "1. View student details" << std::endl;
        std::cout << "2. Edit student details" << std::endl;
        std::cout << "3. Calculate grades" << std::endl; //! Ensure grades cannot be altered once calculated
        std::cout << "4. Exit" << std::endl;
        std::cout << "Enter option: ";

        int option;
        std::cin >> option;

            StudentDetails studentDetails(studentCount);
            switch (option)
            {
            case 1:
                studentDetails.viewStudentDetails(students);
                currentTaskInfo = "You've successfully viewed student regNumber " + std::to_string(option) + ". What do you wish to do next?";
                break;
            case 2:
                studentDetails.editDetails(students);
                currentTaskInfo = "You've successfully edited details for student regNumber " + std::to_string(option) + ". What do you wish to do next?";
                break;
            case 3:
                studentDetails.calculateGrades(students);
                currentTaskInfo = "You've successfully calculated grades for student regNumber " + std::to_string(option) + ". What do you wish to do next?";
                break;
            case 4:
                std::cout << "Exiting..." << std::endl;
                return 0;
                break;
            default:
                std::cout << "Invalid option, options available are 1, 2, 3, 4" << std::endl;
                break;
        }; 
    }while(true);


    return 0;     
}
