import numpy as np

# ============================================================
# PARAMETERS — change these to simulate different scenarios
# ============================================================

num_antennas    = 4       # number of antennas
num_samples     = 131072  # number of IQ samples (must be power of 2)
sample_rate     = 32000   # must match GNU Radio samp_rate
jammer_angle    = 77     # true jammer direction in degrees
jammer_freq     = 1000    # jammer frequency in Hz
antenna_spacing = 0.5     # half wavelength spacing
SNR_dB          = 20      # signal to noise ratio

# ============================================================
# GENERATE JAMMER SIGNAL
# ============================================================

t = np.arange(num_samples) / sample_rate

# Jammer as complex sine wave
jammer_signal = np.exp(1j * 2 * np.pi * jammer_freq * t)

# ============================================================
# CREATE STEERING VECTOR (phase shift per antenna)
# ============================================================

angle_rad = np.deg2rad(jammer_angle)

steering_vector = np.exp(
    1j * 2 * np.pi * antenna_spacing *
    np.sin(angle_rad) *
    np.arange(num_antennas)
)

# ============================================================
# CREATE 4 ANTENNA SIGNALS WITH NOISE
# ============================================================

SNR_linear  = 10 ** (SNR_dB / 10)
noise_power = 1 / SNR_linear

antenna_signals = []

for i in range(num_antennas):
    # Each antenna gets jammer signal with its phase shift
    signal = steering_vector[i] * jammer_signal

    # Add complex Gaussian noise
    noise = (np.random.randn(num_samples) +
             1j * np.random.randn(num_samples)) * np.sqrt(noise_power / 2)

    antenna_signals.append(signal + noise)

# ============================================================
# SAVE EACH ANTENNA SIGNAL AS SEPARATE .iq FILE
# ============================================================

for i in range(num_antennas):
    # GNU Radio reads float32 interleaved IQ format
    iq_data = antenna_signals[i].astype(np.complex64)

    filename = f"antenna_{i+1}.iq"
    iq_data.tofile(filename)
    print(f"Saved: {filename} — {num_samples} samples")

# Save all 4 antenna signals together for MUSIC processing
np.save("all_antennas.npy", np.array(antenna_signals))
print("Saved: all_antennas.npy — all 4 antenna signals for MUSIC")

print("")
print("=" * 40)
print(f"True jammer angle : {jammer_angle} degrees")
print(f"Sample rate       : {sample_rate} Hz")
print(f"Jammer frequency  : {jammer_freq} Hz")
print(f"Samples generated : {num_samples}")
print("=" * 40)
print("Now open GNU Radio and load antenna_1.iq")