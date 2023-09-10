i=1
while [ $i -le 10 ]
do
   #     echo $i
    	if [ $i -eq 5 ]
        then
                continue
        fi
        echo $i
        let i++
done
