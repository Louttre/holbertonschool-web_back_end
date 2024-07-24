/*eslint-disable*/
import { uploadPhoto, createUser} from './utils.js';

export default function handleProfileSignup() {
  Promise.all([
    uploadPhoto(), 
    createUSer()
  ]).then((array) => {
    [photo, user] = array;
    console.log('${photo.body} ${user.firstName} ${user.lastName}');
  }).catch(() => {
    console.log('Signup system offline');
  });
}
