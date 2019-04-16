package ru.spbu.apmath.prog.hw1.task1;

  class Binary {
    private int number;

    public Binary(int number){
        this.number = number;
    }

    public String toBinary(){
        if (number < 0)
            throw new ArithmeticException("Число не должно быть отрицательным");
        int copy = number;
        StringBuilder answer = new StringBuilder();
        while (copy > 0){
            if (copy % 2 == 0)
                answer.append(0);
            else
                answer.append(1);
            copy = copy / 2;
        }
        String str = answer.toString();
        String result = "";
        for (int i = 0; i < str.length(); i++) {
            result = str.charAt(i) + result;
        }
        return result;
    }
}
