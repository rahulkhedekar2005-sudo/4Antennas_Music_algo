import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# PARAMETERS — must match generate_iq.py
# ============================================================

num_antennas    = 4
antenna_spacing = 0.5
num_signals     = 1      # number of jammer signals

# ============================================================
# LOAD ALL 4 ANTENNA SIGNALS
# ============================================================

print("Loading antenna signals...")
antenna_signals = np.load("all_antennas.npy")
print(f"Loaded shape: {antenna_signals.shape}")
print(f"Antennas: {antenna_signals.shape[0]}")
print(f"Samples : {antenna_signals.shape[1]}")

# ============================================================
# BUILD COVARIANCE MATRIX
# ============================================================

num_samples = antenna_signals.shape[1]

# R = (1/N) * X * X^H
R = (1 / num_samples) * (antenna_signals @ antenna_signals.conj().T)
print("Covariance matrix built — shape:", R.shape)

# ============================================================
# EIGEN DECOMPOSITION
# ============================================================

eigenvalues, eigenvectors = np.linalg.eigh(R)

# Sort largest to smallest
idx          = np.argsort(eigenvalues)[::-1]
eigenvalues  = eigenvalues[idx]
eigenvectors = eigenvectors[:, idx]

# ============================================================
# NOISE SUBSPACE
# ============================================================

noise_subspace = eigenvectors[:, num_signals:]

# ============================================================
# MUSIC SPECTRUM SCAN
# ============================================================

scan_angles    = np.linspace(-90, 90, 1800)
music_spectrum = np.zeros(len(scan_angles))

print("Scanning angles...")

for i, angle in enumerate(scan_angles):
    scan_rad = np.deg2rad(angle)

    a = np.exp(
        1j * 2 * np.pi * antenna_spacing *
        np.sin(scan_rad) *
        np.arange(num_antennas)
    ).reshape(-1, 1)

    denom             = a.conj().T @ noise_subspace @ noise_subspace.conj().T @ a
    music_spectrum[i] = 1 / np.abs(denom.squeeze())

# ============================================================
# NORMALIZE AND FIND PEAK
# ============================================================

music_spectrum    = music_spectrum / np.max(music_spectrum)
music_spectrum_dB = 10 * np.log10(music_spectrum)
detected_angle    = scan_angles[np.argmax(music_spectrum)]

print("")
print("=" * 40)
print("JAMMER DIRECTION RESULT")
print("=" * 40)
print(f"Detected Angle : {detected_angle:.2f} degrees")
print("=" * 40)

# ============================================================
# PLOT 4 GRAPHS
# ============================================================

fig, axes = plt.subplots(1, 2, figsize=(14, 5))
fig.suptitle(
    f'MUSIC Algorithm — Jammer Direction Finding\n'
    f'4 Antenna Simulation | Detected Angle: {detected_angle:.1f}°',
    fontsize=13, fontweight='bold'
)

# Graph 1 — MUSIC Spectrum
axes[0].plot(scan_angles, music_spectrum_dB, color='blue', linewidth=2)
axes[0].axvline(x=detected_angle, color='green', linestyle='--',
                linewidth=2, label=f'Detected: {detected_angle:.1f}°')
axes[0].set_title('MUSIC Spectrum — Jammer Direction')
axes[0].set_xlabel('Angle (degrees)')
axes[0].set_ylabel('Power (dB)')
axes[0].legend()
axes[0].grid(True)
axes[0].set_xlim([-90, 90])

# Graph 2 — Antenna 1 IQ Signal
axes[1].plot(np.real(antenna_signals[0, :200]),
             color='orange', linewidth=1.5, label='I (Real)')
axes[1].plot(np.imag(antenna_signals[0, :200]),
             color='purple', linewidth=1.5, label='Q (Imag)', alpha=0.7)
axes[1].set_title('Antenna 1 — IQ Signal (first 200 samples)')
axes[1].set_xlabel('Sample')
axes[1].set_ylabel('Amplitude')
axes[1].legend()
axes[1].grid(True)

plt.tight_layout()
plt.savefig('music_result.png', dpi=150, bbox_inches='tight')
plt.show()
print("Graph saved as music_result.png")