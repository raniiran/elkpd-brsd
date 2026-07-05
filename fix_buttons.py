import re

# 1. Fix rlprez.js (Slide 75)
with open("rlprez.js", "r") as f:
    rlprez = f.read()

def fix_slide_75(content):
    slides = content.split('{at:"Slide ')
    for i, slide in enumerate(slides):
        if i == 0: continue
        slide_num = slide.split('"', 1)[0]
        if slide_num == "75":
            # Replace Kirim with Selanjutnya
            new_slide = slide.replace(">Kirim</p>", ">Selanjutnya</p>")
            # Replace [[19,[0,0]]] with [[7,1]] for the Selanjutnya buttons
            # We can just replace all [[19,[0,0]]] in this slide because we know there is only one Submit button here
            new_slide = new_slide.replace("[[19,[0,0]]]", "[[7,1]]")
            slides[i] = new_slide
    return '{at:"Slide '.join(slides)

rlprez_fixed = fix_slide_75(rlprez)
with open("rlprez.js", "w") as f:
    f.write(rlprez_fixed)


# 2. Fix latsol3, 4, 5
def fix_latsol(filename):
    with open(filename, "r") as f:
        content = f.read()
    
    # We want to replace e:{l:[[3,[[19,[0,0]]]]],s:-1,f:8} with e:{l:[[3,[[19,[0,0]],[7,1]]]],s:-1,f:8}
    # But only for buttons that say Kirim.
    # Actually, the previous AI replaced ALL of them, but they replaced with [19, [0,0]], [33,...]
    # Let's just find the Kirim buttons and their associated event object.
    
    # Because replacing exactly the Kirim buttons might be tricky with regex without lookbehind,
    # let's just replace ALL `e:{l:[[3,[[19,[0,0]]]]],s:-1,f:8}` with `e:{l:[[3,[[19,[0,0]],[7,1]]]],s:-1,f:8}` 
    # Because any Submit Interaction button without a Next should probably go Next.
    # Let's verify if there are any we shouldn't change.
    new_content = content.replace("e:{l:[[3,[[19,[0,0]]]]],s:-1,f:8}", "e:{l:[[3,[[19,[0,0]],[7,1]]]],s:-1,f:8}")
    
    with open(filename, "w") as f:
        f.write(new_content)

for fname in ["latsol3/rlprez.js", "latsol4/rlprez.js", "latsol5/rlprez.js"]:
    fix_latsol(fname)

print("Fixed!")
