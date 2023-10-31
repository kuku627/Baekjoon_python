#include <stdio.h>
#include <stdbool.h>
#include <math.h>

// 소수를 판별하는 함수
bool is_prime(int num) {
    if (num <= 1) return false;
    if (num <= 3) return true;
    if (num % 2 == 0 || num % 3 == 0) return false;
    for (int i = 5; i * i <= num; i += 6) {
        if (num % i == 0 || num % (i + 2) == 0) return false;
    }
    return true;
}

int main() {
    int M, N;
    scanf("%d %d", &M, &N);
    
    for (int i = M; i <= N; i++) {
        if (is_prime(i)) {
            printf("%d\n", i);
        }
    }
    
    return 0;
}
