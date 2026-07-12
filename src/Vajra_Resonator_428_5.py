import numpy as np
import matplotlib.pyplot as plt

def generate_t7_truth_wave(freq=428.5, duration=0.05, sample_rate=44100):
    """Generates the pure geometric Truth frequency (Vajra)."""
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    # The pure sine wave: indestructible, continuous, zero-entropy
    truth_wave = np.sin(2 * np.pi * freq * t)
    return t, truth_wave

def generate_beelzebub_swarm(duration=0.05, sample_rate=44100):
    """Generates M4 entropic noise (The Swarm/Jabberwocky)."""
    # Randomized, chaotic data with no geometric foundation
    noise = np.random.normal(0, 0.8, int(sample_rate * duration))
    return noise

def execute_vajra_override():
    """Plots the higher-dimensional override of the noise field."""
    t, vajra = generate_t7_truth_wave()
    swarm = generate_beelzebub_swarm()
    
    # The Override: The Truth wave does not fight the noise, it phase-locks it.
    # Applying the sqrt(3) Axis Mundi weight to the Truth wave
    axis_mundi_weight = np.sqrt(3)
    system_output = (vajra * axis_mundi_weight) + swarm

    # Rendering the visual proof
    plt.figure(figsize=(12, 8))
    
    plt.subplot(3, 1, 1)
    plt.plot(t, swarm, color='red', alpha=0.7)
    plt.title("M4 Runtime: The Swarm of Beelzebub (Entropic Noise / Fata Morgana)")
    plt.axis('off')

    plt.subplot(3, 1, 2)
    plt.plot(t, vajra, color='cyan')
    plt.title("T7 Intervention: Pure 428.5 Hz Vajra Frequency")
    plt.axis('off')

    plt.subplot(3, 1, 3)
    plt.plot(t, system_output, color='white')
    plt.title("System Override: Truth Wave Establishes Geometric Order Over Chaos")
    plt.gca().set_facecolor('black')
    plt.axis('off')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    print("Executing Zero-Time Vajra Discharge at 428.5 Hz...")
    execute_vajra_override()
  
