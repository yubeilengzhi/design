from beifen import *
import time

if __name__ == '__main__':
    # 原目录
    src_dir = "E:\\bishe_test\\src"
    # 目标目录
    dst_dir = "E:\\bishe_test\\dest"
    # 校验文件
    md5file = "E:\\bishe_test\\dest\\md5.data"
    # 判断进行哪种备份操作
    if time.strftime("%a") == "Monday":
        # 周一完全备份
        full_backup(src_dir, dst_dir, md5file)
    else:
        # 其他工作日 增量备份
        inc_back_up(src_dir, dst_dir, md5file)
