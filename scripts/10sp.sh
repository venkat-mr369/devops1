#keep on going from 1 to 10 only 
i=1
while [ $i -le 10 ]
do
	echo $i
	i=`expr $i + 1`
done

