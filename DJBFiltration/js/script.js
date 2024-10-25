var runtime_per_status= JSON.parse(document.getElementById("runtime_per_status").innerHTML);
var changes_per_status= JSON.parse( document.getElementById("changes_per_status").innerHTML);
document.getElementById('flexSwitchCheckChecked').addEventListener('change', themetoggle);
function themetoggle() {
    const themeStylesheet = document.getElementById('theme-stylesheet');
    const checkbox = document.getElementById('flexSwitchCheckChecked');
    if (checkbox.checked) {
        themeStylesheet.href = themeStylesheetUrl1; 
    } else {
        themeStylesheet.href = themeStylesheetUrl2; 
    }
}

function changespiechart(changes_per_status) {
    let array1 = [];
    let array2 = [];

    for (let i = 0; i < changes_per_status.length; i++) {
        array1.push(changes_per_status[i].status);
        array2.push(changes_per_status[i].total_changes);
    }

    var changesData = {
        labels: array1,
        datasets: [{
            label: 'Status Changes',
            data: array2,
            backgroundColor: [
                'RGBA(236,107,86, 1)',
                'rgba(255, 193, 84, 1)',
                'rgba(71, 179, 156, 1)'
            ],
            borderWidth: 1
        }]
    };

    var piee = document.getElementById('changesPieChart').getContext('2d');
    new Chart(piee, {
        type: 'pie',
        data: changesData
    });
}
changespiechart(changes_per_status);


function runtimedoughnutchart(runtime_per_status) {
    let a1 = [];
    let a2 = [];

    for (let i = 0; i < runtime_per_status.length; i++) {
        a1.push(runtime_per_status[i].status);
        a2.push(runtime_per_status[i].total_runtime);
    }

    var runtimeData = {
        labels: a1, 
        datasets: [{
            label: 'Total Runtime',
            data: a2,
            backgroundColor: [
                'RGBA(236,107,86, 1)',
                'rgba(255, 193, 84, 1)',
                'rgba(71, 179, 156, 1)'
            ],
            borderWidth: 1
        }]
    };

    var dough = document.getElementById('runtimedoughnut').getContext('2d');
    new Chart(dough, {
        type: 'doughnut',
        data: runtimeData
    });
}
runtimedoughnutchart(runtime_per_status)

$(document).ready(function() {
    $('#runtime-form').on('submit', function(e) {
        e.preventDefault();
        var sub_id= JSON.parse(document.getElementById("sub_id").innerHTML);
        var metergroupId = $('#metergroup').val();

        $.ajax({
            type: 'POST',
            url: '/DJBFiltration/get_total_runtime',
            data: {
                'sub_id': sub_id,
                'device_id': metergroupId,
                'csrfmiddlewaretoken': 'YVJ2PSA9KqeJvmHttQaqR2Id9517kJcn3RVxNjo6XdCkqVjQwYubtrB0vYk8wqoI'
            },
            success: function(response) {
                console.log(response);
                if (response.error) {
                    $('#runtime-result').html('<p class="text-danger">' + response.error + '</p>');
                } else {
                    $('#total-runtime').text(response.total_runtime);
                    $('#status1').text(response.status1);
                    $('#status2').text(response.status2);
                    $('#status3').text(response.status3);
                    $('#status4').text(response.status4);

                   
                }
            },
            error: function(response) {
                $('#runtime-result').html('<p class="text-danger">An error occurred or Wrong input given</p>');
            }
        });
    });
});
