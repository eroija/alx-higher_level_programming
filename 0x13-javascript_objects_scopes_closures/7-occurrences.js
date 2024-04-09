#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  if (!list || typeof searchElement === 'undefined') {
    return 0;
  }

  return list.filter(item => item === searchElement).length;
};
