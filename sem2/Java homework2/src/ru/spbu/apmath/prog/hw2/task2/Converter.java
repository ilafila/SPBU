package ru.spbu.apmath.prog.hw2.task2;


// Советовался с Костей Коганом


public class Converter {
    static String[] edinici = {"", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"};
    static String[] sotni = {"", "сто","двести","триста","четыреста","пятьсот",
            "шестьсот","семьсот", "восемьсот","девятьсот"};
    static String[] do20 = {"десять","одиннадцать","двенадцать","тринадцать","четырнадцать",
            "пятнадцать","шестнадцать","семнадцать","восемнадцать","девятнадцать"};
    static String[] decyatki = {"", "десять","двадцать","тридцать","сорок","пятьдесят","шестьдесят",
            "семьдесят","восемьдесят","девяносто"};
    public static String convert(int n) {
        if (n / 1000 == 1) {
            return "тысяча";
        }
        if (numCounter(n) == 1) {
            return edinici[n % 10];
        }
        if (numCounter(n) == 2) {
            if (n < 20) {
                return (do20[n % 10]);
            } else {
                String ed = edinici[n % 10];
                String des = decyatki[n / 10];
                return des + " " + ed;
            }
        } else {
            if ((n % 100) > 19) {
                String sot = sotni[n / 100];
                String des = decyatki[(n % 100) / 10];
                String ed = edinici[n % 10];
                return sot + " " + des + " " + ed;
            } else if (n % 100 <= 19 && n % 100 >= 10){
                String sot = sotni[n / 100];
                String des = do20[n % 10];
                return sot + " " + des;
            } else {
                String sot = sotni[n / 100];
                String ed = edinici[n % 10];
                return sot + " " + ed;
            }
        }
    }
    private static int numCounter(int num) {
        int count = 1;
        while (num / 10 > 0) {
            count++;
            num /= 10;
        }
        return count;
    }
}
