"""
Add Valletta branding (header logo, footer, cobalt/black accent colors,
Bookman Old Style / Calibri typography) to five previously-unbranded Door
Security training documents. No text content is touched anywhere: every
substitution targets only XML attribute values (hex colors, a font-family
name) or adds wholly new structural parts (header/footer/relationships/
content-type declarations) -- it never rewrites a <w:t> text node, and the
new header/footer parts carry only the Valletta identity (logo, title,
page number), not any paraphrase of the document's own content.

Run with: python3 -I rebrand_door_security.py
"""
import zipfile
import os

HERE = os.path.dirname(os.path.abspath(__file__))
LOGO_PATH = os.path.join(HERE, "valletta-soc-lockup.png")
with open(LOGO_PATH, "rb") as f:
    LOGO_BYTES = f.read()

COURSE_TITLE = "Door Security Verification & Alarm Response"

SOURCES = [
    ("/root/.claude/uploads/740649a2-a5a9-5a9b-a94a-a0a642982174/1251bf7f-Door_Security_Curriculum_1.docx",
     "valletta_Door_Security_Curriculum.docx", "curriculum", f"{COURSE_TITLE} – Course Curriculum"),
    ("/root/.claude/uploads/740649a2-a5a9-5a9b-a94a-a0a642982174/288700f7-DoorSecurity_Module1_Training_Video_Transcript_1.docx",
     "valletta_DoorSecurity_Module1_Training_Video_Transcript.docx", "transcript", f"{COURSE_TITLE} – Module 1 of 4"),
    ("/root/.claude/uploads/740649a2-a5a9-5a9b-a94a-a0a642982174/8d26d1bc-DoorSecurity_Module2_Training_Video_Transcript_1.docx",
     "valletta_DoorSecurity_Module2_Training_Video_Transcript.docx", "transcript", f"{COURSE_TITLE} – Module 2 of 4"),
    ("/root/.claude/uploads/740649a2-a5a9-5a9b-a94a-a0a642982174/3e16e61b-DoorSecurity_Module3_Training_Video_Transcript_1.docx",
     "valletta_DoorSecurity_Module3_Training_Video_Transcript.docx", "transcript", f"{COURSE_TITLE} – Module 3 of 4"),
    ("/root/.claude/uploads/740649a2-a5a9-5a9b-a94a-a0a642982174/4e62dadc-DoorSecurity_Module4_Training_Video_Transcript_1.docx",
     "valletta_DoorSecurity_Module4_Training_Video_Transcript.docx", "transcript", f"{COURSE_TITLE} – Module 4 of 4"),
]

COBALT = "1B4FA0"
BLACK = "0A0A0A"

# (find, replace) pairs for document.xml -- only the curriculum doc has any
# direct color/font overrides in its body; the four transcripts are entirely
# style-driven (verified: zero w:color/w:fill/border-color hits in their XML).
CURRICULUM_DOC_SUBSTITUTIONS = [
    ('w:fill="2b2d6e"', f'w:fill="{BLACK}"'),            # table header row fill -> black
    ('w:color w:val="2b2d6e"', f'w:color w:val="{COBALT}"'),  # direct title color override -> cobalt
    ('w:color="00b8d9"', f'w:color="{COBALT}"'),          # subtitle underline rule -> cobalt
    ('w:ascii="Arial"', 'w:ascii="Calibri"'),
    ('w:hAnsi="Arial"', 'w:hAnsi="Calibri"'),
    ('w:cs="Arial"', 'w:cs="Calibri"'),
    ('w:eastAsia="Arial"', 'w:eastAsia="Calibri"'),
    ('w:ascii="Arial Unicode MS"', 'w:ascii="Calibri"'),
    ('w:hAnsi="Arial Unicode MS"', 'w:hAnsi="Calibri"'),
    ('w:cs="Arial Unicode MS"', 'w:cs="Calibri"'),
    ('w:eastAsia="Arial Unicode MS"', 'w:eastAsia="Calibri"'),
]

