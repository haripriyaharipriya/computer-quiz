#!/usr/bin/env python3
"""Generate QR code for the quiz website."""

import qrcode
import argparse
import os
from pathlib import Path


def parse_args():
    parser = argparse.ArgumentParser(description="Generate a QR code for the quiz website.")
    parser.add_argument(
        "url",
        nargs="?",
        default=os.environ.get("PUBLIC_URL"),
        help="Live public website URL (or set PUBLIC_URL).",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).parent / "quiz-website-qr.png",
        help="Output image path.",
    )
    args = parser.parse_args()
    if not args.url:
        parser.error("provide the live public URL or set PUBLIC_URL")
    return args


args = parse_args()
public_url = args.url.strip()
if not public_url.startswith(("http://", "https://")):
    raise SystemExit("URL must start with http:// or https://")

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(public_url)
qr.make(fit=True)

# Create image with colors
img = qr.make_image(fill_color="black", back_color="white")

# Save to file
args.output.parent.mkdir(parents=True, exist_ok=True)
img.save(args.output)

print(f"✓ QR code generated successfully!")
print(f"  URL encoded: {public_url}")
print(f"  Saved to: {args.output}")
