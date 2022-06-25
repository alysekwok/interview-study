

/*
Given a square matrix, calculate the absolute difference between the sums of its diagonals.
EX: in the matrix below,
1 2 3 
4 5 6
9 8 9
left to right diagonal is 1 + 5 + 9 = 15
right to left diagonal is 3 + 5 + 9 = 17
the difference is |15 - 17| = 2
*/

package hackerrank;
import java.util.List;


public class DiagonalDifference {
    public static int diagonalDifference(List<List<Integer>> arr) {
        int sum1 = 0;
        int sum2 = 0;
        int col = 0;
        int row = 0;
        for (int i = 0; i < arr.size(); i++) {
            sum1 += arr.get(col).get(row);
            col++;
            row++;
        }
        col = 0;
        row--;
        for (int j = 0; j < arr.size(); j++) {
            sum2 += arr.get(col).get(row);
            col++;
            row--;
        }
        return Math.abs(sum1 - sum2);
    }
    
    // public static void main(String[] args) {
    //     // int arr[][] = {{1, 2}, {3, 3}, {4, 5}};
    //     List<List<Integer>> arr = new List
    //     System.out.println(arr.get(0).size);
    // }
   
}

