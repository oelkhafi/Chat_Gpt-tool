public static Integer lcs_length(String s, String t) {
    Map<Integer, Map<Integer,Integer>> dp = new HashMap<Integer,Map<Integer,Integer>>();

    for (int i=0; i < s.length(); i++) {