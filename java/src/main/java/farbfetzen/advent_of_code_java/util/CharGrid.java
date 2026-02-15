package farbfetzen.advent_of_code_java.util;

import lombok.Getter;

@Getter
public class CharGrid implements Grid {

    private final int width;
    private final int height;
    private final char[] content;

    // TODO: unit test
    public CharGrid(final String input) {
        final var lines = input.lines().toList();
        width = lines.getFirst().length();
        height = lines.size();
        content = String.join("", lines).toCharArray();
    }

    // TODO: unit test
    public char getAt(final int x, final int y) {
        return content[x + y * width];
    }

    // TODO: unit test
    public char getAt(final IntVector2 position) {
        return getAt(position.x(), position.y());
    }
}
