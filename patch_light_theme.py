"""Light-theme conversion patch for index.html"""
import re

PATH = r"C:\Users\Ronnie\.claude\Sir Law\main project file with database file\index.html"

with open(PATH, "r", encoding="utf-8") as f:
    src = f.read()

orig = src

# ── 1. :root CSS variables ──
src = src.replace(
    "    :root {\n"
    "      --bg-main: #0B0F19;\n"
    "      --bg-card: #111827;\n"
    "      --bg-card-hover: #1F2937;\n"
    "      --bg-elevated: #1E293B;\n"
    "      --border-color: #334155;\n"
    "      --border-focus: #3B82F6;\n"
    "\n"
    "      --accent-primary: #3B82F6;\n"
    "      --accent-secondary: #6366F1;\n"
    "      --accent-gradient: linear-gradient(135deg, #3B82F6 0%, #8B5CF6 100%);\n"
    "\n"
    "      --status-available: #10B981; /* 🟢 Green */\n"
    "      --status-held: #F59E0B;      /* 🟡 Yellow / Amber */\n"
    "      --status-sold: #EF4444;      /* 🔴 Red */\n"
    "      --status-selected: #3B82F6;  /* 🔵 Blue */\n"
    "\n"
    "      --text-main: #F8FAFC;\n"
    "      --text-muted: #94A3B8;\n"
    "      --text-dim: #64748B;\n"
    "\n"
    "      --font-sans: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;\n"
    "      --font-mono: 'JetBrains Mono', monospace;\n"
    "\n"
    "      --radius-sm: 6px;\n"
    "      --radius-md: 10px;\n"
    "      --radius-lg: 16px;\n"
    "      --shadow-lg: 0 10px 25px -5px rgba(0, 0, 0, 0.5), 0 8px 10px -6px rgba(0, 0, 0, 0.5);\n"
    "      --glow-blue: 0 0 20px rgba(59, 130, 246, 0.35);\n"
    "      --glow-amber: 0 0 20px rgba(245, 158, 11, 0.4);\n"
    "    }",
    # --- REPLACEMENT ---
    "    :root {\n"
    "      --bg-main: #F1F5F9;\n"
    "      --bg-card: #FFFFFF;\n"
    "      --bg-card-hover: #F8FAFC;\n"
    "      --bg-elevated: #F1F5F9;\n"
    "      --border-color: #E2E8F0;\n"
    "      --border-focus: #3B82F6;\n"
    "\n"
    "      --accent-primary: #2563EB;\n"
    "      --accent-secondary: #4F46E5;\n"
    "      --accent-gradient: linear-gradient(135deg, #2563EB 0%, #7C3AED 100%);\n"
    "\n"
    "      --status-available: #059669; /* 🟢 Green */\n"
    "      --status-held: #D97706;      /* 🟡 Yellow / Amber */\n"
    "      --status-sold: #DC2626;      /* 🔴 Red */\n"
    "      --status-selected: #2563EB;  /* 🔵 Blue */\n"
    "\n"
    "      --text-main: #1E293B;\n"
    "      --text-muted: #64748B;\n"
    "      --text-dim: #94A3B8;\n"
    "\n"
    "      --text-secondary: #64748B;\n"
    "\n"
    "      --font-sans: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;\n"
    "      --font-mono: 'JetBrains Mono', monospace;\n"
    "\n"
    "      --radius-sm: 6px;\n"
    "      --radius-md: 10px;\n"
    "      --radius-lg: 16px;\n"
    "      --shadow-lg: 0 4px 15px -3px rgba(0, 0, 0, 0.08), 0 2px 6px -2px rgba(0, 0, 0, 0.05);\n"
    "      --glow-blue: 0 0 12px rgba(37, 99, 235, 0.15);\n"
    "      --glow-amber: 0 0 12px rgba(217, 119, 6, 0.15);\n"
    "    }"
)

# ── 2. Header background ──
src = src.replace(
    "      background-color: rgba(17, 24, 39, 0.85);",
    "      background-color: rgba(255, 255, 255, 0.88);"
)

# ── 3. System hero gradient ──
src = src.replace(
    "      background: linear-gradient(180deg, rgba(30, 41, 59, 0.7) 0%, rgba(17, 24, 39, 0.9) 100%);",
    "      background: linear-gradient(180deg, rgba(255,255,255,0.9) 0%, rgba(241,245,249,0.95) 100%);"
)

# ── 4. Hero::before radial glow ──
src = src.replace(
    "      background: radial-gradient(circle, rgba(59, 130, 246, 0.15) 0%, rgba(0, 0, 0, 0) 70%);\n"
    "      pointer-events: none;\n"
    "    }\n"
    "\n"
    "    .hero-title {",
    "      background: radial-gradient(circle, rgba(37, 99, 235, 0.08) 0%, rgba(255,255,255,0) 70%);\n"
    "      pointer-events: none;\n"
    "    }\n"
    "\n"
    "    .hero-title {"
)

# ── 5. Spec border-top ──
src = src.replace(
    "      border-top: 1px solid rgba(255, 255, 255, 0.08);",
    "      border-top: 1px solid var(--border-color);"
)

# ── 6. Featured card gradient ──
src = src.replace(
    "      background: linear-gradient(180deg, rgba(30, 41, 59, 0.5) 0%, rgba(17, 24, 39, 0.9) 100%);",
    "      background: linear-gradient(180deg, rgba(239,246,255,0.7) 0%, rgba(255,255,255,0.95) 100%);"
)

# ── 7. Event card hover border ──
src = src.replace("border-color: #475569;\n      box-shadow: var(--shadow-lg);",
                 "border-color: var(--accent-primary);\n      box-shadow: var(--shadow-lg);")

