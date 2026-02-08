package farbfetzen.advent_of_code_java.year2023;

import java.util.Map;
import java.util.regex.Pattern;

import farbfetzen.advent_of_code_java.Inputs;
import farbfetzen.advent_of_code_java.Results;
import farbfetzen.advent_of_code_java.Solution;

/**
 * <a href="https://adventofcode.com/2023/day/1">adventofcode.com/2023/day/1</a>
 */
public class Solution2023Day01 implements Solution {

    private static final String GENERAL_REGEX = "(%s)(?:.*(%s))?";
    private static final Pattern PART_1_PATTERN = Pattern.compile(GENERAL_REGEX.formatted("\\d", "\\d"));
    private static final String PART_2_DIGIT = "\\d|one|two|three|four|five|six|seven|eight|nine";
    private static final Pattern PART_2_PATTERN = Pattern.compile(GENERAL_REGEX.formatted(PART_2_DIGIT, PART_2_DIGIT));

    // @formatter:off
    private static final Map<String, Integer> WORD_VALUES = Map.of(
            "one", 1,
            "two", 2,
            "three", 3,
            "four", 4,
            "five", 5,
            "six", 6,
            "seven", 7,
            "eight", 8,
            "nine", 9
    );
    // @formatter:on

    @Override
    public Results solve(final Inputs inputs) {
        final var results = new Results();
        results.addPart1Sample(solvePart1(inputs.samples().getFirst()));
        results.addPart2Sample(solvePart2(inputs.samples().getLast()));
        results.setPart1(solvePart1(inputs.input()));
        results.setPart2(solvePart2(inputs.input()));
        return results;
    }

    private static int solvePart1(final String input) {
        return PART_1_PATTERN.matcher(input).results().mapToInt(matchResult -> {
            final int firstValue = Integer.parseInt(matchResult.group(1));
            final String last = matchResult.group(2);
            return firstValue * 10 + (last == null ? firstValue : Integer.parseInt(last));
        }).sum();
    }

    private static int solvePart2(final String input) {
        return PART_2_PATTERN.matcher(input).results().mapToInt(matchResult -> {
            final int firstValue = parseInt(matchResult.group(1));
            final String last = matchResult.group(2);
            return firstValue * 10 + (last == null ? firstValue : parseInt(last));
        }).sum();
    }

    private static int parseInt(final String str) {
        return str.length() == 1 ? Integer.parseInt(str) : WORD_VALUES.get(str);
    }
}
