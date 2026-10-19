import os
import sys

W, H = 3840, 2160
CX, CY = W / 2, H / 2 - 90
LOGO = 620        # altura do logo em px (path original é 24x24)

out = os.path.expanduser(sys.argv[1])

# Logo do Arch (Simple Icons, sem o "TM")
ARCH = ("M11.39.605C10.376 3.092 9.764 4.72 8.635 7.132c.693.734 1.543 1.589 2.923 2.554"
        "-1.484-.61-2.496-1.224-3.252-1.86C6.86 10.842 4.596 15.138 0 23.395c3.612-2.085 "
        "6.412-3.37 9.021-3.862a6.61 6.61 0 01-.171-1.547l.003-.115c.058-2.315 1.261-4.095 "
        "2.687-3.973 1.426.12 2.534 2.096 2.478 4.409a6.52 6.52 0 01-.146 1.243c2.58.505 "
        "5.352 1.787 8.914 3.844-.702-1.293-1.33-2.459-1.929-3.57-.943-.73-1.926-1.682-3.933"
        "-2.713 1.38.359 2.367.772 3.137 1.234-6.09-11.334-6.582-12.84-8.67-17.74z")

s = LOGO / 24
tx, ty = CX - 12 * s, CY - 12 * s

p = []
a = p.append

a(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">')
a(f'''<defs>
  <radialGradient id="bg" cx="0.5" cy="0.45" r="0.75">
    <stop offset="0" stop-color="#121820"/>
    <stop offset="0.6" stop-color="#0a0c10"/>
    <stop offset="1" stop-color="#050608"/>
  </radialGradient>
  <linearGradient id="logo" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#5ef1ff"/>
    <stop offset="1" stop-color="#5ea1ff"/>
  </linearGradient>
  <pattern id="dots" width="64" height="64" patternUnits="userSpaceOnUse">
    <circle cx="32" cy="32" r="2" fill="#ffffff" fill-opacity="0.05"/>
  </pattern>
  <radialGradient id="dotFade" cx="0.5" cy="0.45" r="0.6">
    <stop offset="0" stop-color="#fff" stop-opacity="1"/>
    <stop offset="1" stop-color="#fff" stop-opacity="0"/>
  </radialGradient>
  <mask id="dotMask"><rect width="{W}" height="{H}" fill="url(#dotFade)"/></mask>
  <filter id="halo" filterUnits="userSpaceOnUse" x="0" y="0" width="{W}" height="{H}">
    <feGaussianBlur stdDeviation="120"/>
  </filter>
  <filter id="glow" filterUnits="userSpaceOnUse" x="0" y="0" width="{W}" height="{H}">
    <feGaussianBlur stdDeviation="18" result="b"/>
    <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
  </filter>
</defs>''')

a(f'<rect width="{W}" height="{H}" fill="url(#bg)"/>')
a(f'<rect width="{W}" height="{H}" fill="url(#dots)" mask="url(#dotMask)"/>')

# Halo difuso atrás do logo
a(f'<circle cx="{CX}" cy="{CY + 60}" r="380" fill="#5ef1ff" fill-opacity="0.10" filter="url(#halo)"/>')

# Logo
a(f'<g filter="url(#glow)"><path d="{ARCH}" transform="translate({tx} {ty}) scale({s})" fill="url(#logo)"/></g>')

# Texto
a(f'<text x="{CX}" y="{CY + LOGO / 2 + 200}" text-anchor="middle" '
  f'font-family="JetBrainsMono Nerd Font" font-weight="300" font-size="72" '
  f'letter-spacing="28" fill="#e6e8eb" fill-opacity="0.55">arch linux</text>')

a('</svg>')

svg = out.rsplit('.', 1)[0] + '.svg'
with open(svg, 'w') as f:
    f.write('\n'.join(p))
os.system(f'rsvg-convert "{svg}" -o "{out}"')
print(out)