# ── 8. Tier row dashed border ──
src = src.replace(
    "      border-bottom: 1px dashed rgba(255, 255, 255, 0.06);",
    "      border-bottom: 1px dashed var(--border-color);"
)

# ── 9. Stage element gradient ──
src = src.replace(
    "      background: linear-gradient(90deg, #1E293B, #3B82F6, #1E293B);",
    "      background: linear-gradient(90deg, #E2E8F0, var(--accent-primary), #E2E8F0);"
)

# ── 10. Concurrency box ──
src = src.replace("background: rgba(30, 41, 59, 0.4);",
                 "background: rgba(241, 245, 249, 0.8);")

# ── 11. Sim btn hover ──
src = src.replace("      background: #334155;\n      border-color: #64748B;\n      color: var(--text-main);",
                 "      background: var(--bg-elevated);\n      border-color: var(--border-color);\n      color: var(--text-main);")

# ── 12. Table bottom borders ──
src = src.replace(
    "      border-bottom: 1px solid rgba(255, 255, 255, 0.06);",
    "      border-bottom: 1px solid var(--border-color);"
)

# ── 13. Status badges (available/held/sold) bg colors ──
src = src.replace(
    "      background: rgba(16, 185, 129, 0.2);",
    "      background: rgba(5, 150, 105, 0.1);"
)
src = src.replace(
    "      background: rgba(245, 158, 11, 0.25);",
    "      background: rgba(217, 119, 6, 0.1);"
)
src = src.replace(
    "      background: rgba(239, 68, 68, 0.25);",
    "      background: rgba(220, 38, 38, 0.1);"
)

# ── 14. Btn confirm pay disabled ──
src = src.replace(
    "      background: #334155;\n    }\n\n    /* FlexiPass Tab",
    "      background: #CBD5E1;\n    }\n\n    /* FlexiPass Tab"
)

# ── 15. E-ticket card gradient ──
src = src.replace(
    "      background: linear-gradient(145deg, #1E293B, #0F172A);",
    "      background: linear-gradient(145deg, #FFFFFF, #F8FAFC);"
)

# ── 16. SQL terminal ──
src = src.replace(
    "      background: #030712;\n"
    "      border: 1px solid #1F2937;",
    "      background: #0F172A;\n"
    "      border: 1px solid #1E293B;"
)

# ── 17. SQL syntax colors (keep readable on dark terminal but adjust) ──
src = src.replace(
    "    .sql-keyword { color: #F472B6; font-weight: bold; }",
    "    .sql-keyword { color: #F472B6; font-weight: bold; }"
)  # no change needed, pink on dark terminal fine

# ── 18. Modal overlay ──
src = src.replace(
    "      background: rgba(0, 0, 0, 0.75);",
    "      background: rgba(0, 0, 0, 0.45);"
)

# ── 19. Login overlay backdrop ──
src = src.replace(
    "      background: rgba(3, 7, 18, 0.92);",
    "      background: rgba(241, 245, 249, 0.85);"
)

# ── 20. Login inner shadow ──
src = src.replace(
    "      box-shadow: 0 30px 80px -10px rgba(0, 0, 0, 0.7), 0 0 50px rgba(59, 130, 246, 0.12);",
    "      box-shadow: 0 20px 60px -10px rgba(0, 0, 0, 0.15), 0 0 30px rgba(37, 99, 235, 0.08);"
)

# ── 21. Login brand panel gradient ──
src = src.replace(
    "      background: linear-gradient(160deg, #0F172A 0%, #1E293B 40%, #0F172A 100%);",
    "      background: linear-gradient(160deg, #1E40AF 0%, #3B82F6 40%, #1E40AF 100%);"
)

# ── 22. Login brand panel ::before glow ──
src = src.replace(
    "      background: radial-gradient(circle, rgba(59, 130, 246, 0.15) 0%, rgba(0, 0, 0, 0) 70%);\n"
    "      pointer-events: none;\n"
    "    }\n"
    "    .login-brand-panel::after {",
    "      background: radial-gradient(circle, rgba(255, 255, 255, 0.12) 0%, rgba(255,255,255,0) 70%);\n"
    "      pointer-events: none;\n"
    "    }\n"
    "    .login-brand-panel::after {"
)

# ── 23. Login brand panel ::after glow ──
src = src.replace(
    "      background: radial-gradient(circle, rgba(139, 92, 246, 0.12) 0%, rgba(0, 0, 0, 0) 70%);",
    "      background: radial-gradient(circle, rgba(255, 255, 255, 0.08) 0%, rgba(255,255,255,0) 70%);"
)

# ── 24. Brand icon bg in login brand panel ──
src = src.replace(
    "      background: rgba(59, 130, 246, 0.15);\n"
    "      border: 1px solid rgba(59, 130, 246, 0.3);\n"
    "      display: flex;\n"
    "      align-items: center;\n"
    "      justify-content: center;\n"
    "      color: #60A5FA;\n"
    "      font-size: 24px;\n"
    "    }\n"
    "    .brand-logo-big h2 {",
    "      background: rgba(255, 255, 255, 0.2);\n"
    "      border: 1px solid rgba(255, 255, 255, 0.3);\n"
    "      display: flex;\n"
    "      align-items: center;\n"
    "      justify-content: center;\n"
    "      color: #FFFFFF;\n"
    "      font-size: 24px;\n"
    "    }\n"
    "    .brand-logo-big h2 {"
)

# ── 25. Brand db badge ──
src = src.replace(
    "      background: rgba(59, 130, 246, 0.08);\n"
    "      border: 1px solid rgba(59, 130, 246, 0.2);",
    "      background: rgba(255, 255, 255, 0.12);\n"
    "      border: 1px solid rgba(255, 255, 255, 0.2);"
)

