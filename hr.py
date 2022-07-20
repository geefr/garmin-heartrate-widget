from turtle import color, width
import PySimpleGUI as psg

from ant.easy.node import Node
from ant.easy.channel import Channel
from ant.base.message import Message

from threading import Thread, Event

g_heart_rate = 0
sentinel = Event()
thread_hr_done = Event()
node = None

NETWORK_KEY = [0xB9, 0xA5, 0x21, 0xFB, 0xBD, 0x72, 0xC3, 0x45]

colour_low=(0,255,0)
colour_high=(255,0,0)
hr_low = 60
hr_high = 180

def colour_to_hex(c):
    return '#%02x%02x%02x' % c

def colour():
    if g_heart_rate < hr_low:
        return colour_to_hex(colour_low)
    elif g_heart_rate > hr_high:
        return colour_to_hex(colour_high)

    f = (g_heart_rate - 60) / (hr_high - hr_low)
    r = (colour_high[0] - colour_low[0]) * f + colour_low[0]
    g = (colour_high[1] - colour_low[1]) * f + colour_low[1]
    b = (colour_high[2] - colour_low[2]) * f + colour_low[2]
    return colour_to_hex((int(r),int(g),int(b)))

def on_data(data):
    global sentinel
    if sentinel.is_set():
        node.stop()
        return

    global g_heart_rate
    heartrate = data[7]
    g_heart_rate = heartrate

def thread_hr():
    global node
    global thread_hr_done
    node = Node()
    # Many thanks: https://github.com/Tigge/openant/blob/master/examples/heart_rate_monitor.py
    node.set_network_key(0x00, NETWORK_KEY)
    channel = node.new_channel(Channel.Type.BIDIRECTIONAL_RECEIVE)
    channel.on_broadcast_data = on_data
    channel.on_burst_data = on_data
    channel.set_period(8070)
    channel.set_search_timeout(12)
    channel.set_rf_freq(57)
    channel.set_id(0, 120, 0)
    try:
        channel.open()
        node.start()
    finally:
        node.stop()
        thread_hr_done.set()

def main():
    global node
    global sentinel
    global g_heart_rate

    psg.set_options(suppress_error_popups=False)

    hr = Thread(target=thread_hr)
    hr.start()

    layout=[
        [psg.Text(f"", key='hr_text', justification='center', expand_x=True, expand_y=True, font=('Arial',96),text_color='#ff00ff', background_color='black')]
    ]
    win = psg.Window(
        title="Heart Rate",
        layout=layout,
        size=(240,160),
        background_color='black'
    )

    while True:
        event, values = win.read(timeout=50)
        if event == psg.WIN_CLOSED:
            break
        if thread_hr_done.is_set():
           break
    
        win['hr_text'].update(f"{g_heart_rate}", text_color=colour())

    sentinel.set()
    win.close()
    node.stop()
    hr.join()

if __name__ == "__main__":
    main()
