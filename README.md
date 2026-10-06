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

### Sample output

This is the report format CompScan is built to produce. The spec lines come from published specs; the measured values are placeholders from a design mockup, not real scan results.

```text
+==============================================================================+
|                                                                              |
|               C O M P S C A N   -   Hardware Diagnostic Report               |
|       v0.1.0  |  Stress profile: SUSTAINED (10 min)  |  SAMPLE OUTPUT        |
|                                                                              |
+==============================================================================+
|  DEVICE     NVIDIA GeForce GTX 1660 SUPER  (TU116, 6 GB GDDR6, 192-bit)      |
|  DRIVER     535.154.05      PCIe Gen3 x16      Board power limit: 125 W      |
|  SPECS      1408 CUDA cores | boost 1785 MHz | 336 GB/s | 125 W TGP          |
|  BASELINE   Healthy-card reference profile for this SKU                      |
+==============================================================================+
|                         GPU  -  EXPECTED vs MEASURED                         |
+==============================================================================+
|                                                                              |
|  GPU TEMPERATURE                                                   [ WARN ]  |
|    expected  ###################-------  72 C                                |
|    measured  ######################----  84 C       +12 C  (+16.7%)          |
|                                                                              |
|  VRAM TEMPERATURE                                                  [ N/A  ]  |
|    sensor not exposed by this GPU/driver (common on GeForce cards)           |
|                                                                              |
|  POWER DRAW                                                        [ WARN ]  |
|    expected  #########################-  120 W                               |
|    measured  ####################------  96 W       -24 W  (-20.0%)          |
|                                                                              |
|  GPU UTILIZATION                                                   [  OK  ]  |
|    expected  ##########################  99 %                                |
|    measured  #########################-  97 %       -2 %  (-2.0%)            |
|                                                                              |
|  MEMORY CONTROLLER UTILIZATION                                     [  OK  ]  |
|    expected  ################----------  62 %                                |
|    measured  ################----------  61 %       -1 %  (-1.6%)            |
|                                                                              |
|  VRAM USAGE                                                        [  OK  ]  |
|    expected  #######################---  5.2 GB                              |
|    measured  ######################----  5.1 GB     -0.1 GB  (-1.9%)         |
|                                                                              |
|  FAN SPEED                                                         [ WARN ]  |
|    expected  ##############------------  55 %                                |
|    measured  #######################---  88 %       +33 %  (+60.0%)          |
|                                                                              |
|  CORE CLOCK                                                        [ WARN ]  |
|    expected  #######################---  1785 MHz                            |
|    measured  #####################-----  1590 MHz   -195 MHz  (-10.9%)       |
|                                                                              |
|  PERFORMANCE STATE                                                 [ WARN ]  |
|    expected  P0  (full performance, held for the whole run)                  |
|    measured  P0 -> P2 at 4m12s                                               |
|              throttle reason: SW thermal slowdown                            |
|                                                                              |
+==============================================================================+
|                          GPU TEMPERATURE OVER TIME                           |
+==============================================================================+
|                                                                              |
|  Temperature (C) during sustained load                                       |
|                                                                              |
|     90 |                                                                     |
|     85 |                       * * * * * * * * * *                           |
|     80 |               * * * *                                               |
|     75 |           * *                                                       |
|     70 |       * * . . . . . . . . . . . . . . . .                           |
|     65 |     * .                                                             |
|     60 |     .                                                               |
|     55 |   *                                                                 |
|     50 |   .                                                                 |
|     45 |                                                                     |
|     40 | *                                                                   |
|        +-------------------------------------------                          |
|          0   1   2   3   4   5   6   7   8   9   10  min                     |
|          * measured    . expected for a healthy card                         |
|                                                                              |
+==============================================================================+
|  VERDICT   CAUTION   (4 warnings, 0 failures)                                |
+==============================================================================+


+==============================================================================+
|                                                                              |
|               C O M P S C A N   -   Hardware Diagnostic Report               |
|       v0.1.0  |  Stress profile: SUSTAINED (10 min)  |  SAMPLE OUTPUT        |
|                                                                              |
+==============================================================================+
|  DEVICE     Intel Xeon E5-1650 v4  (Broadwell-EP, 6C/12T, 15 MB L3)          |
|  PART NO.   BX80660E51650V4      Base 3.6 GHz / Turbo 4.0 GHz    TDP 140 W   |
|  MEMORY     4 x DDR4-2400 channels (76.8 GB/s theoretical)                   |
|  SPECS      Max case temp 69 C | all-core turbo 3.8 GHz | 140 W TDP          |
|  BASELINE   Healthy-chip reference profile for this SKU                      |
+==============================================================================+
|                         CPU  -  EXPECTED vs MEASURED                         |
+==============================================================================+
|                                                                              |
|  PACKAGE TEMPERATURE                                               [ WARN ]  |
|    expected  ##################--------  68 C                                |
|    measured  #####################-----  81 C       +13 C  (+19.1%)          |
|                                                                              |
|  ALL-CORE CLOCK                                                    [ WARN ]  |
|    expected  #########################-  3.8 GHz                             |
|    measured  ######################----  3.4 GHz    -0.4 GHz  (-10.5%)       |
|                                                                              |
|  PACKAGE POWER DRAW                                                [ WARN ]  |
|    expected  #########################-  135 W                               |
|    measured  #####################-----  112 W      -23 W  (-17.0%)          |
|                                                                              |
|  CPU UTILIZATION                                                   [  OK  ]  |
|    expected  ##########################  100 %                               |
|    measured  ##########################  100 %      +0 %  (+0.0%)            |
|                                                                              |
|  MEMORY BANDWIDTH                                                  [ FAIL ]  |
|    expected  ####################------  58 GB/s                             |
|    measured  ##############------------  41 GB/s    -17 GB/s  (-29.3%)       |
|                                                                              |
|  TURBO RESIDENCY                                                   [ WARN ]  |
|    expected  #########################-  95 %                                |
|    measured  ##################--------  71 %       -24 %  (-25.3%)          |
|                                                                              |
|  THERMAL THROTTLE EVENTS                                           [ WARN ]  |
|    expected  0                                                               |
|    measured  14 events (first at 3m40s)                                      |
|                                                                              |
|  PER-CORE TEMPERATURE (end of run)                                 [ WARN ]  |
|    core 0    ####################------  78 C                                |
|    core 1    #####################-----  79 C                                |
|    core 2    ####################------  77 C                                |
|    core 3    #######################---  88 C                                |
|    core 4    #####################-----  79 C                                |
|    core 5    ####################------  78 C                                |
|                                                                              |
+==============================================================================+
|                        PACKAGE TEMPERATURE OVER TIME                         |
+==============================================================================+
|                                                                              |
|  Temperature (C) during sustained load                                       |
|                                                                              |
|     85 |                                                                     |
|     80 |                 * * * * * * * * * * * * *                           |
|     75 |           * * *                                                     |
|     70 |         *   . . . . . . . . . . . . . . .                           |
|     65 |       * . .                                                         |
|     60 |     *                                                               |
|     55 |                                                                     |
|     50 |   *                                                                 |
|     45 |                                                                     |
|     40 | *                                                                   |
|     35 |                                                                     |
|        +-------------------------------------------                          |
|          0   1   2   3   4   5   6   7   8   9   10  min                     |
|          * measured    . expected for a healthy chip                         |
|                                                                              |
+==============================================================================+
|  VERDICT   FAIL   (1 failure, 5 warnings)                                    |   
+==============================================================================+
```

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