# ── 26. Nav btn hover (lighten) ──
src = src.replace(
    "      background: rgba(255, 255, 255, 0.05);\n"
    "    }\n"
    "\n"
    "    .nav-btn.active {",
    "      background: var(--bg-elevated);\n"
    "    }\n"
    "\n"
    "    .nav-btn.active {"
)

# ── 27. Social btn hover ──
src = src.replace(
    "      background: #334155;\n    }\n\n    .btn.social",
    "      background: var(--bg-elevated);\n    }\n\n    .btn.social"
)

# ── 28. Admin action btn hover ──
src = src.replace(
    "      background: #334155;\n"
    "      border-color: #64748B;\n"
    "      color: var(--text-main);\n"
    "    }\n"
    "    .admin-action-btn.danger",
    "      background: var(--bg-elevated);\n"
    "      border-color: var(--border-color);\n"
    "      color: var(--text-main);\n"
    "    }\n"
    "    .admin-action-btn.danger"
)

# ── 29. Login form panel bg (ensure white) ──
src = src.replace(
    "      flex: 1;\n"
    "      padding: 32px 28px 24px;\n"
    "      display: flex;\n"
    "      flex-direction: column;\n"
    "      justify-content: center;\n"
    "      background: var(--bg-card);",
    "      flex: 1;\n"
    "      padding: 32px 28px 24px;\n"
    "      display: flex;\n"
    "      flex-direction: column;\n"
    "      justify-content: center;\n"
    "      background: var(--bg-card);"
)

# ── 30. Concurrency box border (lighten) ──
src = src.replace(
    "      border: 1px solid rgba(59, 130, 246, 0.5);\n"
    "      box-shadow: 0 4px 20px rgba(59, 130, 246, 0.25);",
    "      border: 1px solid rgba(37, 99, 235, 0.25);\n"
    "      box-shadow: 0 2px 10px rgba(37, 99, 235, 0.08);"
)

# ── 31. Badge status (spec-item icon) ──
src = src.replace(
    "      background: rgba(59, 130, 246, 0.15);\n"
    "      color: #60A5FA;\n"
    "      border: 1px solid rgba(59, 130, 246, 0.3);\n"
    "      font-size: 0.7rem;",
    "      background: rgba(37, 99, 235, 0.08);\n"
    "      color: #2563EB;\n"
    "      border: 1px solid rgba(37, 99, 235, 0.2);\n"
    "      font-size: 0.7rem;"
)

# ── 32. Spec icon bg ──
src = src.replace(
    "      background: rgba(59, 130, 246, 0.15);\n"
    "      color: #60A5FA;\n"
    "      display: flex;\n"
    "      align-items: center;\n"
    "      justify-content: center;\n"
    "      font-size: 1rem;\n"
    "      flex-shrink: 0;\n"
    "    }\n"
    "\n"
    "    .spec-text h4 {",
    "      background: rgba(37, 99, 235, 0.08);\n"
    "      color: #2563EB;\n"
    "      display: flex;\n"
    "      align-items: center;\n"
    "      justify-content: center;\n"
    "      font-size: 1rem;\n"
    "      flex-shrink: 0;\n"
    "    }\n"
    "\n"
    "    .spec-text h4 {"
)

# ── 33. Category badge colors (lighter tints for light bg) ──
src = src.replace(
    "      background: rgba(139, 92, 246, 0.15);\n"
    "      color: #A78BFA;\n"
    "      border: 1px solid rgba(139, 92, 246, 0.3);",
    "      background: rgba(124, 58, 237, 0.08);\n"
    "      color: #7C3AED;\n"
    "      border: 1px solid rgba(124, 58, 237, 0.2);"
)
src = src.replace(
    "      background: rgba(236, 72, 153, 0.15);\n"
    "      color: #F472B6;\n"
    "      border: 1px solid rgba(236, 72, 153, 0.3);",
    "      background: rgba(219, 39, 119, 0.08);\n"
    "      color: #DB2777;\n"
    "      border: 1px solid rgba(219, 39, 119, 0.2);"
)

# ── 34. Tour text color (event-tour) ──
src = src.replace(
    "      color: #60A5FA;\n"
    "      font-weight: 600;\n"
    "      margin-bottom: 0.75rem;\n"
    "    }\n"
    "\n"
    "    .event-meta {",
    "      color: #2563EB;\n"
    "      font-weight: 600;\n"
    "      margin-bottom: 0.75rem;\n"
    "    }\n"
    "\n"
    "    .event-meta {"
)

# ── 35. Tier price text ──
src = src.replace(
    "      color: #F8FAFC;\n"
    "    }\n"
    "\n"
    "    .btn-select-event {",
    "      color: var(--text-main);\n"
    "    }\n"
    "\n"
    "    .btn-select-event {"
)

# ── 36. Seat detail sidebar border ──
src = src.replace(
    "      border-bottom: 1px solid rgba(255, 255, 255, 0.06);\n"
    "    }\n"
    "\n"
    "    .detail-row:last-child",
    "      border-bottom: 1px solid var(--border-color);\n"
    "    }\n"
    "\n"
    "    .detail-row:last-child"
)

# ── 37. BFI (brand feature icon) classes ──
src = src.replace(
    "    .bfi-blue { background: rgba(59, 130, 246, 0.12); color: #60A5FA; border: 1px solid rgba(59, 130, 246, 0.25); }",
    "    .bfi-blue { background: rgba(37, 99, 235, 0.08); color: #2563EB; border: 1px solid rgba(37, 99, 235, 0.15); }"
)
src = src.replace(
    "    .bfi-green { background: rgba(16, 185, 129, 0.12); color: #34D399; border: 1px solid rgba(16, 185, 129, 0.25); }",
    "    .bfi-green { background: rgba(5, 150, 105, 0.08); color: #059669; border: 1px solid rgba(5, 150, 105, 0.15); }"
)
src = src.replace(
    "    .bfi-amber { background: rgba(245, 158, 11, 0.12); color: #FCD34D; border: 1px solid rgba(245, 158, 11, 0.25); }",
    "    .bfi-amber { background: rgba(217, 119, 6, 0.08); color: #D97706; border: 1px solid rgba(217, 119, 6, 0.15); }"
)
src = src.replace(
    "    .bfi-purple { background: rgba(139, 92, 246, 0.12); color: #A78BFA; border: 1px solid rgba(139, 92, 246, 0.25); }",
    "    .bfi-purple { background: rgba(124, 58, 237, 0.08); color: #7C3AED; border: 1px solid rgba(124, 58, 237, 0.15); }"
)

