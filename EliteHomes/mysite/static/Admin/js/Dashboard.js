var dt = $('#dataTable').DataTable({
    "oLanguage": {
        "sLengthMenu": "Show Entries _MENU_",
    },
    dom: "<'row d-flex flex-row align-items-end'>tr<'row d-flex flex-row align-items-end'<'col-auto'l><'col-md-8'i><'col-md-2'p>>",
    "lengthMenu": [5,10, 25, 50,],
    "pageLength": 5,
    "order": [],
    "columnDefs": [{
        "targets": 0,
        "orderable": false,
        "className": "text-center select-checkbox",
    },{
        "targets": 8,
        "orderable": false,
        "className": "text-center",
        width: 100,
    }],
    select: {
        style: 'multi',
        selector: 'tr>td:nth-child(1)'
    },
    "paging": true,
    "searching": true,
    "ordering": true,
    "info": true,
    "autoWidth": false,
    "responsive": true,
    "bDestroy": true
});

var dt1 = $('#dataTable1').DataTable({
    "oLanguage": {
        "sLengthMenu": "Show Entries _MENU_",
    },
    dom: "<'row d-flex flex-row align-items-end'>tr<'row d-flex flex-row align-items-end'<'col-auto'l><'col-md-8'i><'col-md-2'p>>",
    "lengthMenu": [5,10, 25, 50,],
    "pageLength": 5,
    "order": [],
    "columnDefs": [{
        "targets": 0,
        "orderable": false,
        "className": "select-checkbox",
    },{
        "targets": 5,
        "orderable": false,
        "className": "text-center",
        width: 100,
    }],
    select: {
        style: 'multi',
        selector: 'tr>td:nth-child(1)'
    },
    "paging": true,
    "searching": true,
    "ordering": true,
    "info": true,
    "autoWidth": false,
    "responsive": true,
});

var dt2 = $('#dataTable2').DataTable({
    "oLanguage": {
        "sLengthMenu": "Show Entries _MENU_",
    },
    dom: "<'row d-flex flex-row align-items-end'>tr<'row d-flex flex-row align-items-end'<'col-auto'l><'col-md-8'i><'col-md-2'p>>",
    "lengthMenu": [5,10, 25, 50,],
    "pageLength": 5,
    "order": [],
    "columnDefs": [{
        "targets": 0,
        "orderable": false,
        "className": "select-checkbox",
    },{
        "targets": 5,
        "orderable": false,
        "className": "text-center",
        width: 100,
    }],
    select: {
        style: 'multi',
        selector: 'tr>td:nth-child(1)'
    },
    "paging": true,
    "searching": true,
    "ordering": true,
    "info": true,
    "autoWidth": false,
    "responsive": true,
});

var dt3 = $('#dataTable3').DataTable({
    "oLanguage": {
        "sLengthMenu": "Show Entries _MENU_",
    },
    dom: "<'row d-flex flex-row align-items-end'>tr<'row d-flex flex-row align-items-end'<'col-auto'l><'col-md-8'i><'col-md-2'p>>",
    "lengthMenu": [5,10, 25, 50,],
    "pageLength": 5,
    "order": [],
    "columnDefs": [{
        "targets": 0,
        "orderable": false,
        "className": "select-checkbox",
    },{
        "targets": 3,
        "orderable": false,
        "className": "text-center",
        width: 100,
    }],
    select: {
        style: 'multi',
        selector: 'tr>td:nth-child(1)'
    },
    "paging": true,
    "searching": true,
    "ordering": true,
    "info": true,
    "autoWidth": false,
    "responsive": true,
});

// new $.fn.dataTable.Buttons(dt, {
//     "buttons": [{
//         extend: 'excel',
//         text: 'Excel Selected',
//         exportOptions: {
//             modifier: {
//                 selected: true
//             }
//         },
//     }, {
//         extend: 'pdf',
//         text: 'PDF Selected',
//         exportOptions: {
//             modifier: {
//                 selected: true
//             }
//         },
//     }, {
//         extend: 'print',
//         text: 'Print Selected',
//         exportOptions: {
//             modifier: {
//                 selected: true
//             }
//         },
//     }]
// }).container().appendTo('#beforeLD1');
function hideAll(){
    w3.hide('#UserTable');
    w3.hide('#ProductTable');
    w3.hide('#OrderTable');
    w3.hide('#DeliveryTable');
}