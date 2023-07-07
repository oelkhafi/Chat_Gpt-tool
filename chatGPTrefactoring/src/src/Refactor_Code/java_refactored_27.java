public static void main(String[] args) throws Exception {
    Scanner in = new Scanner(System.in);
    while(in.hasNext()) {
        String parens = in.next();
        int depth = 0;
        for(int i=0;