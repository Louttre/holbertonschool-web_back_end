/*eslint-disable*/
function getStudentsByLocation(array, location) {
  let new_array = array.filter(person => person.location === location)
  return new_array;
}

export default function updateStudentGradeByCity(array_student, location, array_grade) {
  const gradeMap = array_grade.reduce((acc, { studentId, grade }) => {
    acc[studentId] = grade;
    return acc;
  }, {});
  let loc_array = getStudentsByLocation(array_student, location);
  let final_array = loc_array.map(student => {
        return ({
          ...student,
          grade: gradeMap[student.id] !== undefined ? gradeMap[student.id] : 'N/A'
        });
  });
  return final_array;
}