# ── 38. Login section: login-forgot hint ──
src = src.replace(
    "    .fp-hint b { color: #60A5FA;",
    "    .fp-hint b { color: #2563EB;"
)
src = src.replace(
    "    .fp-resend button { background: none; border: none; color: #60A5FA;",
    "    .fp-resend button { background: none; border: none; color: #2563EB;"
)

# ── 39. Role badges ──
src = src.replace(
    "    .role-user { background: rgba(59, 130, 246, 0.2); color: #60A5FA; }",
    "    .role-user { background: rgba(37, 99, 235, 0.1); color: #2563EB; }"
)

# ── 40. Role admin (keep gold but lighter bg) ──
src = src.replace(
    "      background: rgba(245, 158, 11, 0.25);\n"
    "      color: #FCD34D;\n"
    "      border: 1px solid rgba(245, 158, 11, 0.4);",
    "      background: rgba(217, 119, 6, 0.1);\n"
    "      color: #B45309;\n"
    "      border: 1px solid rgba(217, 119, 6, 0.2);"
)

# ── 41. Admin mode strip ──
src = src.replace(
    "      background: linear-gradient(90deg, rgba(245, 158, 11, 0.12) 0%, rgba(217, 119, 6, 0.08) 100%);\n"
    "      border: 1px solid rgba(245, 158, 11, 0.25);",
    "      background: linear-gradient(90deg, rgba(245, 158, 11, 0.08) 0%, rgba(217, 119, 6, 0.05) 100%);\n"
    "      border: 1px solid rgba(245, 158, 11, 0.2);"
)

# ── 42. Admin mode strip text color ──
src = src.replace(
    "      color: #FCD34D;\n"
    "    }\n"
    "\n"
    "    /* Admin stats grid */",
    "      color: #92400E;\n"
    "    }\n"
    "\n"
    "    /* Admin stats grid */"
)

# ── 43. Admin stat value (gold stat numbers) ──
src = src.replace(
    "      color: #FCD34D;\n"
    "    }\n"
    "    .admin-stat-card .stat-label {",
    "      color: #B45309;\n"
    "    }\n"
    "    .admin-stat-card .stat-label {"
)

# ── 44. Admin status colors (available/held/sold) ──
src = src.replace(
    "    .admin-status-available { color: #10B981; font-weight: 600; }",
    "    .admin-status-available { color: #059669; font-weight: 600; }"
)
src = src.replace(
    "    .admin-status-held     { color: #FCD34D; font-weight: 600; }",
    "    .admin-status-held     { color: #D97706; font-weight: 600; }"
)
src = src.replace(
    "    .admin-status-sold     { color: #F87171; font-weight: 600; }",
    "    .admin-status-sold     { color: #DC2626; font-weight: 600; }"
)

# ── 45. Admin ledger/inventory h4 icon colors ──
src = src.replace(
    "    .admin-ledger h4 i  { color: #F59E0B; }",
    "    .admin-ledger h4 i  { color: #D97706; }"
)

# ── 46. Admin action btn gold color ──
src = src.replace(
    "      color: #FCD34D;\n"
    "    }\n"
    "    .admin-action-btn.gold",
    "      color: #B45309;\n"
    "    }\n"
    "    .admin-action-btn.gold"
)

src = src.replace(
    "      color: #F87171;\n"
    "    }\n"
    "    .admin-action-btn.gold",
    "      color: #DC2626;\n"
    "    }\n"
    "    .admin-action-btn.gold"
)

# ── 47. Admin action btn danger border ──
src = src.replace(
    "      border-color: #EF4444;",
    "      border-color: #FCA5A5;"
)
src = src.replace(
    "      border-color: #F59E0B;",
    "      border-color: #FCD34D;"
)

# ── 48. Inline HTML: Forgot password link color ──
src = src.replace(
    "style=\"background:none;border:none;color:#60A5FA;font-size:12px;",
    "style=\"background:none;border:none;color:#2563EB;font-size:12px;"
)

# ── 49. Inline HTML: verify email color ──
src = src.replace(
    "style=\"font-weight:700;color:#60A5FA;",
    "style=\"font-weight:700;color:#2563EB;"
)

# ── 50. Inline HTML: hero server icon ──
src = src.replace(
    'style="color: #60A5FA;">',
    'style="color: #2563EB;">'
)

# ── 51. Inline HTML: active event name badge ──
src = src.replace(
    'style="color: #60A5FA;">Taylor Swift',
    'style="color: #2563EB;">Taylor Swift'
)

# ── 52. Inline HTML: section icons in seatlock ──
src = src.replace(
    'style="color: #F59E0B;"></i> VIP A',
    'style="color: #D97706;"></i> VIP A'
)
src = src.replace(
    'style="color: #F59E0B;"></i> VIP B',
    'style="color: #D97706;"></i> VIP B'
)
src = src.replace(
    'style="color: #3B82F6;"></i> Lower Box 1',
    'style="color: #2563EB;"></i> Lower Box 1'
)
src = src.replace(
    'style="color: #3B82F6;"></i> Lower Box 2',
    'style="color: #2563EB;"></i> Lower Box 2'
)
src = src.replace(
    'style="color: #10B981;"></i> Upper Box',
    'style="color: #059669;"></i> Upper Box'
)
src = src.replace(
    'style="color: #94A3B8;"></i> General Admission',
    'style="color: #64748B;"></i> General Admission'
)
src = src.replace(
    'style="color: #F59E0B;"></i> Pessimistic',
    'style="color: #D97706;"></i> Pessimistic'
)

