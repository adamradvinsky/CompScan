#!/usr/bin/env python3

import json
import os
import platform
import re
import subprocess
from pathlib import Path


OUTPUT_FILE = Path(__file__).parent.parent / "hardware.json"


def get_cpu_info():
    cpu = {
        "architecture": platform.machine(),
        "model": "Unknown",
        "cores": os.cpu_count(),
    }

    # Linux exposes detailed CPU information here.
    cpuinfo = Path("/proc/cpuinfo")

    if cpuinfo.exists():
        text = cpuinfo.read_text()

        model_match = re.search(r"^model name\s*:\s*(.+)$", text, re.MULTILINE)

        if model_match:
            cpu["model"] = model_match.group(1).strip()

        physical_cores = re.findall(
            r"^cpu cores\s*:\s*(\d+)$",
            text,
            re.MULTILINE,
        )

        if physical_cores:
            cpu["physical_cores"] = int(physical_cores[0])

    return cpu


def get_system_info():
    return {
        "operating_system": platform.system(),
        "os_release": platform.release(),
        "kernel": platform.version(),
        "hostname": platform.node(),
    }


def main():
    hardware = {
        "system": get_system_info(),
        "cpu": get_cpu_info(),
        "benchmarks": {},
    }

    with OUTPUT_FILE.open("w", encoding="utf-8") as file:
        json.dump(hardware, file, indent=2)

    print(f"Hardware information written to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()