import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        // 문자열 입력 받기
        String id = sc.next();
        
        // 문자열 연결 후 출력
        System.out.println(id + "??!");
        
        sc.close();
    }
}