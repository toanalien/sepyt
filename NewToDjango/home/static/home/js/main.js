cusor = '+';
count = 0;
mess = '<b>Welcome to New To Django</b><br />' +
    '<br />' +
    'The web framework for perfectionists with deadlines. <br /> <br />' +
        'newbie @toanalien';

function type() {
    if (cusor == '+') cusor = ' ';
    else cusor = '_';
    document.getElementById('scr').innerHTML = mess.substring(0, count++) + cusor;
    if (count <= mess.length) setTimeout("type()", 80);

}