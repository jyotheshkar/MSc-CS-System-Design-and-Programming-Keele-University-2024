# Recovered coursework source

`carpark.py`, `cmdui.py` and `gui.py` are byte-for-byte copies of the local **system design assignment** folder recovered on 14 November 2026. SHA-256 values are recorded in [the evidence manifest](../../docs/MODULE_EVIDENCE.json). Their contents were inspected for embedded credentials and student identifiers before inclusion. File-system modification dates are not used as evidence of submission time.

These files preserve the earlier classes, separate CLI and Tkinter interface. They are historical evidence, not the supported launch path. In particular, running this version of `carpark.py` directly calls a missing `mainMenu` method; `cmdui.py` supplied the original menu. The earlier allocator also counts historical records as occupied and can fail when no space remains. Those behaviours are preserved here rather than silently rewritten.

Use the root-level [maintained CLI](../../carpark.py) or [desktop interface](../../gui.py) for demonstrations. No assessment brief or complete submitted archive was located for this module, so this folder does not claim to be one. No CSV containing vehicle records was added to this snapshot.
