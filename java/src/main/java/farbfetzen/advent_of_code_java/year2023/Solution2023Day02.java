package farbfetzen.advent_of_code_java.year2023;

import java.util.regex.Pattern;

import farbfetzen.advent_of_code_java.Inputs;
import farbfetzen.advent_of_code_java.Results;
import farbfetzen.advent_of_code_java.Solution;

/**
 * <a href="https://adventofcode.com/2023/day/2">adventofcode.com/2023/day/2</a>
 */
public class Solution2023Day02 implements Solution {

    private static final Pattern GAME_ID = Pattern.compile("Game (\\d+)");
    private static final Pattern CUBES = Pattern.compile("(\\d+) ([a-z]+)");

    @Override
    public Results solve(final Inputs inputs) {
        final var results = new Results();

        final var bothSampleResults = solveBoth(inputs.samples().getFirst());
        results.addPart1Sample(bothSampleResults[0]);
        results.addPart2Sample(bothSampleResults[1]);

        final var bothResults = solveBoth(inputs.input());
        results.setPart1(bothResults[0]);
        results.setPart2(bothResults[1]);

        return results;
    }

    /**
     * Solve both parts in one pass over the list of games.
     */
    private static int[] solveBoth(final String input) {
        int sumOfPossibleGameIds = 0;
        int sumOfGamePowers = 0;
        for (final var line : input.lines().toList()) {
            final var idMatcher = GAME_ID.matcher(line);
            if (!idMatcher.find()) {
                throw new IllegalStateException("Input line without game id? " + line);
            }
            final int id = Integer.parseInt(idMatcher.group(1));

            int maxRed = 0;
            int maxGreen = 0;
            int maxBlue = 0;
            final var cubeMatcher = CUBES.matcher(line);
            while (cubeMatcher.find()) {
                final var n = Integer.parseInt(cubeMatcher.group(1));
                final var color = cubeMatcher.group(2);
                if (color.equals("red")) {
                    maxRed = Math.max(maxRed, n);
                } else if (color.equals("green")) {
                    maxGreen = Math.max(maxGreen, n);
                } else {
                    maxBlue = Math.max(maxBlue, n);
                }
            }
            if (maxRed <= 12 && maxGreen <= 13 && maxBlue <= 14) {
                sumOfPossibleGameIds += id;
            }
            sumOfGamePowers += maxRed * maxGreen * maxBlue;
        }
        return new int[] {sumOfPossibleGameIds, sumOfGamePowers};
    }
}
