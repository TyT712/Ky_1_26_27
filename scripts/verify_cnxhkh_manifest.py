import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

manifest_path = "docs/data/courses_manifest.json"
with open(manifest_path, "r", encoding="utf-8") as f:
    manifest = json.load(f)

cnxhkh = next(c for c in manifest["courses"] if c["id"] == "cnxhkh")
print("Found course:", cnxhkh["title"])
print("Books count:", len(cnxhkh["books"]))

for b in cnxhkh["books"]:
    print(f"Book: {b['title']}")
    for ch in b["chapters"]:
        tf = os.path.join("docs", ch["theory"])
        ef = os.path.join("docs", ch["exercises"])
        assert os.path.exists(tf), f"Missing theory file: {tf}"
        assert os.path.exists(ef), f"Missing exercises file: {ef}"
        with open(ef, "r", encoding="utf-8") as f:
            edata = json.load(f)
            assert len(edata["multiple_choice"]) == ch["counts"]["multiple_choice"]
            assert len(edata["short_answers"]) == ch["counts"]["short_answers"]
            assert len(edata["essays"]) == ch["counts"]["essays"]
        print(f"  OK [Chương {ch['number']}]: {ch['title']} -> {ch['counts']}")

for tp in cnxhkh["topics"]:
    tpf = os.path.join("docs", tp["file"])
    assert os.path.exists(tpf), f"Missing topic file: {tpf}"
    print(f"  OK Topic: {tp['title']} -> {tp['file']}")

print("\nALL MANIFEST ASSETS AND REFERENCES VERIFIED PERFECTLY!")
