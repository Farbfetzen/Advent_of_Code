public class Day15 {
    public static void main(String[] args) {
        // TODO: Read the values from the input file.
        int[] challengeInput = {14, 8, 16, 0, 1, 17};
        play(challengeInput, 2020);
        play(challengeInput, 300_000_00);
    }

    public static void play(int[] startNumbers, int endTurn) {
        int[] memory = new int[endTurn];
        int lastNum = 0;
        int lastSeen = 0;
        int turn = 1;
        for (; turn <= startNumbers.length; turn++) {
            lastNum = startNumbers[turn - 1];
            lastSeen = memory[lastNum];
            memory[lastNum] = turn;
        }
        for (; turn <= endTurn; turn++) {
            lastNum = lastSeen == 0 ? 0 : turn - lastSeen - 1;
            lastSeen = memory[lastNum];
            memory[lastNum] = turn;
        }
        System.out.println(lastNum);
    }
}
