#!/usr/bin/node
exports.converter = function (base) {
  return function convertNumber (number) {
    if (number === 0) {
      return '';
    } else {
      return convertNumber(Math.floor(number / base)) + (number % base);
    }
  };
};
