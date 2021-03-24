public class Day15 {

    public static void main(String[] args) {
        final int[] challengeInput = {14, 8, 16, 0, 1, 17};
        play(challengeInput, 2020);        // part 1: 240
        play(challengeInput, 300_000_00);  // part 2: 505
    }

    public static void play(final int[] startNumbers, final int endTurn) {
        final int[] memory = new int[endTurn];
        int turn = 0;
        int lastSeen = 0;
        for (int sn : startNumbers) {
            lastSeen = memory[sn];
            memory[sn] = ++turn;
        }
        int num = 0;
        while (turn < endTurn) {
            num = lastSeen == 0 ? 0 : turn - lastSeen;
            lastSeen = memory[num];
            memory[num] = ++turn;
        }
        System.out.println(num);
    }
}
