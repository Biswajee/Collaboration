
/* Removes all file input div elements to be created using + button */

(function() {
  for(start=1;start<=6; start++) {
    document.getElementById('div_id_doc_url_' + start).remove();
  }
})();


(function() {
  var maindiv = document.createElement('div');
  maindiv.className = 'form-group';
  maindiv.id = 'div_id_doc_url_' + 1;

  var lb = document.createElement('label');
  lb.for = 'div_id_doc_url_' + 1;
  lb.className = 'col-form-label';
  lb.innerHTML = 'Document ' + 1;

  var context = document.createElement('div');

  var inp = document.createElement('input');
  inp.type = 'file';
  inp.name = 'doc_url_'+ 1;
  inp.className = 'clearablefileinput';
  inp.id = 'id_doc_url_' + 1;


  context.appendChild(inp);
  maindiv.appendChild(lb);
  maindiv.appendChild(context);

  var element = document.getElementById('upload-form');
  element.appendChild(maindiv);
})();



var i = 2;


function addelement() {
  if (i <= 6) {
    var maindiv = document.createElement('div');
    maindiv.className = 'form-group';
    maindiv.id = 'div_id_doc_url_' + i;

    var lb = document.createElement('label');
    lb.for = 'div_id_doc_url_' + i;
    lb.className = 'col-form-label';
    lb.innerHTML = 'Document ' + i;

    var context = document.createElement('div');

    var inp = document.createElement('input');
    inp.type = 'file';
    inp.name = 'doc_url_'+i;
    inp.className = 'clearablefileinput';
    inp.id = 'id_doc_url_' + i;


    context.appendChild(inp);
    maindiv.appendChild(lb);
    maindiv.appendChild(context);

    var element = document.getElementById('upload-form');
    element.appendChild(maindiv);

    i = i + 1;
  }
};
