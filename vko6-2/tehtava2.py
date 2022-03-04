import argparse
parser = argparse.ArgumentParser()
parser.add_argument("Rivimäärä", type=int, help="Tulostettavien rivien määrä")
args = parser.parse_args()