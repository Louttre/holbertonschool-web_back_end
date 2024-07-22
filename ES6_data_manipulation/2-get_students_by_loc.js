export default function getStudentsByLocation(array, location) {
  let new_array = array.filter(person => person.location === location)
  return new_array;
}
