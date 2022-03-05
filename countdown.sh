#!/bin/bash
'
# use can also us /sh too
#this program print number in a primal style.

a=0
while [ "$a" -lt 20 ]
do
   b="$a"
   while [ "$b" -ge 0 ]
   do
      echo -n "$b "
      b=`expr $b - 1`
   done
   echo
   a=`expr $a + 1`
done
'

#!/bin/sh
# Script to print currently logged in users information, and current date & time.
#This is for personal study
#To be continued.
clear
echo "Hello $USER"
echo -e "Today is \c ";date
echo -e "Number of user login : \c" ; who | wc -l
echo "Calendar"
cal
exit 0
