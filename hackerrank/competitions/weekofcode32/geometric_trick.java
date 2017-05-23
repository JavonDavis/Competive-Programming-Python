import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;


public class geometric_trick {

    static String subseq;
    static int[][] tbl, seq;
    static int n;

    static public int countMatches() {
        tbl = new int[n + 1][subseq.length() + 1];

        for (int row = 0; row < tbl.length; row++)
            for (int col = 0; col < tbl[row].length; col++)
                tbl[row][col] = countMatchesFor(row, col);

        return tbl[n][subseq.length()];
    }

    static private int countMatchesFor(int seqDigitsLeft, int subseqDigitsLeft) {
        if (subseqDigitsLeft == 0)
            return 1;

        if (seqDigitsLeft == 0)
            return 0;

        char currSeqDigit = (char) seq[n-seqDigitsLeft][0];
        char currSubseqDigit = subseq.charAt(subseq.length()-subseqDigitsLeft)  ;

        int result = 0;

        if (currSeqDigit == currSubseqDigit)
            result += tbl[seqDigitsLeft - 1][subseqDigitsLeft - 1];

        result += tbl[seqDigitsLeft - 1][subseqDigitsLeft];

        return result;
    }

    static int geometricTrick(String s){
        // int n = s.length();
        // seq = new int[n][2];
        //
        // for(int i = 0; i < n; i ++ ) {
        //     seq[i][0] = s.charAt(i);
        //     seq[i][1] = i;
        // }
        //
        // // for (int i = 0; i < n; i ++) {
        // //     System.out.println(seq[i][0]+"-"+seq[i][1]);
        // // }
        // subseq = "abc";
        // int result = countMatches();
        // subseq = "abc";
        // result += countMatches();
        findFactors(new int[] {2, 3}, new int[] {2, 2}, 0, 1);
    return 0;
    }

    static void findFactors(int[] primeDivisors, int[] multiplicity, int currentDivisor, long currentResult) {
    if (currentDivisor == primeDivisors.length) {
        // no more balls
        System.out.println(currentResult);
        return;
    }
    // how many times will we take current divisor?
    // we have to try all options
    for (int i = 0; i <= multiplicity[currentDivisor]; ++i) {
        findFactors(primeDivisors, multiplicity, currentDivisor + 1, currentResult);
        currentResult *= primeDivisors[currentDivisor];
    }
}

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        n = in.nextInt();
        String s = in.next();
        int result = geometricTrick(s);
        System.out.println(result);
    }
}
