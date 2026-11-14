# System Design and Programming

**A car parking desktop application and command-line interface, developed during Jyothesh Karnam's MSc Computer Science at Keele University.** The project models seven parking spaces, vehicle entry and exit, ticket lookup, time-based fees and local CSV records.

| Academic context | Verified detail |
| --- | --- |
| Module | System Design & Programming (CSC-40044) |
| Programme / year | MSc Computer Science, Keele University, 2023/24 |
| Final module result | **99%** |
| Credit | 15 CATS |

The result is the **final module mark** on the official transcript issued 15 January 2025. It does not grade this repository's later maintenance. The `2024` repository suffix describes the academic year; documentation, tests and fixes added in November 2026 are identified separately. See [academic provenance](docs/ACADEMIC_PROVENANCE.md).

## Explore the work

| Material | What it demonstrates |
| --- | --- |
| [Maintained parking model and CLI](carpark.py) | Classes, linked parking-space nodes, availability, registration checks, tickets, fees and persistence |
| [Tkinter desktop interface](gui.py) | Event callbacks for entry, exit, availability and ticket queries |
| [Original assignment source](coursework/original/) | Three byte-preserved local coursework files, including the separate original CLI |
| [Architecture and decisions](docs/ARCHITECTURE.md) | Data contract, failure handling, tradeoffs and scaling boundaries |
| [Verification](docs/VERIFICATION.md) | Executed checks, regression coverage and remaining limitations |

The original university assessment brief was not located. The source archive is authentic recovered project material; it is not represented as a complete submission export or reconstructed official brief.

## Download and run

[Download the source ZIP](https://github.com/jyotheshkar/MSc-CS-System-Design-and-Programming-Keele-University-2024/archive/refs/heads/main.zip), extract it, and open a terminal in the extracted directory. Use **Python 3.11 or later**. The project uses the standard library. Tkinter is included with many Python installers; Linux distributions may provide it separately as `python3-tk`.

Create an isolated data directory so demonstrations use their own records:

```bash
python -c "from pathlib import Path; Path('demo-data').mkdir(exist_ok=True)"
python gui.py --data-file demo-data/parking.csv
```

For the command-line version:

```bash
python carpark.py --data-file demo-data/parking.csv
```

Both interfaces use the same six-column CSV format. The first successful vehicle entry creates a missing file. Its parent directory must already exist and be writable. Launch **one interface at a time per file**. Without `--data-file`, both interfaces use the historical `parkingRecords.csv` beside `carpark.py`. `cmd.py` is an empty historical placeholder; it is not a launcher.

Try entering `LA07EDC`, copy the generated ticket, query it, exit using the registration and check that the space is available again. Fees are GBP 2 per elapsed hour, prorated and rounded to two decimals. No payment is collected. The registration check recognises a modern UK example format; it does not query a vehicle registry.

This is a desktop application run from source. No packaged executable or installer is currently published.

## Verify

```bash
python -m unittest discover -s tests -v
```

Nine regressions exercise full capacity, released spaces, a single free space, empty CSV input, atomic-write failure, fee boundaries, schema/BOM handling and a real CLI entry saved to an explicit temporary data file. Tests use temporary directories and synthetic records.

## Engineering scope

The design demonstrates object-oriented modelling, a linked list, set-based occupancy, event-driven GUI callbacks, file I/O and behavioural testing. CSV writes replace a flushed temporary file so a failed replacement does not truncate the existing file. The November 2026 update also rejects an incorrect CSV header rather than silently discarding a data row and provides explicit data-file selection.

It remains a single-process learning application: tickets are random rather than database-enforced unique, UI orchestration is partly duplicated, and CSV provides no concurrency control. Timestamp and registration content beyond the documented schema is trusted local data. See [architecture](docs/ARCHITECTURE.md) for a specific path to transactional storage and [verification](docs/VERIFICATION.md) for the checks actually performed.

## Academic use

Review this work to understand the design and its limitations. Original recovered coursework is kept separate from later AI-assisted maintenance. Keele's [2023/24 Computer Science programme specification, module table on page 4](https://www.keele.ac.uk/media/keeleuniversity/sas/qa/pgtprogrammespecifications/pgtprogspecs2023-24/Programme-Specification-Computer-Science-Taught-Masters-2023-24.pdf) independently identifies this module and its credits. University material retains its authorship; the private transcript is not included.
