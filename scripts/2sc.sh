echo -n "enter the month:"
read mon
k=`echo $mon|cut -c 1-3|tr "[a-z]" "[A-Z]"`
echo $k
