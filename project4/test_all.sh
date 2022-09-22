in="puzzle"
my="my_output"
inst="output" # not used
msg="DIFF WITH: in"
tail=" ---"

num_fails=0
echo ""

for i in `seq $1 $2`;
do                 
    echo $msg$i$tail
    python3 word_finder.py < $in$i > $my$i
    diff $inst$i $my$i
    let num_fails=$num_fails+$?
done

echo ""
echo $num_fails" failure(s) found."
if [ $num_fails -eq 0 ] ; then
    echo "ALL DIFF TESTING PASSED! Good Job :D"
fi
echo ""
