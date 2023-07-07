public static int is_properly_nested(int[] A) {
    int depth = 0;
    for (int i = 0; i < A.length; i++) {
        depth += A[i];
        if (depth < 0) {
            return 0