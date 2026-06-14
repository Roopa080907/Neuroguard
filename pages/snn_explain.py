import numpy as np
import matplotlib.pyplot as plt

def plot_spike_raster(spike_record):
    spike_record = np.array(spike_record)

    plt.figure()
    plt.imshow(spike_record.T, cmap="binary", aspect="auto")
    plt.title("Spike Raster Plot (Neuron Activity Over Time)")
    plt.xlabel("Time Steps")
    plt.ylabel("Neurons")
    return plt
