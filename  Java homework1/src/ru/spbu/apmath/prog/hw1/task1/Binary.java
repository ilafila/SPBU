package ru.spbu.apmath.prog.hw1.task1;
import java.util.Scanner;

public class Binary {
    public static void main(String[] args) throws IllegalArgumentException,ArithmeticException {
        System.out.println("Введите число");
         Scanner chislo = new Scanner(System.in);
         int number = 0;
         try {
             number = chislo.nextInt();
         }catch (Exception e){
             throw new IllegalArgumentException("Введите целое не отрицательное число");
         }
        if (number < 0){
            throw new ArithmeticException("Число не должно быть отрицательным");
        }
        String result = toBinary(number);
        System.out.println("Ваше число в двоичной системе:" + result);
    }

    public static String toBinary(int num){
        StringBuilder answer = new StringBuilder();
        while (num > 0){
            if (num % 2 == 0)
                answer.append(0);
            else
                answer.append(1);
            num = num / 2;
        }
        String str = answer.toString();
        String result = "";
        for (int i = 0; i < str.length(); i++) {
            result = str.charAt(i) + result;
        }
        return result;
    }
}
