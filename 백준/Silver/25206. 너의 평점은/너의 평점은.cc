#include <stdio.h>
#include <string.h>

double getGradePoints(char *grade);

int main() {
    char subject[50];
    double credit, total_points = 0, total_credits = 0;

    for (int i = 0; i < 20; i++) {
        char grade[3];
        scanf("%s %lf %s", subject, &credit, grade);

        if (strcmp(grade, "P") != 0) {  
            double subject_points = credit * getGradePoints(grade);
            total_points += subject_points;
            total_credits += credit;
        }
    }

    double major_gpa = total_points / total_credits;

    printf("%.6lf\n", major_gpa);

    return 0;
}

double getGradePoints(char *grade) {
    if (strcmp(grade, "A+") == 0) return 4.5;
    if (strcmp(grade, "A0") == 0) return 4.0;
    if (strcmp(grade, "B+") == 0) return 3.5;
    if (strcmp(grade, "B0") == 0) return 3.0;
    if (strcmp(grade, "C+") == 0) return 2.5;
    if (strcmp(grade, "C0") == 0) return 2.0;
    if (strcmp(grade, "D+") == 0) return 1.5;
    if (strcmp(grade, "D0") == 0) return 1.0;
    if (strcmp(grade, "F") == 0) return 0.0;

    return 0.0;  
}
