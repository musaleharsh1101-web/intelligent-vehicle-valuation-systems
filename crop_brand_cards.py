"""Create local brand-card assets from the supplied 32-brand reference board."""

from pathlib import Path
import sys

from PIL import Image


if len(sys.argv) != 2:
    raise SystemExit("Usage: python tools/crop_brand_cards.py <reference-image>")

source_path = Path(sys.argv[1])
output_directory = Path(__file__).resolve().parents[1] / "assets" / "brand-cards"
output_directory.mkdir(parents=True, exist_ok=True)

source_image = Image.open(source_path).convert("RGB")
if source_image.size == (1402, 1122):
    source_image = source_image.crop((1, 1, 1401, 1121))
elif source_image.size != (1400, 1120):
    raise ValueError(f"Expected a 1400x1120 reference image, got {source_image.size}.")

row_tops = [70, 332, 597, 883]
row_bottoms = [328, 593, 879, 1117]
for row_index, (top, bottom) in enumerate(zip(row_tops, row_bottoms)):
    for column_index in range(8):
        left = column_index * 175 + 3
        right = (column_index + 1) * 175 - 3
        brand_number = row_index * 8 + column_index + 1
        card = source_image.crop((left, top, right, bottom))
        card.save(output_directory / f"brand-{brand_number:02d}.jpg", quality=92, optimize=True)
