#!/usr/bin/env python3
"""Build a print-ready 'Scan to book a demo' card (PDF + PNG) from the QR SVG."""
import base64, pathlib

HERE = pathlib.Path(__file__).parent
# Embed the already-decode-verified PNG as a data URI (pixel-identical to the
# standalone QR that scans), so the card QR can't be broken by SVG scaling.
_png = base64.b64encode((HERE / 'demo-request.png').read_bytes()).decode()
qr_img = f'<img src="data:image/png;base64,{_png}" alt="QR code to book a demo" style="width:100%;height:100%;display:block;image-rendering:pixelated">'

LOGO = '''<svg viewBox="0 0 120 118" aria-hidden="true">
  <path d="M40 70 L58 82 L80 70" fill="none" stroke="#16205a" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>
  <rect x="22" y="92" width="76" height="7" rx="3.5" fill="#16205a"/>
  <g fill="#343da0"><circle cx="33" cy="30" r="12"/><path d="M17 84 V56 C17 47 24 42 33 42 C42 42 49 47 49 56 V84 C49 86 47 88 45 88 H21 C19 88 17 86 17 84 Z"/></g>
  <g fill="#2f8f5b"><circle cx="60" cy="24" r="13.5"/><path d="M42 84 V52 C42 42 50 37 60 37 C70 37 78 42 78 52 V84 C78 86 76 88 74 88 H46 C44 88 42 86 42 84 Z"/></g>
  <g fill="#7b3aa0"><circle cx="87" cy="30" r="12"/><path d="M71 84 V56 C71 47 78 42 87 42 C96 42 103 47 103 56 V84 C103 86 101 88 99 88 H75 C73 88 71 86 71 84 Z"/></g>
</svg>'''

HTML = f'''<!doctype html><html><head><meta charset="utf-8"><style>
  @page {{ size: 4in 6in; margin: 0; }}
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  html,body {{ width:4in; height:6in; }}
  body {{ font-family:"Helvetica Neue",Arial,sans-serif; color:#0d1020; background:#fff;
         -webkit-print-color-adjust:exact; print-color-adjust:exact; }}
  .card {{ width:4in; height:6in; display:flex; flex-direction:column; position:relative; overflow:hidden; }}

  .band {{ background:#343da0; color:#fff; padding:0.26in 0.34in 0.24in; display:flex; align-items:center; gap:0.11in; }}
  .chip {{ width:0.46in; height:0.46in; background:#fff; border-radius:0.1in; padding:0.06in; flex:none;
           box-shadow:0 1px 3px rgba(0,0,0,.18); }}
  .chip svg {{ width:100%; height:100%; display:block; }}
  .wm {{ font-size:18pt; font-weight:700; letter-spacing:-0.01em; line-height:1; }}
  .wm .c2 {{ color:#b9c0f2; }}
  .wm sup {{ font-size:7.5pt; font-weight:500; letter-spacing:.06em; color:#aeb6ea; top:-0.9em; margin-left:1px; }}

  .body {{ flex:1; display:flex; flex-direction:column; align-items:center; justify-content:center;
           text-align:center; padding:0.16in 0.34in; }}
  h1 {{ font-size:23pt; font-weight:800; line-height:1.03; letter-spacing:-0.02em; color:#131a45; }}
  h1 .accent {{ color:#343da0; }}
  .sub {{ font-size:9.5pt; line-height:1.38; color:#565c6e; margin-top:0.1in; max-width:3in; }}

  .qrwrap {{ margin-top:0.16in; width:2.15in; height:2.15in; background:#fff; border:1.5px solid #e6e8ee;
             border-radius:0.14in; padding:0.12in; box-shadow:0 6px 22px -10px rgba(19,26,69,.28); }}
  .qrwrap svg {{ display:block; }}
  .scanline {{ margin-top:0.12in; font-size:9pt; font-weight:600; color:#343da0; letter-spacing:.02em;
               display:flex; align-items:center; gap:6px; }}
  .scanline svg {{ width:14px; height:14px; }}
  .url {{ margin-top:0.03in; font-family:"SF Mono",ui-monospace,Menlo,monospace; font-size:8.5pt; color:#8a90a0; }}

  .foot {{ background:#131a45; color:#c8cbe6; padding:0.15in 0.34in; display:flex; align-items:center;
           justify-content:space-between; font-size:7.4pt; letter-spacing:.01em; }}
  .dots {{ display:flex; gap:5px; }}
  .dots i {{ width:7px; height:7px; border-radius:50%; display:block; }}
</style></head><body>
  <div class="card">
    <div class="band">
      <div class="chip">{LOGO}</div>
      <div class="wm"><span class="c1">Unity</span><span class="c2">Core</span><sup>OS</sup></div>
    </div>
    <div class="body">
      <h1>Scan to<br>book a <span class="accent">demo</span></h1>
      <p class="sub">See UnityCoreOS run your real workflow &mdash; one platform connecting facilities, staffing agencies, and providers.</p>
      <div class="qrwrap">{qr_img}</div>
      <div class="scanline">
        <svg viewBox="0 0 24 24" fill="none" stroke="#343da0" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 7V5a2 2 0 0 1 2-2h2M17 3h2a2 2 0 0 1 2 2v2M21 17v2a2 2 0 0 1-2 2h-2M7 21H5a2 2 0 0 1-2-2v-2"/><path d="M7 12h10"/></svg>
        Point your phone camera here
      </div>
      <div class="url">unitycoreos.com</div>
    </div>
    <div class="foot">
      <span>The operating system for medical staffing.</span>
      <span class="dots"><i style="background:#8b93e6"></i><i style="background:#5cbd85"></i><i style="background:#b483d8"></i></span>
    </div>
  </div>
</body></html>'''

out = HERE / 'demo-card.html'
out.write_text(HTML)
print("wrote", out)
