package bender;

enum Element {
    Earth,
    Air,
    Fire,
    Water
}

enum Race {
    Aarakocra,
    Asimar,
    Bugbear,
    Dragonborn,
    Dwarf,
    Elf,
    Firbolg,
    Genasi,
    Gith,
    Gnome,
    Goblin,
    Goliath,
    Half_Elf,
    Half_Orc,
    Halfling,
    Hobgoblin,
    Human,
    Kenku,
    Kobold,
    Lizardfolk,
    Orc,
    Tabaxi,
    Tiefling,
    Tortle,
    Triton,
    Yuan_Ti
};

public class Bender {
    private Element element;
    private String name;
    private Integer level;
    private Integer experience;
    private Race race;
    private String features;
    private Integer points;
    private Integer spentPoints;
    Bender(Element e, String n, Integer l, Integer exp, Race r) {
        element = e;
        name = n;
        setExperience(exp);
        race = r;
        // Define features
        features += "Bender Features\n";
        switch (element) {
            case Earth:
                features += "";
                break;
            case Air:
                features += "";
                break;
            case Fire:
                features += "";
                break;
            case Water:
                features += "";
                break;
        }
        features += "\nRacial Features\n";
        switch (race) {
            case Aarakocra:
                features += "";
                break;
            case Asimar:
                features += "";
                break;
            case Bugbear:
                features += "";
                break;
            case Dragonborn:
                features += "";
                break;
            case Dwarf:
                features += "";
                break;
            case Elf:
                features += "";
                break;
            case Firbolg:
                features += "";
                break;
            case Genasi:
                features += "";
                break;
            case Gith:
                features += "";
                break;
            case Gnome:
                features += "";
                break;
            case Goblin:
                features += "";
                break;
            case Goliath:
                features += "";
                break;
            case Half_Elf:
                features += "";
                break;
            case Half_Orc:
                features += "";
                break;
            case Halfling:
                features += "";
                break;
            case Hobgoblin:
                features += "";
                break;
            case Human:
                features += "";
                break;
            case Kenku:
                features += "";
                break;
            case Kobold:
                features += "";
                break;
            case Lizardfolk:
                features += "";
                break;
            case Orc:
                features += "";
                break;
            case Tabaxi:
                features += "";
                break;
            case Tiefling:
                features += "";
                break;
            case Tortle:
                features += "";
                break;
            case Triton:
                features += "";
                break;
            case Yuan_Ti:
                features += "";
                break;
        }
        // Set points
        points = 25 + (level * 5);
    }

    // element getter
    public Element getElement() {
        return element;
    }

    // name getter
    public String getName() {
        return name;
    }

    // level getter
    public Integer getLevel() {
        return level;
    }

    // experience getter
    public Integer getExperience() {
        return experience;
    }

    // experience setter
    public void setExperience(Integer exp) {
        experience = exp;
        if (exp >= 0) {
            level = 1;
        }
        if (exp >= 300) {
            level = 2;
        }
        if (exp >= 300) {
            level = 2;
        }
        if (exp >= 900) {
            level = 3;
        }
        if (exp >= 2700) {
            level = 4;
        }
        if (exp >= 6500) {
            level = 5;
        }
        if (exp >= 14000) {
            level = 6;
        }
        if (exp >= 23000) {
            level = 7;
        }
        if (exp >= 34000) {
            level = 8;
        }
        if (exp >= 48000) {
            level = 9;
        }
        if (exp >= 64000) {
            level = 10;
        }
        if (exp >= 85000) {
            level = 11;
        }
        if (exp >= 100000) {
            level = 12;
        }
        if (exp >= 120000) {
            level = 13;
        }
        if (exp >= 140000) {
            level = 14;
        }
        if (exp >= 1650000) {
            level = 15;
        }
        if (exp >= 195000) {
            level = 16;
        }
        if (exp >= 225000) {
            level = 17;
        }
        if (exp >= 265000) {
            level = 18;
        }
        if (exp >= 305000) {
            level = 19;
        }
        if (exp >= 355000) {
            level = 20;
        }
    }

    // race getter
    public String getRace() {
        switch (race) {
            case Half_Elf:
                return "Half Elf";
            case Half_Orc:
                return "Half Orc";
            case Yuan_Ti:
                return "Yuan-Ti";
            default:
                return race.name();
        }
    }
}
