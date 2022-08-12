# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2022 Graham Beland
#
# SPDX-License-Identifier: Unlicense

# import the CircuitPython board and busio libraries
import board
import sparkfun_qwiicquadsolidstaterelay

# Create bus object using the board's I2C port
i2c = board.I2C()

# Note: default i2c address is 8
relay = None
try:
    relay = sparkfun_qwiicquadsolidstaterelay.Sparkfun_QwiicQuadSolidStateRelay(i2c)
    print("Opened: Relay Controller")
    if relay.connected:
        print("Relay connected. ")
    else:
        print("Relay does not appear to be connected. Please check wiring. ")
except ValueError as e:
    print("Error: Could not open Relay Controller rxception:" + str(e))

# For a different address use QwiicRelay(i2c, address)
# Warning - this is stored in non-volitile memory and you must remember the setting
# to change it back to the default address of  8.
# relay.set_i2c_address(9)

relay.relay_on(1)
relay.on(2)
relay.on(3)
relay.on(4)
relay.relay_off(1)
relay.relay_off(4)
relay.relay_all_toggle()
relay.relay_all_on()
relay.relay_all_off()
