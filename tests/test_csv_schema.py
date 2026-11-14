import csv
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from carpark import CarParkingSystem


class ParkingCSVSchemaTests(unittest.TestCase):
    def test_wrong_header_rejected_without_modifying_file(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "records.csv"
            path.write_text("registration,ticket,space,entry,exit,fee\nLA07EDC,T1,1,2026-11-14,Parking...,Parking...\n", encoding="utf-8")
            before = path.read_bytes()
            with self.assertRaisesRegex(ValueError, "header"):
                CarParkingSystem(path)
            self.assertEqual(path.read_bytes(), before)

    def test_utf8_bom_and_original_header_accepted(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "records.csv"
            expected = CarParkingSystem(path).csv_titles
            with path.open("w", encoding="utf-8-sig", newline="") as stream:
                csv.writer(stream).writerow(expected)
            self.assertEqual(CarParkingSystem(path).car_parking_records, [])

    def test_cli_uses_explicit_data_file_and_persists_entry(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "demo.csv"
            result = subprocess.run(
                [sys.executable, str(Path(__file__).resolve().parents[1] / "carpark.py"), "--data-file", str(path)],
                input="1\nLA07EDC\n5\n", text=True, capture_output=True, check=True,
            )
            records = CarParkingSystem(path).car_parking_records
            self.assertIn("Vehicle entered", result.stdout)
            self.assertEqual(len(records), 1)
            self.assertEqual(records[0][0], "LA07EDC")
            self.assertEqual(records[0][4], "Parking...")


if __name__ == "__main__":
    unittest.main()
