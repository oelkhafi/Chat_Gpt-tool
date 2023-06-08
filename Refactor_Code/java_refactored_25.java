//Refactored method
public static int inverse(int base, int mod) {
    if (base == 1) {
        return 1;
    }
    int coeff = base - inverse(mod % base, base);
    return (coeff * mod) / base;