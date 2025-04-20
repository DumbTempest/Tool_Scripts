import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.util.ArrayList;

public class MouseCoordTracker {

    private final JLabel positionLabel;
    private final JLabel savedLabel;
    private final ArrayList<Point> savedCoords = new ArrayList<>();

    public MouseCoordTracker() {
        JFrame frame = new JFrame("Mouse Coord Tracker");
        frame.setSize(500, 300);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(new FlowLayout());

        positionLabel = new JLabel("Mouse Coord: (0, 0)");
        positionLabel.setFont(new Font("Arial", Font.PLAIN, 14));
        frame.add(positionLabel);

        JButton saveButton = new JButton("Save Coords");
        frame.add(saveButton);

        savedLabel = new JLabel("Saved Coords:");
        savedLabel.setFont(new Font("Arial", Font.PLAIN, 12));
        frame.add(savedLabel);

        Timer timer = new Timer(100, e -> updateMousePosition());
        timer.start();

        saveButton.addActionListener(e -> saveCoord());

        // Key listener for 'S' key
        frame.addKeyListener(new KeyAdapter() {
            @Override
            public void keyPressed(KeyEvent e) {
                if (e.getKeyChar() == 's') {
                    saveCoord();
                }
            }
        });

        frame.setFocusable(true);  // Ensure JFrame can receive key events
        frame.setVisible(true);
        frame.requestFocusInWindow();  // Force focus on the window
    }

    private void updateMousePosition() {
        Point mousePos = MouseInfo.getPointerInfo().getLocation();
        positionLabel.setText("Mouse Position: (" + mousePos.x + ", " + mousePos.y + ")");
    }

    private void saveCoord() {
        Point mousePos = MouseInfo.getPointerInfo().getLocation();
        savedCoords.add(mousePos);
        updateSavedCoords();
    }

    private void updateSavedCoords() {
        StringBuilder sb = new StringBuilder("Saved Coords:<br>");
        for (Point p : savedCoords) {
            sb.append("(").append(p.x).append(", ").append(p.y).append(")<br>");
        }
        savedLabel.setText("<html>" + sb.toString() + "</html>");
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(MouseCoordTracker::new);
    }
}
