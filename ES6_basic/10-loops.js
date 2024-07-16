export default function appendToEachArrayValue(array, appendString) {
  let idx = 0;
  for (let elem of array) {
    array[idx]  = appendString + elem;
    idx++;
  }

  return array;
}
