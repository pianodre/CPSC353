# Step 4) File Reading — Read requested file content
# Paste these lines where your skeleton shows:
#   outputdata = #Fill in start ...
#   ...
#   #Fill in end
#
# Assumes `filename` is a path beginning with '/' (e.g., '/index.html').

with open(filename[1:], 'r', encoding='utf-8', errors='replace') as f:
    outputdata = f.read()
