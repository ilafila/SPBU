package ru.spbu.apmath.prog.hw1.task2;

 class Employee {
    private String name;
    private double salary_per_hour;
    private int hours;


    public Employee(String name, double salary_per_hour,int hours){
        this.name = name;
        this.salary_per_hour = salary_per_hour;
        this.hours = hours;
    }

    public String getName(){
        return name;
    }

     public double getSalary_per_hour() {
         return salary_per_hour;
     }

     public int getHours(){
        return hours;
     }

     private static final double min_salary_per_hour = 70d;
     private static final int norm_work_time = 40;
     private static final int max_max_time = 60;



     public double getSalary(){
         if(hours > max_max_time || (min_salary_per_hour - salary_per_hour) > 0.00001d){
             throw new IllegalStateException();
         }
         if (hours > norm_work_time && hours < max_max_time){
             return hours*1.5d*salary_per_hour;
         }
        return hours*salary_per_hour;
     }
 }
