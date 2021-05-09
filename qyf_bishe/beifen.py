"""
实现数据的完全备份和差量备份
"""

import time,os,hashlib,sys,zipfile
import pickle as p


# 定义函数，用来遍历检验目录中的文件
def walkdir(folder,md5file):
    # 字典保存文件的 md5值
    md5_dict = {}
    if os.path.exists(folder):
        # os.walk()遍历目录
        # 返回元组：目录路径，子目录名，子文件名
        contents = os.walk(folder)
        for path,folders,files in contents:
            #对目录中的文件进行 md5 校验
            for fname in files:
                # os.path.join() 把目录和文件名合成一个路径
                full_path = os.path.join(path,fname)
                md5_dict[full_path] = md5check(full_path)
        # 以二进制可写方式打开 md5 file文件
        with open(md5file,'wb') as fobj:
            # pickle 模块中的dump（）方法将对象写入到文件中
            p.dump(md5_dict,fobj)
    else:
        print("指定的目录不存在！")


def md5check(fname):
    """
    检验文件md5值
    :param fname:
    :return:
    """

    if os.path.isfile(fname):
        # 生成一个 md5 的 hash对象
        m = hashlib.md5()
        with open(fname) as fobj:
            while True:
                data = fobj.read(4096)
                if not data:
                    break
                # 更新加密
                m.update(data.encode(encoding="utf-8"))
        return m.hexdigest()
    else:
        print("校验的文件不存在！")


def full_backup(src_dir,dst_dir,md5file):
    """
    完全备份
    :param src_dir:
    :param dst_dir:
    :param md5file:
    :return:
    """
    # os.path.split()方法拆分字符串，返回列表
    par_dir,base_dir = os.path.split(src_dir.rstrip("/"))
    # 备份的文件名
    back_name = "%s_full_%s.zip"%(base_dir,time.strftime("%Y%m%d"))
    # 完整备份路径
    full_name = os.path.join(dst_dir,back_name)
    # 文件校验
    walkdir(src_dir)
    # 切换到par_dir目录
    os.chdir(par_dir)
    # 文件打包
    z = zipfile.ZipFile(full_name,"w")
    z.write(base_dir,full_name,zipfile.ZIP_DEFLATED)
    z.close()


def inc_back_up(src_dir,dst_dir,md5file):
    """
    增量备份
    :param src_dir:
    :param dst_dir:
    :param md5file:
    :return:
    """
    if os.path.exists(md5file):
        par_dir,base_dir = os.path.split(src_dir.rstrip("/"))
        back_name = "%s_inc_%s.zip"%(base_dir,time.strftime("%Y%m%d"))
        # 增量备份路径
        full_name = os.path.join(dst_dir,back_name)
        # 字典保存md5值
        md5new = {}
        # 判断目录是否存在
        if os.path.exists(src_dir):
            # 返回目录路径，子目录名，自文件名
            contents = os.walk(src_dir)
            for path,folders,files in contents:
                for fname in files:
                    full_path = os.path.join(path,fname)
                    md5new[full_path] = md5check(full_path)
            with open(md5file,"rb") as fobj:
                try:
                    md5old = p.load(fobj)
                except EOFError:
                    pass
            with open(md5file,"wb") as fobj:
                p.dump(md5new,fobj)
            os.chdir(par_dir)
            # 文件打包
            z = zipfile.ZipFile(full_name,"a")
            # 校验md5值
            for key in md5new:
                # 两次md5值不一致时，说明文件被修改过
                if md5old.get(key) != md5new[key]:
                    z.write(base_dir,full_name,zipfile.ZIP_DEFLATED)
            z.close()
        else:
            print("指定的目录不存在")
    else:
        # 校验文件不存在，说明没有进行过完全备份
        full_backup(src_dir,dst_dir,md5file)










