package ru.spbu.apmath.prog.hw1.task1;
import java.util.Scanner;

public class BinaryTest {
    public static void main(String[] args) throws IllegalArgumentException,ArithmeticException {
        System.out.println("Введите число");
         Scanner chislo = new Scanner(System.in);
         int value;
         try {
             value = chislo.nextInt();
         }catch (Exception e){
             throw new IllegalArgumentException("Введите целое не отрицательное число");
         }

        if (value < 0){
            throw new ArithmeticException("Число не должно быть отрицательным");
        }

        Binary result = new Binary(value);
        System.out.println("Ваше число в двоичной системе:" + result.toBinary());
    }

}
