def main():
    file_name = input("File name: ").lower().strip()

    ext = extension(file_name)

    match ext:
        case "gif" | "jpg" | "jpeg" | "png":
            print("image/" + ext)
        case "pdf" | "txt" | "zip":
            print("application/" + ext)
        case _:
            print("application/octet-stream")


def extension(filename):
    dot_index = filename.find(".")

    if dot_index != -1:
        return filename[dot_index + 1 :]
    else:
        return


main()
