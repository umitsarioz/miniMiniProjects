/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package uzayoyunu;

import java.awt.Color;
import java.awt.Graphics;
import java.awt.List;
import java.awt.Rectangle;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;

import java.util.LinkedList;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.imageio.ImageIO;
import javax.imageio.stream.FileImageInputStream;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.Timer;

/**
 *
 * @author zoirasu
 */
public class Oyun extends JPanel implements KeyListener, ActionListener {

    Timer timer = new Timer(5, this);
    private int gecen_sure = 0;
    private int harcanan_ates = 0;

    private BufferedImage image;  // Uzay gemisini yerleştirmek için eklendi.

    private LinkedList<Ates> atesler = new LinkedList<Ates>(); // Ateşlerin tutulacağı arraylist

    private int atesdirY = 1; // Ateşlerin ileri gidişi için.
    private int topX = 0; // Top ekranda sağa sola gidecek.

    private int topdirX = 2; // Top'un aldığı mesafe

    private int uzayGemisiX = 0; // Uzay gemisinin başlangıç noktası
    private int dirUzayX = 20; // Uzay gemisinin hareket menzili

    public boolean kontrolEt() {

        for (Ates ates : atesler) {

            if (new Rectangle(ates.getX(), ates.getY(), 10, 20).intersects(new Rectangle(topX, 0, 20, 20))) {
                return true;
            }
        }

        return false;
    }

    public Oyun() {
        setBackground(Color.BLACK);

        // Uzay gemisi image ekle.
        try {
            image = ImageIO.read(new FileImageInputStream(new File("uzaygemisi.png")));
        } catch (IOException ex) {
            Logger.getLogger(Oyun.class.getName()).log(Level.SEVERE, null, ex);
        }

        // Timer başlat
        timer.start();
    }

    @Override
    public void paint(Graphics g) {
        super.paint(g);

        g.setColor(Color.red);
        g.fillOval(topX, 0, 20, 20); // Daire şeklinde top.
        g.drawImage(image, uzayGemisiX, 490, image.getWidth() / 10, image.getHeight() / 10, this); // resim,x koordinat,y koordinat,genişlik,uzunluk,ve çalışacağı panel.

        for (Ates ates : atesler) {
            if (ates.getY() < 0) {
                atesler.remove(ates); // Eğer ateş oyun sahasını terkederse arraylist'den sil.
            }
        }

        g.setColor(Color.blue);
        for (Ates ates : atesler) {
            g.fillRect(ates.getX(), ates.getY(), 10, 20); // Ateş şeklini oluştur yani çizer.
        }

        if (kontrolEt()) {
            timer.stop();
            JOptionPane.showMessageDialog(this, "GG!","KAZANDINIZ ! GG ! ",1);
      
            System.exit(0);
        }

    }

    @Override
    public void repaint() {
        super.repaint(); // Paint metodunu tekrarlar..
    }

    @Override
    public void keyTyped(KeyEvent ke) {

    }

    @Override
    public void keyPressed(KeyEvent ke) {

        int c = ke.getKeyCode(); // Karakter 
        switch (c) {
            case KeyEvent.VK_LEFT:
                if (uzayGemisiX <= 0) {
                    uzayGemisiX = 0;
                } else {
                    uzayGemisiX -= dirUzayX;
                }   break;
            case KeyEvent.VK_RIGHT:
                if (uzayGemisiX > 720) {
                    uzayGemisiX = 748;
                } else {
                    uzayGemisiX += dirUzayX;
                }   break;
            case KeyEvent.VK_SPACE:
                atesler.add(new Ates(uzayGemisiX + 15, 475)); // ateş oluştur.
                harcanan_ates++;
                break;
            default:
                break;
        }
    }

    @Override
    public void keyReleased(KeyEvent ke) {
    }

    @Override
    public void actionPerformed(ActionEvent ae) {

        for (Ates ates : atesler) {
            ates.setY(ates.getY() - atesdirY); // Ateş'i yukarı doğru hareket ettir.
        }

        topX += topdirX;
        if (topX >= 750) {
            topdirX = -2;
        }
        if (topX <= 0) {
            topdirX = 2;
        }
        repaint();
    }
}
