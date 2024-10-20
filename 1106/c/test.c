#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>


#define print(...) printf(__VA_ARGS__); fflush(stdout);


void short_circut(char* expr, size_t* i) {
    int left = 1;
    for (;;) {
        /*print("%zu: %c\n", *i, expr[*i]);*/
        switch (expr[*i]) {
            case '(': {
                left += 1;
            } break;
            case ')': {
                left -= 1;
                if (left == 0) {
                    return;
                }
            } break;
            default: {
            }
        }
        *i += 1;
    }
}


bool parse(char* expr, size_t* i) {
    if (expr[*i] == 't') {
        /**i += 1;*/
        return true;
    } else if (expr[*i] == 'f') {
        /**i += 1;*/
        return false;
    }

    switch (expr[*i]) {
        case '!': {
            *i += 2;
            bool res = !parse(expr, i);
            *i += 1;
            return res;
        } break;
        case '&': {
            *i += 2;
            for (; expr[*i] != ')'; *i += 1) {
                switch (expr[*i]) {
                    case ',': {
                        continue;
                    } break;
                    default: {
                        if (parse(expr, i) == false) {
                            short_circut(expr, i);
                            return false;
                        }
                    }
                }
            }
            return true;
        } break;
        case '|': {
            *i += 2;
            for (; expr[*i] != ')'; *i += 1) {
                switch (expr[*i]) {
                    case ',': {
                        continue;
                    } break;
                    default: {
                        if (parse(expr, i) == true) {
                            short_circut(expr, i);
                            return true;
                        }
                    }
                }
            }
            return false;
        } break;
    }
    return false;
}


bool parseBoolExpr(char* expression) {
    return parse(expression, &(size_t){0});
}


int main(void) {
    char* expression = "|(&(t,f,t),!(t))";
    bool res = parseBoolExpr(expression);
    printf("%s\n", res ? "true" : "false");
}
