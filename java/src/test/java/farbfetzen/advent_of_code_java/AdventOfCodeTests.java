package farbfetzen.advent_of_code_java;

import static org.assertj.core.api.Assertions.assertThat;
import static org.assertj.core.api.Assertions.assertThatExceptionOfType;

import java.util.List;
import java.util.stream.Stream;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.MethodSource;

import farbfetzen.advent_of_code_java.AdventOfCode.ParsedArgs;

class AdventOfCodeTests {

    private static final String ERROR_MESSAGE_INT = "Error: All arguments must be integers.";
    private static final String ERROR_MESSAGE_TWO = "Error: Exactly two positional arguments expected: year and day.";

    @Test
    void shouldParseArgs() {
        final var parsedArgs = AdventOfCode.parseArgs(new String[]{"2023", "1"});
        final var expected = new ParsedArgs(2023, 1);
        assertThat(parsedArgs).isEqualTo(expected);
    }

    @ParameterizedTest
    @MethodSource("provideInvalidArgs")
    void parsingInvalidArgsShouldThrow(final String[] args, final String expectedMessage) {
        assertThatExceptionOfType(UserErrorException.class)
                .isThrownBy(() -> AdventOfCode.parseArgs(args))
                .withMessage(expectedMessage);
    }

    private static Stream<Arguments> provideInvalidArgs() {
        return Stream.of(
                Arguments.of(new String[]{}, ERROR_MESSAGE_TWO),
                Arguments.of(new String[]{"2023"}, ERROR_MESSAGE_TWO),
                Arguments.of(new String[]{"2023", "1", "2"}, ERROR_MESSAGE_TWO),
                Arguments.of(new String[]{"", ""}, ERROR_MESSAGE_INT),
                Arguments.of(new String[]{"foo", "bar"}, ERROR_MESSAGE_INT),
                Arguments.of(new String[]{"2023.", "1,9"}, ERROR_MESSAGE_INT)
        );
    }

    @Test
    void shouldSolve() throws Exception {
        final var inputs = Inputs.fromFile(2023, 1);
        final var results = AdventOfCode.solve(2023, 1, inputs);
        assertThat(results.getPart1Samples()).singleElement().isEqualTo("142");
        assertThat(results.getPart2Samples()).singleElement().isEqualTo("281");
        assertThat(results.getOtherSamples()).isEmpty();
        assertThat(results.getPart1()).isEqualTo("54697");
        assertThat(results.getPart2()).isEqualTo("54885");
    }

    @Test
    void solvingShouldThrowIfSolutionDoesntExist() {
        final var inputs = new Inputs("", List.of());
        assertThatExceptionOfType(UserErrorException.class)
                .isThrownBy(() -> AdventOfCode.solve(1999, 0, inputs))
                .withMessage("Error: No solution found for year \"1999\" and day \"0\"");
    }
}
