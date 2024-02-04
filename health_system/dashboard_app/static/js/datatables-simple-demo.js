window.addEventListener('DOMContentLoaded', event => {
    // Simple-DataTables
    // https://github.com/fiduswriter/Simple-DataTables/wiki


    const reviewTable = document.getElementById('reviewTable');
    if (reviewTable) {
        new simpleDatatables.DataTable(reviewTable);
    }



    const datatablesSimple = document.getElementById('datatablesSimple');
    if (datatablesSimple) {
        new simpleDatatables.DataTable(datatablesSimple);
    }
});
