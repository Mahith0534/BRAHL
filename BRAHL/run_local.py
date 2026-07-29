#!/usr/bin/env python3
"""Start BRAHL Local on http://127.0.0.1:8766"""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
API_DIR = ROOT / "api"
PORT = int(os.environ.get("BRAHL_PORT") or os.environ.get("QOA_PORT", "8766"))


def main() -> None:
    # BRAHL_LOCAL is canonical; QOA_DESKTOP kept as legacy alias.
    if "BRAHL_LOCAL" in os.environ:
        os.environ.setdefault("QOA_DESKTOP", os.environ["BRAHL_LOCAL"])
    else:
        os.environ.setdefault("BRAHL_LOCAL", "1")
        os.environ.setdefault("QOA_DESKTOP", "1")

    # Prefer nested FoXYiZ next to this BRAHL folder (User zip), else sibling trees.
    if "FOXYIZ_ROOT" not in os.environ:
        parent = ROOT.parent
        nested = parent / "FoXYiZ"
        if (nested / "y").is_dir() and (
            (nested / "f" / "FoXYiZ.exe").is_file() or (nested / "f" / "fEngine2.py").is_file()
        ):
            os.environ["FOXYIZ_ROOT"] = str(nested.resolve())
        elif (parent / "f" / "FoXYiZ.exe").is_file() and (parent / "y").is_dir():
            os.environ["FOXYIZ_ROOT"] = str(parent.resolve())
        else:
            for name in ("FoXYiZ_User", "FoXYiZ__code", "FoXYiZ"):
                cand = parent / name
                if (cand / "y").is_dir():
                    os.environ["FOXYIZ_ROOT"] = str(cand.resolve())
                    break
                nested2 = cand / "FoXYiZ"
                if (nested2 / "y").is_dir():
                    os.environ["FOXYIZ_ROOT"] = str(nested2.resolve())
                    break
    try:
        import uvicorn  # noqa: F401
    except ImportError:
        print("Installing BRAHL API dependencies…")
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", "-q", "-r", str(API_DIR / "requirements.txt")]
        )
    sys.path.insert(0, str(API_DIR))
    import uvicorn

    print(f"BRAHL Local — http://127.0.0.1:{PORT}")
    print(f"API health — http://127.0.0.1:{PORT}/api/health")
    uvicorn.run("main:app", host="127.0.0.1", port=PORT, reload=False, app_dir=str(API_DIR))


if __name__ == "__main__":
    main()
