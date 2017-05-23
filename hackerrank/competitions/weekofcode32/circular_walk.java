import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

class CircleNode {
    ArrayList<Integer> nexts;
    int key;

    public CircleNode(int key) {
        this.key = key;
        this.nexts = new ArrayList<Integer>();
    }
}

public class circular_walk {

    static final int infinity = ((Double) Math.pow(10, 7)).intValue();

    static int traverse(int[] nodes, int start, int end, int[] R, int n) {
        HashMap<Integer, Integer> visited = new HashMap<Integer, Integer>();
        visited.put(start, 0);
        int min_dist = infinity;
        while (visited.size() != n) {
            Integer min_node = null;
            for(int i = 0; i < n; i ++) {
                int node = nodes[i];
                if(visited.containsKey(node)) {
                    if(min_node == null) {
                        min_node = node;
                    } else if(visited.get(node) < visited.get(min_node)){
                        min_node = node;
                    }
                }
            }

            if (min_node == null) {
                break;
            }

            int current_weight = visited.get(min_node);

            int p = min_node - R[min_node];
            int q = min_node + R[min_node];

            for(int i = p; i <= q; i++) {
                int edge = i;
                if(edge < 0) {
                    edge += n;
                }

                if(edge >= n) {
                    edge %= n;
                }

                int weight = 1 + current_weight;
                if(edge == end) {
                    if(weight < min_dist) {
                        min_dist = weight;
                    }
                }

                if(!visited.containsKey(edge) || weight < visited.get(edge)) {
                    visited.put(edge, weight);
                }
            }
        }
        return min_dist;
    }

    static int circularWalk(int n, int s, int t, int r_0, int g, int seed, int p){
        // Complete this function
        if (s == t) { // Started at same position
            return 0;
        }


        int[] R = new int[n];
        R[0] = r_0;
        for (int i = 1; i < n; i ++) {
            R[i] = (R[i-1] * g + seed) % p;
        }

        int[] nodes = new int[n];
        for(int i = 0; i < n; i ++) {
            nodes[i] = i;
        }
        System.out.println(R[0]);
        System.out.println(nodes[0]);
        int min_dist = traverse(nodes, s, t, R, n);
        if (min_dist >= infinity)
            return -1;
        return min_dist;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int s = in.nextInt();
        int t = in.nextInt();
        int r_0 = in.nextInt();
        int g = in.nextInt();
        int seed = in.nextInt();
        int p = in.nextInt();
        int result = circularWalk(n, s, t, r_0, g, seed, p);
        if(result == infinity) {
            System.out.println("-1");
        } else {
            System.out.println(result);
        }

    }
}
