function addelement() {
  var maindiv = document.createElement('div');
  maindiv.className = 'form-group';
  var context = document.createElement('div');
  context.className = 'custom-file';
  var inp = document.createElement('input');
  inp.className = 'custom-file-input';
  var lb = document.createElement('label');
  lb.className = 'custom-file-label';

  context.appendChild(inp);
  context.appendChild(lb);

  maindiv.appendChild(context);

  var element = document.getElementById('upload-form');
  element.appendChild(maindiv);
};
