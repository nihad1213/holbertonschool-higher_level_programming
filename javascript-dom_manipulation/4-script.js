document.getElementById('add_item').onclick = function() {
    const item = document.createElement('li');
    item.textContent = 'item';
    document.querySelector('.my_list').appendChild(item);
  };