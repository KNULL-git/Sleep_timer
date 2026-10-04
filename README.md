# Sleep Timer

A tiny command-line tool for Windows that puts your PC to sleep after a
specified number of minutes. Perfect for falling asleep while watching
YouTube or an OTT service in bed.

## Features

- Pass the delay in minutes as an argument
- Live countdown updated every 10 seconds
- Cancel anytime with `Ctrl+C`
- No third-party dependencies (standard library only)

## Setup

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

## Usage

```powershell
python sleep_timer.py 45
```

Output:

```
Sleeping in 45m 0s. Press Ctrl+C to cancel.
Time left: 44m 50s
```

After the countdown finishes, the system sleeps automatically.
