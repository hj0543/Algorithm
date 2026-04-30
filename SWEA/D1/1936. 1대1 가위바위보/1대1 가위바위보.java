import java.util.Scanner;
import java.io.FileInputStream;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int A = sc.nextInt();
        int B = sc.nextInt();

        if ((A - B) == 1 || (A - B) == -2) {
            System.out.println('A');            
        }
        if ((B - A) == 1 || (B - A) == -2) {
            System.out.println('B');
        }
    }
}