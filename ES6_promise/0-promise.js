#!/usr/bin/node
export default function getResponseFromAPI() {
  return new Promise((resolve, reject) => {
      // Simulating an async operation, you can resolve or reject based on some conditions
      resolve('Success');
  });
}
