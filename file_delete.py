import os

os.removedirs("myfolder")  # os rmdir functionality 只有當資料夾為空時才能刪除
os.remove("myfile.html")  # os unlink functionality

# 1. os.wlak() 邊歷邊刪除
# 2. shutil.rmtree() 刪除整個資料夾
