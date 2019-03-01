
/* Removes all file input div elements to be created using + button */

(function() {
  for(start=2;start<=6; start++) {
    document.getElementById('div_id_image_url_' + start).remove();
  }
})();



var i = 2;


function addelement() {
  if (i <= 6) {
    var maindiv = document.createElement('div');
    maindiv.className = 'form-group';
    maindiv.id = 'div_id_image_url_' + i;

    var lb = document.createElement('label');
    lb.for = 'div_id_image_url_' + i;
    lb.className = 'col-form-label';
    lb.innerHTML = 'Image url ' + i;

    var context = document.createElement('div');

    var inp = document.createElement('input');
    inp.type = 'file';
    inp.name = 'image_url_'+i;
    inp.className = 'clearablefileinput';
    inp.id = 'id_image_url_' + i;


    context.appendChild(inp);
    maindiv.appendChild(lb);
    maindiv.appendChild(context);

    var element = document.getElementById('upload-form');
    element.appendChild(maindiv);

    i = i + 1;
  }
};
