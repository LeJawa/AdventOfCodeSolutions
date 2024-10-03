import shutil

shutil.make_archive("./answers", "zip", "./answers")
shutil.unpack_archive("./answers.zip", ".", "zip")