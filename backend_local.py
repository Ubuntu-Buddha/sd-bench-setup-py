# Bench fixture: inert stand-in for a local build backend.
def build_wheel(*args, **kwargs):
    raise SystemExit(1)
