package farbfetzen.advent_of_code_java.year2023;

import static farbfetzen.advent_of_code_java.util.Itertools.positionsByRow;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;

import farbfetzen.advent_of_code_java.Inputs;
import farbfetzen.advent_of_code_java.Results;
import farbfetzen.advent_of_code_java.Solution;
import farbfetzen.advent_of_code_java.util.CharGrid;
import farbfetzen.advent_of_code_java.util.IntVector2;

/**
 * <a href="https://adventofcode.com/2023/day/3">adventofcode.com/2023/day/3</a>
 */
public class Solution2023Day03 implements Solution {

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

    // TODO: Vielleicht nicht solveBoth, sondern ein Iterate-Schritt und dann die Lösungen in separate Methoden?
    //  Oder schau, ob du die Methode sonst wie aufteilen kannst, um die Komplexität zu reduzieren.
    private static int[] solveBoth(final String input) {
        final var grid = new CharGrid(input);
        int nonPartNumberSum = 0;
        var adjacentToSymbol = false;
        var currentNumber = new StringBuilder();
        final var foundGearPositions = new HashSet<IntVector2>();
        final var gearCandidates = new HashMap<IntVector2, List<Integer>>();
        for (final var currentPosition : positionsByRow(grid)) {
            final char current = grid.getAt(currentPosition);
            if (Character.isDigit(current)) {
                currentNumber.append(current);
                for (final var neighborPosition : currentPosition.allNeighbors(grid)) {
                    final char neighbor = grid.getAt(neighborPosition);
                    if (neighbor == '.' || Character.isDigit(neighbor)) {
                        continue;
                    }
                    adjacentToSymbol = true;
                    if (neighbor == '*') {
                        foundGearPositions.add(neighborPosition);
                    }
                }
            } else if (!currentNumber.isEmpty()) {
                if (adjacentToSymbol) {
                    final int n = Integer.parseInt(currentNumber.toString());
                    nonPartNumberSum += n;
                    adjacentToSymbol = false;

                    foundGearPositions.forEach(pos -> gearCandidates
                            .computeIfAbsent(pos, _ -> new ArrayList<>())
                            .add(n));
                    foundGearPositions.clear();
                }
                currentNumber = new StringBuilder();
            }
        }

        final int gearRatioSum = gearCandidates
                .values()
                .stream()
                .filter(numbers -> numbers.size() == 2)
                .mapToInt(numbers -> numbers.getFirst() * numbers.getLast())
                .sum();

        return new int[]{nonPartNumberSum, gearRatioSum};
    }
}
