package java_programs.extra;

public class MAXIMUM_WEIGHTED_SUBSET {
    public static int maxSubsetWeight(int[] weights, int bound) {
        if (weights.length == 0) {
            return 0;
        }