package farbfetzen.advent_of_code_java;

import java.io.IOException;
import java.io.UncheckedIOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;
import java.util.stream.Stream;

public record Inputs(String input, List<String> samples) {

    public static Inputs fromFile(final int year, final int day) throws IOException {
        final Path yearDir = Path.of("").toAbsolutePath().getParent().resolve("input", String.valueOf(year));
        final var paddedDay = "%02d".formatted(day);

        final Path inputFilePath = yearDir.resolve(paddedDay + "-input.txt");
        if (Files.notExists(inputFilePath)) {
            throw new UserErrorException("No input file found for year \"%d\" and day \"%d\".".formatted(year, day));
        }
        final String input = Files.readString(inputFilePath).stripTrailing();

        final List<String> samples;
        try (final Stream<Path> paths = Files.list(yearDir)) {
            samples = paths
                    .filter(p -> p.getFileName().toString().matches(paddedDay + "-sample.*\\.txt"))
                    .sorted()
                    .map(path -> {
                        try {
                            return Files.readString(path).stripTrailing();
                        } catch (final IOException e) {
                            throw new UncheckedIOException(e);
                        }
                    })
                    .toList();
        }
        return new Inputs(input, samples);
    }
}
