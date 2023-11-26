#!/usr/bin/node
exports.esrever = function (list) {
  const reveredList = [];
  for (let k = list.length - 1; k >= 0; k--) {
    reveredList.push(list[k]);
  }
  return reveredList;
};
