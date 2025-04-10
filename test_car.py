import keyboard
import serial
import time

def main():
    port = 'COM26' #Replace with your Bluetooth output COM port
    ser = serial.Serial(port, 9600, timeout = 1, write_timeout = 1)
    print(f'Connected to the port{port}')

    key_command_map = {
        'w': (b'1', 'forward'),
        's': (b'2', 'backward'),
        'a': (b'3', 'left'),
        'd': (b'4', 'right'),
        'i': (b'5', 'straight speedup'),
        'k': (b'6', 'straight speedup'),
        'o': (b'7', 'turn speedup'),
        'l': (b'8', 'turn speeddown'),
    }

    while ser.is_open:
        print("\r{}".format(' ' * 30), end="", flush=True)
        command_sent = False

        for key, (cmd, label) in key_command_map.items():
            if keyboard.is_pressed(key):
                print(f"\r{label}", end = '', flush = True)
                ser.write(cmd)
                command_sent = True
                break
        if not command_sent:
            print("\r...", end="", flush=True)
            ser.write(b'0')
        time.sleep(0.2)



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")
    except serial.SerialException as e:
        print(f"Serial error: {e}")