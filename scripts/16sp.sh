#delete all empty files in a directory
#1 it wont display the files after deleting

for i in *
	do
	if [ ! -s $i ]
	then
#1	    echo "$i"
	    rm -rf $i
	    echo "deleted $i file"
    fi
	done
