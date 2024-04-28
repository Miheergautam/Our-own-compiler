func add(a : num, b : num)
{
    var result : num;
    result = a + b;
    show(result);
    give(result);
}

add(5, 10);


-> {Example of jump statements}
var a : num;
a = 0;
while (a < 5) do {
    a = a + 1;
    either (a == 2) {
        carryon;
    }
    show(a);
}
