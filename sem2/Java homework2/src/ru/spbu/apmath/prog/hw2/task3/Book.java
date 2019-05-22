package ru.spbu.apmath.prog.hw2.task3;

public class Book {
    private String title;
    private boolean borrowed;


    // Создает новую книгу
    public Book(String bookTitle) {
        this.title = bookTitle;
    }

    // Отмечает книгу как взятую
    public void borrowed() {
        borrowed = true;
    }

    // Отмечает книгу как не взятую
    public void returned() {
        borrowed = false;
    }

    // Возвращает true, если книгу уже кто-то взял
    public boolean isBorrowed() {
        if (borrowed) {
            return true;
        }
        return false;
    }

    // Возвращает название книги
    public String getTitle() {
        return title;
    }
    public static void main(String[] arguments) {
        // Небольшой тест для класса Book
        Book example = new Book("Дневник кота");

        System.out.println("Название книги (должно быть 'Дневник кота'): " + example.getTitle());
        System.out.println("Взята? (должно быть false): " + example.isBorrowed());
        example.borrowed();
        System.out.println("Взята? (должно быть true): " + example.isBorrowed());
        example.returned();
        System.out.println("Взята? (должно быть false): " + example.isBorrowed());
    }

}
