package ru.spbu.apmath.prog.hw1.task3;

import java.util.ArrayList;

public class RotateArr {
    public  static ArrayList<Integer> rotate(ArrayList<Integer> array){
        array.add(0,array.size());
        array.remove(array.size()-1);
        return array;
    }
}
