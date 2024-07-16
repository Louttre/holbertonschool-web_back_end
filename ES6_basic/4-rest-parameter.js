export default function returnHowManyArguments() {
  let num = 0;
  for (let arg of args) {
    num += 1;
  }
  return num;
}
