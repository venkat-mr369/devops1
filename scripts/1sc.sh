echo -n "delete the numbers from this file:"
read fname
tr -d "[0-9]" <$fname >sc1.log
mv sc1.log test3.log
echo "all files deleted from $fname"
