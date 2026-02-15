package farbfetzen.advent_of_code_java.util;

import static farbfetzen.advent_of_code_java.util.Itertools.product;
import static org.assertj.core.api.Assertions.assertThat;

import org.junit.jupiter.api.Test;

class ItertoolsTests {

    @Test
    void shouldReturnProduct() {
        assertThat(product(-1, 2, 0, 3)).containsExactly(
                new IntVector2(-1, 0),
                new IntVector2(0, 0),
                new IntVector2(1, 0),
                new IntVector2(-1, 1),
                new IntVector2(0, 1),
                new IntVector2(1, 1),
                new IntVector2(-1, 2),
                new IntVector2(0, 2),
                new IntVector2(1, 2)
        );
    }

    // TODO: Product where from == to for x or y or both.
    // TODO: Product where to < from for x or y or both.
}
