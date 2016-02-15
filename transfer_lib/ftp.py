# -*- coding: utf-8 -*-
import sftp
import stat
from ftplib import FTP
from ftplib import FTP_TLS


class FtpLibWrapper(object):
    def __init__(self, host, user, password, is_pasv=True, is_ssl=False):
        if is_ssl:
            self.__ftp = FTP_TLS(host, user, password)
            self.__ftp.prot_p()
        else:
            self.__ftp = FTP(host, user, password)
            self.__ftp.set_pasv(is_pasv)

    def get_file_list(self):
        return self.__ftp.nlst()

    def chg_dir(self, path):
        self.__ftp.cwd(path)

    def make_dir(self, dir_name):
        if self.__is_dir(dir_name) is False:
            self.__ftp.mkd(dir_name)

    def get_file(self, server_file_name, local_file_name):
        self.__ftp.retrbinary('RETR ' + server_file_name, open(local_file_name, 'wb').write)

    def delete_file(self, server_file_name):
        if self.__is_dir(server_file_name):
            current = self.__ftp.pwd()
            self.__inner_delete_file(current + '/' + server_file_name)
            self.chg_dir(current)
            self.__ftp.rmd(server_file_name)
        else:
            self.__ftp.delete(server_file_name)

    def __inner_delete_file(self, current):
        self.chg_dir(current)
        for file_name in self.get_file_list():
            self.delete_file(file_name)

    def __get_detail_file_inf_list(self):
        file_info_list = []
        self.__ftp.retrlines('LIST', file_info_list.append)
        return file_info_list

    def __is_dir(self, file_name):
        file_info_list = self.__get_detail_file_inf_list()
        for file_info in file_info_list:
            tmp_file_name = file_info.split(' ')[-1]
            if file_name != tmp_file_name:
                continue
            if file_info.split(' ')[0][0] == 'd':
                return True
            break
        return False

    def upload_file(self, server_file_name, local_file_name):
        self.__ftp.storbinary('STOR ' + server_file_name, open(local_file_name, 'rb'))

    def rename_file(self, server_file_name, new_name):
        self.__ftp.rename(server_file_name, new_name)

    def quit(self):
        self.__ftp.quit()


class SftpLibWrapper(object):
    def __init__(self, host, user, password=None, port=22, private_key=None):
        self.__sftp = sftp.Connection(host=host, port=port, password=password, username=user, private_key=private_key)

    def chg_dir(self, path):
        self.__sftp.chdir(path)

    def make_dir(self, dir_name):
        file_name_list = self.get_list()
        for file_name in file_name_list:
            if file_name != dir_name:
                continue
            if self.__is_dir(file_name):
                return
            else:
                raise Exception('same name file exists'.format(dir_name))
        self.__sftp.mkdir(dir_name)

    def quit(self):
        self.__sftp.close()

    def get_file(self, server_file_name, local_file_name):
        self.__sftp.get(server_file_name, localpath=local_file_name)

    def rename_file(self, server_file_name, new_name):
        self.__sftp.rename(server_file_name, new_name)

    def upload_file(self, server_file_name, local_file_name):
        self.__sftp.put(local_file_name, server_file_name)

    def get_list(self):
        return self.__sftp.listdir()

    def get_file_list(self):
        file_list = []
        for file_name in self.get_list():
            if self.__is_dir(file_name):
                continue
            file_list.append(file_name)
        return file_list

    def delete_file(self, server_file_name):
        if server_file_name not in self.get_list():
            raise Exception('{0} is not found'.format(server_file_name))
        if self.__is_dir(server_file_name):
            self.__sftp.rmdir(server_file_name)
        else:
            self.__sftp.remove_file(server_file_name)

    def __is_dir(self, file_name):
        file_stat = self.__sftp._sftp.stat(file_name)
        return stat.S_ISDIR(file_stat.st_mode)