# styles.xml substitutions, by doc kind
CURRICULUM_STYLES_SUBSTITUTIONS = [
    ('w:color w:val="2b2d6e"', f'w:color w:val="{COBALT}"'),  # Title/Heading1/Heading2
    ('w:color w:val="1f4d78"', f'w:color w:val="{COBALT}"'),  # Heading3
    ('w:color w:val="2e74b5"', f'w:color w:val="{COBALT}"'),  # Heading4/Heading5, unused styles, updated for consistency
    ('w:ascii="Arial"', 'w:ascii="Bookman Old Style"'),
    ('w:hAnsi="Arial"', 'w:hAnsi="Bookman Old Style"'),
    ('w:cs="Arial"', 'w:cs="Bookman Old Style"'),
    ('w:eastAsia="Arial"', 'w:eastAsia="Bookman Old Style"'),
    ('w:ascii="Georgia"', 'w:ascii="Bookman Old Style"'),   # unused Subtitle style, updated for consistency
    ('w:hAnsi="Georgia"', 'w:hAnsi="Bookman Old Style"'),
    ('w:cs="Georgia"', 'w:cs="Bookman Old Style"'),
    ('w:eastAsia="Georgia"', 'w:eastAsia="Bookman Old Style"'),
]
# docDefaults body font (literal override) -> Calibri; done as a targeted
# replace of the exact docDefaults block seen in the curriculum file.
CURRICULUM_DOCDEFAULTS_FIND = '<w:rPrDefault><w:rPr><w:rFonts w:ascii="Arial" w:cs="Arial" w:eastAsia="Arial" w:hAnsi="Arial"/>'
CURRICULUM_DOCDEFAULTS_REPLACE = '<w:rPrDefault><w:rPr><w:rFonts w:ascii="Calibri" w:cs="Calibri" w:eastAsia="Calibri" w:hAnsi="Calibri"/>'

TRANSCRIPT_STYLES_SUBSTITUTIONS = [
    ('w:color w:val="000000"', f'w:color w:val="{COBALT}"'),  # Title style (defined, unused in body, updated for consistency)
    ('w:color w:val="2e74b5"', f'w:color w:val="{COBALT}"'),  # Heading1/Heading2
    ('w:color w:val="1f4d78"', f'w:color w:val="{COBALT}"'),  # Heading3
    ('w:ascii="Times New Roman"', 'w:ascii="Bookman Old Style"'),
    ('w:hAnsi="Times New Roman"', 'w:hAnsi="Bookman Old Style"'),
    ('w:cs="Times New Roman"', 'w:cs="Bookman Old Style"'),
    ('w:eastAsia="Times New Roman"', 'w:eastAsia="Bookman Old Style"'),
    ('w:ascii="Georgia"', 'w:ascii="Bookman Old Style"'),  # unused Subtitle style, updated for consistency
    ('w:hAnsi="Georgia"', 'w:hAnsi="Bookman Old Style"'),
    ('w:cs="Georgia"', 'w:cs="Bookman Old Style"'),
    ('w:eastAsia="Georgia"', 'w:eastAsia="Bookman Old Style"'),
]

TRANSCRIPT_THEME_SUBSTITUTIONS = [
    ('<a:minorFont><a:latin typeface="Cambria"', '<a:minorFont><a:latin typeface="Calibri"'),
]

# ============================================================
# new header1.xml / footer1.xml (built fresh -- none existed before)
# ============================================================
NS_DECLS = (
    'xmlns:wpc="http://schemas.microsoft.com/office/word/2010/wordprocessingCanvas" '
    'xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006" '
    'xmlns:o="urn:schemas-microsoft-com:office:office" '
    'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" '
    'xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math" '
    'xmlns:v="urn:schemas-microsoft-com:vml" '
    'xmlns:wp14="http://schemas.microsoft.com/office/word/2010/wordprocessingDrawing" '
    'xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing" '
    'xmlns:w10="urn:schemas-microsoft-com:office:word" '
    'xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" '
    'xmlns:w14="http://schemas.microsoft.com/office/word/2010/wordml" '
    'xmlns:wne="http://schemas.microsoft.com/office/word/2006/wordml" '
    'xmlns:wps="http://schemas.microsoft.com/office/word/2010/wordprocessingShape" '
    'mc:Ignorable="w14"'
)

