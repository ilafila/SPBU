package ru.spbu.apmath.prog.hw2.task3;

import java.util.ArrayList;
import java.util.List;

public class Library {
    private String address;
    List<Book> books = new ArrayList<>();


    public Library(String address) {
        this.address = address;
    }


    public void addBook(Book book) {
        if (books.contains(book)) {
            System.out.println("Такая книга уже есть");
        } else {
            books.add(book);
            System.out.println("Книга \"" + book.getTitle() + "\" успешно добавлена в библиотеку");
        }
    }

    public void printAddress() {
        System.out.println(address);
    }

    public void borrowBook(String title) {
        if (findBook(title) != null) {
            if (!findBook(title).isBorrowed()) {
                findBook(title).borrowed();
                System.out.println("Книга успешно взята");
            } else {
                System.out.println("Книга уже взята");
            }

        } else {
            System.out.println("Такой книги нет в каталоге");
        }

    }


    public void returnBook(String title) {
        if (findBook(title) != null) {
            if (findBook(title).isBorrowed()) {
                findBook(title).returned();
                System.out.println("Вы успешно вернули книгу");
            } else {
                System.out.println("Книга уже возвращена");
            }

        } else {
            System.out.println("Такой книги не было в библиотеке");
        }
    }

    public void printAvailableBooks() {
        if (books.size() != 0) {
            for (int i = 0; i < books.size(); i++) {
                if (!books.get(i).isBorrowed()) {
                    System.out.println(books.get(i).getTitle());
                }
            }
        } else {
            System.out.println("В библиотеке нет книг");
        }
    }

    public Book findBook(String title) {
        Book out = null;
        for (int i = 0; i < books.size(); i++) {
            if (books.get(i).getTitle().equals(title)) {
                out = books.get(i);
            }
        }
        return out;
    }



    public static void printOpeningHours() {
        System.out.println("Все библиотеки работают с понедельника по субботу с 9 до 18");
    }


    public static void main (String[]args){
        // Создаем две библиотеки
        Library firstLibrary = new Library("Университетский пр., 120");
        Library secondLibrary = new Library("Московский пр., 86");

        // Добавляем четыре книги в первую библиотеку
        firstLibrary.addBook(new Book("Код да Винчи")); // При добавлении на экран должно выводиться сообщение об успешном добавлении соответствующей книги
        firstLibrary.addBook(new Book("50 оттенков серого"));
        firstLibrary.addBook(new Book("Учебник мемологии"));
        firstLibrary.addBook(new Book("Властелин Колец"));

        // Выводим на экран часы работы и адреса
        System.out.println("Часы работы библиотек:");
        printOpeningHours(); // Что-то типа "Все библиотеки работают с понедельника по субботу с 9 до 18", текст на ваше усмотрение
        System.out.println();

        System.out.println("Адреса библиотек:");
        firstLibrary.printAddress(); // Выводит адрес
        secondLibrary.printAddress();
        System.out.println();

        // Пытаемся взять Властелина Колец из обеих библиотек
        System.out.println("Берем лучшую книгу на земле:");
        firstLibrary.borrowBook("Властелин Колец");  // Должно пройти успешно, мы должны получить соответствующее сообщение об успехе
        firstLibrary.borrowBook("Властелин Колец");   // Книга уже взята, об этом нам должны написать
        secondLibrary.borrowBook("Властелин Колец");  // Такой книги нет в каталоге, это тоже отдельное сообщение для нас
        System.out.println();

        // Выводим названия всех книг в обеих библиотеках
        System.out.println("Доступные книги в первой библиотеке:");
        firstLibrary.printAvailableBooks();  // Только список книг, которые можно взять
        System.out.println();
        System.out.println("Доступные книги во второй библиотеке:");
        secondLibrary.printAvailableBooks(); // Так как во вторую книг не добавляли, то тут надо написать что-то типа "В каталоге пусто"
        System.out.println();

        // Возвращаем Властелина Колец в первую библиотеку
        System.out.println("Прочитали Властелина Колец, возвращаем:");
        firstLibrary.returnBook("Властелин Колец"); // Сообщение об успешном возвращении
        System.out.println();

        // Снова выводим список доступных книг в первой библиотеке
        System.out.println("Доступные книги в первой библиотеке:");
        firstLibrary.printAvailableBooks();
    }
}
