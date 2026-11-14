# Verification - 14 November 2026

Base revision: `3a7f5572e21d92541be6ded72935807d2af7fb82`. Environment: Windows, Python 3.11.15. All test data is synthetic and uses temporary directories.

| Check | Result |
| --- | --- |
| Baseline `python -m unittest discover -s tests -v` | 6 tests passed |
| After maintenance, same command | **9 tests passed** |
| Source and test compilation | Passed; original source is checked for syntax only, not runtime correctness |
| Evidence hashes and local documentation links | Checked against the final working tree |

The three new tests reject the wrong header without changing bytes, accept a UTF-8 BOM with the expected schema, and drive the real CLI through entry and quit using `--data-file`. Existing checks cover historical slot release, full capacity, one remaining slot, empty files, atomic replacement failure and negative-duration/90-minute fees.

The recovered originals are copied byte-for-byte and are intentionally not patched. The transcript module row was visually read; the full transcript is excluded. No official assessment brief was located. No interactive GUI acceptance session or packaged desktop build was performed; no production scale, durability across every crash scenario or multi-user support is asserted.

To reproduce:

```bash
python -m unittest discover -s tests -v
python -m compileall -q carpark.py gui.py coursework tests
```
