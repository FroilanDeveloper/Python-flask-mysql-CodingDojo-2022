const str1 = "hello";
const expected1 = "olleh";

const str2 = "hello world";
const expected2 = "olleh dlrow";

const str3 = "abc def ghi";
const expected3 = "cba fed ihg";

function reverseWords(str){
  var r = "";
  for(var i = str.length - 1; i >= 0; i--){
    r += str.charAt(i);
  }
  return r;
}

console.log("Acutal:   ",reverseWords(str1));
console.log("Expected: ", expected1);

console.log("Acutal:   ",reverseWords(str2));
console.log("Expected: ", expected2);

console.log("Acutal:   ",reverseWords(str3));
console.log("Expected: ", expected3);