clear
tput cup 10 40
echo "Menu"
tput cup 11 40
echo "****"
tput cup 14 1
echo "1.Today date"
tput cup 15 1
echo "2.Delete a file"
tput cup 16 1
echo "3.Number of users connected to the server"
tput cup 17 1
echo "4.current working directory"
tput cup 18 1
echo "5.Current connected user"
tput cup 22 10
echo -n "Enter your choice:"
read choice
case $choice in
1)echo "Today date is: `date`";;
2)sh script18.sh;;
3)echo "Number of connected users: `who|wc -l`";;
4)pwd;;
5)whoami;;
*)echo "Wrong choice.. try again";;
esac


