
To use xiv with known actions: python xiv.py -i <input_file> -o <output_file> -a <action>

1. place input file in input dir
2. run script:
     python xiv.py -i stam.txt -o stam_0.text -a sort
3. view results in a file of the -o argument in output

input file should be placed in input dir
output will be written to output dir
actions refers to a script in actions folder




To add an app create a python file and put it in the actions folder of this project

1. import dont_touch.interfaces.XivAction
2. implemnt the interface make sure to implement the start method
2. addclass name e.g. Tester:
3. run using the -c argument:
    python xiv.py -i stam.txt -o stam_0.text -a sort -c Sorter