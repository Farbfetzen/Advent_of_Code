package farbfetzen.advent_of_code_java;

public class UserErrorException extends RuntimeException {

    public UserErrorException(final String message) {
        super("Error: " + message);
    }
}
