export default function appendToEachArrayValue(array, appendString) {
  let idx = 0;
  for (let elem of array) {
    array[idx]  = elem + appendString;
    idx++;
  }

  return array;
}
