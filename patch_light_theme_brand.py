"""Follow-up: scope white text inside the blue login brand panel."""
PATH = r"C:\Users\Ruellyn Viola\.claude\Sir Law DBMS prototype\index.html"

with open(PATH, "r", encoding="utf-8") as f:
    src = f.read()

orig = src

# ── 1. Anchor after `.brand-db-badge code` rule, before `/* --- RIGHT FORM PANEL --- */`
anchor_left = """    .brand-db-badge code {
      color: #2563EB;
      font-weight: 600;
    }
"""
anchor_right = """    .brand-db-badge code {
      color: #FFFFFF;
      font-weight: 600;
    }

    /* Force white text on the blue brand panel in light theme */
    .login-brand-panel .brand-logo-big h2 { color: #FFFFFF; }
    .login-brand-panel .brand-logo-big h2 span { color: rgba(255,255,255,0.75); }
    .login-brand-panel .brand-feature-text b { color: #FFFFFF; }
    .login-brand-panel .brand-feature-text p { color: rgba(255,255,255,0.78); }
    .login-brand-panel .brand-db-badge { color: rgba(255,255,255,0.8); border-color: rgba(255,255,255,0.25); }
    .login-brand-panel .bfi-blue   { background: rgba(255,255,255,0.16); color: #FFFFFF; border-color: rgba(255,255,255,0.25); }
    .login-brand-panel .bfi-green  { background: rgba(255,255,255,0.16); color: #FFFFFF; border-color: rgba(255,255,255,0.25); }
    .login-brand-panel .bfi-amber  { background: rgba(255,255,255,0.16); color: #FFFFFF; border-color: rgba(255,255,255,0.25); }
    .login-brand-panel .bfi-purple { background: rgba(255,255,255,0.16); color: #FFFFFF; border-color: rgba(255,255,255,0.25); }
    .login-brand-panel .pin-visual { border-color: rgba(255,255,255,0.25); background: rgba(255,255,255,0.08); }
    .login-brand-panel .pin-visual i { color: #FFFFFF; }
    .login-brand-panel .brand-panel-tag { color: rgba(255,255,255,0.85); }
"""

if anchor_left in src:
    src = src.replace(anchor_left, anchor_right)
    print("[OK] brand panel white-text overrides inserted")
else:
    print("[FAIL] anchor not found — brand panel override NOT inserted")

# ── 2. Also make the `brand-panel-tag` (if present) white ──
# (any remaining .login-brand-panel text that uses var(--text-*) is already covered above)

with open(PATH, "w", encoding="utf-8") as f:
    f.write(src)

# ── Verification ──
checks = {
    "brand h2 white":       ".login-brand-panel .brand-logo-big h2 { color: #FFFFFF; }" in src,
    "brand h2 span light":  ".login-brand-panel .brand-logo-big h2 span { color: rgba(255,255,255,0.75); }" in src,
    "feature b white":      ".login-brand-panel .brand-feature-text b { color: #FFFFFF; }" in src,
    "feature p light":      ".login-brand-panel .brand-feature-text p { color: rgba(255,255,255,0.78); }" in src,
    "db badge code white":  "color: #FFFFFF;\n      font-weight: 600;\n    }\n\n    /* Force white text" in src,
}
passed = sum(1 for v in checks.values() if v)
print(f"\nRESULT: {passed}/{len(checks)} checks passed")
for k, v in checks.items():
    print(f"  {'[OK]' if v else '[FAIL]'} {k}")