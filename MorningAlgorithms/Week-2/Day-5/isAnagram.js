/* 
  An anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
  typically using all the original letters exactly once.
  Is there a quick way to determine if they aren't an anagram before spending more time?
  Given two strings
  return whether or not they are anagrams
  */
 
 const strA1 = "yes";
 const strB1 = "eys";
 const expected1 = true;
 
 const strA2 = "yes";
 const strB2 = "eYs";
 const expected2 = true;
 
 const strA3 = "no";
 const strB3 = "noo";
 const expected3 = false;
 
 const strA4 = "silent";
 const strB4 = "listen";
 const expected4 = true;
 
 /**
  * Determines whether s1 and s2 are anagrams of each other.
  * Anagrams have all the same letters but in different orders.
  * - Time: O(?).
  * - Space: O(?).
  * @param {string} s1
  * @param {string} s2
  * @returns {boolean} Whether s1 and s2 are anagrams.
  */
function isAnagram(s1, s2) {
  var lower_case1 = s1.toLowerCase1()
  var lower_case2 = s2.toLowerCase1()
  if (s1.length != s2.length){
    return false
  }
  let map = new Map();
  for (let i = 0; i < s1.length; i++){
    if(map.has(s1[i])) {
      map.set(s1[i],
        map.get(s1[i])+ 1 );
    }
    else {
      map.set(s1[i], 1);
    }
  }
  for (let i = 0; i < s2.length; i++) {
    if(map.has(s2[i])){
      map.set(s2[i],
        map.get(s2[i]) - 1);
    }
  }
  let keys = map.keys();
  for (let key of keys) {
    if (map.get(key) != 0) {
      return false;
    }
  }
  return true;
}

console.log(isAnagram(strA1,strB1));
console.log(isAnagram(strA2,strB2));
console.log(isAnagram(strA3,strB3));
console.log(isAnagram(strA4,strB4));

