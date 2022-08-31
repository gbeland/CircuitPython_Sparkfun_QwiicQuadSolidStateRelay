import time
import board
import CircuitPython_DFRobot_Gravity_DRF0627_I2C_Dual_Uart as DualUart

i2c = board.I2C()


iic_uart1 = DualUart.DFRobot_IIC_Serial(
    i2c,
    sub_uart_channel=DualUart.DFRobot_IIC_Serial.SUBUART_CHANNEL_1,
    IA1=1,
    IA0=1,
)

iic_uart2 = DualUart.DFRobot_IIC_Serial(
    i2c,
    sub_uart_channel=DualUart.DFRobot_IIC_Serial.SUBUART_CHANNEL_2,
    IA1=1,
    IA0=1,
)

try:
    iic_uart1.begin(baud=9600, format=iic_uart1.IIC_Serial_8N1)
    print("Opened: UART 1 ")
except Exception as e:
    iic_uart1 = None
    print("Error: Could not open UART 1 Exception: " + str(e))

try:
    iic_uart2.begin(baud=9600, format=iic_uart2.IIC_Serial_8N1)
    print("Opened: UART 2")
except Exception as e:
    iic_uart2 = None
    print("Error: Could not open UART 2 Exception: " + str(e))

sendID = 1
sendDelayCount = 1

while True:
    time.sleep(.3)
    sendDelayCount -= 1
    if sendDelayCount <= 0:
        sendDelayCount = 10
        iic_uart1.write("From1:" + str(sendID))
        iic_uart2.write("From2:" + str(sendID))

    if iic_uart1 is not None:
        if iic_uart1.available():
            s = ""
            while iic_uart1.available():
                b = iic_uart1.read(1)
                s += chr(b[0])
            print("<1:" + s + " len:" + str(len(s)) + ">")

    if iic_uart2 is not None:
        if iic_uart2.available():
            s = ""
            while iic_uart2.available():
                b = (iic_uart2.read(1))
                s += chr(b[0])
            print("<2:" + s + " len:" + str(len(s)) + ">")