# ── 53. Hold lock timer label ──
src = src.replace(
    "color: #FCD34D;\";",
    "color: #D97706;\";"
)

# ── 54. Inline HELD status color ──
src = src.replace(
    'id="detailLockStatus" style="color: #F59E0B;"',
    'id="detailLockStatus" style="color: #D97706;"'
)

# ── 55. Inline price color ──
src = src.replace(
    'id="detailPrice" style="font-size: 1.1rem; color: #34D399;',
    'id="detailPrice" style="font-size: 1.1rem; color: #059669;'
)

# ── 56. Inline payment method icons ──
src = src.replace(
    'style="color: #3B82F6;"></i>\n'
    '                  <span style="font-size: 0.75rem;">GatePass NFC</span>',
    'style="color: #2563EB;"></i>\n'
    '                  <span style="font-size: 0.75rem;">GatePass NFC</span>'
)

# ── 57. CONFIRMED ADMISSION badge ──
src = src.replace(
    'style="background: rgba(16, 185, 129, 0.2); color: #34D399; border-color: #10B981;"',
    'style="background: rgba(5, 150, 105, 0.1); color: #059669; border-color: #059669;"'
)

# ── 58. Ticket icon color ──
src = src.replace(
    'style="font-size: 2rem; color: #3B82F6;"',
    'style="font-size: 2rem; color: #2563EB;"'
)

# ── 59. Seat assignment color on ticket ──
src = src.replace(
    'id="ticketCardSeat" style="font-weight: 700; color: #F59E0B;"',
    'id="ticketCardSeat" style="font-weight: 700; color: #D97706;"'
)

# ── 60. QR payload text color ──
src = src.replace(
    'id="qrRawPayload"',
    'id="qrRawPayload"'
)  # #38BDF8 is fine — adjust below
src = src.replace(
    'font-size: 0.75rem; color: #38BDF8;"',
    'font-size: 0.75rem; color: #0369A1;"'
)

# ── 61. ticket-detail-item border (inline) ──
src = src.replace(
    'style="border-top: 1px dashed rgba(255,255,255,0.1);',
    'style="border-top: 1px dashed var(--border-color);'
)

# ── 62. Log GRANTED color ──
src = src.replace(
    "color: #34D399;\">GRANTED",
    "color: #059669;\">GRANTED"
)

# ── 63. Status badge icon (server) — already covered by broad replace above, but check ──

# ── 64. Footer / bottom info area bg ──
src = src.replace(
    "      background: rgba(59, 130, 246, 0.08);\n"
    "      border: 1px solid rgba(59, 130, 246, 0.2);",
    "      background: rgba(37, 99, 235, 0.04);\n"
    "      border: 1px solid rgba(37, 99, 235, 0.12);"
)

# ── 65. Flexipass / gatepass info boxes ──
src = src.replace(
    "      background: rgba(59, 130, 246, 0.1);\n"
    "      border: 1px solid rgba(59, 130, 246, 0.3);",
    "      background: rgba(37, 99, 235, 0.05);\n"
    "      border: 1px solid rgba(37, 99, 235, 0.15);"
)

# ── 66. Hold lock banner (keep amber but lighter bg) ──
src = src.replace(
    "      background: rgba(245, 158, 11, 0.12);\n"
    "      border: 1px solid rgba(245, 158, 11, 0.35);",
    "      background: rgba(217, 119, 6, 0.08);\n"
    "      border: 1px solid rgba(217, 119, 6, 0.25);"
)

# ── 67. Hold lock banner text color ──
src = src.replace(
    "      color: #FCD34D;\n"
    "      animation: pulse-glow 2.5s infinite alternate;\n"
    "    }\n"
    "\n"
    "    .hold-lock-banner.inactive",
    "      color: #B45309;\n"
    "      animation: pulse-glow 2.5s infinite alternate;\n"
    "    }\n"
    "\n"
    "    .hold-lock-banner.inactive"
)

# ── 68. Hold lock inactive ──
src = src.replace(
    "      background: rgba(100, 116, 139, 0.12);\n"
    "      border-color: rgba(100, 116, 139, 0.25);",
    "      background: rgba(100, 116, 139, 0.06);\n"
    "      border-color: rgba(100, 116, 139, 0.15);"
)

# ── 69. Pulse glow keyframes (lighter) ──
src = src.replace(
    "      0% { box-shadow: 0 0 5px rgba(245, 158, 11, 0.2); }\n"
    "      100% { box-shadow: 0 0 16px rgba(245, 158, 11, 0.5); }",
    "      0% { box-shadow: 0 0 4px rgba(217, 119, 6, 0.12); }\n"
    "      100% { box-shadow: 0 0 12px rgba(217, 119, 6, 0.25); }"
)

# ── 70. Seat dot glows (lighter for light bg) ──
src = src.replace(
    ".dot-available { background-color: var(--status-available); box-shadow: 0 0 6px rgba(16, 185, 129, 0.4); }",
    ".dot-available { background-color: var(--status-available); box-shadow: 0 0 4px rgba(5, 150, 105, 0.25); }"
)
src = src.replace(
    ".dot-held { background-color: var(--status-held); box-shadow: 0 0 6px rgba(245, 158, 11, 0.5); }",
    ".dot-held { background-color: var(--status-held); box-shadow: 0 0 4px rgba(217, 119, 6, 0.3); }"
)
src = src.replace(
    ".dot-selected { background-color: var(--status-selected); box-shadow: 0 0 8px rgba(59, 130, 246, 0.7); }",
    ".dot-selected { background-color: var(--status-selected); box-shadow: 0 0 6px rgba(37, 99, 235, 0.35); }"
)

