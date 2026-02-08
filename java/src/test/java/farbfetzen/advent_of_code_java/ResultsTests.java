package farbfetzen.advent_of_code_java;

import static org.assertj.core.api.Assertions.assertThat;

import org.junit.jupiter.api.Test;

class ResultsTests {

    @Test
    void shouldHaveToStringEmpty() {
        assertThat(new Results()).hasToString("No results.");
    }

    @Test
    void shouldHaveToStringSimple() {
        final var results = new Results();
        results.addPart1Sample("foo");
        results.addPart2Sample("bar");
        results.setPart1("baz");
        results.setPart2("hurtz");

        assertThat(results).hasToString("""
                Results:

                part 1 sample:
                foo

                part 2 sample:
                bar

                part 1:
                baz

                part 2:
                hurtz""");
    }

    @Test
    void shouldHaveToStringFull() {
        final var results = new Results();
        results.addPart1Sample("1");
        results.addPart1Sample("2");
        results.addPart2Sample("3");
        results.addPart2Sample("4");
        results.addOtherSample("a", "A");
        results.addOtherSample("b", "[1, 2, 3]");
        results.setPart1("foo\nbar");
        results.setPart2("""
                █████ ███   ██  █████
                  █   █    █      █ \s
                  █   ███   █     █ \s
                  █   █      █    █ \s
                  █   █       █   █ \s
                  █   ████  ██    █ \s""");

        assertThat(results).hasToString("""
                Results:

                part 1 sample 0:
                1

                part 1 sample 1:
                2

                part 2 sample 0:
                3

                part 2 sample 1:
                4

                sample a:
                A

                sample b:
                [1, 2, 3]

                part 1:
                foo
                bar

                part 2:
                █████ ███   ██  █████
                  █   █    █      █ \s
                  █   ███   █     █ \s
                  █   █      █    █ \s
                  █   █       █   █ \s
                  █   ████  ██    █ \s""");
    }
}
