#script is has accept and delete the file
echo -n "enter filename to name:"
read fname
if grep -w "$fname" /etc/passwd >/dev/null
then 
	echo "$fname is exit"
else
	echo "$fname is not exist"
fi
