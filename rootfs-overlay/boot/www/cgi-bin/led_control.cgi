#!/bin/sh
echo "Content-Type: text/plain"
echo ""

# Read color parameter from URL query (e.g., ?color=red)
COLOR=$(echo "$QUERY_STRING" | sed -n 's/^.color=\([^&]\).*$/\1/p')

case $COLOR in
  red)
    gpioset gpiochip0 12=1 20=0 18=0 ;;
  yellow)
    gpioset gpiochip0 12=0 20=0 18=1 ;;
  redyellow)
    gpioset gpiochip0 12=1 20=0 18=1 ;;
  green)
    gpioset gpiochip0 12=0 20=1 18=0 ;;
  off)
    gpioset gpiochip0 12=0 20=0 18=0 ;;
  *)
    echo "Invalid color"
    exit 1
esac

echo "LED set to $COLOR"