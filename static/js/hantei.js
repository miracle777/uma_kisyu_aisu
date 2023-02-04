//九星の相性の数字によって、背景色を変える


//window.onload = hantei();

function hantei() {
  let table1 = document.getElementById(`kanteitable`);

  //九星の相性の数字によって、背景色を変える
  for (let row of table1.rows) {
    for (let cell of row.cells) {
      //celllが判定の範囲かどうか
      if (cell.id == "chk") {
        if (cell.innerText == "1") {
                cell.style.backgroundColor = "#FF0000";
        } else if (cell.innerText == "2") {
                cell.style.backgroundColor = "#FF7F00";
        } else if (cell.innerText == "3") {
                cell.style.backgroundColor = "#ffffff";
        }
      }
    }
  }




}
