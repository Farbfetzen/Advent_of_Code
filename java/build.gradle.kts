plugins {
    application
}

group = "farbfetzen"
version = "1.0-SNAPSHOT"

repositories {
    mavenCentral()
}

dependencies {
    testImplementation(platform("org.junit:junit-bom:6.0.2"))
    testImplementation("org.junit.jupiter:junit-jupiter")
}

java {
    toolchain {
        languageVersion = JavaLanguageVersion.of(25)
    }
}

application {
    mainClass = "farbfetzen.advent_of_code_java.AdventOfCode"
}

tasks.test {
    useJUnitPlatform()
}
