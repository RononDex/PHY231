Tracking detectors at particle physics experiments usually consist of several detector layers.
A certain experiment just mounted a new tracking detector. It consists of 6 layers, and each layer has a single-hit efficiency of 90% (i.e. the probability that a signal is recorded if a charged particle crosses that layer).
In order to correctly reconstruct a particle's track, physicists require that at least N layers are fired. Increasing N, the track reconstruction efficiency drops, but the quality of the tracks increases.

Interesting events usually feature several tracks. An example is the decay B -> K* mu mu, with the K* decaying to K pi, that has four charged tracks in the final state! To study this kind of events, you need to properly reconstruct all four tracks.

a) Calculate the track reconstruction efficiency for at least 6, 5 or 4 fired layers.
b) Calculate the probability that a B -> K* mu mu event is totally reconstructed, for all three cases above.

--------- suggestions and requests -------------

Develop a python function that calculates the reconstruction efficiency for one track, given:
- a minimum number of fired layers
- the total number of layers of the tracking detector
- the single-hit efficiency of each layer (assuming they are all equal)

Develop then a python function that calculates the event reconstruction efficiency, as a function of the needed number of reconstructed tracks. You can/should reuse the function for the single-track reconstruction efficiency...

