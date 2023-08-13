"""
Main loader
"""

from sources.classes.class_engine import DwgbEngine
from sources.commands import DwgbCmdConsts

print("Connecting...")
tmp_engine = DwgbEngine("", "", 0, "",
                        {
                           2000000002: None,
                           2000000009: None,
                           2000000010: None,
                        })
print("Listening...")
tmp_engine.listen()
