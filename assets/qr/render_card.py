#!/usr/bin/env python3
"""Render demo-card.html to a 4x6in print PDF + a 300dpi PNG preview."""
import pathlib
from playwright.sync_api import sync_playwright

HERE = pathlib.Path(__file__).parent
url = (HERE / 'demo-card.html').resolve().as_uri()

with sync_playwright() as p:
    b = p.chromium.launch(channel="chrome")
    # PNG preview: card is 4x6in = 384x576 CSS px; DSF 3.125 -> 1200x1800 (300dpi)
    pg = b.new_page(viewport={'width': 384, 'height': 576}, device_scale_factor=3.125)
    pg.goto(url)
    pg.wait_for_timeout(300)
    pg.screenshot(path=str(HERE / 'demo-card.png'))
    # Print PDF at exact trim size
    pg.pdf(path=str(HERE / 'demo-card.pdf'), width='4in', height='6in',
           print_background=True, margin={'top': '0', 'right': '0', 'bottom': '0', 'left': '0'})
    b.close()
print("wrote demo-card.pdf + demo-card.png")
