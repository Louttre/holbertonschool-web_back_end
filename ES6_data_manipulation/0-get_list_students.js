/*eslint-disable*/
export default function getListStudents() {
  const array = [{
    id: 1,
    firstname: 'Guillaume',
    location: 'San Francisco'
  }, {
    id: 2,
    firstname: 'James',
    location: 'Columbia'
  }, {
    id: 5,
    firstname: 'Serena',
    location: 'San Francisco'
  }]

  let new_array = array.map(person => ({ id: person.id, firstname: person.firstname, location: person.location }));
  return new_array;
}
