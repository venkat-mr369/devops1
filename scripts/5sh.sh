echo -n "Enter a filename:"
read fname
if [ -e $fname ]
then
	echo "The give file $fname is exist"
	if [ -f $fname ]
	then
	echo "$fname is regular file"
		if [ -r $fname ]
		then
		echo "$fname has read permission"
		echo "###########################"
		cat $fname
		echo "############################"
		else
		echo "$fname not having read permission"
	fi
	else
	echo "$fname is not a regular file"
	fi
else
echo "$fname not exist"
fi
echo "Bye"
