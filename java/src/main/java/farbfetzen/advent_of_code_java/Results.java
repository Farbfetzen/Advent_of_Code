package farbfetzen.advent_of_code_java;

import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

import lombok.Getter;
import org.apache.commons.lang3.StringUtils;
import org.jspecify.annotations.Nullable;

@Getter
public class Results {

    private final List<String> part1Samples = new ArrayList<>();
    private final List<String> part2Samples = new ArrayList<>();
    private final Map<String, String> otherSamples = new LinkedHashMap<>();

    @Nullable
    private String part1;

    @Nullable
    private String part2;

    public void addPart1Sample(final String result) {
        part1Samples.add(result);
    }

    public void addPart1Sample(final int result) {
        addPart1Sample(String.valueOf(result));
    }

    public void addPart2Sample(final String result) {
        part2Samples.add(result);
    }

    public void addPart2Sample(final int result) {
        addPart2Sample(String.valueOf(result));
    }

    public void addOtherSample(final String key, final String result) {
        otherSamples.put(key, result);
    }

    public void setPart1(final String result) {
        part1 = result;
    }

    public void setPart1(final int result) {
        setPart1(String.valueOf(result));
    }

    public void setPart2(final String result) {
        part2 = result;
    }

    public void setPart2(final int result) {
        setPart2(String.valueOf(result));
    }

    @Override
    public String toString() {
        final var stringParts = new ArrayList<String>();
        samplesToString(part1Samples, 1, stringParts);
        samplesToString(part2Samples, 2, stringParts);
        if (!otherSamples.isEmpty()) {
            for (final var entry : otherSamples.entrySet()) {
                stringParts.add("sample %s:%n%s".formatted(entry.getKey(), entry.getValue()));
            }
        }
        if (StringUtils.isNotBlank(part1)) {
            stringParts.add("part 1:%n%s".formatted(part1));
        }
        if (StringUtils.isNotBlank(part2)) {
            stringParts.add("part 2:%n%s".formatted(part2));
        }
        if (stringParts.isEmpty()) {
            return "No results.";
        }
        stringParts.addFirst("Results:");
        return String.join("\n\n", stringParts);
    }

    private static void samplesToString(
            final List<String> samples,
            final int partNumber,
            final List<String> parts
    ) {
        if (!samples.isEmpty()) {
            if (samples.size() == 1) {
                parts.add("part %d sample:%n%s".formatted(partNumber, samples.getFirst()));
            } else {
                for (int i = 0; i < samples.size(); i++) {
                    parts.add("part %d sample %d:%n%s".formatted(partNumber, i, samples.get(i)));
                }
            }
        }
    }
}
