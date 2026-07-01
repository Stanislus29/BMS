import argparse

SUFFIXES = {"k": 1e3, "m": 1e6, "g": 1e9, "u": 1e-6, "n": 1e-9}

def parse_value(s):
    s = s.strip()
    suffix = s[-1].lower()
    if suffix in SUFFIXES:
        return float(s[:-1]) * SUFFIXES[suffix]
    return float(s)

parser = argparse.ArgumentParser(description="Resistor voltage divider calculator")
parser.add_argument("--vin", type=parse_value, help="Input voltage")
parser.add_argument("--vout", type=parse_value, help="Output voltage")
parser.add_argument("--r1", type=parse_value, help="R1 in ohms (supports k/M suffix)")
parser.add_argument("--r2", type=parse_value, help="R2 in ohms (supports k/M suffix)")
args = parser.parse_args()

vin, vout, r1, r2 = args.vin, args.vout, args.r1, args.r2

if vout is None:
    vout = vin * r2 / (r1 + r2)
    print(f"Vout = {vout:.4f} V")
elif r2 is None:
    r2 = r1 * vout / (vin - vout)
    print(f"R2 = {r2:.4f} ohms")
elif r1 is None:
    r1 = r2 * (vin - vout) / vout
    print(f"R1 = {r1:.4f} ohms")
elif vin is None:
    vin = vout * (r1 + r2) / r2
    print(f"Vin = {vin:.4f} V")