import os
import json
import sys

# Configure UTF-8 for console output
sys.stdout.reconfigure(encoding='utf-8')

# Add scripts directory to path
sys.path.insert(0, os.path.abspath("scripts"))

from chapter_data_cnxhkh import cnxhkh_ch1
from chapter_data_cnxhkh import cnxhkh_ch2
from chapter_data_cnxhkh import cnxhkh_ch3
from chapter_data_cnxhkh import cnxhkh_ch4
from chapter_data_cnxhkh import cnxhkh_ch5
from chapter_data_cnxhkh import cnxhkh_ch6
from chapter_data_cnxhkh import cnxhkh_ch7

chapters = [
    cnxhkh_ch1.DATA,
    cnxhkh_ch2.DATA,
    cnxhkh_ch3.DATA,
    cnxhkh_ch4.DATA,
    cnxhkh_ch5.DATA,
    cnxhkh_ch6.DATA,
    cnxhkh_ch7.DATA
]

out_dir = os.path.join("docs", "data", "cnxhkh")
os.makedirs(out_dir, exist_ok=True)

total_mcq = 0
total_short = 0
total_essay = 0

for ch in chapters:
    cid = ch["chapter_id"]
    mcq = ch.get("multiple_choice", [])
    short = ch.get("short_answers", [])
    essay = ch.get("essays", [])
    
    print(f"\n--- Checking {cid}: {ch.get('chapter_title')} ---")
    print(f"MCQ count: {len(mcq)}")
    print(f"Short answers count: {len(short)}")
    print(f"Essays count: {len(essay)}")
    
    assert len(mcq) == 30, f"{cid} must have 30 MCQs, got {len(mcq)}"
    assert len(short) == 8, f"{cid} must have 8 Short Answers, got {len(short)}"
    assert len(essay) == 4, f"{cid} must have 4 Essays, got {len(essay)}"
    
    for q in mcq:
        assert q["correct_answer"] in ["A", "B", "C", "D"], f"Invalid answer in {cid} q {q['id']}"
        assert set(q["options"].keys()) == {"A", "B", "C", "D"}, f"Invalid options in {cid} q {q['id']}"
        assert len(q["explanation"]) > 10, f"Explanation too short in {cid} q {q['id']}"
        
    for sa in short:
        assert len(sa["expected_answer"]) > 10, f"Expected answer too short in {cid} sa {sa['id']}"
        
    for es in essay:
        assert len(es["solution_steps"]) >= 2, f"Essay solution steps too short in {cid} es {es['id']}"
        
    out_file = os.path.join(out_dir, f"{cid}_exercises.json")
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(ch, f, ensure_ascii=False, indent=1)
        
    print(f"Successfully generated {out_file} ({os.path.getsize(out_file)} bytes)")
    total_mcq += len(mcq)
    total_short += len(short)
    total_essay += len(essay)

print(f"\n==========================================")
print(f"ALL 7 CHAPTERS COMPILED AND VERIFIED!")
print(f"Total Multiple Choice Questions: {total_mcq}")
print(f"Total Short Answer Questions:    {total_short}")
print(f"Total Essay Questions:           {total_essay}")
print(f"==========================================")
