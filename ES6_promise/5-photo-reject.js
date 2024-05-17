#!/usr/bin/node
function uploadPhoto(fileName) {
  return Promise.reject(new Error(`${fileName} cannot be processed`));
}

export default uploadPhoto('test.jpg');
