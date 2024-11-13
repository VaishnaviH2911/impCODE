// import java.util.Scanner;

// class FibonacciExample1 {
//     public static void main(String args[]) {

//         Scanner sc = new Scanner(System.in);
//         int n1 = 0, n2 = 1, n3;
//         int count = 0;

//         System.out.println("Enter the count:");
//         count = sc.nextInt();

//         System.out.print(n1 + " " + n2);

//         for (int i = 2; i < count; ++i) {
//             n3 = n1 + n2;
//             System.out.print(" " + n3);
//             n1 = n2;
//             n2 = n3;
//         }
//     }
// }
// TC: O(n)
// SC: O(1)

import java.util.Scanner;

class FibonacciExample1 {
    static int n1 = 0, n2 = 1, n3 = 0, stepcount = 0;

    static void printFibonacci(int count) {
        if (count > 0) {
            stepcount++;
            n3 = n1 + n2;
            n1 = n2;
            n2 = n3;
            System.out.print(" " + n3);
            printFibonacci(count - 1);
        }
    }

    public static void main(String args[]) {

        Scanner sc = new Scanner(System.in);
        int count = 0;

        System.out.println("Enter the count:");
        count = sc.nextInt();

        System.out.print(n1 + " " + n2);
        printFibonacci(count - 2);

        System.out.println("Stepcount is:" + stepcount);
    }
}
// TC: O(2^n)
// SC: O(n)