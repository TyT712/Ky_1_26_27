import glob
import sys
import os

sys.path.insert(0, os.path.abspath("."))
from src.skills.chapter_study_pack_generator import ChapterStudyPackValidator

files = sorted(glob.glob('docs/courses/he_qtcsdl/*.md'))
print(f"Total study pack files: {len(files)}")
all_valid = True
for f in files:
    res = ChapterStudyPackValidator.validate_file(f)
    print(f"{res['file']}: valid={res['valid']}, mcq={res['mcq_count']}, essay={res['essay_count']}, details={res['details_count']}, even_ticks={res['even_ticks']}, chars={res['size_chars']}")
    if not res['valid']:
        all_valid = False

print(f"\nAll 11 files compliant with 4-part standard: {all_valid}")
if not all_valid:
    sys.exit(1)
