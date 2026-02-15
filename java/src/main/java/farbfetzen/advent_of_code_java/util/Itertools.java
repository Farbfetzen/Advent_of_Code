package farbfetzen.advent_of_code_java.util;

import java.util.Iterator;
import java.util.NoSuchElementException;

public class Itertools {

    private Itertools() {
        // This utility class should not be instantiated.
    }

    // TODO: unit tests
    // TODO: javadoc mi erwähnung, dass toX und toY exklusiv sind. Und warum die Methode "product" heißt (math. Produkt).
    public static Iterable<IntVector2> product(final int fromX, final int toX, final int fromY, final int toY) {
        return () -> new Iterator<>() {
            int x = fromX;
            int y = fromY;

            @Override
            public boolean hasNext() {
                return y < toY;
            }

            @Override
            public IntVector2 next() {
                if (hasNext()) {
                    final var result = new IntVector2(x++, y);
                    if (x >= toX) {
                        x = fromX;
                        y++;
                    }
                    return result;
                }
                throw new NoSuchElementException();
            }
        };
    }

    // TODO: unit tests
    // TODO: javadoc
    public static Iterable<IntVector2> positionsByRow(final Grid grid) {
        return product(0, grid.getWidth(), 0, grid.getHeight());
    }
}
