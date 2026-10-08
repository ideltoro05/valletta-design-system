"""
In-place rebrand of the three NBAF report docx files: swap the old
Valletta-only logo for the combined Valletta+SOC lockup, and remap the old
red/navy accent colors to Valletta Cobalt (#1B4FA0) / black, per the v2.0
design system. No text content is touched anywhere -- every substitution
targets only XML attribute values (hex color codes, a font-family name,
an image part, and its extent), never a <w:t> text node.

Run with: python3 -I rebrand_nbaf.py
"""
import zipfile
import shutil
import os

HERE = os.path.dirname(os.path.abspath(__file__))
LOGO_PATH = os.path.join(HERE, "valletta-soc-lockup.png")

SOURCES = [
    ("/root/.claude/uploads/740649a2-a5a9-5a9b-a94a-a0a642982174/38894e8b-Valletta_NBAF_Completed_Training_Summary_September.docx",
     "valletta_NBAF_Completed_Training_Summary_September.docx"),
    ("/root/.claude/uploads/740649a2-a5a9-5a9b-a94a-a0a642982174/5170cf40-Valletta_NBAF_Incident_Report_September.docx",
     "valletta_NBAF_Incident_Report_September.docx"),
    ("/root/.claude/uploads/740649a2-a5a9-5a9b-a94a-a0a642982174/3bbdb131-Valletta_NBAF_Monthly_Report_September.docx",
     "valletta_NBAF_Monthly_Report_September.docx"),
]

# old logo extent (EMU), present twice per header (wp:extent and the shape's a:xfrm/a:ext)
OLD_EXTENT = 'cx="1733550" cy="742950"'
# new logo is 694x533 (aspect 1.302), sized to fit the header space the old logo already used
NEW_EXTENT = 'cx="1130910" cy="868680"'

XML_PARTS_TO_PATCH = [
    "word/document.xml",
    "word/styles.xml",
    "word/theme/theme1.xml",
    "word/header1.xml",
    "word/footer1.xml",
]

# (find, replace) pairs applied to every XML part above, in order.
# Fills (large backgrounds) map to black; text/border accents map to cobalt;
# unifying the navy stat-number color into the same single cobalt accent.
COLOR_SUBSTITUTIONS = [
    ('w:fill="DC1E25"', 'w:fill="0A0A0A"'),   # red table-header fill -> black
    ('w:fill="333333"', 'w:fill="0A0A0A"'),   # dark-gray table-header fill -> black
    ('w:color w:val="DC1E25"', 'w:color w:val="1B4FA0"'),  # red text -> cobalt
    ('w:color="DC1E25"', 'w:color="1B4FA0"'),               # red border -> cobalt
    ('w:color w:val="002451"', 'w:color w:val="1B4FA0"'),  # navy text -> cobalt
    ('w:color="002451"', 'w:color="1B4FA0"'),               # navy border -> cobalt
]

FONT_SUBSTITUTIONS = [
    ("Aptos Display", "Bookman Old Style"),  # theme majorFont (headings) -- do first (longer match)
    ("Aptos", "Calibri"),                     # theme minorFont + styles.xml Normal style (body)
]


def process(src_path, out_name):
    out_path = os.path.join(HERE, out_name)
    with zipfile.ZipFile(src_path, "r") as zin:
        names = zin.namelist()
        with zipfile.ZipFile(out_path, "w", zipfile.ZIP_DEFLATED) as zout:
            for name in names:
                data = zin.read(name)
                if name == "word/media/image1.png":
                    with open(LOGO_PATH, "rb") as f:
                        data = f.read()
                elif name in XML_PARTS_TO_PATCH:
                    text = data.decode("utf-8")
                    for find, repl in COLOR_SUBSTITUTIONS:
                        text = text.replace(find, repl)
                    for find, repl in FONT_SUBSTITUTIONS:
                        text = text.replace(find, repl)
                    if name == "word/header1.xml":
                        text = text.replace(OLD_EXTENT, NEW_EXTENT)
                    data = text.encode("utf-8")
                zout.writestr(name, data)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    for src, out_name in SOURCES:
        process(src, out_name)
