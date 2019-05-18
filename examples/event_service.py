from bluezero import microbit
from time import sleep

ubit = microbit.Microbit(adapter_addr='FC:F8:AE:8F:0C:A4',
                         device_addr='F1:55:90:65:29:DC',
                         accelerometer_service=False,
                         button_service=False,
                         led_service=False,
                         magnetometer_service=False,
                         pin_service=False,
                         temperature_service=False,
                         uart_service=False,
                         event_service=True)

ubit.connect()
print(ubit.microbit_requirements)
ubit.client_event = [1104, 1]
sleep(0.5)
ubit.client_event = [1104, 2]
sleep(0.5)
ubit.client_event = [1104, 3]
sleep(0.5)
ubit.client_event = [1104, 4]
sleep(0.5)
ubit.disconnect()
