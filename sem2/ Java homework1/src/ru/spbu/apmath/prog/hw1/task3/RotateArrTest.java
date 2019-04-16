package ru.spbu.apmath.prog.hw1.task3;
import java.util.ArrayList;
import java.util.List;

public class RotateArrTest {
    public static void main(String[] args) {
        List < Integer > mylst = new ArrayList <> ();
        List < Integer > emp_lst = new ArrayList <> ();
        mylst.add(1);
        mylst.add(2);
        mylst.add(3);
        mylst.add(6);
        List<Integer> result = RotateArr.rotate(mylst);
        List<Integer> result2 = RotateArr.rotate(emp_lst);
        System.out.println(result2);
        System.out.println(result);
    }

}
