#Perl script to find the factorial of given number.
#!/usr/bin/perl
print("Enter the number:");
chomp($n=<>);
#$n=<>;
#print("$n");
$i=1;
$f=1;
while($i<=$n)
{
$f=$f*$i;
$i++;
}
print("Factorial of $n is $f.\n")