package ru.spbu.apmath.prog.hw2.task1;

import java.util.Scanner;

public class SaleSumTest {
    public static void main(String[] args) throws IllegalArgumentException,ArithmeticException {
        System.out.println("Введите скидку,предлагаемую магазином");
        Scanner chislo = new Scanner(System.in);
        int value;
        try {
            value = chislo.nextInt();
        }catch (Exception e){
            throw new IllegalArgumentException("Введите целое не отрицательное число");
        }
        SaleSum sale = new SaleSum(value);
        System.out.println("Ваша реальная скидка равна " + sale.realSale() + "%");
    }
}
