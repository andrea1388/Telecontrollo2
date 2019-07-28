echo "out" > /sys/class/gpio/gpio18/direction
echo "1" > /sys/class/gpio/gpio18/value
espeak -v it -p 70 -s 155 "$1" 2>/dev/null
echo "0" > /sys/class/gpio/gpio18/value
