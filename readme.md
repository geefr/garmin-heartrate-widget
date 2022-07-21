# ANT+ HR from Garmin watch

I'm using the CooSpo adapter. They link to [This PDF for drivers](https://m.media-amazon.com/images/I/91VK9flfq7L.pdf)


On Windows no special setp should be necessary, past installing drivers:

That links directly to thisisant downloads for [USB2 drivers](http://www.thisisant.com/assets/resources/Software%20Tools/ant_usb2_drivers.zip)

```
# (In a virtual env)
pip install -r requirements.txt
python hr.py
```

On Linux, I had to install in the base python env, and run `pip install` as root - openant will install the udev rules for the ANT+ USB devices

Dependencies:
* [PySimpleGUI](https://github.com/PySimpleGUI/PySimpleGUI) (LGPL-3.0)
* [OpenANT](https://github.com/telent/python-ant) (MIT)
* [PyUSB](https://pypi.org/project/pyusb/) (BSD)
* [libusb](https://pypi.org/project/libusb/) ([zlib](https://opensource.org/licenses/Zlib))

Known Issues:
* Possible issues when running with high USB polling rates
* May need to run as root on Linux, or be a member of the dialout group
* On Linux, may need to re-plug the usb adapter before application start
* Python 3.8 is recommended. Running with 3.6 probably won't work.
