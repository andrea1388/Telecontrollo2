base=0x38
canalei2c=1
l1=$(i2cget -y $canalei2c $base)
l2=$(i2cget -y $canalei2c $(($base+1)))
l=$(($l2*256))
l=$(($l+l1))
printf "0x%04x\n" $l

