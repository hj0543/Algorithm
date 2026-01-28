import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        // 불기 연도 입력
        int year = sc.nextInt();
        
        // 서기 연도로 변환하여 출력 (불기 - 543)
        System.out.println(year - 543);
        
        sc.close();
    }
}