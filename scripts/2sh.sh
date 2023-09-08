#script is has accept and delete the file
echo -n "enter filename to delete:"
read fname
if rm $fname 2>tmp
#if rm $fname 2>/dev/null
then 
	echo "$fname is deleted"
else
	echo "$fname is not exist"
fi
