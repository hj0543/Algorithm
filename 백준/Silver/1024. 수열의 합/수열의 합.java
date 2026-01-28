import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main 
{
    public static void main(String[] args) throws IOException 
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        long N = Long.parseLong(st.nextToken());
        int L = Integer.parseInt(st.nextToken());

        for (int K = L; K <= 100; K++) 
        { 
            long sum_of_sequence_base = (long)K * (K - 1) / 2;
            long Remainder = N - sum_of_sequence_base;

            if (Remainder < 0) 
            {
                break;
            }

            if (Remainder % K == 0) {
                long x = Remainder / K; 
                
                for (int i = 0; i < K; i++) 
                {
                    System.out.print((x + i) + (i == K - 1 ? "" : " "));
                }
                System.out.println();
                
                return; 
            }
        }

        System.out.println("-1");
    }
}