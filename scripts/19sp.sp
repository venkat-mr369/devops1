#passing arguments, will provide total arguments
i=1
for user in "$@"
do
	echo "user name:-$i $user"
	let i++
done	
	echo "total no of arguments: $#"

