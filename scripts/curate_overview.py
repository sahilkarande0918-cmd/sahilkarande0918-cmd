#!/usr/bin/env python3
"""Reflow live overview cards without changing their dynamic values."""
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

NS_URI = "http://www.w3.org/2000/svg"
NS = {"s": NS_URI}
ET.register_namespace("", NS_URI)
REMOVE = {"Pull requests merged", "Issues opened"}
POSITIONS = [(24.5,60.5),(295,60.5),(565.5,60.5),
             (24.5,166.5),(295,166.5),(565.5,166.5)]

def label(card):
    labels = ["".join(e.itertext()).strip() for e in card.findall(".//s:text", NS)
              if e.get("class") == "t-label"]
    if len(labels) != 1:
        raise ValueError(f"Unexpected labels: {labels}")
    return labels[0]

src = Path(sys.argv[1])
tree = ET.parse(src)
root = tree.getroot()
group = next((g for g in root.findall(".//s:g",NS) if g.get("class")=="fade"),None)
if group is None:
    raise ValueError("Source chart does not contain card group")
cards = list(group)
if len(cards) != 8 or not REMOVE.issubset({label(c) for c in cards}):
    raise ValueError("Unexpected source dashboard structure")
keep = [c for c in cards if label(c) not in REMOVE]
assert len(keep) == 6
for c in cards:
    group.remove(c)
for (nx,ny),card in zip(POSITIONS,keep):
    rect = card.find("s:rect",NS)
    if rect is None:
        raise ValueError(f"Missing rectangle for {label(card)}")
    dx,dy = nx-float(rect.attrib["x"]),ny-float(rect.attrib["y"])
    card.set("transform",f"translate({dx:g} {dy:g})")
    rect.set("width","256.5")
    group.append(card)
out = ET.tostring(root,encoding="unicode")
assert all(f">{v}<" not in out for v in REMOVE)
src.write_text(out+"\n",encoding="utf-8")
print("Six live overview cards generated: " + ", ".join(map(label,keep)))
