package org.example;

import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;

public class PrizeToy {
    public static void main(String[] args) {
        PrizeToy prizeToy = new PrizeToy();
        prizeToy.addToy(new Toy(1, "Кукла", 5, 20));
        prizeToy.addToy(new Toy(2, "Мяч", 10, 30));
        prizeToy.addToy(new Toy(3, "Машинка", 8, 15));
        prizeToy.addToy(new Toy(4, "Конструктор", 3, 35));

        prizeToy.getPrizeToy();
    }
    private ArrayList<Toy> toys;

    public PrizeToy() {
        toys = new ArrayList<>();
    }

    public void addToy(Toy toy) {
        toys.add(toy);
    }

    public Toy chooseToy() {
        double random = Math.random() * 100;
        double sum = 0;
        for (Toy toy : toys) {
            sum += toy.getWeight();
            if (random <= sum) {
                return toy;
            }
        }
        return null;
    }

    public void getPrizeToy() {
        Toy prizeToy = chooseToy();
        if (prizeToy != null) {
            toys.remove(prizeToy);
            prizeToy.decreaseQuantity();
            try {
                FileWriter writer = new FileWriter("prize_toys.txt", true);
                writer.write(prizeToy.getName() + "\n");
                writer.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
}
