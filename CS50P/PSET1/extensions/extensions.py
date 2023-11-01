l = {
    "gif": "image/gif",
    "jpg": "image/jpeg",
    "jpeg": "image/jpeg",
    "png": "image/png",
    "pdf": "application/pdf",
    "txt": "text/plain",
    "zip": "application/zip",
}

a = input("File name: ").strip().lower()

# The rfind() method finds the last occurrence of the specified value
if a.rfind(".") != -1:
    index = int(a.rindex(".")) + 1
    b = a[index:]
    # print(b)
    if b in l:

        print(l[b])
    elif b =="" or b not in l:
        print("application/octet-stream")
