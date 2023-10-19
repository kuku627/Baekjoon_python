#include <stdio.h>

int main() {
    int a, b, c, d, e, f;
    int x, y;

    // 입력 받기
    scanf("%d %d %d %d %d %d", &a, &b, &c, &d, &e, &f);

    // 연립방정식 풀기
    // ax + by = c
    // dx + ey = f
    // x = (ce - bf) / (ae - bd)
    // y = (af - cd) / (ae - bd)
    x = (c * e - b * f) / (a * e - b * d);
    y = (a * f - c * d) / (a * e - b * d);

    // 결과 출력
    printf("%d %d\n", x, y);

    return 0;
}
