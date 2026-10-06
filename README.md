# CompScan

A bootable USB hardware tester. Plug it into a computer, boot from it, and CompScan stress-tests the CPU, GPU, RAM, and storage so you can tell if a secondhand machine is actually in good shape before you pay for it.

## Inspiration

I've bought used electronics before, and it's always a gamble. A laptop can look perfect in the listing photos, seem fine for the ten minutes you test it in person, and then turn out to have a dying drive or a CPU that overheats as soon as you do anything real.

Most people can't tell the difference between "works" and "works well." I wanted something you could carry in your pocket, plug in during a meetup with a seller, and get an honest answer from, even if you're not a hardware person.

## What it does

- Boots from a USB drive straight into a lightweight Linux environment, so it doesn't matter what's installed on the machine (or whether it even has an OS)
- Runs tests on the CPU, GPU, RAM, and storage
- Stress-tests the hardware over a sustained period to see if performance drops as things heat up, which can point to worn-out parts
- Looks up the manufacturer's advertised specs and compares them to what the machine actually measured
- Flags any component that's running below spec

## How I built it

- **Linux environment:** I built a minimal Linux image that boots from USB and launches the tests automatically. I kept it small so it boots fast and works on a wide range of machines.
- **Stress tests:** The core tests are custom C++ programs I wrote to push the CPU, RAM, and storage hard. I also combined them with existing benchmarking tools so the results are more trustworthy than just my own code.
- **Spec checking:** I wrote a Python scraper that collects the manufacturer's advertised specs for a given part. CompScan then compares those numbers against the measured performance and flags anything that falls short.

## Challenges I ran into

Getting the thing to boot on different machines was harder than I expected. Something that worked on my laptop wouldn't boot on another one because of different firmware settings and drivers, so I spent a lot of time just testing across hardware.

Another challenge was figuring out what counts as a bad result. A chip running a bit under its advertised speed isn't always a problem, since thermals and power limits are a normal thing. I had to learn how to tell normal variation from a part that's actually wearing out.

The scraper was also annoying, since manufacturer sites are all formatted differently and tend to break whenever they change a page.

## Accomplishments that I'm proud of

I'm proud that it works on real hardware and not just in a virtual machine. Watching it catch a performance drop under sustained load, the kind of thing you'd never notice in a quick check, felt really good. I'm also happy that I built something that solves a problem I actually had.

## What I learned

- How a computer boots, and what it takes to make a custom Linux image start on its own
- Writing low-level C++ that really stresses hardware
- How benchmarking works, and why a single number never tells the whole story
- Scraping messy real-world data and making it usable

## What's next for CompScan

- Add battery health and display checks, since those matter a lot for used laptops
- Generate a simple report at the end that anyone can read at a glance
- Support more hardware and make the spec lookup more reliable
- Add a pass/fail summary for people who don't want to read the numbers
