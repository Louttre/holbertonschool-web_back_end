/*eslint-disable*/
function getListStudentIds(array) {
  if (!Array.isArray(array)) {
    return [];
  }
  let new_array = array.map(person => person.id);
  return new_array;
}
