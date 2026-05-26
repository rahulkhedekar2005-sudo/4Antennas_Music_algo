# Complete Project Workflow

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Generates antenna signals and runs MUSIC algorithm |
| GNU Radio | Visualizes RF signals |
| Radioconda / Anaconda Prompt | Runs Python scripts |

---

# STEP 1 — Create Project Folder

## Open Windows File Explorer

Go to:

```text
C:\Users\User\OneDrive\Desktop
```

Create a new folder:

```text
direction_finding
```

---

# STEP 2 — Create Python Files

Inside the `direction_finding` folder create these files:

```text
generate_iq.py
music_direction.py
```

---

# STEP 3 — Paste Code Into Files

## Create generate_iq.py

### Steps

1. Right click inside folder
2. Click:
   - New → Text Document
3. Rename file to:

```text
generate_iq.py
```

4. Open file
5. Paste signal generator code
6. Save file

---

## Create music_direction.py

Create second file:

```text
music_direction.py
```

Paste MUSIC algorithm code and save.

---

# STEP 4 — Open Radioconda / Anaconda Prompt

## Open From Start Menu

Search:

```text
radioconda prompt
```

OR

```text
anaconda prompt
```

Open it.

A black terminal window will appear.

---

# STEP 5 — Go To Project Folder

Inside terminal type:

```bash
cd OneDrive\Desktop\direction_finding
```

Press Enter.

Now terminal is inside the project folder.

---

# STEP 6 — Run Signal Generator

Run:

```bash
python generate_iq.py
```

---

# What This Script Does

The script will:

- Generate fake jammer signal
- Create 4 antenna signals
- Add phase differences
- Add Gaussian noise
- Save IQ data files

---

# Files Generated Automatically

After running, these files appear inside folder:

```text
antenna_1.iq
antenna_2.iq
antenna_3.iq
antenna_4.iq
all_antennas.npy
```

---

# STEP 7 — Open GNU Radio

## Open GNU Radio Companion

From Start Menu search:

```text
GNU Radio Companion
```

Open it.

---

# STEP 8 — Build GNU Radio Flowgraph

## Add These Blocks

Press:

```text
Ctrl + F
```

Add:

- File Source
- Throttle
- QT GUI Frequency Sink
- QT GUI Waterfall Sink
- QT GUI Time Sink

---

# STEP 9 — Configure File Source

Double click **File Source** block.

Set values:

| Field | Value |
|---|---|
| File | `C:\Users\User\OneDrive\Desktop\direction_finding\antenna_1.iq` |
| Type | Complex |
| Repeat | Yes |

Click OK.

---

# STEP 10 — Configure Throttle

| Field | Value |
|---|---|
| Type | Complex |
| Sample Rate | `samp_rate` |

---

# STEP 11 — Configure Frequency Sink

| Field | Value |
|---|---|
| Type | Complex |
| FFT Size | 1024 |
| Bandwidth | `samp_rate` |

---

# STEP 12 — Configure Waterfall Sink

| Field | Value |
|---|---|
| Type | Complex |
| FFT Size | 1024 |
| Bandwidth | `samp_rate` |

---

# STEP 13 — Configure Time Sink

| Field | Value |
|---|---|
| Type | Complex |
| Number of Points | 1024 |
| Sample Rate | `samp_rate` |

---

# STEP 14 — Connect Blocks

Connect blocks like this:

```text
File Source → Throttle → Frequency Sink
                         → Waterfall Sink
                         → Time Sink
```

---

# STEP 15 — Save GNU Radio Flowgraph

Press:

```text
Ctrl + S
```

Save file as:

```text
direction_finding.grc
```

inside project folder.

---

# STEP 16 — Run GNU Radio

Press:

```text
F6
```

---

# What You Will See

## Frequency Sink

You will see:

- A spike at 1 kHz

Meaning:

- Jammer signal detected in frequency domain

---

## Waterfall Sink

You will see:

- Continuous colored line

Meaning:

- Jammer is continuously transmitting

---

## Time Sink

You will see:

- IQ waveform

Meaning:

- Raw antenna signal

---

# STEP 17 — Run MUSIC Algorithm

## IMPORTANT

Keep GNU Radio running.

Open a SECOND terminal window.

Again open:

```text
Radioconda Prompt
```

---

# Go To Project Folder Again

Type:

```bash
cd OneDrive\Desktop\direction_finding
```

---

# Run MUSIC Processing

Run:

```bash
python music_direction.py
```

Press Enter.

---

# What This Script Does

The MUSIC algorithm will:

- Load all antenna signals
- Build covariance matrix
- Separate signal and noise
- Scan possible angles
- Detect jammer direction
- Open result graphs

---

# Final Output

Terminal shows:

```text
Detected Angle : 45.00 degrees
```

Meaning:

- Jammer direction is 45°

---

# Graph Window Opens

## Graph 1 — MUSIC Spectrum

A sharp peak appears at:

```text
45°
```

This peak represents jammer direction.

---

## Graph 2 — IQ Signal

Displays:

- I signal
- Q signal

for antenna 1.

---

# STEP 18 — Test Different Directions

Open:

```text
generate_iq.py
```

Find:

```python
jammer_angle = 45
```

Change to:

```python
jammer_angle = 30
```

Save file.

---

# Run Again

First run:

```bash
python generate_iq.py
```

Then run:

```bash
python music_direction.py
```

Now MUSIC spectrum peak shifts to:

```text
30°
```

Meaning:

- MUSIC algorithm correctly detected the new jammer direction.

---

# Final System Workflow

```text
Virtual Jammer Signal
          ↓
4 Virtual Antennas
          ↓
IQ Signal Generation
          ↓
GNU Radio Visualization
          ↓
MUSIC DOA Processing
          ↓
Direction Detection
```
