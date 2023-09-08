#verify the regularfile, read access & view the data 
clear
echo -n "enter the regularfile name:-"
read fname
if [ -e $fname ]
then
	echo "$fname is exit"
	if [ -f $fname ]
	then 
		echo "$fname is regular file"
		if [ -r $fname ]
		then
		echo "$fname is have read access"
		echo "=========================="
		cat $fname
		echo "=========================="
		else
		echo "$fname is not having read access"
		fi
	else
		echo "$fname is not regular file"
	fi
else
	echo "$fname is not exit"
fi
