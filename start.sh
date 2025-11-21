#!/bin/bash
# start.sh
# arranca el bot en background y luego el web server en foreground (Render necesita un proceso en foreground)
python -u bot.py &    # -u para logs sin buffer
python -u app.py