# ── 71. Btn primary shadows (lighter) ──
src = src.replace(
    "      box-shadow: 0 4px 15px rgba(59, 130, 246, 0.4);",
    "      box-shadow: 0 4px 12px rgba(37, 99, 235, 0.2);"
)
src = src.replace(
    "      box-shadow: 0 6px 20px rgba(59, 130, 246, 0.6);",
    "      box-shadow: 0 6px 16px rgba(37, 99, 235, 0.25);"
)

# ── 72. Login tabs active shadow ──
src = src.replace(
    "      box-shadow: 0 2px 10px rgba(59, 130, 246, 0.45);",
    "      box-shadow: 0 2px 8px rgba(37, 99, 235, 0.18);"
)

# ── 73. Login input focus ring ──
src = src.replace(
    "      box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.25);",
    "      box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.15);"
)

# ── 74. Login error state ──
src = src.replace(
    "      background: rgba(239, 68, 68, 0.08);",
    "      background: rgba(220, 38, 38, 0.05);"
)

# ── 75. Nav btn active shadow ──
src = src.replace(
    "      box-shadow: 0 2px 10px rgba(59, 130, 246, 0.4);",
    "      box-shadow: 0 2px 8px rgba(37, 99, 235, 0.18);"
)

# ── 76. Seat node selected glow ──
src = src.replace(
    "      box-shadow: 0 0 10px rgba(59, 130, 246, 0.8);",
    "      box-shadow: 0 0 8px rgba(37, 99, 235, 0.3);"
)

# ── 77. Stage element shadow ──
src = src.replace(
    "      box-shadow: 0 4px 20px rgba(59, 130, 246, 0.25);",
    "      box-shadow: 0 2px 10px rgba(37, 99, 235, 0.12);"
)

# ── 78. Pay btn shadows ──
src = src.replace(
    "      box-shadow: 0 4px 15px rgba(16, 185, 129, 0.4);",
    "      box-shadow: 0 4px 12px rgba(5, 150, 105, 0.2);"
)
src = src.replace(
    "      box-shadow: 0 6px 20px rgba(16, 185, 129, 0.5);",
    "      box-shadow: 0 6px 16px rgba(5, 150, 105, 0.25);"
)

# ── 79. FP code input focus ──
src = src.replace(
    "      box-shadow: 0 0 12px rgba(59, 130, 246, 0.3);",
    "      box-shadow: 0 0 8px rgba(37, 99, 235, 0.15);"
)

# ── 80. FP success check shadow ──
src = src.replace(
    "      box-shadow: 0 8px 25px rgba(16, 185, 129, 0.45);",
    "      box-shadow: 0 6px 18px rgba(5, 150, 105, 0.2);"
)

# ── 81. Login logo glow ──
src = src.replace(
    "      box-shadow: 0 0 20px rgba(59, 130, 246, 0.15);",
    "      box-shadow: 0 0 12px rgba(37, 99, 235, 0.1);"
)

# ── 82. Admin tab active shadow ──
src = src.replace(
    "      box-shadow: 0 2px 12px rgba(245, 158, 11, 0.45);",
    "      box-shadow: 0 2px 8px rgba(217, 119, 6, 0.2);"
)

# ── 83. Btn select event hover ──
src = src.replace(
    "      box-shadow: 0 4px 14px rgba(37, 99, 235, 0.4);",
    "      box-shadow: 0 4px 12px rgba(37, 99, 235, 0.2);"
)

# ── 84. Button hover color (select event) ──
src = src.replace(
    "      background: #2563EB;",
    "      background: #1D4ED8;"
)

# ── 85. Concurrency box bg (second occurrence if any) ──
src = src.replace(
    "      background: rgba(30, 41, 59, 0.4);\n"
    "      border: 1px solid rgba(59, 130, 246, 0.5);",
    "      background: rgba(241, 245, 249, 0.8);\n"
    "      border: 1px solid rgba(37, 99, 235, 0.2);"
)

# ── 86. Hold lock timer inline area ──
src = src.replace(
    "      background: rgba(245, 158, 11, 0.1);\n"
    "      border: 1px solid rgba(245, 158, 11, 0.3);",
    "      background: rgba(217, 119, 6, 0.06);\n"
    "      border: 1px solid rgba(217, 119, 6, 0.18);"
)

# ── 87. Ticket badge confirmed (flexipass) ──
src = src.replace(
    'color: #34D399;">CONFIRMED ADMISSION',
    'color: #059669;">CONFIRMED ADMISSION'
)

# ── 88. System viewer ──
src = src.replace(
    "      background: var(--bg-main);\n"
    "      border-radius: var(--radius-md);\n"
    "      overflow: hidden;\n"
    "      border: 1px solid var(--border-color);",
    "      background: var(--bg-card);\n"
    "      border-radius: var(--radius-md);\n"
    "      overflow: hidden;\n"
    "      border: 1px solid var(--border-color);"
)

# ── 89. CSS remaining: login-forgot area, status chip, etc ──
# Status badge colors (held/sold in seat detail view)
src = src.replace(
    "      background: rgba(245, 158, 11, 0.25);\n"
    "      color: #FCD34D;\n"
    "      border-color: rgba(245, 158, 11, 0.6);",
    "      background: rgba(217, 119, 6, 0.08);\n"
    "      color: #B45309;\n"
    "      border-color: rgba(217, 119, 6, 0.2);"
)
src = src.replace(
    "      background: rgba(239, 68, 68, 0.25);\n"
    "      color: #F87171;\n"
    "      border-color: rgba(239, 68, 68, 0.6);",
    "      background: rgba(220, 38, 38, 0.08);\n"
    "      color: #DC2626;\n"
    "      border-color: rgba(220, 38, 38, 0.2);"
)

