var i = 2;


function addelement() {
  var maindiv = document.createElement('div');
  maindiv.className = 'form-group';
  var context = document.createElement('div');
  context.className = 'custom-file';
  var inp = document.createElement('input');
  inp.type = 'file';
  inp.name = 'f'+i;
  inp.id = 'fileid'+i;
  inp.className = 'custom-file-input';
  var lb = document.createElement('label');
  lb.className = 'custom-file-label';
  lb.for = 'fileid'+i;
  lb.id = 'label-fileid'+i;
  lb.innerHTML = 'Choose file';

  context.appendChild(inp);
  context.appendChild(lb);
  maindiv.appendChild(context);

  var element = document.getElementById('upload-form');
  element.appendChild(maindiv);

  i = i + 1;
};
