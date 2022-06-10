"use strict";


(function(){
        let download = document.getElementById("download")
        download.addEventListener("click", function(event){
            ExportToExcel('xlsx')
        });


          function ExportToExcel(type, fn, dl) {
            var elt = document.getElementById('table');
            var wb = XLSX.utils.table_to_book(elt, { sheet: "sheet1" });
            return dl ?
                XLSX.write(wb, { bookType: type, bookSST: true, type: 'base64' }) :
                XLSX.writeFile(wb, fn || ('ChurchPortal-{{ table_name }}.' + (type || 'xlsx')));
        }
})()