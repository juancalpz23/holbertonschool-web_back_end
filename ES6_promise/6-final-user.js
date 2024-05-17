#!/usr/bin/node
import handleProfileSignup from './6-profile-signup';

handleProfileSignup('Alice', 'Doe', 'test-photo.jpg')
  .then((results) => {
    console.log(results);
  })
  .catch((error) => {
    console.error(error);
  });
