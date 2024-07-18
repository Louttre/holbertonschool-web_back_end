export default class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof name !== 'string') {
      throw new Error('Must be a string')
    }
    if (typeof length !== 'number' || length < 0){
      throw new Error('Must be a positive number')
    }
    if (!Array.isArray(students)) {
      throw new Error('must be an array of string')
    }
    if (!students.every(item => typeof item === 'string')){
      throw new Error('must be an array of string')
    }
    this._name = name;
    this._legnth = length;
    this._students = students;
  };
