#!/usr/bin/env bash 
## analysis.sh

#To make executable shell file
chmod +x analysis.sh

# Download the sonnets
curl http://www.gutenberg.org/cache/epub/1041/pg1041.txt > sonnets/sonnets.txt

cd sonnets/

# Trim introduction and concluding lines
 head -n +2662 sonnets.txt | tail -n +43 >> cleaned_sonnets.txt

# Remove leading blank characters 
 cat cleaned_sonnets.txt | cut -c 3-100 > cleaned-sonnets1.txt
 
# Split sonnets into individual files. This will involve *many* commands.

head cleaned-sonnets1.txt --lines=1666 > sonnets-1-.txt
head cleaned-sonnets1.txt --lines=1685 | tail --lines=18 > sonnet-2-aa.txt
head cleaned-sonnets1.txt --lines=2127 | tail --lines=442 > sonnets-3-.txt
head cleaned-sonnets1.txt --lines=2142 | tail --lines=15 > sonnet-4-aa.txt
tail cleaned-sonnets1.txt --lines=476 > sonnets-5-.txt

split --lines=17 sonnets-1-.txt sonnet-1- --additional-suffix=.txt
split --lines=17 sonnets-3-.txt sonnet-3- --additional-suffix=.txt
split --lines=17 sonnets-5-.txt sonnet-5- --additional-suffix=.txt

rm sonnets-?-.txt

: '
head -n +86 cleaned-sonnets1.txt | tail -n +2 > cleaned_sonnets2.txt
head -n +1667 cleaned-sonnets1.txt | tail -n +87 > cleaned_sonnets3.txt
head -n +1685 cleaned-sonnets1.txt | tail -n +1669 > cleaned_sonnets4.txt
head -n +2127 cleaned-sonnets1.txt | tail -n +1687 > cleaned_sonnets5.txt
head -n +2143 cleaned-sonnets1.txt | tail -n +2129 > cleaned_sonnets6.txt
head -n +2364 cleaned-sonnets1.txt | tail -n +2144 > cleaned_sonnets7.txt
head -n +2619 cleaned-sonnets1.txt | tail -n +2365 > cleaned_sonnets8.txt

split -l 17 cleaned_sonnets2.txt sonnets2_ --additional-suffix=.txt
split -l 17 cleaned_sonnets3.txt sonnets3_ --additional-suffix=.txt
split -l 17 cleaned_sonnets4.txt sonnets4_ --additional-suffix=.txt
split -l 17 cleaned_sonnets5.txt sonnets5_ --additional-suffix=.txt
split -l 17 cleaned_sonnets6.txt sonnets6_ --additional-suffix=.txt
split -l 17 cleaned_sonnets7.txt sonnets7_ --additional-suffix=.txt
split -l 17 cleaned_sonnets8.txt sonnets8_ --additional-suffix=.txt
'


# Find the longest sonnet (most words)
#wc -w /c/Users/MAYURESH/Desktop/IMT511/a1-git-and-command-shell-mayureshmali/sonnets/*|sort -n -r > lengths.txt
wc --word sonnet-?-*.txt | sort -g -r > lengths.txt

# Search for specific words in  the sonnets
grep "truth" sonnet-?-*.txt > truth.txt
grep "love" sonnet-?-*a.txt > love.txt
