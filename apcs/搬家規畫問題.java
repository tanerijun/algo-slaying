import java.util.Scanner;

public class Knapsack {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String[] weightStr = scanner.nextLine().split(" ");
        int[] weights = new int[weightStr.length];
        for (int i = 0; i < weightStr.length; i++) {
            weights[i] = Integer.parseInt(weightStr[i]);
        }

        String[] valueStr = scanner.nextLine().split(" ");
        int[] values = new int[valueStr.length];
        for (int i = 0; i < valueStr.length; i++) {
            values[i] = Integer.parseInt(valueStr[i]);
        }

        int capacity = scanner.nextInt();
        scanner.close();

        int[] cache = new int[capacity + 1];

        for (int i = 0; i < weights.length; i++) {
            for (int j = capacity; j >= weights[i]; j--) {
                cache[j] = Math.max(cache[j], cache[j - weights[i]] + values[i]);
            }
        }

        System.out.println(cache[capacity]);
    }
}