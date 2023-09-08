#script:- user exit are not
echo -n "enter filename to name:"
read fname
if grep -w "$fname" /etc/passwd >/dev/null
then 
	echo "$fname is exit"
else
	echo "$fname is not exist"
fi
