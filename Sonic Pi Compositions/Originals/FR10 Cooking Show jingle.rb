# FR10 Cooking show jingle
use_synth :piano

live_loop :ambi do
  sample :ambi_choir
  sleep 2
  sample :ambi_piano
  play :C3
end

sync "/live_loop/ambi"

with_synth :subpulse do
  live_loop :bass do
    sync "/live_loop/ambi"
    with_fx :lpf, cutoff: 70 do
      play :C3
      sleep 2
      play :D3
      sleep 1
      play :E3
      sleep 0.5
    end
  end
end
