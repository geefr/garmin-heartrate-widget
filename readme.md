# ANT+ HR from Garmin watch

I'm using the CooSpo adapter. They link to [This PDF for drivers](https://m.media-amazon.com/images/I/91VK9flfq7L.pdf)

That links directly to thisisant downloads for [USB2 drivers](http://www.thisisant.com/assets/resources/Software%20Tools/ant_usb2_drivers.zip)

```
# (In a virtual env)
pip install -r requirements.txt
python hr.py
```

Dependencies:
* [PySimpleGUI](https://github.com/PySimpleGUI/PySimpleGUI) (LGPL-3.0)
* [OpenANT](https://github.com/telent/python-ant) (MIT)
* [PyUSB](https://pypi.org/project/pyusb/) (BSD)
* [libusb](https://pypi.org/project/libusb/) ([zlib](https://opensource.org/licenses/Zlib))
