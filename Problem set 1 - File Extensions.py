file_name = input("File name: ")

corrected_file_name = file_name.strip().lower()

if corrected_file_name.endswith(".gif"):
    print("image/gif")

elif corrected_file_name.endswith(".jpg"):
    print("image/jpeg")

elif corrected_file_name.endswith(".jpeg"):
    print("image/jpeg")

elif corrected_file_name.endswith(".png"):
    print("image/png")

elif corrected_file_name.endswith(".pdf"):
    print("application/pdf")

elif corrected_file_name.endswith(".txt"):
    print("text/plain")

elif corrected_file_name.endswith(".zip"):
    print("application/zip")

else:
    print("application/octet-stream")