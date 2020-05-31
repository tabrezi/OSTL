#Perl script to find the factorial of given number.
sub factorial
{
$i=1;
$f=1;
while($i<=$_[0])
{
$f=$f*$i;
$i++;
}
#print("Factorial of $_[0] is $f.\n");
return($f);
}

print("Enter the number:");
chomp($n=<>);
$f=factorial($n);
print("Factorial of $n is $f.\n")
#print("$n");