HEADER_XML = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:hdr {NS_DECLS}><w:p><w:pPr><w:spacing w:line="240" w:lineRule="auto"/></w:pPr><w:r><w:rPr><w:noProof/></w:rPr><w:drawing><wp:inline distT="0" distB="0" distL="0" distR="0"><wp:extent cx="1130910" cy="868680"/><wp:effectExtent l="0" t="0" r="0" b="0"/><wp:docPr id="1" name="Logo" descr="Valletta Industries logo" title="Valletta Industries logo"/><wp:cNvGraphicFramePr><a:graphicFrameLocks xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" noChangeAspect="1"/></wp:cNvGraphicFramePr><a:graphic xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"><a:graphicData uri="http://schemas.openxmlformats.org/drawingml/2006/picture"><pic:pic xmlns:pic="http://schemas.openxmlformats.org/drawingml/2006/picture"><pic:nvPicPr><pic:cNvPr id="0" name=""/><pic:cNvPicPr><a:picLocks noChangeAspect="1" noChangeArrowheads="1"/></pic:cNvPicPr></pic:nvPicPr><pic:blipFill><a:blip r:embed="rId1"/><a:srcRect/><a:stretch><a:fillRect/></a:stretch></pic:blipFill><pic:spPr bwMode="auto"><a:xfrm><a:off x="0" y="0"/><a:ext cx="1130910" cy="868680"/></a:xfrm><a:prstGeom prst="rect"><a:avLst/></a:prstGeom></pic:spPr></pic:pic></a:graphicData></a:graphic></wp:inline></w:drawing></w:r></w:p><w:p><w:pPr><w:pBdr><w:bottom w:val="single" w:sz="12" w:space="1" w:color="{COBALT}"/></w:pBdr><w:spacing w:before="120" w:line="120" w:lineRule="exact"/></w:pPr></w:p></w:hdr>'''

HEADER_RELS_XML = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" Target="media/image1.png"/></Relationships>'''


