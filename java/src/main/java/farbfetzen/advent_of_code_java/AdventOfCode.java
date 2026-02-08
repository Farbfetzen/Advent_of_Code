package farbfetzen.advent_of_code_java;

import java.io.IOException;
import java.lang.reflect.InvocationTargetException;

public class AdventOfCode {

    record ParsedArgs(int year, int day) {}

    static void main(final String[] args)
            throws IOException, InvocationTargetException, NoSuchMethodException, InstantiationException,
                   IllegalAccessException {
        try {
            final var parsedArgs = parseArgs(args);
            final var inputs = Inputs.fromFile(parsedArgs.year(), parsedArgs.day());
            final var results = solve(parsedArgs.year(), parsedArgs.day(), inputs);
            IO.println(results);
        } catch (final UserErrorException e) {
            IO.println(e.getMessage());
            System.exit(1);
        }
    }

    static ParsedArgs parseArgs(final String[] args) {
        if (args.length != 2) {
            throw new UserErrorException("Exactly two positional arguments expected: year and day.");
        }
        try {
            final int year = Integer.parseInt(args[0]);
            final int day = Integer.parseInt(args[1]);
            return new ParsedArgs(year, day);
        } catch (final NumberFormatException _) {
            throw new UserErrorException("All arguments must be integers.");
        }
    }

    static Results solve(final int year, final int day, final Inputs inputs)
            throws NoSuchMethodException, InvocationTargetException, InstantiationException, IllegalAccessException {
        final Class<? extends Solution> solutionClass;
        try {
            solutionClass = Class
                    .forName("farbfetzen.advent_of_code_java.year%d.Solution%dDay%02d".formatted(year, year, day))
                    .asSubclass(Solution.class);
        } catch (final ClassNotFoundException _) {
            throw new UserErrorException("No solution found for year \"%d\" and day \"%d\"".formatted(year, day));
        }
        return solutionClass.getDeclaredConstructor().newInstance().solve(inputs);
    }
}
