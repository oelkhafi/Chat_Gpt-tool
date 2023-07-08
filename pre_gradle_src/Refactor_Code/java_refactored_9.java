public static Object flatten(Object arr) {
    if (arr instanceof ArrayList) {
        ArrayList narr = (ArrayList) arr;
        ArrayList result = new ArrayList(50);
        for (Object x : narr) {
            if (x instanceof Array