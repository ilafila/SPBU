package ru.spbu.apmath.prog.hw1.task3;
import java.util.ArrayList;

public class RotateArr {
    public static void main(String[] args) {
        ArrayList < Integer > mylst = new ArrayList <> ();
        mylst.add(1);
        mylst.add(2);
        mylst.add(3);
        ArrayList < Integer > result = rotate(mylst);
        System.out.println(result);
    }

    public  static ArrayList<Integer> rotate(ArrayList<Integer> arr){
        arr.add(0,arr.size());
        arr.remove(arr.size()-1);
        return arr;
    }
}
