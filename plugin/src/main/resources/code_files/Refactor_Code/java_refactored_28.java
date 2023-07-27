public static String next_palindrome(int[] digit_list) {
    int high_mid = Math.floorDiv(digit_list.length, 2);
    int low_mid = Math.floorDiv(digit_list.length - 1, 2);

    while (high