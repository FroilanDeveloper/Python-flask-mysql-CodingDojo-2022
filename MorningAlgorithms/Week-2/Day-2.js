/* 
  Given a string,
  return a new string with the duplicates excluded
  Bonus: Keep only the last instance of each character.
*/

const str1 = "abcABC";
const expected1 = "abcABC";

const str2 = "helloo";
const expected2 = "helo";

const str3 = "";
const expected3 = "";

const str4 = "aaaaa";
const expected4 = "a";

const str5 = "banana";
const expected5 = "ban";

/**
 * De-dupes the given string.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str A string that may contain duplicates.
 * @returns {string} The given string with any duplicate characters removed.
 */
function stringDedupe(str) {
var rtObj = {};
    var rtStr = "";
    for(var i = 0; i < str.length; i++){
        if(rtObj.hasOwnProperty(str.charAt(i))){
            rtObj[str.charAt(i)] += 1;
        }
        else{
            rtObj[str.charAt(i)] = 1;
        }
    }
    for(key in rtObj){
        rtStr += key;
    }
    return rtStr;
}
// [5:06 AM]

console.log(stringDedupe(str1));
console.log(stringDedupe(str2));
console.log(stringDedupe(str3));
console.log(stringDedupe(str4));


console.log("*************")
/* 
  Given a string containing space separated words
  Reverse each word in the string.
  If you need to, use .split to start, then try to do it without.
*/

const strr1 = "hello";
const expected1 = "olleh";

const strr2 = "hello world";
const expected2 = "olleh dlrow";

const strr3 = "abc def ghi";
const expected3 = "cba fed ihg";

/**
 * Reverses the letters in each words in the given space separated
 * string of words. Does NOT reverse the order of the words themselves.
 * - Time: O(?). 0(squared)
 * - Space: O(?).
 * @param {string} str Contains space separated words.
 * @returns {string} The given string with each word's letters reversed.
 */ 
function reverseWords(str) {
  let reverseWordArr = str.split(" ").map(word => word.split("").reverse().join(""));
  return reverseWordArr.join(" ");
}


console.log("Acutal:   ",reverseWords(strr1));
console.log("Expected: ", expected1);

console.log("Acutal:   ",reverseWords(strr2));
console.log("Expected: ", expected2);

console.log("Acutal:   ",reverseWords(strr3));
console.log("Expected: ", expected3);



