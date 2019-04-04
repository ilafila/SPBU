package ru.spbu.apmath.prog.hw1.task3;
import java.util.ArrayList;

public class RotateArrTest {
    public static void main(String[] args) {
        ArrayList < Integer > mylst = new ArrayList <> ();
        mylst.add(1);
        mylst.add(2);
        mylst.add(3);
        ArrayList < Integer > result = RotateArr.rotate(mylst);
        System.out.println(result);
    }

}
