
(function() {
  var maindiv = document.createElement('div');
  maindiv.className = 'form-group';
  maindiv.id = 'slide_div';

  var lb = document.createElement('label');
  lb.for = 'slide';
  lb.className = 'col-form-label';
  lb.innerHTML = 'Presentation ' + 1;

  var context = document.createElement('div');

  var inp = document.createElement('input');
  inp.type = 'file';
  inp.name = 'slide';
  inp.className = 'clearablefileinput';
  inp.id = 'id_ppt_url_' + 1;


  context.appendChild(inp);
  maindiv.appendChild(lb);
  maindiv.appendChild(context);

  var element = document.getElementById('upload-form');
  element.appendChild(maindiv);

})();


var i = 2;


function addelement() {

    var maindiv = document.createElement('div');
    maindiv.className = 'form-group';
    maindiv.id = 'slide_div';

    var lb = document.createElement('label');
    lb.for = 'slide';
    lb.className = 'col-form-label';
    lb.innerHTML = 'Presentation ' + i;

    var context = document.createElement('div');

    var inp = document.createElement('input');
    inp.type = 'file';
    inp.name = 'slide';
    inp.className = 'clearablefileinput';
    inp.id = 'slide';


    context.appendChild(inp);
    maindiv.appendChild(lb);
    maindiv.appendChild(context);

    var element = document.getElementById('upload-form');
    element.appendChild(maindiv);

    i = i + 1;

};
