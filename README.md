transfer_lib
======================
�e�v���g�R�����g�p�����t�@�C���]���Ɋ֘A���郉�b�p�[�N���X���쐬���܂���
�����p�͎��ȐӔC�ł����R�ɂǂ���

�g����
------
�P�Dpip�R�}���h�����s���A���W���[�����_�E�����[�h���Ă�������

    pip install transfer_lib

�Q�D�N���X���C���|�[�g���A���L��̗p�Ɏg�p���Ă�������

    from transfer_lib.ftp import FtpLibWrapper
    ftp = FtpLibWrapper('host', 'user', 'password')
    ftp.chg_dir('dir_name')
    for file_name in ftp.get_file_list()
        print file_name
    ftp.get_file('hoge.txt', '/tmp/hogehoge.txt')


�@�\�Љ�
------
### FtpLibWrapper
#### FTP�AFTPS�v���g�R�����g�p�����ʐM�����̃��b�p�[�N���X�ł�
***
__init__(host, user, password, is_pasv=True, is_ssl=False):

| ���O | �K�{ | ���� | �f�t�H���g�l | 
|:-----------|:------------:|:-----------|:-----------| 
| host | �� | �ڑ��T�[�o�h���C���� | - |
| user | �� | �ڑ����[�U | - |
| password | �� | �ڑ��p�X���[�h | - |
| is_pasv | �~ | �p�b�V�u���[�h���ǂ��� | True |
| is_ssl | �~ | FTPS���g�p���邩�ǂ��� | False |
***
get_file_list():���݂̃f�B���N�g���ɑ��݂���t�@�C���̈ꗗ�����X�g�ŕԂ��܂�(�t�H���_�͏��O)

�߂�l�FList
***
chg_dir(path):�w�肵���p�X�Ɉړ����܂�

| ���O | �K�{ | ���� | �f�t�H���g�l | 
|:-----------|:------------:|:-----------|:-----------| 
| path | �� | �ړ��������f�B���N�g���� | - |
�߂�l�F�Ȃ�
***
make_dir(path):�f�B���N�g�����쐬���܂��A���łɑ��݂���ꍇ�͉������܂���

| ���O | �K�{ | ���� | �f�t�H���g�l | 
|:-----------|:------------:|:-----------|:-----------| 
| path | �� | �쐬�������f�B���N�g���� | - |
�߂�l�F�Ȃ�
***
get_file(server_file_name, local_file_name):�t�@�C�����_�E�����[�h���܂�

| ���O | �K�{ | ���� | �f�t�H���g�l | 
|:-----------|:------------:|:-----------|:-----------| 
| server_file_name | �� | �擾�������t�@�C���� | - |
| local_file_name | �� | �擾�����t�@�C���̃��[�J���t���p�X | - |
�߂�l�F�Ȃ�
***
delete_file(server_file_name):�w�肵���t�@�C���A�t�H���_���폜���܂��A�t�H���_�̒��g�����݂���ꍇ���폜���܂�

| ���O | �K�{ | ���� | �f�t�H���g�l | 
|:-----------|:------------:|:-----------|:-----------| 
| server_file_name | �� | �폜�������t�@�C���� | - |
�߂�l�F�Ȃ�
***
upload_file(server_file_name, local_file_name):�t�@�C�����A�b�v���[�h���܂�

| ���O | �K�{ | ���� | �f�t�H���g�l | 
|:-----------|:------------:|:-----------|:-----------| 
| server_file_name | �� | �A�b�v���[�h����t�@�C���̖��� | - |
| local_file_name | �� | �A�b�v���[�h�������t�@�C���̃��[�J���t���p�X | - |
�߂�l�F�Ȃ�
***
rename_file(server_file_name, new_name):�t�@�C������ύX���܂�

| ���O | �K�{ | ���� | �f�t�H���g�l | 
|:-----------|:------------:|:-----------|:-----------| 
| server_file_name | �� | �ύX�O�̖��� | - |
| new_name | �� | �ύX��̖��� | - |
�߂�l�F�Ȃ�
***
quit():�T�[�o�Ƃ̒ʐM���I�����܂��A�Ō�ɂ��Ȃ炸���s���Ă�������

�߂�l�F�Ȃ�
***


### SftpLibWrapper
#### SFTP�v���g�R�����g�p�����ʐM�����̃��b�p�[�N���X�ł�
***
__init__(host, user, password, port=22, private_key=None):

| ���O | �K�{ | ���� | �f�t�H���g�l | 
|:-----------|:------------:|:-----------|:-----------| 
| host | �� | �ڑ��T�[�o�h���C���� | - |
| user | �� | �ڑ����[�U | - |
| password | �~ | �ڑ��p�X���[�h | None |
| port | �~ | �g�p�|�[�g | 22 |
| private_key | �~ | �閧���p�X | None |
***
get_file_list():���݂̃f�B���N�g���ɑ��݂���t�@�C���̈ꗗ�����X�g�ŕԂ��܂�(�t�H���_�͏��O)

�߂�l�FList
***
chg_dir(path):�w�肵���p�X�Ɉړ����܂�

| ���O | �K�{ | ���� | �f�t�H���g�l | 
|:-----------|:------------:|:-----------|:-----------| 
| path | �� | �ړ��������f�B���N�g���� | - |
�߂�l�F�Ȃ�
***
make_dir(path):�f�B���N�g�����쐬���܂��A���łɑ��݂���ꍇ�͉������܂���

| ���O | �K�{ | ���� | �f�t�H���g�l | 
|:-----------|:------------:|:-----------|:-----------| 
| path | �� | �쐬�������f�B���N�g���� | - |
�߂�l�F�Ȃ�
***
get_file(server_file_name, local_file_name):�t�@�C�����_�E�����[�h���܂�

| ���O | �K�{ | ���� | �f�t�H���g�l | 
|:-----------|:------------:|:-----------|:-----------| 
| server_file_name | �� | �擾�������t�@�C���� | - |
| local_file_name | �� | �擾�����t�@�C���̃��[�J���t���p�X | - |
�߂�l�F�Ȃ�
***
delete_file(server_file_name):�w�肵���t�@�C���A�t�H���_���폜���܂��A�t�H���_�̒��g�����݂���ꍇ���폜���܂�

| ���O | �K�{ | ���� | �f�t�H���g�l | 
|:-----------|:------------:|:-----------|:-----------| 
| server_file_name | �� | �폜�������t�@�C���� | - |
�߂�l�F�Ȃ�
***
upload_file(server_file_name, local_file_name):�t�@�C�����A�b�v���[�h���܂�

| ���O | �K�{ | ���� | �f�t�H���g�l | 
|:-----------|:------------:|:-----------|:-----------| 
| server_file_name | �� | �A�b�v���[�h����t�@�C���̖��� | - |
| local_file_name | �� | �A�b�v���[�h�������t�@�C���̃��[�J���t���p�X | - |
�߂�l�F�Ȃ�
***
rename_file(server_file_name, new_name):�t�@�C������ύX���܂�

| ���O | �K�{ | ���� | �f�t�H���g�l | 
|:-----------|:------------:|:-----------|:-----------| 
| server_file_name | �� | �ύX�O�̖��� | - |
| new_name | �� | �ύX��̖��� | - |
�߂�l�F�Ȃ�
***
quit():�T�[�o�Ƃ̒ʐM���I�����܂��A�Ō�ɂ��Ȃ炸���s���Ă�������

�߂�l�F�Ȃ�
***
get_list():���݂̃f�B���N�g���ɑ��݂���t�@�C���A�t�H���_�̈ꗗ�����X�g�ŕԂ��܂�

�߂�l�FList
***


### HttpFileTransfer
#### HTTP�AHTTPS�v���g�R�����g�p�����ʐM�����̃��b�p�[�N���X�ł�
***
__init__(self, domain, user, password, is_ssl=False):

| ���O | �K�{ | ���� | �f�t�H���g�l | 
|:-----------|:------------:|:-----------|:-----------| 
| domain | �� | �ڑ��T�[�o�h���C���� | - |
| user | �� | �ڑ����[�U | - |
| password | �� | �ڑ��p�X���[�h | - |
| is_ssl | �~ | HTTPS���g�p���邩�ǂ��� | False |
***
get_file(file_path, local_file_path, local_file_encode):�t�@�C�����_�E�����[�h���܂�

| ���O | �K�{ | ���� | �f�t�H���g�l | 
|:-----------|:------------:|:-----------|:-----------| 
| file_path | �� | �擾�������t�@�C���p�X | - |
| local_file_path | �� | �擾�����t�@�C���̃��[�J���t���p�X | - |
| local_file_encode | �� | �擾�����t�@�C���̕����R�[�h | - |
�߂�l�F�Ȃ�
***


�֘A���
--------
1. [�O�O���J�X(�u���O)](http://gugurekasu.blogspot.jp/)
2. [LinkedIn](https://jp.linkedin.com/in/akirataniguchi1)
 
���C�Z���X
----------
Distributed under the [MIT License][mit].
[MIT]: http://www.opensource.org/licenses/mit-license.php
