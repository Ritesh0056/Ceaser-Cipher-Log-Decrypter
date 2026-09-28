# Caesar Cipher Log Decryptor
# Reads raw_logs.txt, decrypts each line (left shift of 3), writes all lines
# to decrypted_master.txt and any line containing "BREACH" to security_alerts.txt.

# Task 1: open the input file and both output files at the same time
infile = open("raw_logs.txt", "r")
master = open("decrypted_master.txt", "w")
alerts = open("security_alerts.txt", "w")

# Task 2: decrypt each line character by character
for line in infile:
    decrypted = ""
    for ch in line:
        if ch >= "A" and ch <= "Z":
            # uppercase letter: shift left by 3 with wrap-around (A -> X)
            decrypted = decrypted + chr((ord(ch) - ord("A") - 3) % 26 + ord("A"))
        elif ch >= "a" and ch <= "z":
            # lowercase letter: shift left by 3 with wrap-around (a -> x)
            decrypted = decrypted + chr((ord(ch) - ord("a") - 3) % 26 + ord("a"))
        else:
            # spaces, digits, punctuation and newlines are kept unchanged
            decrypted = decrypted + ch

    # Task 3: strip whitespace, write to master file
    decrypted = decrypted.strip()
    if decrypted != "":
        master.write(decrypted + "\n")

        # case-insensitive check for the keyword BREACH
        if "BREACH" in decrypted.upper():
            alerts.write(decrypted + "\n")

# close all files so the data is saved
infile.close()
master.close()
alerts.close()

print("Decryption complete.")
print("All decrypted lines saved to decrypted_master.txt")
print("Breach alerts saved to security_alerts.txt")