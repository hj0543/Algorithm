Java에서는 Python처럼 `input().split()` 한 줄로 모든 것이 해결되지는 않지만, 크게 **두 가지 방법**이 있습니다.

1. **Scanner:** 사용이 쉽고 직관적 (초보자용)
2. **BufferedReader + StringTokenizer:** 코드가 길지만 속도가 매우 빠름 (실전/알고리즘용)

Python의 `input`, `split`, `map` 기능이 Java에서 각각 어떻게 매칭되는지 단계별로 설명해 드릴게요.

---

### 1. Scanner (직관적인 방법)

`java.util.Scanner` 클래스는 Python의 `input()`과 `split()`과 `map()` 기능을 **알아서 처리해 주는 만능 도구**입니다.

* **특징:** 공백(스페이스, 엔터)을 알아서 건너뛰며 데이터를 가져옵니다. 즉, **`split()`을 명시적으로 할 필요가 없습니다.**

#### ① 기본 사용법

```java
import java.util.Scanner; // 필수

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in); // 입력 도구 준비

        // Python: a = int(input())
        int a = sc.nextInt(); // 정수 하나 읽기

        // Python: word = input()
        String word = sc.next(); // 단어 하나 읽기 (공백 전까지)
        
        System.out.println(a);
        System.out.println(word);
    }
}

```

#### ② Python과의 1:1 대응 (Scanner 기준)

| Python | Java (Scanner) | 설명 |
| --- | --- | --- |
| `input()` | `sc.next()` | 공백을 기준으로 **단어(문자열)** 하나를 가져옴 |
| `int(input())` | `sc.nextInt()` | 공백을 건너뛰고 **정수** 하나를 가져옴 |
| `split()` | (자동) | Scanner는 기본적으로 공백을 기준으로 데이터를 자름 |
| `input()` (한 줄 통째로) | `sc.nextLine()` | 공백 포함 한 줄 전체를 가져옴 |

---

### 2. BufferedReader + StringTokenizer (빠른 방법)

백준 문제를 풀다 보면 `Scanner`는 느려서 **시간 초과**가 날 때가 있습니다. 이때 사용하는 것이 Python의 `sys.stdin.readline`에 해당하는 **`BufferedReader`**입니다.

이 방법은 **"읽기(Read) -> 자르기(Split) -> 변환하기(Parse)"** 과정을 직접 명시해야 합니다.

#### ① 구조 분석

```java
import java.io.*; // 입출력 관련
import java.util.StringTokenizer; // 자르기 도구

public class Main {
    public static void main(String[] args) throws IOException { // 예외처리 필수!
        // 1. 읽기 도구 (Python의 sys.stdin.readline)
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 2. 한 줄 읽어오기 (Python의 input())
        String str = br.readLine(); 

        // 3. 자르기 도구 (Python의 split())
        StringTokenizer st = new StringTokenizer(str);

        // 4. 하나씩 꺼내서 변환하기 (Python의 int())
        int a = Integer.parseInt(st.nextToken()); // 첫 번째 숫자
        int b = Integer.parseInt(st.nextToken()); // 두 번째 숫자
    }
}

```

#### ② Python과의 1:1 대응 (BufferedReader 기준)

1. **데이터 가져오기 (`input`)**
* Java: `br.readLine()`
* 설명: 무조건 **한 줄(Line) 전체**를 문자열로 가져옵니다.


2. **데이터 자르기 (`split`)**
* Java: `StringTokenizer st = new StringTokenizer(문자열);`
* 설명: 가져온 문자열을 공백 기준으로 잘라서 보관함(토큰화)에 넣습니다.


3. **데이터 변환하기 (`int()`)**
* Java: `Integer.parseInt(st.nextToken())`
* 설명: `st.nextToken()`으로 잘린 조각 하나를 꺼내고, `Integer.parseInt()`로 숫자로 바꿉니다.



---

### 💡 요약 및 추천

* **처음 시작할 때:**
**`Scanner`**를 쓰세요. `sc.nextInt()` 하나면 입력, 자르기, 변환이 다 되므로 로직에 집중하기 좋습니다.
```java
Scanner sc = new Scanner(System.in);
int A = sc.nextInt();
int B = sc.nextInt();

```


* **본격적으로 문제를 풀 때:**
**`BufferedReader`** 패턴을 외우세요. 코드는 길지만 실행 속도가 훨씬 빠릅니다. 백준 상위권 문제에서는 필수입니다.

혹시 **"두 정수 A와 B를 입력받아 합을 출력하는 코드"**를 Java의 `Scanner` 방식으로 직접 한 번 작성해 보시겠습니까? 코드를 짜주시면 제가 맞게 작성되었는지 봐드릴게요!