# ── 90. Lock status box / warning area ──
src = src.replace(
    "      color: #FCD34D;\n"
    "      font-weight: 700;\n"
    "    }\n"
    "\n"
    "    .lock-expired-msg {",
    "      color: #D97706;\n"
    "      font-weight: 700;\n"
    "    }\n"
    "\n"
    "    .lock-expired-msg {"
)

# ── 91. Seat status color legend dots ──
src = src.replace(
    "    .seat-legend-item .dot-available",
    "    .seat-legend-item .dot-available"
)  # these use var() — no change needed

# ── 92. Remaining rgba(59, 130, 246, ...) inline border in login ──
src = src.replace(
    "      border: 1px solid rgba(59, 130, 246, 0.4);",
    "      border: 1px solid rgba(37, 99, 235, 0.2);"
)

# ── 93. Login divider area ──
src = src.replace(
    "      border-bottom: 1px solid rgba(255, 255, 255, 0.08);",
    "      border-bottom: 1px solid var(--border-color);"
)

# ── 94. Remaining rgba(255, 255, 255, 0.05) hover states ──
src = src.replace(
    "      background: rgba(255, 255, 255, 0.05);",
    "      background: var(--bg-elevated);"
)

# ── 95. Brand logo big color in login ──
src = src.replace(
    "      color: #60A5FA;\n"
    "      font-size: 24px;",
    "      color: #FFFFFF;\n"
    "      font-size: 24px;"
)

# ── 96. Inline event badge status ──
src = src.replace(
    'color: #60A5FA;',
    'color: #2563EB;'
)

# ── 97. JS tier price colors ──
src = src.replace(
    "color:#FCD34D;\">${ev.vip}",
    "color:#B45309;\">${ev.vip}"
)
src = src.replace(
    "color:#60A5FA;\">${ev.lower}",
    "color:#2563EB;\">${ev.lower}"
)
src = src.replace(
    "color:#34D399;\">${ev.upper}",
    "color:#059669;\">${ev.upper}"
)

# ── 98. JS QR code color (keep dark modules for scannability) ──
# QR code dark stays #0B0F19 — no change needed for scanners

# ── 99. JS result colors (turnstile log) ──
src = src.replace(
    "const resColor = result.includes('GRANTED') ? '#34D399' : '#F87171';",
    "const resColor = result.includes('GRANTED') ? '#059669' : '#DC2626';"
)

# ── 100. JS seat status colors in DB viewer ──
src = src.replace(
    "let statusStyle = 'color: #34D399;';\n"
    "        if (s.status === 'HELD') statusStyle = 'color: #FCD34D; font-weight: bold;';\n"
    "        if (s.status === 'SOLD') statusStyle = 'color: #F87171;';",
    "let statusStyle = 'color: #059669;';\n"
    "        if (s.status === 'HELD') statusStyle = 'color: #D97706; font-weight: bold;';\n"
    "        if (s.status === 'SOLD') statusStyle = 'color: #DC2626;';"
)

# ── 101. JS admin ledger colors ──
src = src.replace(
    "color: #10B981;\">' + row.sold",
    "color: #059669;\">' + row.sold"
)
src = src.replace(
    "color: #FCD34D;\">₱' + row.revenue",
    "color: #B45309;\">₱' + row.revenue"
)
src = src.replace(
    "color: #10B981;\">' + t.totalSold",
    "color: #059669;\">' + t.totalSold"
)
src = src.replace(
    "color: #FCD34D;\">₱' + t.totalRevenue",
    "color: #B45309;\">₱' + t.totalRevenue"
)

# ── 102. Admin stat card value (JS-generated color) ──
src = src.replace(
    "color: #FCD34D;\">${",
    "color: #B45309;\">${"
)

# ── 103. Seat node hover bg ──
src = src.replace(
    "      background: rgba(59, 130, 246, 0.12);",
    "      background: rgba(37, 99, 235, 0.08);"
)

# ── 104. Seat node tooltip border ──
src = src.replace(
    "      border: 1px solid rgba(59, 130, 246, 0.35);",
    "      border: 1px solid rgba(37, 99, 235, 0.2);"
)

# ── 105. Login overlay remaining dark bg ──
src = src.replace(
    "background: rgba(3, 7, 18, 0.92)",
    "background: rgba(241, 245, 249, 0.85)"
)

# ── 106. Event card border hover ──
src = src.replace(
    "      border-color: rgba(59, 130, 246, 0.4);",
    "      border-color: rgba(37, 99, 235, 0.3);"
)

# ── 107. Footer area / flexipass hint bg ──
src = src.replace(
    "    .flexipass-hint {\n"
    "      background: rgba(59, 130, 246, 0.1);\n"
    "      border: 1px solid rgba(59, 130, 246, 0.3);",
    "    .flexipass-hint {\n"
    "      background: rgba(37, 99, 235, 0.05);\n"
    "      border: 1px solid rgba(37, 99, 235, 0.15);"
)

# ── 108. Lock warning badge ──
src = src.replace(
    "      background: rgba(239, 68, 68, 0.2);",
    "      background: rgba(220, 38, 38, 0.08);"
)
src = src.replace(
    "      color: #F87171;\n"
    "      border-color: rgba(239, 68, 68, 0.4);",
    "      color: #DC2626;\n"
    "      border-color: rgba(220, 38, 38, 0.2);"
)

# ── 109. Flexipass form input group bg ──
src = src.replace(
    "      background: rgba(59, 130, 246, 0.12);",
    "      background: rgba(37, 99, 235, 0.06);"
)

