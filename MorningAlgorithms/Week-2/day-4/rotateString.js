/* 
  String: Rotate String
  Create a standalone function that accepts a string and an integer,
  and rotates the characters in the string to the right by that given
  integer amount.
*/

const str = "Hello World";

const rotateAmnt1 = 0;
const expected1 = "Hello World";

const rotateAmnt2 = 1;
const expected2 = "dHello Worl";

const rotateAmnt3 = 2;
const expected3 = "ldHello Wor";

const rotateAmnt4 = 4;
const expected4 = "orldHello W";

const rotateAmnt5 = 13;
const expected5 = "ldHello Wor";
/* 
Explanation: this is 2 more than the length so it ends up being the same
as rotating it 2 characters because after rotating every letter it gets back
to the original position.
*/

/**
 * Rotates a given string's characters to the right by the given amount,
 * wrapping characters to the beginning.
 * - Time: O(n).
 * - Space: O(n).
 * @param {string} str
 * @param {number} amnt The amount of characters in the given str to rotate to the
 *    right.
 * @returns {string} The string rotated by the given amount.
 */
function rotateStr(str, amnt) {
  var rtStr = "";
  var reminderStrAmnt = 0;
  if(amnt > str.length){
      reminderStrAmnt = amnt % str.length;
  }
  else{
      reminderStrAmnt = amnt;
  }

  for(var i = str.length-reminderStrAmnt;  i < str.length; i++){

      //console.log(str.charAt(i), i);
      rtStr += str.charAt(i);
  }
  for(var i =0; i < str.length -reminderStrAmnt; i++){
      rtStr += str.charAt(i);
  }
  return rtStr;
}


console.log(rotateStr(str, 1));
console.log(rotateStr(str, 2));
console.log(rotateStr(str, 3));
console.log(rotateStr(str, 4));
console.log(rotateStr(str, 5));
console.log(rotateStr(str, 13));
console.log(rotateStr(str, 11));
console.log(rotateStr(str, 22));

