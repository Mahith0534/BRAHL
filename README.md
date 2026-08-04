FoXYiZ_User 1.0.1
====================

END-USER package. Three main folders:

  _Docs\     documentation
  BRAHL\     desktop Arena UI (Python, port 8766)
  FoXYiZ\    engine + yPAD  (FOXYIZ_ROOT)

The test engine lives at:

  FoXYiZ\f\FoXYiZ.exe

There is no fEngine2.py or xActions.py here. Architects keep those in FoXYiZ__code
and publish a new FoXYiZ_User when the engine changes.

Quick start
-----------
1. Unzip this folder anywhere.
2. Double-click  Run FoXYiZ.bat
   (runs the API_Petstore Smoke demo by default)

Or from a terminal in this folder:

  set FOXYIZ_ROOT=%CD%\FoXYiZ
  FoXYiZ\f\FoXYiZ.exe --config FoXYiZ\f\fStart\API_Petstore.json
  FoXYiZ\f\FoXYiZ.exe --config FoXYiZ\f\fStart\Math.json
  FoXYiZ\f\FoXYiZ.exe --config FoXYiZ\f\fStart\UI_internet.json
  FoXYiZ\f\FoXYiZ.exe --config FoXYiZ\f\fStart\BRAHL_Local.json

BRAHL (optional UI)
-------------------
Double-click  Run BRAHL.bat
Opens http://127.0.0.1:8766/app
Run / Loop always call FoXYiZ\f\FoXYiZ.exe.

What you may edit
-----------------
  FoXYiZ\y\          yPAD suites
  FoXYiZ\f\fStart\   which suite and tags to run
  FoXYiZ\_pyUtils\   small helper scripts (optional; needs Python)
  FoXYiZ\z\          results after runs
  BRAHL\             desktop Arena UI (Python)
  _Docs\             package docs

What you must not change
------------------------
  FoXYiZ\f\FoXYiZ.exe and its runtime files (_internal)
  Core capabilities - ask an architect for a new release

Browsers
--------
UI demos need Microsoft Edge or Chrome installed.

AI (optional — BRAHL helpers only)
---------------------------------
Copy FoXYiZ\f\.env.example → FoXYiZ\f\.env
  A) OPENAI_API_KEY=…          cloud BYOK
  B) Ollama (free local): OPENAI_API_KEY=ollama
     OPENAI_BASE_URL=http://127.0.0.1:11434/v1
     OPENAI_MODEL=llama3.2
Then restart BRAHL. Run / Loop / Verify never need a key.

Docs: _Docs\  (start with Vision.md — same story as qaonair.com/vision)
