document.addEventListener("DOMContentLoaded", function() {
    var springData = JSON.parse(document.getElementById('data-holder').textContent);
    var tableBody = document.getElementById("myTableBody");

    springData.forEach(function(rowData) {
        var row = document.createElement("tr");
        var singerCell = document.createElement("td");
        singerCell.textContent = rowData[0]; // 가수
        row.appendChild(singerCell);

        var titleCell = document.createElement("td");
        titleCell.textContent = rowData[1]; // 제목
        row.appendChild(titleCell);

        tableBody.appendChild(row);
    });
});