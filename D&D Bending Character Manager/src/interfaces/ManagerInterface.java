package interfaces;

import java.awt.*;
import bender.*;

public class ManagerInterface extends Frame(){
    ManagerInterface(boolean selectFile, Bender character) {
        Label nameLabel = new Label(character.getName);
        add(nameLabel);
        Label elementLabel = new Label(character.getElement);
        add(elementLabel);
        Label raceLabel = new Label(character.getRace);
        add(racelabel);
        Label levelLabel = new Label(character.getLevel);
    }
}
