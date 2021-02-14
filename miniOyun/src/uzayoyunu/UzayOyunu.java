package uzayoyunu;

import javax.swing.JFrame;

/**
 *
 * @author zoirasu
 */
public class UzayOyunu extends JFrame {

    public UzayOyunu(String frameBaslik) {

    }

    public static void main(String[] args) {

        UzayOyunu anaEkran = new UzayOyunu("Uzay Oyunu");

        anaEkran.setResizable(false);
        anaEkran.setFocusable(false); // Jframe yerine JPanel'e odaklan.
        anaEkran.setSize(800, 600);
        anaEkran.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        Oyun oyun = new Oyun();

        oyun.requestFocus(); // Klavye işlemlerini anlaması için.
        oyun.addKeyListener(oyun); // KEylistener implemente edilmeli

        oyun.setFocusable(true); // Odağı JPanel'e veriyorum.
        oyun.setFocusTraversalKeysEnabled(false); // Klavye işlemlerinin gerçekleşmesi

        anaEkran.add(oyun);
        anaEkran.setVisible(true); // !!!! Kodların sırası önemli . Mesela Visible yukarıda olursa add oyun dedigimizde bazı özellikler görünmüyor.

    }

}
