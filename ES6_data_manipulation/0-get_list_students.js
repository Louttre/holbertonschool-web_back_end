export default function getListStudents() {
  const array = [{
    id: 1,
    fisrstname: 'Guillaume',
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

array.map((person) => ({ id: person.id, firsname: person.firstname, location: person.location }))
