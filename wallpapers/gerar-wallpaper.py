import os
import random
import sys

W, H = 1920, 1080
HZ = 640          # linha do horizonte
CX = W / 2
random.seed(2077)

out = os.path.expanduser(sys.argv[1])
p = []
a = p.append

a(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">')
a('''<defs>
  <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#05010d"/>
    <stop offset="0.55" stop-color="#16052e"/>
    <stop offset="1" stop-color="#3a0b55"/>
  </linearGradient>
  <linearGradient id="ground" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#1a0630"/>
    <stop offset="1" stop-color="#030008"/>
  </linearGradient>
  <linearGradient id="sun" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#f1ff5e"/>
    <stop offset="0.45" stop-color="#ff9a5e"/>
    <stop offset="1" stop-color="#ff5ef1"/>
  </linearGradient>
  <linearGradient id="fadeGrid" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0.59" stop-color="#fff" stop-opacity="0.05"/>
    <stop offset="0.75" stop-color="#fff" stop-opacity="1"/>
  </linearGradient>
  <mask id="gridMask"><rect x="0" y="0" width="1920" height="1080" fill="url(#fadeGrid)"/></mask>
  <filter id="glow" x="-50%" y="-50%" width="200%" height="200%">
    <feGaussianBlur stdDeviation="6" result="b"/>
    <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
  </filter>
  <filter id="bigGlow" x="-50%" y="-50%" width="200%" height="200%">
    <feGaussianBlur stdDeviation="40"/>
  </filter>
  <pattern id="scan" width="4" height="4" patternUnits="userSpaceOnUse">
    <rect width="4" height="1" fill="#000" opacity="0.35"/>
  </pattern>
''')

# máscara do sol: listras horizontais que engrossam para baixo
R, SY = 250, HZ - 70
a('<mask id="sunMask"><rect x="0" y="0" width="1920" height="1080" fill="#fff"/>')
y, gap = SY - 150, 3
while y < SY + R:
    a(f'<rect x="0" y="{y:.1f}" width="{W}" height="{gap:.1f}" fill="#000"/>')
    y += gap + 18
    gap += 2.2
a('</mask></defs>')

a(f'<rect width="{W}" height="{HZ}" fill="url(#sky)"/>')

# estrelas
for _ in range(220):
    x, yy = random.uniform(0, W), random.uniform(0, HZ - 150)
    r = random.choice([0.6, 0.8, 1.0, 1.4])
    o = random.uniform(0.2, 0.9)
    c = random.choice(["#ffffff", "#5ef1ff", "#ff5ef1"])
    a(f'<circle cx="{x:.1f}" cy="{yy:.1f}" r="{r}" fill="{c}" opacity="{o:.2f}"/>')

# sol + halo
a(f'<circle cx="{CX}" cy="{SY}" r="{R + 60}" fill="#ff5ef1" opacity="0.35" filter="url(#bigGlow)"/>')
a(f'<circle cx="{CX}" cy="{SY}" r="{R}" fill="url(#sun)" mask="url(#sunMask)"/>')

# skyline em duas camadas
def skyline(base_col, win_cols, hmin, hmax, wmin, wmax, win_prob, opacity):
    x = -20
    while x < W + 20:
        bw = random.randint(wmin, wmax)
        # prédios mais baixos perto do sol para não escondê-lo
        center_factor = 0.45 if abs(x + bw / 2 - CX) < R * 0.9 else 1.0
        bh = random.randint(hmin, hmax) * center_factor
        top = HZ - bh
        a(f'<rect x="{x}" y="{top:.0f}" width="{bw}" height="{bh:.0f}" fill="{base_col}" opacity="{opacity}"/>')
        if random.random() < 0.25 and bh > 150:   # antena
            ax = x + bw / 2
            a(f'<line x1="{ax}" y1="{top:.0f}" x2="{ax}" y2="{top - 30:.0f}" stroke="{base_col}" stroke-width="3"/>')
            a(f'<circle cx="{ax}" cy="{top - 30:.0f}" r="2.5" fill="#ff5e5e" filter="url(#glow)"/>')
        for wy in range(int(top) + 8, HZ - 6, 12):
            for wx in range(x + 5, x + bw - 6, 9):
                if random.random() < win_prob:
                    col = random.choice(win_cols)
                    a(f'<rect x="{wx}" y="{wy}" width="4" height="5" fill="{col}" opacity="{random.uniform(0.4, 0.95):.2f}"/>')
        x += bw + random.randint(0, 6)

skyline("#120a24", ["#5ef1ff", "#bd5eff"], 120, 330, 40, 90, 0.10, 1)
skyline("#07030f", ["#5ef1ff", "#ff5ef1", "#f1ff5e"], 50, 200, 30, 70, 0.16, 1)

# chão + grid em perspectiva
a(f'<rect x="0" y="{HZ}" width="{W}" height="{H - HZ}" fill="url(#ground)"/>')
a('<g stroke="#ff5ef1" stroke-width="1.6" filter="url(#glow)" mask="url(#gridMask)" opacity="0.85">')
for i in range(-40, 41):
    xb = CX + i * 110
    a(f'<line x1="{CX + i * 6:.1f}" y1="{HZ}" x2="{xb:.1f}" y2="{H}"/>')
t = 1.0
while True:
    yy = HZ + (H - HZ) / t
    if yy - HZ < 14:
        break
    a(f'<line x1="0" y1="{yy:.1f}" x2="{W}" y2="{yy:.1f}"/>')
    t *= 1.32
a('</g>')

# horizonte brilhante
a(f'<line x1="0" y1="{HZ}" x2="{W}" y2="{HZ}" stroke="#5ef1ff" stroke-width="3" filter="url(#glow)" opacity="0.95"/>')
a(f'<rect x="0" y="{HZ - 1}" width="{W}" height="3" fill="#bff9ff"/>')

# código bem sutil no canto
code = [
    "import { hack } from '@net/runner';",
    "",
    "type Node = { id: string; online: boolean };",
    "",
    "export async function jackIn(grid: Node[]) {",
    "  const live = grid.filter((n) => n.online);",
    "  for (const node of live) {",
    "    await hack(node.id, { stealth: true });",
    "  }",
    "  return live.length;",
    "}",
]
a('<g font-family="JetBrainsMono Nerd Font, monospace" font-size="17" fill="#5ef1ff" opacity="0.32">')
for i, line in enumerate(code):
    if line:
        txt = line.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        a(f'<text x="70" y="{90 + i * 26}" xml:space="preserve">{txt}</text>')
a('</g>')

# assinatura glitch
sig = "~/dev $ █"
for dx, col, op in [(-3, "#ff5ef1", 0.6), (3, "#5ef1ff", 0.6), (0, "#ffffff", 0.9)]:
    a(f'<text x="{W - 70 + dx}" y="{H - 60}" text-anchor="end" font-family="JetBrainsMono Nerd Font, monospace" '
      f'font-size="30" font-weight="bold" fill="{col}" opacity="{op}" xml:space="preserve">{sig}</text>')

# scanlines + vinheta
a(f'<rect width="{W}" height="{H}" fill="url(#scan)" opacity="0.5"/>')
a('''<radialGradient id="vig" cx="0.5" cy="0.5" r="0.75">
  <stop offset="0.6" stop-color="#000" stop-opacity="0"/>
  <stop offset="1" stop-color="#000" stop-opacity="0.65"/>
</radialGradient>''')
a(f'<rect width="{W}" height="{H}" fill="url(#vig)"/>')
a('</svg>')

os.makedirs(os.path.dirname(out), exist_ok=True)
with open(out, "w") as f:
    f.write("\n".join(p))
print(out)
