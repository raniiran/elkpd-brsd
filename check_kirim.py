import json, re

def find_kirim_objects(filename):
    with open(filename, "r") as f:
        content = f.read()
    
    # The rlprez.js has var AP = {...};
    # It's technically JS, but the object is JSON-like. 
    # Actually, the quickest way is to find "Kirim" and look at its surrounding object.
    matches = list(re.finditer(r'\{[^\{\}]*?>Kirim</p>[^\{\}]*?\}', content))
    if not matches:
        # maybe it's inside a larger object
        matches = list(re.finditer(r'\{[^{]*?Kirim[^{]*?\}', content))
        
    print(f"--- {filename} ---")
    for m in matches:
        print(m.group(0)[:200] + "...")

for fname in ["rlprez.js", "latsol2/rlprez.js", "latsol3/rlprez.js", "latsol4/rlprez.js", "latsol5/rlprez.js"]:
    find_kirim_objects(fname)
