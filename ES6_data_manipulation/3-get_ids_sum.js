/* eslint-disable */
export default function getStudentIdsSum(array) {
  let new_array = array.reduce((accumulator, person) => accumulator + person.id, 0)
  return new_array;
}
