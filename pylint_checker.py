import subprocess
import tempfile

def run_pylint(code):

    with tempfile.NamedTemporaryFile(delete=False, suffix=".py") as f:
        f.write(code.encode())
        filename = f.name

    result = subprocess.run(
        ["pylint", filename],
        capture_output=True,
        text=True
    )

    return result.stdout