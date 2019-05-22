package ru.spbu.apmath.prog.hw2.task1;

public class SaleSum {
    private int num;
    public SaleSum(int num){
        this.num = num;
    }
    public int realSale(){
        int copyRes = num;
        if (copyRes < 0)
            throw new ArithmeticException("Число не должно быть отрицательным");
        if (copyRes % 10 == copyRes){
            return copyRes;
        }
        int result = 0;
        while (copyRes != 0){
            result += copyRes % 10;
            copyRes /= 10;
        }
        num = result;
        return realSale();
    }
}
