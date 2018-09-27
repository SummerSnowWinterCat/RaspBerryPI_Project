from MyQR import myqr
import os

myqr.run(
    words='http://summersnowwintercat.github.io',
    version=1,
    level='H',
    picture='../raspberrypi_main/test2.jpg',
    colorized=True,
    contrast=1.0,
    brightness=1.0,
    save_name='lulu.png',
    save_dir=os.getcwd()
)
