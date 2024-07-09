#include <stdio.h>
#include <stdint.h>


double averageWaitingTime(int** customers, int customersSize, int* customersColSize) {
    (void) customersColSize;

    double res = 0;
    double curr = 0;
    for (int i = 0; i < customersSize; i++) {
        int* customer = customers[i];
        if (customer[0] > curr) {
            res += customer[1];
            curr = customer[0] + customer[1];
        } else {
            res += curr - customer[0] + customer[1];
            curr += customer[1];
        }
    }
    return res / customersSize;
}


int main(void) {
    int* customers[] = {
        (int[]) {1,2},
        (int[]) {2,5},
        (int[]) {4,3},
    };
    int customersSize = sizeof (customers) / sizeof (int*);
    int customersColSize = 2 * sizeof (int);

    double res = averageWaitingTime(customers, customersSize, &customersColSize);
    printf("%f\n", res);
    return 0;
}
