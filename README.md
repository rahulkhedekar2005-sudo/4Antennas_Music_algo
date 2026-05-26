Project uses:

Python → generates signals + MUSIC algorithm
GNU Radio → visualizes signal
Anaconda / Radioconda Prompt → runs Python files
STEP 1 — Create Project Folder
Where?

In Windows File Explorer.

Go to:

C:\Users\User\OneDrive\Desktop

Create folder:

direction_finding
STEP 2 — Create Python Files

Inside direction_finding folder create:

generate_iq.py
music_direction.py
STEP 3 — Paste Code
Open Notepad
For generate_iq.py
right click
New → Text Document
rename to:
generate_iq.py

Paste generator code.

Save.

For music_direction.py

Create second file:

music_direction.py

Paste MUSIC algorithm code.

Save.

STEP 4 — Open Radioconda / Anaconda Prompt
Where To Run Python?

Open:

Start Menu
Search:
radioconda prompt

OR

anaconda prompt

Open it.

Black terminal window appears.

STEP 5 — Go To Project Folder

Inside terminal type:

cd OneDrive\Desktop\direction_finding

Press Enter.

Now terminal is inside your project folder.

STEP 6 — Run Signal Generator

In same terminal type:

python generate_iq.py

Press Enter.

What Happens Here?

Python will:

create fake jammer
create 4 antenna signals
add phase difference
add noise
save IQ files
Files Created Automatically

Inside folder you will now get:

antenna_1.iq
antenna_2.iq
antenna_3.iq
antenna_4.iq
all_antennas.npy
STEP 7 — Open GNU Radio
Where?

Open:

Start Menu
Search:
GNU Radio Companion

Open it.

STEP 8 — Build GNU Radio Flowgraph
Add These Blocks

Press Ctrl+F and add:

File Source
Throttle
QT GUI Frequency Sink
QT GUI Waterfall Sink
QT GUI Time Sink
STEP 9 — Configure File Source

Double click File Source.

Set:

Field	Value
File	C:\Users\User\OneDrive\Desktop\direction_finding\antenna_1.iq
Type	Complex
Repeat	Yes

Click OK.

STEP 10 — Configure Throttle

Set:

Field	Value
Type	Complex
Sample Rate	samp_rate
STEP 11 — Configure Frequency Sink

Set:

Field	Value
Type	Complex
FFT Size	1024
Bandwidth	samp_rate
STEP 12 — Configure Waterfall Sink

Set:

Field	Value
Type	Complex
FFT Size	1024
Bandwidth	samp_rate
STEP 13 — Configure Time Sink

Set:

Field	Value
Type	Complex
Number of Points	1024
Sample Rate	samp_rate
STEP 14 — Connect Blocks

Connect like this:

File Source → Throttle → Frequency Sink
                         → Waterfall Sink
                         → Time Sink
STEP 15 — Save GNU Radio File

Press:

Ctrl + S

Save as:

direction_finding.grc

inside project folder.

STEP 16 — Run GNU Radio

Press:

F6
What You Will See
Frequency Sink

You see:

peak/spike at 1 kHz

Meaning:

jammer detected in frequency domain
Waterfall Sink

You see:

continuous colored line

Meaning:

jammer continuously transmitting
Time Sink

You see:

IQ waveform

Meaning:

raw antenna signal
STEP 17 — Run MUSIC Algorithm
IMPORTANT

Keep GNU Radio running.

Open SECOND terminal window.

Again open:

Radioconda Prompt
Go To Folder Again

Type:

cd OneDrive\Desktop\direction_finding
Run MUSIC File

Type:

python music_direction.py

Press Enter.

What Happens Now?

Python will:

load all antenna signals
build covariance matrix
separate noise and signal
scan angles
detect jammer direction
open graphs
Final Output

Terminal shows:

Detected Angle : 45.00 degrees

Meaning:

jammer came from 45°
Graph Window Opens

You see:

Graph 1 — MUSIC Spectrum

Sharp peak at:

45°

That peak = jammer direction.

Graph 2 — IQ Signal

Shows:

I signal
Q signal

of antenna 1.

STEP 18 — Test Other Directions

Open:

generate_iq.py

Find:

jammer_angle = 45

Change to:

jammer_angle = 30

Save file.

Run Again

FIRST:

python generate_iq.py

THEN:

python music_direction.py

Now peak shifts to:

30°

Meaning MUSIC correctly found new direction.
