"""Repo roots for BRAHL + FoXYiZ package.

Layouts:
  FoXYiZ_User/BRAHL/api/… + FoXYiZ_User/FoXYiZ/   (end-user zip — preferred)
  KK2/BRAHL/api/… + FoXYiZ_User|FoXYiZ__code|FoXYiZ sibling
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

_API_DIR = Path(__file__).resolve().parent
_BRAHL_ROOT = _API_DIR.parent
_PARENT = _BRAHL_ROOT.parent


def _is_foxyiz_package(root: Path) -> bool:
    return (root / "y").is_dir() and (
        (root / "f" / "FoXYiZ.exe").is_file() or (root / "f" / "fEngine2.py").is_file()
    )


def _default_roots() -> tuple[Path, Path]:
    """Return (foxyiz_root, kk_root)."""
    # End-user zip: BRAHL next to nested FoXYiZ/
    nested = _PARENT / "FoXYiZ"
    if _is_foxyiz_package(nested):
        return nested.resolve(), _PARENT.resolve()

    # Flat: FoXYiZ package is parent of BRAHL
    if _is_foxyiz_package(_PARENT):
        return _PARENT.resolve(), _PARENT.resolve()

    kk = _PARENT.resolve()
    for name in ("FoXYiZ_User", "FoXYiZ__code", "FoXYiZ"):
        cand = kk / name
        if _is_foxyiz_package(cand):
            return cand.resolve(), kk
        nested2 = cand / "FoXYiZ"
        if _is_foxyiz_package(nested2):
            return nested2.resolve(), cand.resolve()
    return (kk / "FoXYiZ__code").resolve(), kk


_FOXYIZ_DEFAULT, _KK_DEFAULT = _default_roots()

KK_ROOT = Path(os.environ.get("KK_ROOT", str(_KK_DEFAULT))).resolve()
FOXYIZ_ROOT = Path(os.environ.get("FOXYIZ_ROOT", str(_FOXYIZ_DEFAULT))).resolve()

F_DIR = FOXYIZ_ROOT / "f"
X_DIR = FOXYIZ_ROOT / "x"
Y_DIR = FOXYIZ_ROOT / "y"
Z_DIR = FOXYIZ_ROOT / "z"
PYUTILS_DIR = FOXYIZ_ROOT / "pyUtils"
if not PYUTILS_DIR.is_dir():
    PYUTILS_DIR = FOXYIZ_ROOT / "_pyUtils"
ENGINE_PY = F_DIR / "fEngine2.py"
ENGINE_EXE = F_DIR / "FoXYiZ.exe"
ENGINE = ENGINE_PY

_FOXYIZ_TOPS = frozenset({"f", "x", "y", "z", "pyUtils", "_pyUtils", ".pyUtils"})


def engine_cmd(config_rel: str) -> list[str]:
    """Prefer FoXYiZ.exe; fall back to python fEngine2.py for architect trees."""
    rel = str(config_rel).replace("\\", "/")
    if ENGINE_EXE.is_file():
        return [str(ENGINE_EXE), "--config", rel]
    if ENGINE_PY.is_file():
        return [sys.executable, str(ENGINE_PY), "--config", rel]
    raise FileNotFoundError(
        f"No FoXYiZ engine at {ENGINE_EXE} or {ENGINE_PY} (FOXYIZ_ROOT={FOXYIZ_ROOT})"
    )


def resolve_repo(rel: str | Path) -> Path:
    """Map short engine paths (f/… y/… z/…) to FoXYiZ package; else KK root."""
    if isinstance(rel, Path):
        p = rel
        if p.is_absolute():
            return p
        rel = p.as_posix()
    s = str(rel).replace("\\", "/").lstrip("./")
    if not s:
        return FOXYIZ_ROOT
    top = s.split("/", 1)[0]
    if top in {"FoXYiZ", "FoXYiZ__code", "FoXYiZ_User"}:
        return (KK_ROOT / s).resolve()
    if top in _FOXYIZ_TOPS:
        if top == ".pyUtils":
            s = "pyUtils" + s[len(".pyUtils") :]
        elif top == "_pyUtils" and not (FOXYIZ_ROOT / "_pyUtils").is_dir():
            s = "pyUtils" + s[len("_pyUtils") :]
        return (FOXYIZ_ROOT / s).resolve()
    return (KK_ROOT / s).resolve()


def repo_rel(path: Path) -> str:
    """Prefer package-relative short paths (z/run, f/…); else KK-relative."""
    path = path.resolve()
    try:
        return path.relative_to(FOXYIZ_ROOT).as_posix()
    except ValueError:
        pass
    try:
        return path.relative_to(KK_ROOT).as_posix()
    except ValueError:
        return path.as_posix()
