import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class fight_the_monsters {


    static int getMaxMonsters(int n, long hit, long t, long[] h){
        // Complete this function
        Arrays.sort(h); // O(nlogn)
        int i = 0;
        int count = 0;

        while(t > 0) { // O(t) > O(nlogn)
            if (i >= n) {
                break;
            }
            long monster = h[i];
            monster -= hit;
            h[i] = monster;
            if(monster <= 0) {
                i += 1;
                count += 1;
            }
            t -= 1;
        }
        return count;
    }

/*
    static int getMaxMonsters(int n, long hit, long t, long[] h){
        long total_hits = t*hit;
        Arrays.sort(h); // O(nlogn)

        int count = 0;
        control:
        for(int i = 0; i < n; i++) { // O(nt) > O(nlogn) worse case
            long strength = hit;
            t -= 1;
            if(t< 0)
                break control;

            while (strength < h[i]) { // O(h[i]/hit) or O(t) either way, not good enough
                strength += hit;
                t-=1;
                if(t< 0) {
                    break control;
                }
            }
            count ++;
        }
        return count;
    }
*//*
    static int getMaxMonsters(int n, long hit, long t, long[] h){
        long total_hits = t*hit;
        Arrays.sort(h); // O(nlogn)

        int count = 0;
        for(int i = 0; i < n; i++) { // O(n)
            total_hits -= h[i];
            double no_hits = Math.ceil((double) h[i]/hit);
            if (total_hits < 0)
                break;
            count ++;
            double remainder_for_seconds = (no_hits*hit) - h[i]; // Have to do this to account for time
            total_hits -= remainder_for_seconds;
        }
        return count;
    }*/

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        long hit = in.nextLong();
        long t = in.nextLong();
        long[] h = new long[n];
        for(int h_i=0; h_i < n; h_i++){
            h[h_i] = in.nextLong();
        }
        int result = getMaxMonsters(n, hit, t, h);
        System.out.println(result);
    }
}