def footer_xml(doc_tag):
    # "Valletta Industries  |  <doc_tag>  |  Page X of Y"
    return f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:ftr {NS_DECLS}><w:p><w:pPr><w:pStyle w:val="Footer"/><w:jc w:val="center"/></w:pPr><w:r><w:rPr><w:color w:val="646464"/><w:sz w:val="16"/></w:rPr><w:t xml:space="preserve">Valletta Industries  |  {doc_tag}  |  Page </w:t></w:r><w:r><w:rPr><w:color w:val="646464"/><w:sz w:val="16"/></w:rPr><w:fldChar w:fldCharType="begin"/></w:r><w:r><w:rPr><w:color w:val="646464"/><w:sz w:val="16"/></w:rPr><w:instrText>PAGE</w:instrText></w:r><w:r><w:rPr><w:color w:val="646464"/><w:sz w:val="16"/></w:rPr><w:fldChar w:fldCharType="separate"/></w:r><w:r><w:rPr><w:color w:val="646464"/><w:sz w:val="16"/><w:noProof/></w:rPr><w:t>1</w:t></w:r><w:r><w:rPr><w:color w:val="646464"/><w:sz w:val="16"/></w:rPr><w:fldChar w:fldCharType="end"/></w:r><w:r><w:rPr><w:color w:val="646464"/><w:sz w:val="16"/></w:rPr><w:t xml:space="preserve"> of </w:t></w:r><w:r><w:rPr><w:color w:val="646464"/><w:sz w:val="16"/></w:rPr><w:fldChar w:fldCharType="begin"/></w:r><w:r><w:rPr><w:color w:val="646464"/><w:sz w:val="16"/></w:rPr><w:instrText>NUMPAGES</w:instrText></w:r><w:r><w:rPr><w:color w:val="646464"/><w:sz w:val="16"/></w:rPr><w:fldChar w:fldCharType="separate"/></w:r><w:r><w:rPr><w:color w:val="646464"/><w:sz w:val="16"/><w:noProof/></w:rPr><w:t>1</w:t></w:r><w:r><w:rPr><w:color w:val="646464"/><w:sz w:val="16"/></w:rPr><w:fldChar w:fldCharType="end"/></w:r></w:p></w:ftr>'''


CT_ADDITIONS = (
    '<Default ContentType="image/png" Extension="png"/>'
    '<Override ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.header+xml" PartName="/word/header1.xml"/>'
    '<Override ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.footer+xml" PartName="/word/footer1.xml"/>'
)

RELS_ADDITIONS = (
    '<Relationship Id="rId6" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/header" Target="header1.xml"/>'
    '<Relationship Id="rId7" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/footer" Target="footer1.xml"/>'
)

SECTPR_REFS = '<w:headerReference w:type="default" r:id="rId6"/><w:footerReference w:type="default" r:id="rId7"/>'


def process(src_path, out_name, kind, doc_tag):
    out_path = os.path.join(HERE, out_name)
    with zipfile.ZipFile(src_path, "r") as zin:
        names = zin.namelist()
        parts = {name: zin.read(name) for name in names}

    # --- document.xml: sectPr header/footer refs + (curriculum only) color/font fixes ---
    doc_xml = parts["word/document.xml"].decode("utf-8")
    assert "<w:sectPr>" in doc_xml, "unexpected sectPr shape"
    doc_xml = doc_xml.replace("<w:sectPr>", f"<w:sectPr>{SECTPR_REFS}", 1)
    if kind == "curriculum":
        for find, repl in CURRICULUM_DOC_SUBSTITUTIONS:
            doc_xml = doc_xml.replace(find, repl)
    parts["word/document.xml"] = doc_xml.encode("utf-8")

    # --- styles.xml ---
    styles_xml = parts["word/styles.xml"].decode("utf-8")
    if kind == "curriculum":
        assert CURRICULUM_DOCDEFAULTS_FIND in styles_xml, "docDefaults shape changed"
        styles_xml = styles_xml.replace(CURRICULUM_DOCDEFAULTS_FIND, CURRICULUM_DOCDEFAULTS_REPLACE)
        for find, repl in CURRICULUM_STYLES_SUBSTITUTIONS:
            styles_xml = styles_xml.replace(find, repl)
    else:
        for find, repl in TRANSCRIPT_STYLES_SUBSTITUTIONS:
            styles_xml = styles_xml.replace(find, repl)
    parts["word/styles.xml"] = styles_xml.encode("utf-8")

    # --- theme1.xml (transcripts only: body font cascades from minorFont) ---
    if kind == "transcript":
        theme_xml = parts["word/theme/theme1.xml"].decode("utf-8")
        for find, repl in TRANSCRIPT_THEME_SUBSTITUTIONS:
            assert find in theme_xml, f"theme substitution not found: {find}"
            theme_xml = theme_xml.replace(find, repl)
        parts["word/theme/theme1.xml"] = theme_xml.encode("utf-8")

    # --- Content_Types.xml ---
    ct_xml = parts["[Content_Types].xml"].decode("utf-8")
    assert "</Types>" in ct_xml
    ct_xml = ct_xml.replace("</Types>", CT_ADDITIONS + "</Types>")
    parts["[Content_Types].xml"] = ct_xml.encode("utf-8")

    # --- document.xml.rels ---
    rels_xml = parts["word/_rels/document.xml.rels"].decode("utf-8")
    assert "</Relationships>" in rels_xml
    rels_xml = rels_xml.replace("</Relationships>", RELS_ADDITIONS + "</Relationships>")
    parts["word/_rels/document.xml.rels"] = rels_xml.encode("utf-8")

    # --- new parts: header1.xml, footer1.xml, header1.xml.rels, logo image ---
    parts["word/header1.xml"] = HEADER_XML.encode("utf-8")
    parts["word/footer1.xml"] = footer_xml(doc_tag).encode("utf-8")
    parts["word/_rels/header1.xml.rels"] = HEADER_RELS_XML.encode("utf-8")
    parts["word/media/image1.png"] = LOGO_BYTES

    with zipfile.ZipFile(out_path, "w", zipfile.ZIP_DEFLATED) as zout:
        for name, data in parts.items():
            zout.writestr(name, data)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    for src, out_name, kind, doc_tag in SOURCES:
        process(src, out_name, kind, doc_tag)
