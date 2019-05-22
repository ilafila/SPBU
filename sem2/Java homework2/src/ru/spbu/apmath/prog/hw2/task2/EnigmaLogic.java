package ru.spbu.apmath.prog.hw2.task2;

import static ru.spbu.apmath.prog.hw2.task2.Converter.convert;

public class EnigmaLogic {
    public static int countLetters() {
        int result = 0;
        for (int i = 1; i <= 1000; i++) {
            String allnum = convert(i);
            allnum = allnum.replaceAll(" ","");
            result += allnum.length();
        }
        return result;
    }
}
