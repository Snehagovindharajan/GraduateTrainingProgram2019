class ImageFormatException(Exception):
    def __init__(self,e):
        print("Invalid File")


class ReadFile:
    def __init__(self, file_name):
        self.file_name = file_name

    def fileformat(self):
        try:
            split_file = self.file_name.split(".")
            file_format = split_file[1]
            if file_format in ['jpeg', 'jpg', 'gif', 'png', 'psd']:
                raise ImageFormatException("ImageFormatException occured")
        except ImageFormatException as e:
            print(e)
        else:
            print("File Accepted")


file = input("Enter the file name")
file_obj = ReadFile(file)
file_obj.fileformat()
