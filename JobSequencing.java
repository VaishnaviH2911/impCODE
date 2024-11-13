
import java.util.Arrays;

class Job {

    int id, deadline, profit;

    Job(int id, int deadline, int profit) {
        this.id = id;
        this.deadline = deadline;
        this.profit = profit;
    }
}

class JobSequencing {

    static void jobSequencing(Job[] jobs, int n) {
        // Sort jobs by profit in descending order
        Arrays.sort(jobs, (a, b) -> b.profit - a.profit);

        int[] result = new int[n]; // Track the job sequence
        boolean[] slot = new boolean[n]; // Track the occupied slots

        // Iterate over each job
        for (Job job : jobs) {
            for (int j = Math.min(n - 1, job.deadline - 1); j >= 0; j--) {
                if (!slot[j]) { // If the slot is free
                    result[j] = job.id;
                    slot[j] = true;
                    break;
                }
            }
        }

        System.out.println("Job sequence for maximum profit:");
        for (int i = 0; i < n; i++) {
            if (slot[i]) {
                System.out.print(result[i] + " ");
            }
        }
    }

    public static void main(String[] args) {
        Job[] jobs = { new Job(1, 2, 100), new Job(2, 1, 50), new Job(3, 2, 10) };
        int n = 2; // Number of slots
        jobSequencing(jobs, n);
    }
}
