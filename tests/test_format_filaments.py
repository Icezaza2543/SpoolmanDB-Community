import tempfile
from pathlib import Path

from scripts.format_filaments import format_file


def test_format_file():
  with tempfile.TemporaryDirectory() as directory:
    path = Path(directory) / "filament.json"
    original = '{"manufacturer":"\u00dcber Filaments","filaments":[{"diameters":[1.75]}]}'
    path.write_bytes(original.encode("utf-8"))

    assert not format_file(path, check=True)
    assert path.read_bytes() == original.encode("utf-8")

    assert format_file(path, check=False)
    formatted = (
        '{\n'
        '  "manufacturer": "Über Filaments",\n'
        '  "filaments": [\n'
        '    {\n'
        '      "diameters": [\n'
        '        1.75\n'
        '      ]\n'
        '    }\n'
        '  ]\n'
        '}\n'
    )
    assert path.read_bytes() == formatted.encode("utf-8")
    assert format_file(path, check=True)

