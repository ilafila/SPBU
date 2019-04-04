package ru.spbu.apmath.prog.hw1.task1;

public class Binary {
    private int number;

    public Binary(int number){
        this.number = number;
    }

    public String toBinary(){
        StringBuilder answer = new StringBuilder();
        while (number > 0){
            if (number % 2 == 0)
                answer.append(0);
            else
                answer.append(1);
            number = number / 2;
        }
        String str = answer.toString();
        String result = "";
        for (int i = 0; i < str.length(); i++) {
            result = str.charAt(i) + result;
        }
        return result;
    }
}
