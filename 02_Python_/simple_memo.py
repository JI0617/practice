
file_name = input("저장할 파일명을 입력해주세요:") + ".txt"
print(f"파일명 : {file_name}","\n" f"{file_name}에 저장합니다.")
print("""
======================
저장할 내용을 입력하세요
======================
""")
with open(f"{file_name}", "wt", encoding="utf-8") as fw:
    while True:
        txt = input("> ")
        if txt == "!q" :
            break
        fw.write(txt+"\n")
