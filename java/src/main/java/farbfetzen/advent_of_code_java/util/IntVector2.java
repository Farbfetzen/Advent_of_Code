package farbfetzen.advent_of_code_java.util;

import java.util.Iterator;
import java.util.List;
import java.util.NoSuchElementException;

public record IntVector2(int x, int y) {

    private static final List<IntVector2> OFFSETS_8 = List.of(
            new IntVector2(-1, -1),
            new IntVector2(0, -1),
            new IntVector2(1, -1),
            new IntVector2(-1, 0),
            new IntVector2(1, 0),
            new IntVector2(-1, 1),
            new IntVector2(0, 1),
            new IntVector2(1, 1)
    );

    IntVector2() {
        this(0, 0);
    }

    // TODO: unit test
    // TODO: javadoc
    public IntVector2 add(final IntVector2 other) {
        return new IntVector2(x + other.x, y + other.y);
    }

    // TODO: unit test
    // TODO: javadoc
    public Iterable<IntVector2> allNeighbors() {
        return () -> new Iterator<>() {
            int i = 0;

            @Override
            public boolean hasNext() {
                return i < 8;
            }

            @Override
            public IntVector2 next() {
                if (hasNext()) {
                    return add(OFFSETS_8.get(i++));
                }
                throw new NoSuchElementException();
            }
        };
    }

    // TODO: unit test
    // TODO: javadoc
    public Iterable<IntVector2> allNeighbors(final int maxXExclusive, final int maxYExclusive) {
        return () -> new Iterator<>() {
            int i = 0;
            IntVector2 next;

            @Override
            public boolean hasNext() {
                while (next == null && i < 8) {
                    next = add(OFFSETS_8.get(i++));
                    if (next.x < 0 || next.x >= maxXExclusive || next.y < 0 || next.y >= maxYExclusive) {
                        next = null;
                    }
                }
                return next != null;
            }

            @Override
            public IntVector2 next() {
                if (hasNext()) {
                    final var result = next;
                    next = null;
                    return result;
                }
                throw new NoSuchElementException();
            }
        };
    }

    // TODO: unit test
    // TODO: javadoc
    public Iterable<IntVector2> allNeighbors(final Grid grid) {
        return allNeighbors(grid.getWidth(), grid.getHeight());
    }
}
