#!/usr/bin/env bash
"$(pwd)/venv/bin/python" -c "from app import app; app.run(port=5001, debug=True)"
