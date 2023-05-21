pragma solidity ^0.8.0;

contract StudentData {
    struct Student {
        string name;
        string major;
        uint age;
    }

    Student[] internal students;
    event StudentAdded (string name, uint age, string major);

    function addStudent(string memory _name, string memory _major, uint _age ) public{
        Student memory newStudent = Student(_name, _major, _age);
        students.push(newStudent);
        emit StudentAdded(_name, _age, _major);
    }

    function getStudentCount()  public view returns(uint) {
        return students.length;
    }

    function getStudent(uint index)  public view returns (string memory, uint, string memory) {
        require(index<students.length, "Invalid length");
        Student memory student = students[index];
        return(student.name, student.age, student.major);
    }

    fallback() external payable{
        revert ("Invalid Function call");
    }

}