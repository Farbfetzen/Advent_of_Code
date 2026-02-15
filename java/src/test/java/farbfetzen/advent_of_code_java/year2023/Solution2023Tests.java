package farbfetzen.advent_of_code_java.year2023;

import static org.assertj.core.api.Assertions.assertThat;

import java.io.IOException;

import org.junit.jupiter.api.Test;

import farbfetzen.advent_of_code_java.Inputs;
import farbfetzen.advent_of_code_java.Results;

class Solution2023Tests {

    @Test
    void testDay01() throws IOException {
        final var inputs = Inputs.fromFile(2023, 1);
        final Results results = new Solution2023Day01().solve(inputs);
        assertThat(results.getPart1Samples()).singleElement().isEqualTo("142");
        assertThat(results.getPart2Samples()).singleElement().isEqualTo("281");
        assertThat(results.getPart1()).isEqualTo("54697");
        assertThat(results.getPart2()).isEqualTo("54885");
    }

    @Test
    void testDay02() throws IOException {
        final var inputs = Inputs.fromFile(2023, 2);
        final var results = new Solution2023Day02().solve(inputs);
        assertThat(results.getPart1Samples()).singleElement().isEqualTo("8");
        assertThat(results.getPart2Samples()).singleElement().isEqualTo("2286");
        assertThat(results.getPart1()).isEqualTo("2727");
        assertThat(results.getPart2()).isEqualTo("56580");
    }
}
