"""SleepTimer - put your Windows PC to sleep after N minutes.

Usage:
    python sleep_timer.py 45
"""

import argparse
import ctypes
import sys
import time


def sleep_system() -> None:
    """Put the Windows machine to sleep (standby)."""
    # SetSuspendState(bHibernate, bForce, bWakeupEventsDisabled)
    # bHibernate=False -> sleep, True -> hibernate
    result = ctypes.windll.powrprof.SetSuspendState(0, 0, 0)
    if result == 0:
        # Fallback in case SetSuspendState fails
        import subprocess

        subprocess.run(
            ["rundll32.exe", "powrprof.dll,SetSuspendState", "0,0,0"],
            check=False,
        )


def format_time(seconds: int) -> str:
    minutes, secs = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    if hours:
        return f"{hours}h {minutes}m {secs}s"
    return f"{minutes}m {secs}s"


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Put your PC to sleep after a given number of minutes."
    )
    parser.add_argument(
        "minutes",
        type=float,
        help="Time in minutes after which the PC will go to sleep.",
    )
    args = parser.parse_args()

    if args.minutes <= 0:
        print("Error: minutes must be a positive number.")
        sys.exit(1)

    total_seconds = int(args.minutes * 60)
    print(f"Sleeping in {format_time(total_seconds)}. Press Ctrl+C to cancel.")

    try:
        end = time.monotonic() + total_seconds
        while True:
            remaining = int(end - time.monotonic())
            if remaining <= 0:
                break
            print(
                f"\rTime left: {format_time(remaining)}   ",
                end="",
                flush=True,
            )
            time.sleep(min(10, remaining))
        print("\rPutting the system to sleep now...        ")
        sleep_system()
    except KeyboardInterrupt:
        print("\nSleep timer cancelled. Your PC will stay awake.")
        sys.exit(0)


if __name__ == "__main__":
    main()
