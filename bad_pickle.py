# contains bunch of buggy examples
# taken from https://hackernoon.com/10-common-security-
# gotchas-in-python-and-how-to-avoid-them-e19fbe265e03
import base64
import pickle
import subprocess


# Input injection
def transcode_file(request, filename):
    command = 'ffmpeg -i "{source}" output_file.mpg'.format(source=filename)
    subprocess.call(command, shell=True)  # a bad idea!


# Assert statements
def abc(request, user):
    assert user.is_admin, 'user does not have access'
   # secure code...


# Pickles
class RunBinSh():
    def __reduce__(self):
        return (subprocess.Popen, (('/bin/sh',),))


print(base64.b64encode(cPickle.dumps(RunBinSh())))
