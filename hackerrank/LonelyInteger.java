/*
Given an array of integers, where all elements but one occur twice, find the unique element.
EX: a = [1, 2, 3, 4, 3, 2, 1]
The unique element is 4.

parameters: a[n]: an array of n integers
returns: the element that only occurs once

notes:
- may be good to use a hashmap

potential pseudocode:
initialize hashmap
iterate through array, if the number is new create a new entry, if it already exists increment value by 1
return the element mapped to the key with value of 1
*/

package hackerrank;
import java.util.Map;
import java.util.HashMap;
import java.util.List;

class LonelyInteger {
    public static int lonelyIntegerSolution(List<Integer> arr) {
        Map<Integer, Integer> hashmap = new HashMap<Integer, Integer>();
        for (Integer num : arr) {
            if (hashmap.containsKey(num)) {
                hashmap.replace(num, hashmap.get(num) + 1);
            } else {
                hashmap.put(num, 1);
            }
        }
        for (Map.Entry<Integer, Integer> entry : hashmap.entrySet()) {
            int key = entry.getKey();
            int val = entry.getValue();
            if (val == 1) {
                return key;
            }
        }
        return 0;
    }

}
