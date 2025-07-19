file_extension = input("File name: ").lower().strip()

if file_extension.endswith(".gif"):
    print("image/gif")
elif file_extension.endswith(".jpg"):
    print("image/jpeg")
elif file_extension.endswith(".jpeg"):
    print("image/jpeg")
elif file_extension.endswith(".png"):
    print("image/png")
elif file_extension.endswith("pdf"):
    print("application/pdf")
elif file_extension.endswith(".zip"):
    print("application/zip")
elif file_extension.endswith(".txt"):
    print("text/plain")
else:
    print("application/octet-stream")
