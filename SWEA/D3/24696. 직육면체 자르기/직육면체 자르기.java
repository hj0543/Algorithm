import java.util.Scanner;
import java.io.FileInputStream;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();

        for (int i = 0; i < T; i++) {
            int A = sc.nextInt();
            int B = sc.nextInt();
            int C = sc.nextInt();

            // A*B*C가 홀수면 다현이가 이기고, 짝수면 나연이가 이긴다.
            // 그런데 하나만 짝수여도 곱한 수가 짝수이므로,

            if ((A % 2) == 1 & (B % 2) == 1 & (C % 2) == 1) {
                System.out.println(2);
            }
            else {
                System.out.println(1);
            }
        }
    }
}