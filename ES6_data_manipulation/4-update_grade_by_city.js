/*eslint-disable*/
export default function updateStudentGradeByCity(array_student, location, array_grade) {
  const gradeObj = newGrades.find(grade => grade.studentId === student.id);
  let loc_array = array.filter(person => person.location === location)
  let final_array = loc_array.map(student => {
        return ({
          ...student,
          grade: gradeObj ? gradeObj.grade : 'N/A',
        });
  });
  return final_array;
}
