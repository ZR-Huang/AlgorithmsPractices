"""
International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, 
as follows: "a" maps to ".-", "b" maps to "-...", "c" maps to "-.-.", and so on.

For convenience, the full table for the 26 letters of the English alphabet is given below:

[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",
".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

Now, given a list of words, each word can be written as a concatenation of the Morse code of each letter. 
For example, "cab" can be written as "-.-.-....-", (which is the concatenation "-.-." + "-..." + ".-"). 
We'll call such a concatenation, the transformation of a word.

Return the number of different transformations among all words we have.

Example:
Input: words = ["gin", "zen", "gig", "msg"]
Output: 2
Explanation: 
The transformation of each word is:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."

There are 2 different transformations, "--...-." and "--...--.".
 

Note:
The length of words will be at most 100.
Each words[i] will have length in range [1, 12].
words[i] will only consist of lowercase letters.
"""

"""
Created Time: Aug. 7, 2018

@author: Zhangrong.Huang
"""

class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        
        letter_to_morse = {"a":".-", "b":"-...", "c":"-.-.", "d":"-..", "e":".", "f":"..-.", "g":"--.",
        "h":"....", "i":"..", "j":".---", "k":"-.-", "l":".-..", "m":"--", "n":"-.", "o":"---", "p":".--.",
        "q":"--.-", "r":".-.", "s":"...", "t":"-", "u":"..-", "v":"...-", "w":".--", "x":"-..-", "y":"-.--", "z":"--.."}

        words_to_morse = []

        for word in words:
            morse = []
            for letter in word:
                morse.append(letter_to_morse[letter])
            morse_str = ''.join(morse)
            words_to_morse.append(morse_str)
        
        labelled = {}
        count = 0
        for item in words_to_morse:
            if item not in labelled:
                count += 1
                labelled[item] = True
        
        return count

