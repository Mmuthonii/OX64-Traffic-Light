#!/bin/sh

### BEGIN INIT INFO
# Provides:          myinit
# Required-Start:
# Required-Stop:
# Default-Start:     S
# Short-Description: Initialize LED on boot
### END INIT INFO

LED_GPIO=12

echo "Turning on LED at GPIO $LED_GPIO..."

gpioset gpiochip0 $LED_GPIO=1

exit 0

# ^C