## project overview

**This is assignment 1 in Cryptography course in Benha University**
This project is a complete python  program to encrypt and decrypt classical ciphers as follows : 

• The program supports encryption and decryption using `shift` and  `affine` ciphers. 
• it is  be callable from command line as follows: 
 -  First argument is the cipher type [“shift”,”affine”]. 
 -  Second argument is the operation type [“enc”, “dec”]. 
 -  The Third argument is the input file. 
 -  The fourth argument is the output file. 
 -  The last argument is the the list of encryption keys required for the cipher. 
...
 Examples calls from terminal: 
     - `solution.py affine decrypt input.text output.text  a b` 
     -  `solution.py shift encrypt input.text output.text a` 
