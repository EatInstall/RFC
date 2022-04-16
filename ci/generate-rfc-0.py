def main():
  import os, glob
  rfcs = []
  
  print(f"::warning::Current working directory is {os.getcwd()}. All RFCs must be stored in there.")
  
  print("Looking up RFCs...")

  for i in glob.glob(f"{os.getcwd()}/rfc-*.md"):
    rfcs.append(i)
  print("Added all rfcs.")
  print("Generating RFC 0...")
  with open(f"{os.getcwd()}/rfc-0.md", "a") as f:
   for i in rfcs:
    f.write(f"\n* {i}")

if __name__ == "__main__":
  main()
