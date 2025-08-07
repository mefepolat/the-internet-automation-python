const dataTransfer = new DataTransfer();
arguments[0].dispatchEvent(new DragEvent('dragstart', { dataTransfer }));
arguments[1].dispatchEvent(new DragEvent('drop', { dataTransfer }));
arguments[0].dispatchEvent(new DragEvent('dragend', { dataTransfer }));
