# CS 327 Compilers: Assignment 1

## Switch

### Team Name: Switch Compilers

Language Name: Switch

An (non-exhaustive and non-complete) example of a simple imperative language would look something like this:

  Expressions e ::= *x* | n | true | false | e1 < e2 | e1 == e2 | e1 > e2 | e1 + e2 | e1 \* e2
  
  Commands c ::= skip | *x* := e | c1; c2 | if e then c1 else c2 | while e do c where x is a variable and n is a number.


Design of our language:

● Identifier ::= [a-zA-Z][a-zA-Z0-9\_]<sup>\*</sup>


  ○ In our language, an acceptable identifier must satisfy all of the following properties:
  
  ■ Must begin with a letter, either upper case or lower case
  
  ■ Can contain all possible combinations of non-empty combinations of lowercase letters [a-z], uppercase letters [A-Z], numbers [0-9], and underscore [_].

○ Syntax examples
    
    ■ a - a single lowercase letters
    
    ■ P - a single upper case letters    
    
    ■ cDe - a combination of uppercase and lowercase letters    
    
    ■ Fg2 - a combination of uppercase letters, lowercase letters, and numbers    
    
    ■ Lm_3 - a combination of uppercase letters, lowercase letters, numbers, and a single underscore    
    
    ■ UV___J - a combination of uppercase letters, lowercase letters, numbers, and multiple consecutive underscores    
    
    ■ KLnp_jk_ik - a combination of uppercase letters, lowercase letters, numbers, and multiple underscores

● Number ::= [0-9]+
    
    ○ In our language, only integers are considered, and thus, any combination of single-digit numbers is permissible.
    
    ○ Syntax examples
    
      ■ 1 - single digit numbers
      
      ■ 19 - two digit numbers      
      
      ■ 109987066 - any length of digits numbers

