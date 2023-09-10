while true
do
        echo "please type something (bye to quit)"
        read input_string
        echo "You typed: $input_string"
        if [ $input_string == 'bye' ]
        then
                break
        fi
done
