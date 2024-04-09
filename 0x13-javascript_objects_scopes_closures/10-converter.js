#!/usr/bin/node
exports.converter = function (num, base) {
  if (base <= 0 || typeof num !== 'number' || Number.isNaN(num)) {
    return 'Error: Invalid input';
  }

  let convertedString = '';
  while (num > 0) {
    const remainder = num % base;
    convertedString = remainder + convertedString;
    num = Math.floor(num / base);
  }

  return convertedString.replace(/\d/g, (match) => {
    const digit = parseInt(match, 10);
    return digit < 10 ? digit : String.fromCharCode(digit + 55);
  });
};
