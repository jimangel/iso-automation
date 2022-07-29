# modified from: https://gist.github.com/s3rj1k/55b10cd20f31542046018fcce32f103e?permalink_comment_id=4205982#gistcomment-4205982

import os, io
import pathlib
import pycdlib

ubuntu = pathlib.Path("/app/" + os.environ['INPUT_ISO_NAME'])
new_iso = pathlib.Path("/app/UPDATED_" + os.environ['INPUT_ISO_NAME'])

iso = pycdlib.PyCdlib()
iso.open(ubuntu)

extracted = io.BytesIO()
iso.get_file_from_iso_fp(extracted, iso_path='/BOOT/GRUB/GRUB.CFG;1')
extracted.seek(0)
data = extracted.read()
print(data.decode())

new = data.replace(b' ---', b'quiet autoinstall ---').replace(b'timeout=30', b'timeout=1')
print(new.decode())

iso.rm_file(iso_path='/BOOT/GRUB/GRUB.CFG;1', rr_name='grub.cfg')
iso.add_fp(io.BytesIO(new), len(new), '/BOOT/GRUB/GRUB.CFG;1', rr_name='grub.cfg')

iso.write(new_iso)
iso.close()