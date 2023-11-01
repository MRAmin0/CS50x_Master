l = {
    "gif": "image/gif",
    "jpg": "image/jpg",
    "jpeg": "image/jpeg",
    "png": "image/png",
    "pdf": "application/pdf",
    "txt": "text/plain",
    "zip": "application/zip",
}

a = input("File name: ").strip().lower()

if a.rfind(".") != -1:
    index = int(a.rindex(".")) + 1
    b = a[index:]
    print(b)
