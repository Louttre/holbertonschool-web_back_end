/*eslint-disable*/
export default function updateStudentGradeByCity(array_student, city, array_grade) {
  const gradeObj = newGrades.find(grade => grade.studentId === student.id);
  let loc_array = array.filter(person => person.location === city)
  let final_array = loc_array.map(student => {
        return ({
          ...student,
          grade: gradeObj ? gradeObj.grade : 'N/A',
        });
  });
  return final_array;
}
