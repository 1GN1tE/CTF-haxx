// gcc -o sol solve.c libfoo.so
// LD_LIBRARY_PATH=$LD_LIBRARY_PATH:. ./sol

extern void print_flag(); // Lib function name

int main() {
    print_flag();
} 
