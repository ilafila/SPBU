package ru.spbu.apmath.prog.hw1.task3;

import java.util.ArrayList;
import java.util.List;

public class RotateArr {
    public  static List<Integer> rotate(List<Integer> array){
        if (array.isEmpty()){
            List<Integer> empty_list = new ArrayList<>();
            return empty_list;
        }

        List<Integer> copy_array = new ArrayList<>();
        for (int i = 0;i < array.size();i++){
            copy_array.add(array.get(i));
        }
        copy_array.add(0,copy_array.get(copy_array.size() - 1));
        copy_array.remove(copy_array.size() - 1);
        return copy_array;
    }
}
