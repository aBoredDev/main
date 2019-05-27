# Riptide - Vance Joy

# Setup
use_synth :beep
use_bpm 102
use_debug true

# Melody
22.times do
  # Am - [:A3, :E3, :A4, :C4, :E4]
  print "Am"
  play_chord [:A3, :E3, :A4, :C4, :E4]
  sleep 1
  play_chord [:A3, :E3, :A4, :C4, :E4]
  sleep 1.5
  play_chord [:A3, :E3, :A4, :C4, :E4]
  sleep 0.5
  play_chord [:E4, :C4, :A4, :E3, :A3]
  sleep 0.5
  play_chord [:A3, :E3, :A4, :C4, :E4]
  sleep 0.5
  
  # G - [:G2, :B3, :D3, :G3, :D4, :G4]
  print "G"
  play_chord [:G2, :B3, :D3, :G3, :D4, :G4]
  sleep 1
  play_chord [:G2, :B3, :D3, :G3, :D4, :G4]
  sleep 1.5
  play_chord [:G2, :B3, :D3, :G3, :D4, :G4]
  sleep 0.5
  play_chord [:G4, :D4, :G3, :D3, :B3, :G2]
  sleep 0.5
  play_chord [:G2, :B3, :D3, :G3, :D4, :G4]
  sleep 0.5
  
  2.times do
    # C - [:C3, :E3, :G3, :C4, :E4]
    print "C"
    play_chord [:C3, :E3, :G3, :C4, :E4]
    sleep 1
    play_chord [:C3, :E3, :G3, :C4, :E4]
    sleep 1.5
    play_chord [:C3, :E3, :G3, :C4, :E4]
    sleep 0.5
    play_chord [:E4, :C4, :G3, :E3, :C3]
    sleep 0.5
    play_chord [:C3, :E3, :G3, :C4, :E4]
    sleep 0.5
  end
end

# Bridge loop
2.times do
  # Am - [:A3, :E3, :A4, :C4, :E4]
  2.times do
    print "Am"
    play_chord [:A3, :E3, :A4, :C4, :E4]
    sleep 1
    play_chord [:A3, :E3, :A4, :C4, :E4]
    sleep 1.5
    play_chord [:A3, :E3, :A4, :C4, :E4]
    sleep 0.5
    play_chord [:E4, :C4, :A4, :E3, :A3]
    sleep 0.5
    play_chord [:A3, :E3, :A4, :C4, :E4]
    sleep 0.5
  end
  
  # G - [:G2, :B3, :D3, :G3, :D4, :G4]
  2.times do
    print "G"
    play_chord [:G2, :B3, :D3, :G3, :D4, :G4]
    sleep 1
    play_chord [:G2, :B3, :D3, :G3, :D4, :G4]
    sleep 1.5
    play_chord [:G2, :B3, :D3, :G3, :D4, :G4]
    sleep 0.5
    play_chord [:G4, :D4, :G3, :D3, :B3, :G2]
    sleep 0.5
    play_chord [:G2, :B3, :D3, :G3, :D4, :G4]
    sleep 0.5
  end
  
  # C - [:C3, :E3, :G3, :C4, :E4]
  2.times do
    print "C"
    play_chord [:C3, :E3, :G3, :C4, :E4]
    sleep 1
    play_chord [:C3, :E3, :G3, :C4, :E4]
    sleep 1.5
    play_chord [:C3, :E3, :G3, :C4, :E4]
    sleep 0.5
    play_chord [:E4, :C4, :G3, :E3, :C3]
    sleep 0.5
    play_chord [:C3, :E3, :G3, :C4, :E4]
    sleep 0.5
  end
  
  # Fmaj7 - [:F3, :A4, :C4, :E4]
  2.times do
    print "Fmaj7"
    play_chord [:F3, :A4, :C4, :E4]
    sleep 1
    play_chord [:F3, :A4, :C4, :E4]
    sleep 1.5
    play_chord [:F3, :A4, :C4, :E4]
    sleep 0.5
    play_chord [:E4, :C4, :A4, :F3]
    sleep 0.5
    play_chord [:F3, :A4, :C4, :E4]
    sleep 0.5
  end
end

# Pre-Chorus
2.times do
  # Am - [:A3, :E3, :A4, :C4, :E4]
  print "Am"
  play_chord [:A3, :E3, :A4, :C4, :E4]
  sleep 4
  
  # G - [:G2, :B3, :D3, :G3, :D4, :G4]
  print "G"
  play_chord [:G2, :B3, :D3, :G3, :D4, :G4]
  sleep 4
  
  # C - [:C3, :E3, :G3, :C4, :E4]
  print "C"
  play_chord [:C3, :E3, :G3, :C4, :E4]
  sleep 8
end

# Chorus and outro
13.times do
  # Am - [:A3, :E3, :A4, :C4, :E4]
  print "Am"
  play_chord [:A3, :E3, :A4, :C4, :E4]
  sleep 1
  play_chord [:A3, :E3, :A4, :C4, :E4]
  sleep 1.5
  play_chord [:A3, :E3, :A4, :C4, :E4]
  sleep 0.5
  play_chord [:E4, :C4, :A4, :E3, :A3]
  sleep 0.5
  play_chord [:A3, :E3, :A4, :C4, :E4]
  sleep 0.5
  
  # G - [:G2, :B3, :D3, :G3, :D4, :G4]
  print "G"
  play_chord [:G2, :B3, :D3, :G3, :D4, :G4]
  sleep 1
  play_chord [:G2, :B3, :D3, :G3, :D4, :G4]
  sleep 1.5
  play_chord [:G2, :B3, :D3, :G3, :D4, :G4]
  sleep 0.5
  play_chord [:G4, :D4, :G3, :D3, :B3, :G2]
  sleep 0.5
  play_chord [:G2, :B3, :D3, :G3, :D4, :G4]
  sleep 0.5
  
  # C - [:C3, :E3, :G3, :C4, :E4]
  print "C"
  play_chord [:C3, :E3, :G3, :C4, :E4]
  sleep 1
  play_chord [:C3, :E3, :G3, :C4, :E4]
  sleep 1.5
  play_chord [:C3, :E3, :G3, :C4, :E4]
  sleep 0.5
  play_chord [:E4, :C4, :G3, :E3, :C3]
  sleep 0.5
  play_chord [:C3, :E3, :G3, :C4, :E4]
  sleep 0.5
end