# ── 110. Flexipass verify btn bg ──
src = src.replace(
    "      background: rgba(59, 130, 246, 0.15);",
    "      background: rgba(37, 99, 235, 0.1);"
)

# ── 111. Remaining lock badge area ──
src = src.replace(
    "      background: rgba(245, 158, 11, 0.12);\n"
    "      border-color: rgba(245, 158, 11, 0.35);",
    "      background: rgba(217, 119, 6, 0.06);\n"
    "      border-color: rgba(217, 119, 6, 0.18);"
)

# ── 112. Lock text ──
src = src.replace(
    "      color: #FCD34D;\n"
    "      font-weight: 700;\n"
    "    }\n"
    "\n"
    "    .lock-badge.error",
    "      color: #B45309;\n"
    "      font-weight: 700;\n"
    "    }\n"
    "\n"
    "    .lock-badge.error"
)

# ── 113. Admin console area remaining colors ──
src = src.replace(
    "      background: rgba(245, 158, 11, 0.08);",
    "      background: rgba(217, 119, 6, 0.04);"
)

# ── 114. Admin ledger/inventory section icons (blue) ──
src = src.replace(
    "    .admin-inventory h4 i { color: #3B82F6; }",
    "    .admin-inventory h4 i { color: #2563EB; }"
)

# ── 115. Remaining dark body / app background artifacts ──
# (body uses var(--bg-main) so the :root change covers it)

# ── 116. Event-card featured border color ──
src = src.replace(
    "      border-color: rgba(59, 130, 246, 0.4);\n"
    "      background: linear-gradient",
    "      border-color: rgba(37, 99, 235, 0.25);\n"
    "      background: linear-gradient"
)

# ── 117. Footer/system info bar ──
src = src.replace(
    "    .system-info-bar {\n"
    "      background: var(--bg-card);\n"
    "      border: 1px solid var(--border-color);",
    "    .system-info-bar {\n"
    "      background: var(--bg-card);\n"
    "      border: 1px solid var(--border-color);"
)  # already using vars — fine

# ── 118. Active seat section highlight ──
src = src.replace(
    "      border-color: #93C5FD;",
    "      border-color: #BFDBFE;"
)

# ── 119. Ensure event card pricing box bg is card-like ──
src = src.replace(
    "      background: var(--bg-main);\n"
    "      border: 1px solid var(--border-color);\n"
    "      border-radius: var(--radius-md);\n"
    "      padding: 0.75rem;\n"
    "      margin-bottom: 1rem;\n"
    "    }\n"
    "\n"
    "    .tier-row {",
    "      background: var(--bg-elevated);\n"
    "      border: 1px solid var(--border-color);\n"
    "      border-radius: var(--radius-md);\n"
    "      padding: 0.75rem;\n"
    "      margin-bottom: 1rem;\n"
    "    }\n"
    "\n"
    "    .tier-row {"
)

# ── 120. Brand logo in nav ── (uses var(--text-main), covered by :root)
# ── 121. Session badge ── (uses var(--bg-elevated), covered by :root)

# ── 122. Remaining hard to reach: QR box inline bg ──
src = src.replace(
    "style=\"background:#030712",
    "style=\"background:#0F172A"
)

# ── 123. Admin tab gold active text on dark bg → now light bg ──
# The admin tab active has color:#0B0F19 which is dark text on gold gradient — that's fine

# ── Write the patched file ──
with open(PATH, "w", encoding="utf-8") as f:
    f.write(src)

# ── Verification ──
import re as re2
checks = {
    "bg-main light":       "--bg-main: #F1F5F9" in src,
    "bg-card white":       "--bg-card: #FFFFFF" in src,
    "text-main dark":      "--text-main: #1E293B" in src,
    "text-muted":          "--text-muted: #64748B" in src,
    "header translucent":  "rgba(255, 255, 255, 0.88)" in src,
    "login overlay light": "rgba(241, 245, 249, 0.85)" in src,
    "brand panel blue":    "linear-gradient(160deg, #1E40AF" in src,
    "system hero light":   "rgba(255,255,255,0.9)" in src,
    "featured card light": "rgba(239,246,255,0.7)" in src,
    "sql terminal dark":   "background: #0F172A;" in src,
    "no #0B0F19 bg":       "#0B0F19" not in src.replace("colorDark", "").replace("admin-tab.active", ""),
    "no #111827 bg":       "#111827" not in src.replace(":root", "ROOTBLOCK"),
    "no rgba(17,24,39":    "rgba(17, 24, 39" not in src,
    "no #1E293B bg in CSS":"#1E293B" not in src.split("</style>")[0].replace("sql-terminal", "SQLTERM"),
    "accent-primary blue": "--accent-primary: #2563EB" in src,
    "shadow lighter":      "rgba(0, 0, 0, 0.5)" not in src.split("</style>")[0],
    "text-secondary fix":  "--text-secondary: #64748B" in src,
    "status-available":    "--status-available: #059669" in src,
    "status-held":         "--status-held: #D97706" in src,
    "status-sold":         "--status-sold: #DC2626" in src,
    "admin stat gold→amber":"color: #B45309;" in src,
    "admin ledger colors": "color: #059669;" in src and "color: #B45309;" in src,
}

passed = sum(1 for v in checks.values() if v)
total = len(checks)
print(f"\n{'='*60}")
print(f"  LIGHT THEME PATCH — VERIFICATION")
print(f"{'='*60}")
for label, ok in checks.items():
    print(f"  {'[OK]' if ok else '[FAIL]'} {label}")
print(f"{'='*60}")
print(f"  RESULT: {passed}/{total} checks passed")
print(f"{'='*60}\n")

if passed < total:
    failed = [k for k, v in checks.items() if not v]
    print("Failed checks:", failed)
else:
    print("All checks passed! Light theme applied successfully.")
