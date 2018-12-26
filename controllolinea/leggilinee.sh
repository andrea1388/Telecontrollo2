base=0x38
l1=$(i2cget -y 1 $base)
l2=$(i2cget -y 1 $(($base+1)))
l=$(($l2*256))
l=$(($l+l1))
printf "0x%04x\n" $l