● Str::= "([^"\\] **|** \\.)\*”
    
    ○ [^"\\] matches any character and regular escape sequences except double quotes and backslashes.
    
    ○ \\., when preceded by a backslash, matches a literal backslash.
    
    ○ (...)\ allows for zero or more occurrences of the enclosed pattern.

● Bool::= “on” | “off”
  
  ○ In our language, we have chosen “on” and “off” to represent boolean values. The value “on” will be used to represent high, always true, or 1. Similarly, the value “off” will be used       to represent low, always false, or 0.
  
  ○ Syntax examples
  
    ■ a = 1;

      b = 2;
    
      show (a == b); -> off
    
      show (a != b); -> on

● Relational Operator ::= "<" | “<=” | "==" | “>=" | ">" | "!="

  ○ In our language, we have chosen to have five relational operators:
    
    < - Less than
   
    <= - Less than or equal to
    
    == - Equal to
    
    >= - Greater than or equal to
    
    > - Greater than

    != - not equal to
  
  ○ Syntax examples
    
      eg. either (a >= 5) {b = 6;} or {b = 9;}

● Additive Operator ::= "+" | "-"

  ○ The symbols + and - will be used to represent addition and subtraction arithmetic operations.

  ○ Syntax examples
     eg. a = 4 + 5;

● Multiplicative Operator ::= "\*"

  ○ The symbol \* will be used to represent multiplication operation.
  
  ○ Syntax examples
     eg. c = 10\*19;

● Division Operator:: = “/”

  ○ The symbol \* will be used to represent division operation.
  
  ○ In the case of floating points, the division will report the integer closest and just smaller than the floating value.
  
  ○ Syntax examples
     eg. c = 10/2;
         j = 19/8;

● Taking Input::= “take”(identifier)“;”
  
  ○ To take input, we have devised a new function, ‘take’. This will ask for input from the user and assign it to the identifier.
  
  ○ Syntax examples
    
    ■ take (a) ;  

        This would enable the user to give an input which will be assigned to the variable ‘a’.

● Giving Output::= “show”(expression(s)) “;”

  ○ To receive output, we have devised a new function, ‘show’. This function would enable printing the expression or expressions.
  
  ○ Syntax examples
    
    ■ show (x1) ;

        The above code would print the value of x1.
    
    ■ show (x1, x2, x3) ;

        The above code will print x1, x2, x3 on separate lines.

● Conditional: “either” ( condition ) {code block} “whatif” ( condition ) {code block} or( expression) {code block}

  ○ In our language, we have used either-whatif-or to represent the conditional operations. Every conditional expression must at least have one “either” and one “or” block. The number of      “whatif “ blocks should be a whole number.
    
      ■ either - if the expression is true, execute the block corresponding to this.
      
      ■ whatif - if the expression (different from the previous expression) is true, execute the block corresponding to this. Can be called multiple times in the same conditional segment. 
      
      ■ or - if none of the above expressions are true, execute the block corresponding to this.
  
  ○ Syntax examples
      
      either (a >= 5)
      
      {b = 6;}
      
      what if (a <= 0)
      
      {b = 9;}
      
      or
      
      {b = 12;}
      
   (If a is greater than or equal to 5, assign the value 6 to b, but if a is less than
    or equal to 0, assign the value 9 to b. Otherwise, assign the value 12 to b.)

● Declaration ::= "var" Identifier ":" Type ";"

  ○ Every declaration must be followed with a semicolon Type ::= "num" | "bool" | "str"
  
  Array Declaration : "var" "<array_name>" "["size"]" ":" Type  ";"
  
  Array Literal ::= "[" [ Entity{ "," Expression }\* ] "]";
  
  Array Access ::= "<array_name>" "["index"]";
  
  ○ Syntax examples
    
    ■ var sd : num ;
    
    ■ var fl : str;

● Assignment ::= Identifier "=" Expression ";"

  ○ Every assignment must be followed with a semicolon.
  
  ○ Syntax examples

    ■ sd = 23 ;

● Loop ::= "while" (condition) "do" {expression}

Loop ::= “from” (expression “to” expression; updation){expression}

  ○ In our programming language, we have designed two types of loops:  

    ■ while loop - will execute the block when the value of an expression is true 
    
    ■ from loop - will execute the block in the given range

  ○ Syntax examples
    
    ■ while (on)
    
    do {sd = 23;}
    
    ■from (j = -4 to j = 56; j=j+1)
          {dfg = dfg +1;}

● Function ::= “func” <func\_name>(parameters) {Block}

  ○ In our programming language, we have defined the func to define a function. The name of the function follows the same 
    naming convention as an identifier.

    Multiple parameters separated by comma can be assigned the data types using ‘=’ sign.
  
  ○ Syntax examples
  
      ■ func ticktock ( start = number, count = number)
      
      {either (start >=0)
      
      {while (count >0)
      
      do {start = start +1;
      
      Count = count -1;
      
      show (count);}
      
      }
      
      or
      
      {give;}
      
      }

  ○ Function Call ::= <func\_name>(arguments);

    ○ Syntax examples:
      
        eg. ticktock(0, 10);

● give:

  ○ Exit the function. Like return    
  
  ○ Syntax examples

      ■ give(expression);
  
● Exception Handling ::=
    
    "try" {
    
    Code Block to be tried for an exception
    
    }
    
    "catch"(ExceptionType Identifier){
    
    Code Block to handle the exception
    
    }
    
    "Finally"{
    
    Code Block that always executes
    
    }

● Comments ::=
      
      Single Line Comments:
      
            eg. "->"

● Precedence and Associativity:

    1. Precedence:

        1. Multiplication, Division

        2. Addition, Subtraction

        3. Relational Operators

        4. Equality Operators

        5. Logical Operators

    2. Associativity:

        1. Left to Right

    3. Parentheses:

        Highest Precedence
  
● Scope:

    1. Global Scope:

        1. Variables declared outside of any function

           eg. var a : num;

    2. Local Scope:

        1. Variables declared inside a function

        2. Parameters of a function

            eg. func add (a = num, b = num) {var c : num; c = a + b;}

● Jump Statements:

    1. stop: Exit the loop

       Syntax: while (a < 10) {a = a + 1; either (a == 5) {stop;}}

    2. carryon: Continue to the next iteration of the loop
    
        Syntax: while (a < 10) {a = a + 1; either (a == 4) {carryon;}}


